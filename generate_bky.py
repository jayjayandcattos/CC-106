import os
import re
import uuid

xml_content = """<xml xmlns="http://www.w3.org/1999/xhtml">
  <block type="global_declaration" x="-1000" y="-800">
    <field name="NAME">turn</field>
    <value name="VALUE"><block type="text"><field name="TEXT">X</field></block></value>
  </block>
  <block type="global_declaration" x="-1000" y="-750">
    <field name="NAME">pending_move</field>
    <value name="VALUE"><block type="text"><field name="TEXT"></field></block></value>
  </block>
  <block type="global_declaration" x="-1000" y="-700">
    <field name="NAME">current_answer</field>
    <value name="VALUE"><block type="text"><field name="TEXT"></field></block></value>
  </block>
  <block type="global_declaration" x="-1000" y="-650">
    <field name="NAME">selected_category</field>
    <value name="VALUE"><block type="text"><field name="TEXT">GEO</field></block></value>
  </block>
"""

categories = {
    "q_geo": [
        ("Geo Easy: Capital of France?", "paris"),
        ("Geo Med: Capital of Australia?", "canberra"),
        ("Geo Hard: Capital of Burkina Faso?", "ouagadougou")
    ],
    "q_math": [
        ("Math Easy: What is 5 + 7?", "12"),
        ("Math Med: What is 12 * 12?", "144"),
        ("Math Hard: Square root of 225?", "15")
    ],
    "q_trivia": [
        ("Trivia Easy: Color of a school bus?", "yellow"),
        ("Trivia Med: How many continents are there?", "7"),
        ("Trivia Hard: A network security system? (Hint: firewall)", "firewall")
    ]
}

y_pos = -600
for cat_name, questions in categories.items():
    xml_content += f"""
  <block type="global_declaration" x="-1000" y="{y_pos}">
    <field name="NAME">{cat_name}</field>
    <value name="VALUE">
      <block type="lists_create_with">
        <mutation items="{len(questions)}"></mutation>
"""
    for idx, (q, a) in enumerate(questions):
        xml_content += f"""
        <value name="ADD{idx}">
          <block type="lists_create_with">
            <mutation items="2"></mutation>
            <value name="ADD0"><block type="text"><field name="TEXT">{q}</field></block></value>
            <value name="ADD1"><block type="text"><field name="TEXT">{a}</field></block></value>
          </block>
        </value>
"""
    xml_content += """
      </block>
    </value>
  </block>
"""
    y_pos += 50

# Navigation Buttons
nav_buttons = [("BtnGeo", "GEO"), ("BtnMath", "MATH"), ("BtnTrivia", "TRIV")]
for btn, val in nav_buttons:
    xml_content += f"""
  <block type="component_event" x="-1500" y="{y_pos}">
    <mutation component_type="Button" is_generic="false" instance_name="{btn}" event_name="Click"></mutation>
    <field name="COMPONENT_SELECTOR">{btn}</field>
    <statement name="DO">
      <block type="lexical_variable_set">
        <field name="VAR">global selected_category</field>
        <value name="VALUE"><block type="text"><field name="TEXT">{val}</field></block></value>
        <next>
          <block type="component_set_get">
            <mutation component_type="VerticalArrangement" set_or_get="set" property_name="Visible" is_generic="false" instance_name="ViewCategory"></mutation>
            <field name="COMPONENT_SELECTOR">ViewCategory</field>
            <field name="PROP">Visible</field>
            <value name="VALUE"><block type="logic_boolean"><field name="BOOL">FALSE</field></block></value>
            <next>
              <block type="component_set_get">
                <mutation component_type="VerticalArrangement" set_or_get="set" property_name="Visible" is_generic="false" instance_name="ViewGame"></mutation>
                <field name="COMPONENT_SELECTOR">ViewGame</field>
                <field name="PROP">Visible</field>
                <value name="VALUE"><block type="logic_boolean"><field name="BOOL">TRUE</field></block></value>
                <next>
                  <block type="procedures_callnoreturn">
                    <mutation name="ResetGame"></mutation>
                  </block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </statement>
  </block>
"""
    y_pos += 100

