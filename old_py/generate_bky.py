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
  <block type="global_declaration" x="-1000" y="-600">
    <field name="NAME">selected_difficulty</field>
    <value name="VALUE"><block type="text"><field name="TEXT">EASY</field></block></value>
  </block>
"""

# Question matrix
categories = {
    "q_geo_easy": [
        ("Capital of France?", "paris"),
        ("Capital of Japan?", "tokyo"),
        ("What continent is Brazil in?", "south america"),
        ("How many oceans are there?", "5"),
        ("Which country has the most people?", "india"),
        ("What is the largest continent?", "asia")
    ],
    "q_geo_med": [
        ("Capital of Australia?", "canberra"),
        ("Capital of Canada?", "ottawa"),
        ("Which river flows through Egypt?", "nile"),
        ("What is the smallest country in the world?", "vatican city"),
        ("Mount Everest is in which mountain range?", "himalayas"),
        ("What country is shaped like a boot?", "italy")
    ],
    "q_geo_hard": [
        ("Capital of Burkina Faso?", "ouagadougou"),
        ("Capital of Madagascar?", "antananarivo"),
        ("Which African country was formerly known as Abyssinia?", "ethiopia"),
        ("What is the deepest trench in the ocean?", "mariana trench"),
        ("Which country borders 14 nations and crosses 11 time zones?", "russia"),
        ("What is the capital of Mongolia?", "ulaanbaatar")
    ],
    "q_math_easy": [
        ("What is 5 + 7?", "12"),
        ("What is 20 - 6?", "14"),
        ("What is 3 x 4?", "12"),
        ("What is 10 / 2?", "5"),
        ("How many sides does a hexagon have?", "6"),
        ("What is 15 - 8?", "7")
    ],
    "q_math_med": [
        ("What is 12 * 12?", "144"),
        ("What is 56 / 8?", "7"),
        ("What is the square root of 81?", "9"),
        ("What is 15% of 100?", "15"),
        ("If x = 3, what is 2x + 4?", "10"),
        ("How many degrees in a right angle?", "90")
    ],
    "q_math_hard": [
        ("Square root of 225?", "15"),
        ("2 to the power of 8?", "256"),
        ("What is the value of Pi to two decimal places?", "3.14"),
        ("What is the derivative of x squared?", "2x"),
        ("If a triangle has sides 3 and 4, what is the hypotenuse?", "5"),
        ("What is the logarithm of 100 to base 10?", "2")
    ],
    "q_trivia_easy": [
        ("Color of a school bus?", "yellow"),
        ("How many legs does a spider have?", "8"),
        ("What sound does a cow make?", "moo"),
        ("What is the opposite of cold?", "hot"),
        ("How many days are in a week?", "7"),
        ("What color are apples usually?", "red")
    ],
    "q_trivia_med": [
        ("How many continents are there?", "7"),
        ("Who wrote Romeo and Juliet?", "shakespeare"),
        ("What planet is known as the Red Planet?", "mars"),
        ("What do bees produce?", "honey"),
        ("How many colors are in a rainbow?", "7"),
        ("What is the main ingredient in guacamole?", "avocado")
    ],
    "q_trivia_hard": [
        ("A network security system? (Hint: firewall)", "firewall"),
        ("What element is 'Fe' on the periodic table?", "iron"),
        ("Who painted the Mona Lisa?", "da vinci"),
        ("What is the hardest natural substance on Earth?", "diamond"),
        ("What is the speed of light in vacuum? (in km/s, approx)", "300000"),
        ("Who invented the telephone?", "bell")
    ]
}

y_pos = -500
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

# Navigation Buttons (Category -> Difficulty)
nav_categories = [("BtnGeo", "GEO"), ("BtnMath", "MATH"), ("BtnTrivia", "TRIV")]
for btn, val in nav_categories:
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
                <mutation component_type="VerticalArrangement" set_or_get="set" property_name="Visible" is_generic="false" instance_name="ViewDifficulty"></mutation>
                <field name="COMPONENT_SELECTOR">ViewDifficulty</field>
                <field name="PROP">Visible</field>
                <value name="VALUE"><block type="logic_boolean"><field name="BOOL">TRUE</field></block></value>
              </block>
            </next>
          </block>
        </next>
      </block>
    </statement>
  </block>
"""
    y_pos += 100

