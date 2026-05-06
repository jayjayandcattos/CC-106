import os
import json
import zipfile
import shutil
import uuid

base_dir = r"c:\Users\Justin\Downloads\LegitNaTo\GreetingApp_Isolated"
project_name = "GreetingApp"
build_dir = os.path.join(base_dir, "build_safe")

if os.path.exists(build_dir):
    shutil.rmtree(build_dir)

# Create dirs using the user's exact email prefix
user_package = "ai_rivera_justin_santilla"
ya_dir = os.path.join(build_dir, "youngandroidproject")
src_dir = os.path.join(build_dir, "src", "appinventor", user_package, project_name)
assets_dir = os.path.join(build_dir, "assets")

os.makedirs(ya_dir, exist_ok=True)
os.makedirs(src_dir, exist_ok=True)
os.makedirs(assets_dir, exist_ok=True)

# Write project.properties
with open(os.path.join(ya_dir, "project.properties"), "w", encoding="utf-8", newline="\n") as f:
    f.write(f"""main=appinventor.{user_package}.{project_name}.Screen1
name={project_name}
aname={project_name}
assets=../assets
source=../src
versioncode=1
versionname=1.0
useslocation=False
defaultfilescope=App
theme=Classic
sizing=Responsive
""")

# Generate UUIDs
uuid_lbl = str(uuid.uuid4())
uuid_txt = str(uuid.uuid4())
uuid_btn = str(uuid.uuid4())
uuid_out = str(uuid.uuid4())

# Write Screen1.scm
scm_data = {
  "authURL": ["ai2.appinventor.mit.edu"],
  "YaVersion": "242",
  "Source": "Form",
  "Properties": {
    "$Name": "Screen1",
    "$Type": "Form",
    "$Version": "30",
    "AppName": project_name,
    "Title": project_name,
    "Uuid": "0",
    "AlignHorizontal": "3",
    "AlignVertical": "2",
    "BackgroundColor": "&HFFEEEEEE",
    "$Components": [
      {
        "$Name": "lblInstruction",
        "$Type": "Label",
        "$Version": "5",
        "Uuid": uuid_lbl,
        "Text": "Enter your name:",
        "FontSize": "18",
        "FontBold": "True"
      },
      {
        "$Name": "txtName",
        "$Type": "TextBox",
        "$Version": "6",
        "Uuid": uuid_txt,
        "Hint": "Type your name here",
        "Width": "-2",
        "FontSize": "16"
      },
      {
        "$Name": "btnGreet",
        "$Type": "Button",
        "$Version": "7",
        "Uuid": uuid_btn,
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
        "Uuid": uuid_out,
        "Text": "",
        "FontSize": "16",
        "TextColor": "&HFF4CAF50",
        "FontBold": "True",
        "HasMargins": "True"
      }
    ]
  }
}

with open(os.path.join(src_dir, "Screen1.scm"), "w", encoding="utf-8", newline="\n") as f:
    f.write("#|\\n$JSON\\n")
    json.dump(scm_data, f, separators=(',', ':'))
    f.write("\\n|#")

# Write Screen1.bky with generated UUIDs
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
  <yacodeblocks ya-version="242" language-version="34"></yacodeblocks>
</xml>"""

with open(os.path.join(src_dir, "Screen1.bky"), "w", encoding="utf-8", newline="\n") as f:
    f.write(bky_data)

# Create an alternate "no blocks" version just in case blocks fail
no_blocks_data = """<xml xmlns="http://www.w3.org/1999/xhtml">
  <yacodeblocks ya-version="242" language-version="34"></yacodeblocks>
</xml>"""
with open(os.path.join(src_dir, "Screen1_noblocks.bky"), "w", encoding="utf-8", newline="\n") as f:
    f.write(no_blocks_data)

# Zip the normal version
aia_path = os.path.join(base_dir, f"{project_name}.aia")
with zipfile.ZipFile(aia_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    zinfo = zipfile.ZipInfo("assets/")
    zipf.writestr(zinfo, '')
    
    for root, dirs, files in os.walk(build_dir):
        for file in files:
            if file == "Screen1_noblocks.bky":
                continue
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, build_dir)
            arcname = arcname.replace(os.sep, '/')
            zipf.write(file_path, arcname)

# Zip the no-blocks version
aia_noblocks_path = os.path.join(base_dir, f"{project_name}_NoBlocks.aia")
with zipfile.ZipFile(aia_noblocks_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    zinfo = zipfile.ZipInfo("assets/")
    zipf.writestr(zinfo, '')
    
    for root, dirs, files in os.walk(build_dir):
        for file in files:
            if file == "Screen1.bky":
                continue
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, build_dir)
            arcname = arcname.replace(os.sep, '/')
            
            # rename Screen1_noblocks.bky to Screen1.bky inside the zip
            if file == "Screen1_noblocks.bky":
                arcname = arcname.replace("Screen1_noblocks.bky", "Screen1.bky")
                
            zipf.write(file_path, arcname)

print(f"Generated {aia_path} and {aia_noblocks_path}")