# BtnBack Click
xml_content += f"""
  <block type="component_event" x="-1500" y="{y_pos}">
    <mutation component_type="Button" is_generic="false" instance_name="BtnBack" event_name="Click"></mutation>
    <field name="COMPONENT_SELECTOR">BtnBack</field>
    <statement name="DO">
      <block type="component_set_get">
        <mutation component_type="VerticalArrangement" set_or_get="set" property_name="Visible" is_generic="false" instance_name="ViewCategory"></mutation>
        <field name="COMPONENT_SELECTOR">ViewCategory</field>
        <field name="PROP">Visible</field>
        <value name="VALUE"><block type="logic_boolean"><field name="BOOL">TRUE</field></block></value>
        <next>
          <block type="component_set_get">
            <mutation component_type="VerticalArrangement" set_or_get="set" property_name="Visible" is_generic="false" instance_name="ViewGame"></mutation>
            <field name="COMPONENT_SELECTOR">ViewGame</field>
            <field name="PROP">Visible</field>
            <value name="VALUE"><block type="logic_boolean"><field name="BOOL">FALSE</field></block></value>
          </block>
        </next>
      </block>
    </statement>
  </block>
"""

# HandleMove procedure
xml_content += """
  <block type="procedures_defnoreturn" x="-1000" y="-400">
    <mutation><arg name="btnId"></arg></mutation>
    <field name="NAME">HandleMove</field>
    <statement name="STACK">
      <block type="lexical_variable_set">
        <field name="VAR">global pending_move</field>
        <value name="VALUE"><block type="lexical_variable_get"><field name="VAR">btnId</field></block></value>
        <next>
          <block type="procedures_callnoreturn">
            <mutation name="AskQuestion"></mutation>
          </block>
        </next>
      </block>
    </statement>
  </block>

  <!-- Ask Question (with Category filter) -->
  <block type="procedures_defnoreturn" x="-1000" y="-200">
    <field name="NAME">AskQuestion</field>
    <statement name="STACK">
      <block type="local_declaration_statement">
        <mutation><localname name="q_pair"></localname></mutation>
        <field name="VAR0">q_pair</field>
        <value name="DECL0">
          <block type="controls_choose">
            <value name="TEST">
              <block type="logic_compare">
                <field name="OP">EQ</field>
                <value name="A"><block type="lexical_variable_get"><field name="VAR">global selected_category</field></block></value>
                <value name="B"><block type="text"><field name="TEXT">GEO</field></block></value>
              </block>
            </value>
            <value name="THENRETURN">
              <block type="lists_pick_random_item"><value name="LIST"><block type="lexical_variable_get"><field name="VAR">global q_geo</field></block></value></block>
            </value>
            <value name="ELSERETURN">
              <block type="controls_choose">
                <value name="TEST">
                  <block type="logic_compare">
                    <field name="OP">EQ</field>
                    <value name="A"><block type="lexical_variable_get"><field name="VAR">global selected_category</field></block></value>
                    <value name="B"><block type="text"><field name="TEXT">MATH</field></block></value>
                  </block>
                </value>
                <value name="THENRETURN">
                  <block type="lists_pick_random_item"><value name="LIST"><block type="lexical_variable_get"><field name="VAR">global q_math</field></block></value></block>
                </value>
                <value name="ELSERETURN">
                  <block type="lists_pick_random_item"><value name="LIST"><block type="lexical_variable_get"><field name="VAR">global q_trivia</field></block></value></block>
                </value>
              </block>
            </value>
          </block>
        </value>
        <statement name="STACK">
          <block type="lexical_variable_set">
            <field name="VAR">global current_answer</field>
            <value name="VALUE">
              <block type="lists_select_item">
                <value name="LIST"><block type="lexical_variable_get"><field name="VAR">q_pair</field></block></value>
                <value name="NUM"><block type="math_number"><field name="NUM">2</field></block></value>
              </block>
            </value>
            <next>
              <block type="component_method">
                <mutation component_type="Notifier" method_name="ShowTextDialog" is_generic="false" instance_name="Notifier1"></mutation>
                <field name="COMPONENT_SELECTOR">Notifier1</field>
                <value name="ARG0">
                  <block type="lists_select_item">
                    <value name="LIST"><block type="lexical_variable_get"><field name="VAR">q_pair</field></block></value>
                    <value name="NUM"><block type="math_number"><field name="NUM">1</field></block></value>
                  </block>
                </value>
                <value name="ARG1"><block type="text"><field name="TEXT">Knowledge Gate</field></block></value>
                <value name="ARG2"><block type="logic_boolean"><field name="BOOL">FALSE</field></block></value>
              </block>
            </next>
          </block>
        </statement>
      </block>
    </statement>
  </block>
"""