# Navigation Buttons (Difficulty -> Game)
nav_diff = [("BtnEasy", "EASY"), ("BtnMed", "MED"), ("BtnHard", "HARD")]
for btn, val in nav_diff:
    xml_content += f"""
  <block type="component_event" x="-1500" y="{y_pos}">
    <mutation component_type="Button" is_generic="false" instance_name="{btn}" event_name="Click"></mutation>
    <field name="COMPONENT_SELECTOR">{btn}</field>
    <statement name="DO">
      <block type="lexical_variable_set">
        <field name="VAR">global selected_difficulty</field>
        <value name="VALUE"><block type="text"><field name="TEXT">{val}</field></block></value>
        <next>
          <block type="component_set_get">
            <mutation component_type="VerticalArrangement" set_or_get="set" property_name="Visible" is_generic="false" instance_name="ViewDifficulty"></mutation>
            <field name="COMPONENT_SELECTOR">ViewDifficulty</field>
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

# BtnBack Click (Return to Category from Game)
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
            <mutation component_type="VerticalArrangement" set_or_get="set" property_name="Visible" is_generic="false" instance_name="ViewDifficulty"></mutation>
            <field name="COMPONENT_SELECTOR">ViewDifficulty</field>
            <field name="PROP">Visible</field>
            <value name="VALUE"><block type="logic_boolean"><field name="BOOL">FALSE</field></block></value>
            <next>
              <block type="component_set_get">
                <mutation component_type="VerticalArrangement" set_or_get="set" property_name="Visible" is_generic="false" instance_name="ViewGame"></mutation>
                <field name="COMPONENT_SELECTOR">ViewGame</field>
                <field name="PROP">Visible</field>
                <value name="VALUE"><block type="logic_boolean"><field name="BOOL">FALSE</field></block></value>
              </block>
            </next>
          </block>
        </next>
      </block>
    </statement>
  </block>
"""

