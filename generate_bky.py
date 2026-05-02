import os

# We will generate a complete Blockly XML string with all 9 buttons and logic.
xml_content = """<xml xmlns="http://www.w3.org/1999/xhtml">
  <block type="global_declaration" id="global_turn" x="-1000" y="-800">
    <field name="NAME">turn</field>
    <value name="VALUE"><block type="text" id="text_turn"><field name="TEXT">X</field></block></value>
  </block>
  <block type="global_declaration" id="global_pending" x="-1000" y="-750">
    <field name="NAME">pending_move</field>
    <value name="VALUE"><block type="text" id="text_pending"><field name="TEXT"></field></block></value>
  </block>
  <block type="global_declaration" id="global_ans" x="-1000" y="-700">
    <field name="NAME">current_answer</field>
    <value name="VALUE"><block type="text" id="text_ans"><field name="TEXT"></field></block></value>
  </block>
  <block type="global_declaration" id="global_q" x="-1000" y="-600">
    <field name="NAME">questions</field>
    <value name="VALUE">
      <block type="lists_create_with" id="list_q">
        <mutation items="3"></mutation>
        <value name="ADD0">
          <block type="lists_create_with" id="q1">
            <mutation items="2"></mutation>
            <value name="ADD0"><block type="text" id="q1_q"><field name="TEXT">What is the capital of France?</field></block></value>
            <value name="ADD1"><block type="text" id="q1_a"><field name="TEXT">paris</field></block></value>
          </block>
        </value>
        <value name="ADD1">
          <block type="lists_create_with" id="q2">
            <mutation items="2"></mutation>
            <value name="ADD0"><block type="text" id="q2_q"><field name="TEXT">What is 5 + 7?</field></block></value>
            <value name="ADD1"><block type="text" id="q2_a"><field name="TEXT">12</field></block></value>
          </block>
        </value>
        <value name="ADD2">
          <block type="lists_create_with" id="q3">
            <mutation items="2"></mutation>
            <value name="ADD0"><block type="text" id="q3_q"><field name="TEXT">What is a firewall? (Hint: security)</field></block></value>
            <value name="ADD1"><block type="text" id="q3_a"><field name="TEXT">security</field></block></value>
          </block>
        </value>
      </block>
    </value>
  </block>

  <block type="procedures_defnoreturn" id="proc_handle" x="-1000" y="-400">
    <mutation><arg name="btnId"></arg></mutation>
    <field name="NAME">HandleMove</field>
    <statement name="STACK">
      <block type="lexical_variable_set" id="set_pending">
        <field name="VAR">global pending_move</field>
        <value name="VALUE"><block type="lexical_variable_get" id="get_btnId"><field name="VAR">btnId</field></block></value>
        <next>
          <block type="procedures_callnoreturn" id="call_ask">
            <mutation name="AskQuestion"></mutation>
          </block>
        </next>
      </block>
    </statement>
  </block>

  <block type="procedures_defnoreturn" id="proc_ask" x="-1000" y="-200">
    <field name="NAME">AskQuestion</field>
    <statement name="STACK">
      <block type="local_declaration_statement" id="local_qpair">
        <mutation><localname name="q_pair"></localname></mutation>
        <field name="VAR0">q_pair</field>
        <value name="DECL0">
          <block type="lists_pick_random_item" id="pick_random">
            <value name="LIST"><block type="lexical_variable_get" id="get_global_q"><field name="VAR">global questions</field></block></value>
          </block>
        </value>
        <statement name="STACK">
          <block type="lexical_variable_set" id="set_ans">
            <field name="VAR">global current_answer</field>
            <value name="VALUE">
              <block type="lists_select_item" id="select_a">
                <value name="LIST"><block type="lexical_variable_get" id="get_qpair1"><field name="VAR">q_pair</field></block></value>
                <value name="NUM"><block type="math_number" id="num_2"><field name="NUM">2</field></block></value>
              </block>
            </value>
            <next>
              <block type="component_method" id="call_notifier">
                <mutation component_type="Notifier" method_name="ShowTextDialog" is_generic="false" instance_name="Notifier1"></mutation>
                <field name="COMPONENT_SELECTOR">Notifier1</field>
                <value name="ARG0">
                  <block type="lists_select_item" id="select_q">
                    <value name="LIST"><block type="lexical_variable_get" id="get_qpair2"><field name="VAR">q_pair</field></block></value>
                    <value name="NUM"><block type="math_number" id="num_1"><field name="NUM">1</field></block></value>
                  </block>
                </value>
                <value name="ARG1"><block type="text" id="title_kg"><field name="TEXT">Knowledge Gate</field></block></value>
                <value name="ARG2"><block type="logic_boolean" id="bool_f"><field name="BOOL">FALSE</field></block></value>
              </block>
            </next>
          </block>
        </statement>
      </block>
    </statement>
  </block>

  <!-- We will map Button clicks -->
"""

