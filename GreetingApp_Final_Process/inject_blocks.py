import os
import json
import zipfile
import shutil
import uuid

# Paths
aia_file = r"c:\Users\Justin\Downloads\LegitNaTo\Greeting_App (1).aia"
base_dir = r"c:\Users\Justin\Downloads\LegitNaTo\GreetingApp_Final_Process"
final_aia = r"c:\Users\Justin\Downloads\LegitNaTo\Greeting_App_Final.aia"

# Clean up any previous extraction
if os.path.exists(base_dir):
    shutil.rmtree(base_dir)
os.makedirs(base_dir)

# 1. Extract the .aia
with zipfile.ZipFile(aia_file, 'r') as zip_ref:
    zip_ref.extractall(base_dir)

# 2. Find the Screen1.scm and Screen1.bky paths
# The path depends on the user's email prefix which we can dynamically locate.
src_dir = os.path.join(base_dir, "src")
screen1_scm_path = None
screen1_bky_path = None

for root, dirs, files in os.walk(src_dir):
    for file in files:
        if file == "Screen1.scm":
            screen1_scm_path = os.path.join(root, file)
            screen1_bky_path = os.path.join(root, "Screen1.bky")

if not screen1_scm_path:
    print("Error: Could not find Screen1.scm inside the extracted project.")
    exit(1)

# 3. Read the YaVersion from Screen1.scm to match it in the blocks
with open(screen1_scm_path, "r", encoding="utf-8") as f:
    scm_content = f.read()

try:
    json_str = scm_content.split("$JSON")[1].split("|#")[0].strip()
    scm_data = json.loads(json_str)
    ya_version = scm_data.get("YaVersion", "233")
except Exception as e:
    print(f"Failed to parse YaVersion: {e}")
    ya_version = "233"

# 4. Generate the blocks XML with UUIDs
b1 = uuid.uuid4().hex
b2 = uuid.uuid4().hex
b3 = uuid.uuid4().hex
b4 = uuid.uuid4().hex
b5 = uuid.uuid4().hex
b6 = uuid.uuid4().hex

bky_data = f"""<xml xmlns="http://www.w3.org/1999/xhtml">
  <block type="component_event" id="{b1}" x="50" y="50">
    <mutation component_type="Button" is_generic="false" instance_name="btnGreet" event_name="Click"></mutation>
    <field name="COMPONENT_SELECTOR">btnGreet</field>
    <statement name="DO">
      <block type="component_set_get" id="{b2}">
        <mutation component_type="Label" set_or_get="set" property_name="Text" is_generic="false" instance_name="lblOutput"></mutation>
        <field name="COMPONENT_SELECTOR">lblOutput</field>
        <field name="PROP">Text</field>
        <value name="VALUE">
          <block type="text_join" id="{b3}">
            <mutation items="3"></mutation>
            <value name="ADD0">
              <block type="text" id="{b4}">
                <field name="TEXT">Hello, </field>
              </block>
            </value>
            <value name="ADD1">
              <block type="component_set_get" id="{b5}">
                <mutation component_type="TextBox" set_or_get="get" property_name="Text" is_generic="false" instance_name="txtName"></mutation>
                <field name="COMPONENT_SELECTOR">txtName</field>
                <field name="PROP">Text</field>
              </block>
            </value>
            <value name="ADD2">
              <block type="text" id="{b6}">
                <field name="TEXT">! Welcome to Android Development!</field>
              </block>
            </value>
          </block>
        </value>
      </block>
    </statement>
  </block>
  <yacodeblocks ya-version="{ya_version}" language-version="34"></yacodeblocks>
</xml>"""

# 5. Write the blocks file
with open(screen1_bky_path, "w", encoding="utf-8", newline="\n") as f:
    f.write(bky_data)

# 6. Re-zip the project back to .aia
with zipfile.ZipFile(final_aia, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(base_dir):
        # We also need to add empty directories, like assets/ if it's empty
        for d in dirs:
            dir_path = os.path.join(root, d)
            arcname = os.path.relpath(dir_path, base_dir)
            arcname = arcname.replace(os.sep, '/') + '/'
            zinfo = zipfile.ZipInfo(arcname)
            zipf.writestr(zinfo, '')

        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, base_dir)
            arcname = arcname.replace(os.sep, '/')
            zipf.write(file_path, arcname)

print(f"Success! Generated final app with logic at: {final_aia}")
