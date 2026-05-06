import os
import json
import zipfile
import shutil

base_dir = r"c:\Users\Justin\Downloads\LegitNaTo\GreetingApp_Isolated"
extracted_dir = r"c:\Users\Justin\Downloads\LegitNaTo\Extracted"
build_dir = os.path.join(base_dir, "build2")

if os.path.exists(build_dir):
    shutil.rmtree(build_dir)

shutil.copytree(extracted_dir, build_dir)

# 1. Modify project.properties
prop_path = os.path.join(build_dir, "youngandroidproject", "project.properties")
with open(prop_path, "r", encoding="utf-8") as f:
    props = f.read()

props = props.replace("name=test", "name=GreetingApp")
props = props.replace("aname=test", "aname=GreetingApp")

with open(prop_path, "w", encoding="utf-8", newline="\n") as f:
    f.write(props)

# 2. Modify Screen1.scm
scm_path = os.path.join(build_dir, "src", "appinventor", "ai_gordonlu0749", "test", "Screen1.scm")

with open(scm_path, "r", encoding="utf-8") as f:
    scm_content = f.read()

# Extract the JSON part
json_str = scm_content.split("$JSON")[1].split("|#")[0].strip()
scm_data = json.loads(json_str)

scm_data["Properties"]["AppName"] = "GreetingApp"
scm_data["Properties"]["Title"] = "GreetingApp"
scm_data["Properties"]["BackgroundColor"] = "&HFFEEEEEE"

scm_data["Properties"]["$Components"] = [
  {
    "$Name": "lblInstruction",
    "$Type": "Label",
    "$Version": "5",
    "Uuid": "1234567890",
    "Text": "Enter your name:",
    "FontSize": "18",
    "FontBold": "True"
  },
  {
    "$Name": "txtName",
    "$Type": "TextBox",
    "$Version": "6",
    "Uuid": "1234567891",
    "Hint": "Type your name here",
    "Width": "-2",
    "FontSize": "16"
  },
  {
    "$Name": "btnGreet",
    "$Type": "Button",
    "$Version": "7",
    "Uuid": "1234567892",
    "Text": "Greet Me",
    "BackgroundColor": "&HFF2196F3",
    "TextColor": "&HFFFFFFFF",
    "FontSize": "18",
    "FontBold": "True"
  },
  {
    "$Name": "lblOutput",
    "$Type": "Label",
    "$Version": "5",
    "Uuid": "1234567893",
    "Text": "",
    "FontSize": "16",
    "TextColor": "&HFF4CAF50",
    "FontBold": "True",
    "HasMargins": "True"
  }
]

with open(scm_path, "w", encoding="utf-8", newline="\n") as f:
    f.write("#|\\n$JSON\\n")
    json.dump(scm_data, f, separators=(',', ':'))
    f.write("\\n|#")

# 3. Modify Screen1.bky
bky_path = os.path.join(build_dir, "src", "appinventor", "ai_gordonlu0749", "test", "Screen1.bky")

bky_data = """<xml xmlns="http://www.w3.org/1999/xhtml">
  <block type="component_event" id="btn_click_event" x="50" y="50">
    <mutation component_type="Button" is_generic="false" instance_name="btnGreet" event_name="Click"></mutation>
    <field name="COMPONENT_SELECTOR">btnGreet</field>
    <statement name="DO">
      <block type="component_set_get" id="set_lbl_output">
        <mutation component_type="Label" set_or_get="set" property_name="Text" is_generic="false" instance_name="lblOutput"></mutation>
        <field name="COMPONENT_SELECTOR">lblOutput</field>
        <field name="PROP">Text</field>
        <value name="VALUE">
          <block type="text_join" id="join_text">
            <mutation items="3"></mutation>
            <value name="ADD0">
              <block type="text" id="text_hello">
                <field name="TEXT">Hello, </field>
              </block>
            </value>
            <value name="ADD1">
              <block type="component_set_get" id="get_txt_name">
                <mutation component_type="TextBox" set_or_get="get" property_name="Text" is_generic="false" instance_name="txtName"></mutation>
                <field name="COMPONENT_SELECTOR">txtName</field>
                <field name="PROP">Text</field>
              </block>
            </value>
            <value name="ADD2">
              <block type="text" id="text_welcome">
                <field name="TEXT">! Welcome to Android Development!</field>
              </block>
            </value>
          </block>
        </value>
      </block>
    </statement>
  </block>
  <yacodeblocks ya-version="213" language-version="34"></yacodeblocks>
</xml>"""

with open(bky_path, "w", encoding="utf-8", newline="\n") as f:
    f.write(bky_data)

# 4. Zip it
aia_path = os.path.join(base_dir, "GreetingApp.aia")
with zipfile.ZipFile(aia_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(build_dir):
        # Explicitly write directories so empty ones are included
        for d in dirs:
            dir_path = os.path.join(root, d)
            arcname = os.path.relpath(dir_path, build_dir)
            arcname = arcname.replace(os.sep, '/') + '/'
            zinfo = zipfile.ZipInfo(arcname)
            zipf.writestr(zinfo, '')
        
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, build_dir)
            arcname = arcname.replace(os.sep, '/')
            zipf.write(file_path, arcname)

print(f"Successfully generated {aia_path} using known-good template")