# Buttons 1-9
for i in range(1, 10):
    xml_content += f"""
  <block type="component_event" x="-500" y="{i * 100 - 800}">
    <mutation component_type="Button" is_generic="false" instance_name="Btn{i}" event_name="Click"></mutation>
    <field name="COMPONENT_SELECTOR">Btn{i}</field>
    <statement name="DO">
      <block type="controls_if">
        <value name="IF0">
          <block type="logic_compare">
            <field name="OP">EQ</field>
            <value name="A">
              <block type="component_set_get">
                <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn{i}"></mutation>
                <field name="COMPONENT_SELECTOR">Btn{i}</field>
                <field name="PROP">Text</field>
              </block>
            </value>
            <value name="B"><block type="text"><field name="TEXT">_</field></block></value>
          </block>
        </value>
        <statement name="DO0">
          <block type="procedures_callnoreturn">
            <mutation name="HandleMove"><arg name="btnId"></arg></mutation>
            <value name="ARG0"><block type="text"><field name="TEXT">Btn{i}</field></block></value>
          </block>
        </statement>
      </block>
    </statement>
  </block>
"""

# CheckWin Logic
xml_content += """
  <block type="procedures_defnoreturn" x="1000" y="-400">
    <field name="NAME">CheckWin</field>
    <statement name="STACK">
"""

win_combos = [
  (1,2,3), (4,5,6), (7,8,9),
  (1,4,7), (2,5,8), (3,6,9),
  (1,5,9), (3,5,7)
]

for combo in win_combos:
    xml_content += f"""
      <block type="controls_if">
        <value name="IF0">
          <block type="logic_compare">
            <field name="OP">NEQ</field>
            <value name="A">
              <block type="component_set_get">
                <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn{combo[0]}"></mutation>
                <field name="COMPONENT_SELECTOR">Btn{combo[0]}</field>
                <field name="PROP">Text</field>
              </block>
            </value>
            <value name="B"><block type="text"><field name="TEXT">_</field></block></value>
          </block>
        </value>
        <statement name="DO0">
          <block type="controls_if">
            <value name="IF0">
              <block type="logic_compare">
                <field name="OP">EQ</field>
                <value name="A">
                  <block type="component_set_get">
                    <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn{combo[0]}"></mutation>
                    <field name="COMPONENT_SELECTOR">Btn{combo[0]}</field>
                    <field name="PROP">Text</field>
                  </block>
                </value>
                <value name="B">
                  <block type="component_set_get">
                    <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn{combo[1]}"></mutation>
                    <field name="COMPONENT_SELECTOR">Btn{combo[1]}</field>
                    <field name="PROP">Text</field>
                  </block>
                </value>
              </block>
            </value>
            <statement name="DO0">
              <block type="controls_if">
                <value name="IF0">
                  <block type="logic_compare">
                    <field name="OP">EQ</field>
                    <value name="A">
                      <block type="component_set_get">
                        <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn{combo[1]}"></mutation>
                        <field name="COMPONENT_SELECTOR">Btn{combo[1]}</field>
                        <field name="PROP">Text</field>
                      </block>
                    </value>
                    <value name="B">
                      <block type="component_set_get">
                        <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn{combo[2]}"></mutation>
                        <field name="COMPONENT_SELECTOR">Btn{combo[2]}</field>
                        <field name="PROP">Text</field>
                      </block>
                    </value>
                  </block>
                </value>
                <statement name="DO0">
                  <block type="component_method">
                    <mutation component_type="Notifier" method_name="ShowAlert" is_generic="false" instance_name="Notifier1"></mutation>
                    <field name="COMPONENT_SELECTOR">Notifier1</field>
                    <value name="ARG0">
                      <block type="text_join">
                        <mutation items="2"></mutation>
                        <value name="ADD0"><block type="text"><field name="TEXT">Winner: </field></block></value>
                        <value name="ADD1">
                          <block type="component_set_get">
                            <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn{combo[0]}"></mutation>
                            <field name="COMPONENT_SELECTOR">Btn{combo[0]}</field>
                            <field name="PROP">Text</field>
                          </block>
                        </value>
                      </block>
                    </value>
                    <next>
                      <block type="procedures_callnoreturn">
                        <mutation name="ResetGame"></mutation>
                      </block>
                    </next>
                  </block>
                </statement>
              </block>
            </statement>
          </block>
        </statement>
        <next>
"""