# HandleMove
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

  <!-- Ask Question (with strict Category + Difficulty routing) -->
  <block type="global_declaration" x="-1000" y="-150">
    <field name="NAME">current_q_pair</field>
    <value name="VALUE"><block type="lists_create_with"><mutation items="0"></mutation></block></value>
  </block>

  <block type="procedures_defnoreturn" x="-1000" y="-100">
    <field name="NAME">AskQuestion</field>
    <statement name="STACK">
      <block type="controls_if">
        <mutation elseif="8"></mutation>
        <!-- Geo Easy -->
        <value name="IF0">
          <block type="logic_operation">
            <field name="OP">AND</field>
            <value name="A"><block type="logic_compare"><field name="OP">EQ</field><value name="A"><block type="lexical_variable_get"><field name="VAR">global selected_category</field></block></value><value name="B"><block type="text"><field name="TEXT">GEO</field></block></value></block></value>
            <value name="B"><block type="logic_compare"><field name="OP">EQ</field><value name="A"><block type="lexical_variable_get"><field name="VAR">global selected_difficulty</field></block></value><value name="B"><block type="text"><field name="TEXT">EASY</field></block></value></block></value>
          </block>
        </value>
        <statement name="DO0">
          <block type="lexical_variable_set"><field name="VAR">global current_q_pair</field><value name="VALUE"><block type="lists_pick_random_item"><value name="LIST"><block type="lexical_variable_get"><field name="VAR">global q_geo_easy</field></block></value></block></value></block>
        </statement>
        <!-- Geo Med -->
        <value name="IF1">
          <block type="logic_operation">
            <field name="OP">AND</field>
            <value name="A"><block type="logic_compare"><field name="OP">EQ</field><value name="A"><block type="lexical_variable_get"><field name="VAR">global selected_category</field></block></value><value name="B"><block type="text"><field name="TEXT">GEO</field></block></value></block></value>
            <value name="B"><block type="logic_compare"><field name="OP">EQ</field><value name="A"><block type="lexical_variable_get"><field name="VAR">global selected_difficulty</field></block></value><value name="B"><block type="text"><field name="TEXT">MED</field></block></value></block></value>
          </block>
        </value>
        <statement name="DO1">
          <block type="lexical_variable_set"><field name="VAR">global current_q_pair</field><value name="VALUE"><block type="lists_pick_random_item"><value name="LIST"><block type="lexical_variable_get"><field name="VAR">global q_geo_med</field></block></value></block></value></block>
        </statement>
        <!-- Geo Hard -->
        <value name="IF2">
          <block type="logic_operation">
            <field name="OP">AND</field>
            <value name="A"><block type="logic_compare"><field name="OP">EQ</field><value name="A"><block type="lexical_variable_get"><field name="VAR">global selected_category</field></block></value><value name="B"><block type="text"><field name="TEXT">GEO</field></block></value></block></value>
            <value name="B"><block type="logic_compare"><field name="OP">EQ</field><value name="A"><block type="lexical_variable_get"><field name="VAR">global selected_difficulty</field></block></value><value name="B"><block type="text"><field name="TEXT">HARD</field></block></value></block></value>
          </block>
        </value>
        <statement name="DO2">
          <block type="lexical_variable_set"><field name="VAR">global current_q_pair</field><value name="VALUE"><block type="lists_pick_random_item"><value name="LIST"><block type="lexical_variable_get"><field name="VAR">global q_geo_hard</field></block></value></block></value></block>
        </statement>

        <!-- Math Easy -->
        <value name="IF3">
          <block type="logic_operation">
            <field name="OP">AND</field>
            <value name="A"><block type="logic_compare"><field name="OP">EQ</field><value name="A"><block type="lexical_variable_get"><field name="VAR">global selected_category</field></block></value><value name="B"><block type="text"><field name="TEXT">MATH</field></block></value></block></value>
            <value name="B"><block type="logic_compare"><field name="OP">EQ</field><value name="A"><block type="lexical_variable_get"><field name="VAR">global selected_difficulty</field></block></value><value name="B"><block type="text"><field name="TEXT">EASY</field></block></value></block></value>
          </block>
        </value>
        <statement name="DO3">
          <block type="lexical_variable_set"><field name="VAR">global current_q_pair</field><value name="VALUE"><block type="lists_pick_random_item"><value name="LIST"><block type="lexical_variable_get"><field name="VAR">global q_math_easy</field></block></value></block></value></block>
        </statement>
        <!-- Math Med -->
        <value name="IF4">
          <block type="logic_operation">
            <field name="OP">AND</field>
            <value name="A"><block type="logic_compare"><field name="OP">EQ</field><value name="A"><block type="lexical_variable_get"><field name="VAR">global selected_category</field></block></value><value name="B"><block type="text"><field name="TEXT">MATH</field></block></value></block></value>
            <value name="B"><block type="logic_compare"><field name="OP">EQ</field><value name="A"><block type="lexical_variable_get"><field name="VAR">global selected_difficulty</field></block></value><value name="B"><block type="text"><field name="TEXT">MED</field></block></value></block></value>
          </block>
        </value>
        <statement name="DO4">
          <block type="lexical_variable_set"><field name="VAR">global current_q_pair</field><value name="VALUE"><block type="lists_pick_random_item"><value name="LIST"><block type="lexical_variable_get"><field name="VAR">global q_math_med</field></block></value></block></value></block>
        </statement>
        <!-- Math Hard -->
        <value name="IF5">
          <block type="logic_operation">
            <field name="OP">AND</field>
            <value name="A"><block type="logic_compare"><field name="OP">EQ</field><value name="A"><block type="lexical_variable_get"><field name="VAR">global selected_category</field></block></value><value name="B"><block type="text"><field name="TEXT">MATH</field></block></value></block></value>
            <value name="B"><block type="logic_compare"><field name="OP">EQ</field><value name="A"><block type="lexical_variable_get"><field name="VAR">global selected_difficulty</field></block></value><value name="B"><block type="text"><field name="TEXT">HARD</field></block></value></block></value>
          </block>
        </value>
        <statement name="DO5">
          <block type="lexical_variable_set"><field name="VAR">global current_q_pair</field><value name="VALUE"><block type="lists_pick_random_item"><value name="LIST"><block type="lexical_variable_get"><field name="VAR">global q_math_hard</field></block></value></block></value></block>
        </statement>

        <!-- Trivia Easy -->
        <value name="IF6">
          <block type="logic_operation">
            <field name="OP">AND</field>
            <value name="A"><block type="logic_compare"><field name="OP">EQ</field><value name="A"><block type="lexical_variable_get"><field name="VAR">global selected_category</field></block></value><value name="B"><block type="text"><field name="TEXT">TRIV</field></block></value></block></value>
            <value name="B"><block type="logic_compare"><field name="OP">EQ</field><value name="A"><block type="lexical_variable_get"><field name="VAR">global selected_difficulty</field></block></value><value name="B"><block type="text"><field name="TEXT">EASY</field></block></value></block></value>
          </block>
        </value>
        <statement name="DO6">
          <block type="lexical_variable_set"><field name="VAR">global current_q_pair</field><value name="VALUE"><block type="lists_pick_random_item"><value name="LIST"><block type="lexical_variable_get"><field name="VAR">global q_trivia_easy</field></block></value></block></value></block>
        </statement>
        <!-- Trivia Med -->
        <value name="IF7">
          <block type="logic_operation">
            <field name="OP">AND</field>
            <value name="A"><block type="logic_compare"><field name="OP">EQ</field><value name="A"><block type="lexical_variable_get"><field name="VAR">global selected_category</field></block></value><value name="B"><block type="text"><field name="TEXT">TRIV</field></block></value></block></value>
            <value name="B"><block type="logic_compare"><field name="OP">EQ</field><value name="A"><block type="lexical_variable_get"><field name="VAR">global selected_difficulty</field></block></value><value name="B"><block type="text"><field name="TEXT">MED</field></block></value></block></value>
          </block>
        </value>
        <statement name="DO7">
          <block type="lexical_variable_set"><field name="VAR">global current_q_pair</field><value name="VALUE"><block type="lists_pick_random_item"><value name="LIST"><block type="lexical_variable_get"><field name="VAR">global q_trivia_med</field></block></value></block></value></block>
        </statement>
        <!-- Trivia Hard -->
        <value name="IF8">
          <block type="logic_operation">
            <field name="OP">AND</field>
            <value name="A"><block type="logic_compare"><field name="OP">EQ</field><value name="A"><block type="lexical_variable_get"><field name="VAR">global selected_category</field></block></value><value name="B"><block type="text"><field name="TEXT">TRIV</field></block></value></block></value>
            <value name="B"><block type="logic_compare"><field name="OP">EQ</field><value name="A"><block type="lexical_variable_get"><field name="VAR">global selected_difficulty</field></block></value><value name="B"><block type="text"><field name="TEXT">HARD</field></block></value></block></value>
          </block>
        </value>
        <statement name="DO8">
          <block type="lexical_variable_set"><field name="VAR">global current_q_pair</field><value name="VALUE"><block type="lists_pick_random_item"><value name="LIST"><block type="lexical_variable_get"><field name="VAR">global q_trivia_hard</field></block></value></block></value></block>
        </statement>
        <next>
          <block type="lexical_variable_set">
            <field name="VAR">global current_answer</field>
            <value name="VALUE">
              <block type="lists_select_item">
                <value name="LIST"><block type="lexical_variable_get"><field name="VAR">global current_q_pair</field></block></value>
                <value name="NUM"><block type="math_number"><field name="NUM">2</field></block></value>
              </block>
            </value>
            <next>
              <block type="component_method">
                <mutation component_type="Notifier" method_name="ShowTextDialog" is_generic="false" instance_name="Notifier1"></mutation>
                <field name="COMPONENT_SELECTOR">Notifier1</field>
                <value name="ARG0">
                  <block type="lists_select_item">
                    <value name="LIST"><block type="lexical_variable_get"><field name="VAR">global current_q_pair</field></block></value>
                    <value name="NUM"><block type="math_number"><field name="NUM">1</field></block></value>
                  </block>
                </value>
                <value name="ARG1"><block type="text"><field name="TEXT">Knowledge Gate</field></block></value>
                <value name="ARG2"><block type="logic_boolean"><field name="BOOL">FALSE</field></block></value>
              </block>
            </next>
          </block>
        </next>
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
                    <mutation component_type="Notifier" method_name="ShowMessageDialog" is_generic="false" instance_name="Notifier1"></mutation>
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
                    <value name="ARG1"><block type="text"><field name="TEXT">Game Over!</field></block></value>
                    <value name="ARG2"><block type="text"><field name="TEXT">OK</field></block></value>
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

