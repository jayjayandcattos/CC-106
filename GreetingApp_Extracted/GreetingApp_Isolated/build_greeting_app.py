import os
import json
import zipfile
import shutil

base_dir = r"c:\Users\Justin\Downloads\LegitNaTo\GreetingApp_Isolated"
project_name = "GreetingApp"
build_dir = os.path.join(base_dir, "build")
if os.path.exists(build_dir):
    shutil.rmtree(build_dir)

# Create dirs
ya_dir = os.path.join(build_dir, "youngandroidproject")
src_dir = os.path.join(build_dir, "src", "appinventor", "ai_test", project_name)
assets_dir = os.path.join(build_dir, "assets")
os.makedirs(ya_dir, exist_ok=True)
os.makedirs(src_dir, exist_ok=True)
os.makedirs(assets_dir, exist_ok=True)

# Write project.properties
with open(os.path.join(ya_dir, "project.properties"), "w", encoding="utf-8", newline="\n") as f:
    f.write(f"""main=appinventor.ai_test.{project_name}.Screen1
name={project_name}
aname={project_name}
assets=../assets
source=../src
versioncode=1
versionname=1.0
useslocation=False
actionbar=False
theme=Classic
sizing=Responsive
""")

# Write Screen1.scm
scm_data = {
  "authURL": ["ai2.appinventor.mit.edu"],
  "YaVersion": "213",
  "Source": "Form",
  "Properties": {
    "$Name": "Screen1",
    "$Type": "Form",
    "$Version": "30",
    "AppName": "GreetingApp",
    "Title": "GreetingApp",
    "Uuid": "0",
    "AlignHorizontal": "3",
    "AlignVertical": "2",
    "BackgroundColor": "&HFFEEEEEE",
    "AccentColor": "&HFF00728A",
    "PrimaryColor": "&HFFA5CF47",
    "PrimaryColorDark": "&HFF41521C",
    "$Components": [
      {
        "$Name": "lblInstruction",
        "$Type": "Label",
        "$Version": "5",
        "Uuid": "1",
        "Text": "Enter your name:",
        "FontSize": "18",
        "FontBold": "True"
      },
      {
        "$Name": "txtName",
        "$Type": "TextBox",
        "$Version": "6",
        "Uuid": "2",
        "Hint": "Type your name here",
        "Width": "-2",
        "FontSize": "16"
      },
      {
        "$Name": "btnGreet",
        "$Type": "Button",
        "$Version": "7",
        "Uuid": "3",
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
        "Uuid": "4",
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

# Write Screen1.bky
bky_data = """<xml xmlns="http://www.w3.org/1999/xhtml">
  <block type="component_event" id="1" x="50" y="50">
    <mutation component_type="Button" is_generic="false" instance_name="btnGreet" event_name="Click"></mutation>
    <field name="COMPONENT_SELECTOR">btnGreet</field>
    <statement name="DO">
      <block type="component_set_get" id="2">
        <mutation component_type="Label" set_or_get="set" property_name="Text" is_generic="false" instance_name="lblOutput"></mutation>
        <field name="COMPONENT_SELECTOR">lblOutput</field>
        <field name="PROP">Text</field>
        <value name="VALUE">
          <block type="text_join" id="3">
            <mutation items="3"></mutation>
            <value name="ADD0">
              <block type="text" id="4">
                <field name="TEXT">Hello, </field>
              </block>
            </value>
            <value name="ADD1">
              <block type="component_set_get" id="5">
                <mutation component_type="TextBox" set_or_get="get" property_name="Text" is_generic="false" instance_name="txtName"></mutation>
                <field name="COMPONENT_SELECTOR">txtName</field>
                <field name="PROP">Text</field>
              </block>
            </value>
            <value name="ADD2">
              <block type="text" id="6">
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
with open(os.path.join(src_dir, "Screen1.bky"), "w", encoding="utf-8", newline="\n") as f:
    f.write(bky_data)

# Zip it
aia_path = os.path.join(base_dir, f"{project_name}.aia")
with zipfile.ZipFile(aia_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    # Explicitly add empty assets directory
    zinfo = zipfile.ZipInfo("assets/")
    zipf.writestr(zinfo, '')
    
    for root, _, files in os.walk(build_dir):
        # We don't need to walk the assets dir if it's empty, but os.walk is fine.
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, build_dir)
            arcname = arcname.replace(os.sep, '/')
            zipf.write(file_path, arcname)

print(f"Successfully generated {aia_path}")