for i in range(1, 10):
    xml_content += f"""
  <block type="component_event" id="btn{i}_click" x="-500" y="{i * 100 - 800}">
    <mutation component_type="Button" is_generic="false" instance_name="Btn{i}" event_name="Click"></mutation>
    <field name="COMPONENT_SELECTOR">Btn{i}</field>
    <statement name="DO">
      <block type="controls_if" id="if_btn{i}">
        <value name="IF0">
          <block type="logic_compare" id="cmp_btn{i}">
            <field name="OP">EQ</field>
            <value name="A">
              <block type="component_set_get" id="get_btn{i}">
                <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn{i}"></mutation>
                <field name="COMPONENT_SELECTOR">Btn{i}</field>
                <field name="PROP">Text</field>
              </block>
            </value>
            <value name="B"><block type="text" id="empty_btn{i}"><field name="TEXT">_</field></block></value>
          </block>
        </value>
        <statement name="DO0">
          <block type="procedures_callnoreturn" id="call_handle{i}">
            <mutation name="HandleMove"></mutation>
            <value name="ARG0"><block type="text" id="arg_btn{i}"><field name="TEXT">Btn{i}</field></block></value>
          </block>
        </statement>
      </block>
    </statement>
  </block>
"""

# Next, the Notifier handler. It's simplified: If correct, we update the button using a huge IF/ELSE chain or dynamic component. 
# A big IF/ELSE chain is safer for manual XML generation.
xml_content += """
  <block type="component_event" id="notifier_after" x="-1000" y="200">
    <mutation component_type="Notifier" is_generic="false" instance_name="Notifier1" event_name="AfterTextInput"></mutation>
    <field name="COMPONENT_SELECTOR">Notifier1</field>
    <statement name="DO">
      <block type="controls_if" id="check_ans">
        <mutation else="1"></mutation>
        <value name="IF0">
          <block type="logic_compare" id="cmp_ans">
            <field name="OP">EQ</field>
            <value name="A">
              <block type="text_changeCase" id="lower_res">
                <field name="OP">DOWNCASE</field>
                <value name="STRING"><block type="lexical_variable_get" id="get_res"><mutation><eventparam name="response"></eventparam></mutation><field name="VAR">response</field></block></value>
              </block>
            </value>
            <value name="B">
              <block type="text_changeCase" id="lower_cur">
                <field name="OP">DOWNCASE</field>
                <value name="STRING"><block type="lexical_variable_get" id="get_cur"><field name="VAR">global current_answer</field></block></value>
              </block>
            </value>
          </block>
        </value>
        <statement name="DO0">
          <!-- Update the clicked button -->
          <block type="controls_if" id="update_chain">
            <mutation elseif="8"></mutation>
"""