# Tie checking logic (added as the final "next" in the CheckWin chain)
xml_content += """
          <!-- Tie Logic -->
          <block type="controls_if">
            <value name="IF0">
              <block type="logic_boolean"><field name="BOOL">TRUE</field></block>
            </value>
            <statement name="DO0">
              <block type="controls_if">
"""

tie_condition = ""
for i in range(1, 10):
    tie_condition += f"""
                <value name="A">
                  <block type="logic_compare">
                    <field name="OP">NEQ</field>
                    <value name="A"><block type="component_set_get"><mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn{i}"></mutation><field name="COMPONENT_SELECTOR">Btn{i}</field><field name="PROP">Text</field></block></value>
                    <value name="B"><block type="text"><field name="TEXT">_</field></block></value>
                  </block>
                </value>
"""
    if i < 9:
        tie_condition += '<value name="B"><block type="logic_operation"><field name="OP">AND</field>'

tie_condition += "</block></value>" * 8 # Close logic operations

xml_content += f"""
                <value name="IF0">
                  <block type="logic_operation"><field name="OP">AND</field>
                    {tie_condition}
                  </block>
                </value>
                <statement name="DO0">
                  <block type="component_method">
                    <mutation component_type="Notifier" method_name="ShowMessageDialog" is_generic="false" instance_name="Notifier1"></mutation>
                    <field name="COMPONENT_SELECTOR">Notifier1</field>
                    <value name="ARG0"><block type="text"><field name="TEXT">It's a Tie!</field></block></value>
                    <value name="ARG1"><block type="text"><field name="TEXT">Game Over</field></block></value>
                    <value name="ARG2"><block type="text"><field name="TEXT">OK</field></block></value>
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
          <block type="logic_operation">
            <field name="OP">AND</field>
            <!-- Check that response is NOT EMPTY -->
            <value name="A">
              <block type="logic_compare">
                <field name="OP">NEQ</field>
                <value name="A">
                  <block type="text_trim">
                    <value name="TEXT"><block type="lexical_variable_get"><mutation><eventparam name="response"></eventparam></mutation><field name="VAR">response</field></block></value>
                  </block>
                </value>
                <value name="B"><block type="text"><field name="TEXT"></field></block></value>
              </block>
            </value>
            <!-- Check that response equals current_answer -->
            <value name="B">
              <block type="logic_compare">
                <field name="OP">EQ</field>
                <value name="A">
                  <block type="text_changeCase">
                    <field name="OP">DOWNCASE</field>
                    <value name="TEXT">
                      <block type="text_trim">
                        <value name="TEXT"><block type="lexical_variable_get"><mutation><eventparam name="response"></eventparam></mutation><field name="VAR">response</field></block></value>
                      </block>
                    </value>
                  </block>
                </value>
                <value name="B">
                  <block type="text_changeCase">
                    <field name="OP">DOWNCASE</field>
                    <value name="TEXT"><block type="lexical_variable_get"><field name="VAR">global current_answer</field></block></value>
                  </block>
                </value>
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
          <!-- INCORRECT - Using ShowMessageDialog to force user to acknowledge -->
          <block type="component_method">
            <mutation component_type="Notifier" method_name="ShowMessageDialog" is_generic="false" instance_name="Notifier1"></mutation>
            <field name="COMPONENT_SELECTOR">Notifier1</field>
            <value name="ARG0"><block type="text"><field name="TEXT">Incorrect! Turn passed to the opponent.</field></block></value>
            <value name="ARG1"><block type="text"><field name="TEXT">Oops!</field></block></value>
            <value name="ARG2"><block type="text"><field name="TEXT">OK</field></block></value>
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

# Target the proper Screen1.bky file
output_path = r"c:\Users\Justin\Downloads\LegitNaTo\Extracted\src\appinventor\ai_gordonlu0749\test\Screen1.bky"

with open(output_path, "w", encoding="utf-8") as f:
    f.write(xml_content)