xml_content += "  " + "</next></block>" * 8

xml_content += """
    </statement>
  </block>
"""

# Reset Game
xml_content += """
  <block type="procedures_defnoreturn" x="2000" y="-400">
    <field name="NAME">ResetGame</field>
    <statement name="STACK">
"""
for i in range(1, 10):
    xml_content += f"""
      <block type="component_set_get">
        <mutation component_type="Button" set_or_get="set" property_name="Text" is_generic="false" instance_name="Btn{i}"></mutation>
        <field name="COMPONENT_SELECTOR">Btn{i}</field>
        <field name="PROP">Text</field>
        <value name="VALUE"><block type="text"><field name="TEXT">_</field></block></value>
        <next>
"""
xml_content += """
        <block type="lexical_variable_set">
          <field name="VAR">global turn</field>
          <value name="VALUE"><block type="text"><field name="TEXT">X</field></block></value>
          <next>
            <block type="component_set_get">
              <mutation component_type="Label" set_or_get="set" property_name="Text" is_generic="false" instance_name="LblTurn"></mutation>
              <field name="COMPONENT_SELECTOR">LblTurn</field>
              <field name="PROP">Text</field>
              <value name="VALUE"><block type="text"><field name="TEXT">X Turn</field></block></value>
            </block>
          </next>
        </block>
"""
xml_content += "</next></block>" * 9
xml_content += """
    </statement>
  </block>
"""

# Notifier AfterTextInput
xml_content += """
  <block type="component_event" x="-1000" y="200">
    <mutation component_type="Notifier" is_generic="false" instance_name="Notifier1" event_name="AfterTextInput"></mutation>
    <field name="COMPONENT_SELECTOR">Notifier1</field>
    <statement name="DO">
      <block type="controls_if">
        <mutation else="1"></mutation>
        <value name="IF0">
          <block type="logic_compare">
            <field name="OP">EQ</field>
            <value name="A">
              <block type="text_changeCase">
                <field name="OP">DOWNCASE</field>
                <value name="STRING"><block type="lexical_variable_get"><mutation><eventparam name="response"></eventparam></mutation><field name="VAR">response</field></block></value>
              </block>
            </value>
            <value name="B">
              <block type="text_changeCase">
                <field name="OP">DOWNCASE</field>
                <value name="STRING"><block type="lexical_variable_get"><field name="VAR">global current_answer</field></block></value>
              </block>
            </value>
          </block>
        </value>
        <statement name="DO0">
          <!-- CORRECT -->
          <block type="controls_if">
            <mutation elseif="8"></mutation>
"""