for i in range(1, 10):
    condition = f"IF{i-1}"
    do = f"DO{i-1}"
    xml_content += f"""
            <value name="{condition}">
              <block type="logic_compare" id="cmp_update{i}">
                <field name="OP">EQ</field>
                <value name="A"><block type="lexical_variable_get" id="get_pending{i}"><field name="VAR">global pending_move</field></block></value>
                <value name="B"><block type="text" id="text_pending{i}"><field name="TEXT">Btn{i}</field></block></value>
              </block>
            </value>
            <statement name="{do}">
              <block type="component_set_get" id="set_btn{i}">
                <mutation component_type="Button" set_or_get="set" property_name="Text" is_generic="false" instance_name="Btn{i}"></mutation>
                <field name="COMPONENT_SELECTOR">Btn{i}</field>
                <field name="PROP">Text</field>
                <value name="VALUE"><block type="lexical_variable_get" id="get_turn{i}"><field name="VAR">global turn</field></block></value>
              </block>
            </statement>
"""

xml_content += """
          </block>
        </statement>
        <next>
          <!-- Swap Turn (Happens whether correct or wrong to skip turn) -->
          <block type="controls_if" id="swap_turn">
            <mutation else="1"></mutation>
            <value name="IF0">
              <block type="logic_compare" id="cmp_turn">
                <field name="OP">EQ</field>
                <value name="A"><block type="lexical_variable_get" id="get_turn_swap1"><field name="VAR">global turn</field></block></value>
                <value name="B"><block type="text" id="text_x"><field name="TEXT">X</field></block></value>
              </block>
            </value>
            <statement name="DO0">
              <block type="lexical_variable_set" id="set_o">
                <field name="VAR">global turn</field>
                <value name="VALUE"><block type="text" id="text_o2"><field name="TEXT">O</field></block></value>
              </block>
            </statement>
            <statement name="ELSE">
              <block type="lexical_variable_set" id="set_x">
                <field name="VAR">global turn</field>
                <value name="VALUE"><block type="text" id="text_x2"><field name="TEXT">X</field></block></value>
              </block>
            </statement>
            <next>
              <block type="component_set_get" id="set_lbl">
                <mutation component_type="Label" set_or_get="set" property_name="Text" is_generic="false" instance_name="LblTurn"></mutation>
                <field name="COMPONENT_SELECTOR">LblTurn</field>
                <field name="PROP">Text</field>
                <value name="VALUE"><block type="lexical_variable_get" id="get_turn_swap2"><field name="VAR">global turn</field></block></value>
              </block>
            </next>
          </block>
        </next>
      </block>
    </statement>
  </block>

  <block type="component_event" id="reset_click" x="-1000" y="1000">
    <mutation component_type="Button" is_generic="false" instance_name="BtnReset" event_name="Click"></mutation>
    <field name="COMPONENT_SELECTOR">BtnReset</field>
    <statement name="DO">
"""

# Reset all buttons
for i in range(1, 10):
    xml_content += f"""
      <block type="component_set_get" id="reset_btn{i}">
        <mutation component_type="Button" set_or_get="set" property_name="Text" is_generic="false" instance_name="Btn{i}"></mutation>
        <field name="COMPONENT_SELECTOR">Btn{i}</field>
        <field name="PROP">Text</field>
        <value name="VALUE"><block type="text" id="empty_reset{i}"><field name="TEXT">_</field></block></value>
        <next>
"""
xml_content += """
        <block type="lexical_variable_set" id="reset_turn">
          <field name="VAR">global turn</field>
          <value name="VALUE"><block type="text" id="text_reset_x"><field name="TEXT">X</field></block></value>
        </block>
"""
for i in range(1, 10):
    xml_content += "</next></block>"

xml_content += """
    </statement>
  </block>

  <yacodeblocks ya-version="213" language-version="34"></yacodeblocks>
</xml>
"""

with open("c:/Users/Justin/Downloads/LegitNaTo/Extracted/src/appinventor/ai_gordonlu0749/test/Screen1.bky", "w") as f:
    f.write(xml_content)
