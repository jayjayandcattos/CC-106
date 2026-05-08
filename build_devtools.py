import os
import json
import zipfile
import shutil
from xml.etree.ElementTree import Element, SubElement, tostring
import xml.dom.minidom

base_dir = r"c:\Users\Justin\Downloads\LegitNaTo"
source_aia = os.path.join(base_dir, "asdc.aia")
target_aia = os.path.join(base_dir, "DevToolsApp.aia")
work_dir = os.path.join(base_dir, "DevToolsWork")

print(f"[*] Starting process... target AIA: {target_aia}")

# 1. Extract AIA
if os.path.exists(work_dir):
    shutil.rmtree(work_dir)
os.makedirs(work_dir)

with zipfile.ZipFile(source_aia, 'r') as zip_ref:
    zip_ref.extractall(work_dir)
print(f"[*] Extracted {source_aia} to {work_dir}")

# 2. Modify project.properties
props_path = os.path.join(work_dir, "youngandroidproject", "project.properties")
with open(props_path, "r", encoding="utf-8") as f:
    props = f.read()

props = props.replace("aname=asdc", "aname=DevToolsApp")
props = props.replace("name=asdc", "name=DevToolsApp")

with open(props_path, "w", encoding="utf-8") as f:
    f.write(props)
print("[*] Modified project.properties")

# 3. Modify Screen1.scm
scm_path = os.path.join(work_dir, "src", "appinventor", "ai_rivera_justin_santilla", "asdc", "Screen1.scm")
with open(scm_path, "r", encoding="utf-8") as f:
    content = f.read()

# JSON starts after $JSON and ends before |#
try:
    json_part = content.split("$JSON")[1]
    # In case there are multiple lines, just take the portion before |#
    json_str = json_part.split("|#")[0].strip()
except IndexError:
    print("[!] Failed to parse Screen1.scm!")
    exit(1)

scm_data = json.loads(json_str)

uuid_counter = 10000
def get_uuid():
    global uuid_counter
    uuid_counter += 1
    return str(uuid_counter)

components = [
    {
        "$Name": "TitleLabel",
        "$Type": "Label",
        "$Version": "5",
        "Uuid": get_uuid(),
        "Text": "Android Development Tools",
        "FontSize": "24",
        "FontBold": "True"
    },
    {
        "$Name": "BtnAndroidStudio",
        "$Type": "Button",
        "$Version": "7",
        "Uuid": get_uuid(),
        "Text": "Android Studio"
    },
    {
        "$Name": "BtnXamarin",
        "$Type": "Button",
        "$Version": "7",
        "Uuid": get_uuid(),
        "Text": "Xamarin"
    },
    {
        "$Name": "BtnIonic",
        "$Type": "Button",
        "$Version": "7",
        "Uuid": get_uuid(),
        "Text": "Ionic"
    },
    {
        "$Name": "BtnFirebase",
        "$Type": "Button",
        "$Version": "7",
        "Uuid": get_uuid(),
        "Text": "Firebase"
    },
    {
        "$Name": "DescLabel",
        "$Type": "Label",
        "$Version": "5",
        "Uuid": get_uuid(),
        "Text": "Tool description will appear here",
        "FontSize": "16",
        "TextColor": "&HFF444444"
    }
]

scm_data["Properties"]["$Components"] = components

new_json_str = json.dumps(scm_data)
new_scm = f"#|\n$JSON\n{new_json_str}\n|#"

with open(scm_path, "w", encoding="utf-8") as f:
    f.write(new_scm)
print("[*] Injected components into Screen1.scm")

# 4. Modify Screen1.bky
bky_path = os.path.join(work_dir, "src", "appinventor", "ai_rivera_justin_santilla", "asdc", "Screen1.bky")

def create_event_block(btn_name, desc_text, x, y):
    block = Element('block', {'type': 'component_event', 'id': get_uuid(), 'x': str(x), 'y': str(y)})
    SubElement(block, 'mutation', {
        'component_type': 'Button',
        'is_generic': 'false',
        'instance_name': btn_name,
        'event_name': 'Click'
    })
    field_sel = SubElement(block, 'field', {'name': 'COMPONENT_SELECTOR'})
    field_sel.text = btn_name
    
    statement = SubElement(block, 'statement', {'name': 'DO'})
    
    set_block = SubElement(statement, 'block', {'type': 'component_set_get', 'id': get_uuid()})
    SubElement(set_block, 'mutation', {
        'component_type': 'Label',
        'set_or_get': 'set',
        'property_name': 'Text',
        'is_generic': 'false',
        'instance_name': 'DescLabel'
    })
    set_sel = SubElement(set_block, 'field', {'name': 'COMPONENT_SELECTOR'})
    set_sel.text = 'DescLabel'
    set_prop = SubElement(set_block, 'field', {'name': 'PROP'})
    set_prop.text = 'Text'
    
    value = SubElement(set_block, 'value', {'name': 'VALUE'})
    text_block = SubElement(value, 'block', {'type': 'text', 'id': get_uuid()})
    text_field = SubElement(text_block, 'field', {'name': 'TEXT'})
    text_field.text = desc_text
    
    return block

xml_root = Element('xml', {'xmlns': 'http://www.w3.org/1999/xhtml'})

btns = [
    ("BtnAndroidStudio", "Official IDE for Android"),
    ("BtnXamarin", "Cross-platform tool using C#"),
    ("BtnIonic", "Hybrid framework using HTML, CSS, JS"),
    ("BtnFirebase", "Backend service with real-time database")
]

y_pos = 50
for btn_name, desc in btns:
    xml_root.append(create_event_block(btn_name, desc, 50, y_pos))
    y_pos += 150

xml_str = tostring(xml_root, encoding='utf-8').decode('utf-8')
# App inventor expects proper closing tags, not self-closing for empty blocks usually, but ElementTree handles this mostly fine. minidom formats it.
dom = xml.dom.minidom.parseString(xml_str)
# AppInventor blocks XML doesn't include the XML declaration, so we slice it off
pretty_xml = dom.toprettyxml(indent="  ")
xml_lines = pretty_xml.split("\n")
if xml_lines[0].startswith("<?xml"):
    xml_lines = xml_lines[1:]
final_xml = "\n".join(xml_lines).strip()

with open(bky_path, "w", encoding="utf-8") as f:
    f.write(final_xml)
print("[*] Injected blocks into Screen1.bky")

# 5. Repackage to DevToolsApp.aia
if os.path.exists(target_aia):
    os.remove(target_aia)

target_zip = os.path.join(base_dir, "DevToolsApp")
shutil.make_archive(target_zip, 'zip', work_dir)
os.rename(target_zip + ".zip", target_aia)
print(f"[*] Repackaged to {target_aia}")

# Cleanup
if os.path.exists(work_dir):
    shutil.rmtree(work_dir)
print("[*] Done!")