for i in range(1, 10):
    condition = f"IF{i-1}"
    do = f"DO{i-1}"
    xml_content += f"""
            <value name="{condition}">
              <block type="logic_compare">
                <field name="OP">EQ</field>
                <value name="A"><block type="lexical_variable_get"><field name="VAR">global pending_move</field></block></value>
                <value name="B"><block type="text"><field name="TEXT">Btn{i}</field></block></value>
              </block>
            </value>
            <statement name="{do}">
              <block type="component_set_get">
                <mutation component_type="Button" set_or_get="set" property_name="Text" is_generic="false" instance_name="Btn{i}"></mutation>
                <field name="COMPONENT_SELECTOR">Btn{i}</field>
                <field name="PROP">Text</field>
                <value name="VALUE"><block type="lexical_variable_get"><field name="VAR">global turn</field></block></value>
              </block>
            </statement>
"""

xml_content += """
          </block>
        </statement>
        <statement name="ELSE">
          <!-- INCORRECT -->
          <block type="component_method">
            <mutation component_type="Notifier" method_name="ShowAlert" is_generic="false" instance_name="Notifier1"></mutation>
            <field name="COMPONENT_SELECTOR">Notifier1</field>
            <value name="ARG0">
              <block type="text_join">
                <mutation items="2"></mutation>
                <value name="ADD0"><block type="text"><field name="TEXT">Incorrect! Turn passed to the opponent.</field></block></value>
                <value name="ADD1"><block type="text"><field name="TEXT"></field></block></value>
              </block>
            </value>
          </block>
        </statement>
        <next>
          <!-- SWAP TURN & CHECK WIN -->
          <block type="controls_if">
            <mutation else="1"></mutation>
            <value name="IF0">
              <block type="logic_compare">
                <field name="OP">EQ</field>
                <value name="A"><block type="lexical_variable_get"><field name="VAR">global turn</field></block></value>
                <value name="B"><block type="text"><field name="TEXT">X</field></block></value>
              </block>
            </value>
            <statement name="DO0">
              <block type="lexical_variable_set">
                <field name="VAR">global turn</field>
                <value name="VALUE"><block type="text"><field name="TEXT">O</field></block></value>
              </block>
            </statement>
            <statement name="ELSE">
              <block type="lexical_variable_set">
                <field name="VAR">global turn</field>
                <value name="VALUE"><block type="text"><field name="TEXT">X</field></block></value>
              </block>
            </statement>
            <next>
              <block type="component_set_get">
                <mutation component_type="Label" set_or_get="set" property_name="Text" is_generic="false" instance_name="LblTurn"></mutation>
                <field name="COMPONENT_SELECTOR">LblTurn</field>
                <field name="PROP">Text</field>
                <value name="VALUE">
                   <block type="text_join">
                      <mutation items="2"></mutation>
                      <value name="ADD0"><block type="lexical_variable_get"><field name="VAR">global turn</field></block></value>
                      <value name="ADD1"><block type="text"><field name="TEXT"> Turn</field></block></value>
                   </block>
                </value>
                <next>
                  <block type="procedures_callnoreturn">
                    <mutation name="CheckWin"></mutation>
                  </block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </statement>
  </block>

  <block type="component_event" x="-1000" y="1000">
    <mutation component_type="Button" is_generic="false" instance_name="BtnReset" event_name="Click"></mutation>
    <field name="COMPONENT_SELECTOR">BtnReset</field>
    <statement name="DO">
      <block type="procedures_callnoreturn">
        <mutation name="ResetGame"></mutation>
      </block>
    </statement>
  </block>

  <yacodeblocks ya-version="213" language-version="34"></yacodeblocks>
</xml>
"""

# Regex to inject an id attribute to ANY <block> tag that is missing one.
def add_ids(match):
    block_tag = match.group(0)
    if 'id=' not in block_tag:
        return block_tag.replace('<block ', f'<block id="{uuid.uuid4().hex}" ')
    return block_tag

# Apply regex over xml_content
xml_content = re.sub(r'<block\b[^>]*>', add_ids, xml_content)

# Target the proper Screen1.bky file, NOT generate_bky.py itself
output_path = r"c:\Users\Justin\Downloads\LegitNaTo\Extracted\src\appinventor\ai_gordonlu0749\test\Screen1.bky"

with open(output_path, "w", encoding="utf-8") as f:
    f.write(xml_content)
