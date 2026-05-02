<xml xmlns="http://www.w3.org/1999/xhtml">
  <block type="global_declaration" id="global_turn" x="-1000" y="-800">
    <field name="NAME">turn</field>
    <value name="VALUE"><block type="text"><field name="TEXT">X</field></block></value>
  </block>
  <block type="global_declaration" id="global_pending" x="-1000" y="-750">
    <field name="NAME">pending_move</field>
    <value name="VALUE"><block type="text"><field name="TEXT"></field></block></value>
  </block>
  <block type="global_declaration" id="global_ans" x="-1000" y="-700">
    <field name="NAME">current_answer</field>
    <value name="VALUE"><block type="text"><field name="TEXT"></field></block></value>
  </block>
  <block type="global_declaration" id="global_cat" x="-1000" y="-650">
    <field name="NAME">selected_category</field>
    <value name="VALUE"><block type="text"><field name="TEXT">GEO</field></block></value>
  </block>

  <block type="global_declaration" id="global_q_geo" x="-1000" y="-600">
    <field name="NAME">q_geo</field>
    <value name="VALUE">
      <block type="lists_create_with">
        <mutation items="3"></mutation>

        <value name="ADD0">
          <block type="lists_create_with">
            <mutation items="2"></mutation>
            <value name="ADD0"><block type="text"><field name="TEXT">Geo Easy: Capital of France?</field></block></value>
            <value name="ADD1"><block type="text"><field name="TEXT">paris</field></block></value>
          </block>
        </value>

        <value name="ADD1">
          <block type="lists_create_with">
            <mutation items="2"></mutation>
            <value name="ADD0"><block type="text"><field name="TEXT">Geo Med: Capital of Australia?</field></block></value>
            <value name="ADD1"><block type="text"><field name="TEXT">canberra</field></block></value>
          </block>
        </value>

        <value name="ADD2">
          <block type="lists_create_with">
            <mutation items="2"></mutation>
            <value name="ADD0"><block type="text"><field name="TEXT">Geo Hard: Capital of Burkina Faso?</field></block></value>
            <value name="ADD1"><block type="text"><field name="TEXT">ouagadougou</field></block></value>
          </block>
        </value>

      </block>
    </value>
  </block>

  <block type="global_declaration" id="global_q_math" x="-1000" y="-550">
    <field name="NAME">q_math</field>
    <value name="VALUE">
      <block type="lists_create_with">
        <mutation items="3"></mutation>

        <value name="ADD0">
          <block type="lists_create_with">
            <mutation items="2"></mutation>
            <value name="ADD0"><block type="text"><field name="TEXT">Math Easy: What is 5 + 7?</field></block></value>
            <value name="ADD1"><block type="text"><field name="TEXT">12</field></block></value>
          </block>
        </value>

        <value name="ADD1">
          <block type="lists_create_with">
            <mutation items="2"></mutation>
            <value name="ADD0"><block type="text"><field name="TEXT">Math Med: What is 12 * 12?</field></block></value>
            <value name="ADD1"><block type="text"><field name="TEXT">144</field></block></value>
          </block>
        </value>

        <value name="ADD2">
          <block type="lists_create_with">
            <mutation items="2"></mutation>
            <value name="ADD0"><block type="text"><field name="TEXT">Math Hard: Square root of 225?</field></block></value>
            <value name="ADD1"><block type="text"><field name="TEXT">15</field></block></value>
          </block>
        </value>

      </block>
    </value>
  </block>

  <block type="global_declaration" id="global_q_trivia" x="-1000" y="-500">
    <field name="NAME">q_trivia</field>
    <value name="VALUE">
      <block type="lists_create_with">
        <mutation items="3"></mutation>

        <value name="ADD0">
          <block type="lists_create_with">
            <mutation items="2"></mutation>
            <value name="ADD0"><block type="text"><field name="TEXT">Trivia Easy: Color of a school bus?</field></block></value>
            <value name="ADD1"><block type="text"><field name="TEXT">yellow</field></block></value>
          </block>
        </value>

        <value name="ADD1">
          <block type="lists_create_with">
            <mutation items="2"></mutation>
            <value name="ADD0"><block type="text"><field name="TEXT">Trivia Med: How many continents are there?</field></block></value>
            <value name="ADD1"><block type="text"><field name="TEXT">7</field></block></value>
          </block>
        </value>

        <value name="ADD2">
          <block type="lists_create_with">
            <mutation items="2"></mutation>
            <value name="ADD0"><block type="text"><field name="TEXT">Trivia Hard: A network security system? (Hint: firewall)</field></block></value>
            <value name="ADD1"><block type="text"><field name="TEXT">firewall</field></block></value>
          </block>
        </value>

      </block>
    </value>
  </block>

  <block type="component_event" x="-1500" y="-450">
    <mutation component_type="Button" is_generic="false" instance_name="BtnGeo" event_name="Click"></mutation>
    <field name="COMPONENT_SELECTOR">BtnGeo</field>
    <statement name="DO">
      <block type="lexical_variable_set">
        <field name="VAR">global selected_category</field>
        <value name="VALUE"><block type="text"><field name="TEXT">GEO</field></block></value>
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

  <block type="component_event" x="-1500" y="-350">
    <mutation component_type="Button" is_generic="false" instance_name="BtnMath" event_name="Click"></mutation>
    <field name="COMPONENT_SELECTOR">BtnMath</field>
    <statement name="DO">
      <block type="lexical_variable_set">
        <field name="VAR">global selected_category</field>
        <value name="VALUE"><block type="text"><field name="TEXT">MATH</field></block></value>
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

  <block type="component_event" x="-1500" y="-250">
    <mutation component_type="Button" is_generic="false" instance_name="BtnTrivia" event_name="Click"></mutation>
    <field name="COMPONENT_SELECTOR">BtnTrivia</field>
    <statement name="DO">
      <block type="lexical_variable_set">
        <field name="VAR">global selected_category</field>
        <value name="VALUE"><block type="text"><field name="TEXT">TRIV</field></block></value>
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

  <block type="component_event" x="-1500" y="-150">
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

  <!-- Ask Question (with Category filter) -->
  <block type="procedures_defnoreturn" id="proc_ask" x="-1000" y="-200">
    <field name="NAME">AskQuestion</field>
    <statement name="STACK">
      <block type="local_declaration_statement" id="local_qpair">
        <mutation><localname name="q_pair"></localname></mutation>
        <field name="VAR0">q_pair</field>
        <value name="DECL0">
          <!-- Nested IFs for categories -->
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

  <block type="component_event" id="btn1_click" x="-500" y="-700">
    <mutation component_type="Button" is_generic="false" instance_name="Btn1" event_name="Click"></mutation>
    <field name="COMPONENT_SELECTOR">Btn1</field>
    <statement name="DO">
      <block type="controls_if" id="if_btn1">
        <value name="IF0">
          <block type="logic_compare" id="cmp_btn1">
            <field name="OP">EQ</field>
            <value name="A">
              <block type="component_set_get" id="get_btn1">
                <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn1"></mutation>
                <field name="COMPONENT_SELECTOR">Btn1</field>
                <field name="PROP">Text</field>
              </block>
            </value>
            <value name="B"><block type="text" id="empty_btn1"><field name="TEXT">_</field></block></value>
          </block>
        </value>
        <statement name="DO0">
          <block type="procedures_callnoreturn" id="call_handle1">
            <mutation name="HandleMove"><arg name="btnId"></arg></mutation>
            <value name="ARG0"><block type="text" id="arg_btn1"><field name="TEXT">Btn1</field></block></value>
          </block>
        </statement>
      </block>
    </statement>
  </block>

  <block type="component_event" id="btn2_click" x="-500" y="-600">
    <mutation component_type="Button" is_generic="false" instance_name="Btn2" event_name="Click"></mutation>
    <field name="COMPONENT_SELECTOR">Btn2</field>
    <statement name="DO">
      <block type="controls_if" id="if_btn2">
        <value name="IF0">
          <block type="logic_compare" id="cmp_btn2">
            <field name="OP">EQ</field>
            <value name="A">
              <block type="component_set_get" id="get_btn2">
                <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn2"></mutation>
                <field name="COMPONENT_SELECTOR">Btn2</field>
                <field name="PROP">Text</field>
              </block>
            </value>
            <value name="B"><block type="text" id="empty_btn2"><field name="TEXT">_</field></block></value>
          </block>
        </value>
        <statement name="DO0">
          <block type="procedures_callnoreturn" id="call_handle2">
            <mutation name="HandleMove"><arg name="btnId"></arg></mutation>
            <value name="ARG0"><block type="text" id="arg_btn2"><field name="TEXT">Btn2</field></block></value>
          </block>
        </statement>
      </block>
    </statement>
  </block>

  <block type="component_event" id="btn3_click" x="-500" y="-500">
    <mutation component_type="Button" is_generic="false" instance_name="Btn3" event_name="Click"></mutation>
    <field name="COMPONENT_SELECTOR">Btn3</field>
    <statement name="DO">
      <block type="controls_if" id="if_btn3">
        <value name="IF0">
          <block type="logic_compare" id="cmp_btn3">
            <field name="OP">EQ</field>
            <value name="A">
              <block type="component_set_get" id="get_btn3">
                <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn3"></mutation>
                <field name="COMPONENT_SELECTOR">Btn3</field>
                <field name="PROP">Text</field>
              </block>
            </value>
            <value name="B"><block type="text" id="empty_btn3"><field name="TEXT">_</field></block></value>
          </block>
        </value>
        <statement name="DO0">
          <block type="procedures_callnoreturn" id="call_handle3">
            <mutation name="HandleMove"><arg name="btnId"></arg></mutation>
            <value name="ARG0"><block type="text" id="arg_btn3"><field name="TEXT">Btn3</field></block></value>
          </block>
        </statement>
      </block>
    </statement>
  </block>

  <block type="component_event" id="btn4_click" x="-500" y="-400">
    <mutation component_type="Button" is_generic="false" instance_name="Btn4" event_name="Click"></mutation>
    <field name="COMPONENT_SELECTOR">Btn4</field>
    <statement name="DO">
      <block type="controls_if" id="if_btn4">
        <value name="IF0">
          <block type="logic_compare" id="cmp_btn4">
            <field name="OP">EQ</field>
            <value name="A">
              <block type="component_set_get" id="get_btn4">
                <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn4"></mutation>
                <field name="COMPONENT_SELECTOR">Btn4</field>
                <field name="PROP">Text</field>
              </block>
            </value>
            <value name="B"><block type="text" id="empty_btn4"><field name="TEXT">_</field></block></value>
          </block>
        </value>
        <statement name="DO0">
          <block type="procedures_callnoreturn" id="call_handle4">
            <mutation name="HandleMove"><arg name="btnId"></arg></mutation>
            <value name="ARG0"><block type="text" id="arg_btn4"><field name="TEXT">Btn4</field></block></value>
          </block>
        </statement>
      </block>
    </statement>
  </block>

  <block type="component_event" id="btn5_click" x="-500" y="-300">
    <mutation component_type="Button" is_generic="false" instance_name="Btn5" event_name="Click"></mutation>
    <field name="COMPONENT_SELECTOR">Btn5</field>
    <statement name="DO">
      <block type="controls_if" id="if_btn5">
        <value name="IF0">
          <block type="logic_compare" id="cmp_btn5">
            <field name="OP">EQ</field>
            <value name="A">
              <block type="component_set_get" id="get_btn5">
                <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn5"></mutation>
                <field name="COMPONENT_SELECTOR">Btn5</field>
                <field name="PROP">Text</field>
              </block>
            </value>
            <value name="B"><block type="text" id="empty_btn5"><field name="TEXT">_</field></block></value>
          </block>
        </value>
        <statement name="DO0">
          <block type="procedures_callnoreturn" id="call_handle5">
            <mutation name="HandleMove"><arg name="btnId"></arg></mutation>
            <value name="ARG0"><block type="text" id="arg_btn5"><field name="TEXT">Btn5</field></block></value>
          </block>
        </statement>
      </block>
    </statement>
  </block>

  <block type="component_event" id="btn6_click" x="-500" y="-200">
    <mutation component_type="Button" is_generic="false" instance_name="Btn6" event_name="Click"></mutation>
    <field name="COMPONENT_SELECTOR">Btn6</field>
    <statement name="DO">
      <block type="controls_if" id="if_btn6">
        <value name="IF0">
          <block type="logic_compare" id="cmp_btn6">
            <field name="OP">EQ</field>
            <value name="A">
              <block type="component_set_get" id="get_btn6">
                <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn6"></mutation>
                <field name="COMPONENT_SELECTOR">Btn6</field>
                <field name="PROP">Text</field>
              </block>
            </value>
            <value name="B"><block type="text" id="empty_btn6"><field name="TEXT">_</field></block></value>
          </block>
        </value>
        <statement name="DO0">
          <block type="procedures_callnoreturn" id="call_handle6">
            <mutation name="HandleMove"><arg name="btnId"></arg></mutation>
            <value name="ARG0"><block type="text" id="arg_btn6"><field name="TEXT">Btn6</field></block></value>
          </block>
        </statement>
      </block>
    </statement>
  </block>

  <block type="component_event" id="btn7_click" x="-500" y="-100">
    <mutation component_type="Button" is_generic="false" instance_name="Btn7" event_name="Click"></mutation>
    <field name="COMPONENT_SELECTOR">Btn7</field>
    <statement name="DO">
      <block type="controls_if" id="if_btn7">
        <value name="IF0">
          <block type="logic_compare" id="cmp_btn7">
            <field name="OP">EQ</field>
            <value name="A">
              <block type="component_set_get" id="get_btn7">
                <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn7"></mutation>
                <field name="COMPONENT_SELECTOR">Btn7</field>
                <field name="PROP">Text</field>
              </block>
            </value>
            <value name="B"><block type="text" id="empty_btn7"><field name="TEXT">_</field></block></value>
          </block>
        </value>
        <statement name="DO0">
          <block type="procedures_callnoreturn" id="call_handle7">
            <mutation name="HandleMove"><arg name="btnId"></arg></mutation>
            <value name="ARG0"><block type="text" id="arg_btn7"><field name="TEXT">Btn7</field></block></value>
          </block>
        </statement>
      </block>
    </statement>
  </block>

  <block type="component_event" id="btn8_click" x="-500" y="0">
    <mutation component_type="Button" is_generic="false" instance_name="Btn8" event_name="Click"></mutation>
    <field name="COMPONENT_SELECTOR">Btn8</field>
    <statement name="DO">
      <block type="controls_if" id="if_btn8">
        <value name="IF0">
          <block type="logic_compare" id="cmp_btn8">
            <field name="OP">EQ</field>
            <value name="A">
              <block type="component_set_get" id="get_btn8">
                <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn8"></mutation>
                <field name="COMPONENT_SELECTOR">Btn8</field>
                <field name="PROP">Text</field>
              </block>
            </value>
            <value name="B"><block type="text" id="empty_btn8"><field name="TEXT">_</field></block></value>
          </block>
        </value>
        <statement name="DO0">
          <block type="procedures_callnoreturn" id="call_handle8">
            <mutation name="HandleMove"><arg name="btnId"></arg></mutation>
            <value name="ARG0"><block type="text" id="arg_btn8"><field name="TEXT">Btn8</field></block></value>
          </block>
        </statement>
      </block>
    </statement>
  </block>

  <block type="component_event" id="btn9_click" x="-500" y="100">
    <mutation component_type="Button" is_generic="false" instance_name="Btn9" event_name="Click"></mutation>
    <field name="COMPONENT_SELECTOR">Btn9</field>
    <statement name="DO">
      <block type="controls_if" id="if_btn9">
        <value name="IF0">
          <block type="logic_compare" id="cmp_btn9">
            <field name="OP">EQ</field>
            <value name="A">
              <block type="component_set_get" id="get_btn9">
                <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn9"></mutation>
                <field name="COMPONENT_SELECTOR">Btn9</field>
                <field name="PROP">Text</field>
              </block>
            </value>
            <value name="B"><block type="text" id="empty_btn9"><field name="TEXT">_</field></block></value>
          </block>
        </value>
        <statement name="DO0">
          <block type="procedures_callnoreturn" id="call_handle9">
            <mutation name="HandleMove"><arg name="btnId"></arg></mutation>
            <value name="ARG0"><block type="text" id="arg_btn9"><field name="TEXT">Btn9</field></block></value>
          </block>
        </statement>
      </block>
    </statement>
  </block>

  <block type="procedures_defnoreturn" id="proc_checkwin" x="1000" y="-400">
    <field name="NAME">CheckWin</field>
    <statement name="STACK">

      <block type="controls_if" id="win_123">
        <value name="IF0">
          <block type="logic_compare">
            <field name="OP">NEQ</field>
            <value name="A">
              <block type="component_set_get">
                <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn1"></mutation>
                <field name="COMPONENT_SELECTOR">Btn1</field>
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
                    <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn1"></mutation>
                    <field name="COMPONENT_SELECTOR">Btn1</field>
                    <field name="PROP">Text</field>
                  </block>
                </value>
                <value name="B">
                  <block type="component_set_get">
                    <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn2"></mutation>
                    <field name="COMPONENT_SELECTOR">Btn2</field>
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
                        <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn2"></mutation>
                        <field name="COMPONENT_SELECTOR">Btn2</field>
                        <field name="PROP">Text</field>
                      </block>
                    </value>
                    <value name="B">
                      <block type="component_set_get">
                        <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn3"></mutation>
                        <field name="COMPONENT_SELECTOR">Btn3</field>
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
                            <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn1"></mutation>
                            <field name="COMPONENT_SELECTOR">Btn1</field>
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

      <block type="controls_if" id="win_456">
        <value name="IF0">
          <block type="logic_compare">
            <field name="OP">NEQ</field>
            <value name="A">
              <block type="component_set_get">
                <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn4"></mutation>
                <field name="COMPONENT_SELECTOR">Btn4</field>
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
                    <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn4"></mutation>
                    <field name="COMPONENT_SELECTOR">Btn4</field>
                    <field name="PROP">Text</field>
                  </block>
                </value>
                <value name="B">
                  <block type="component_set_get">
                    <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn5"></mutation>
                    <field name="COMPONENT_SELECTOR">Btn5</field>
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
                        <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn5"></mutation>
                        <field name="COMPONENT_SELECTOR">Btn5</field>
                        <field name="PROP">Text</field>
                      </block>
                    </value>
                    <value name="B">
                      <block type="component_set_get">
                        <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn6"></mutation>
                        <field name="COMPONENT_SELECTOR">Btn6</field>
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
                            <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn4"></mutation>
                            <field name="COMPONENT_SELECTOR">Btn4</field>
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

      <block type="controls_if" id="win_789">
        <value name="IF0">
          <block type="logic_compare">
            <field name="OP">NEQ</field>
            <value name="A">
              <block type="component_set_get">
                <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn7"></mutation>
                <field name="COMPONENT_SELECTOR">Btn7</field>
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
                    <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn7"></mutation>
                    <field name="COMPONENT_SELECTOR">Btn7</field>
                    <field name="PROP">Text</field>
                  </block>
                </value>
                <value name="B">
                  <block type="component_set_get">
                    <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn8"></mutation>
                    <field name="COMPONENT_SELECTOR">Btn8</field>
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
                        <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn8"></mutation>
                        <field name="COMPONENT_SELECTOR">Btn8</field>
                        <field name="PROP">Text</field>
                      </block>
                    </value>
                    <value name="B">
                      <block type="component_set_get">
                        <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn9"></mutation>
                        <field name="COMPONENT_SELECTOR">Btn9</field>
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
                            <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn7"></mutation>
                            <field name="COMPONENT_SELECTOR">Btn7</field>
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

      <block type="controls_if" id="win_147">
        <value name="IF0">
          <block type="logic_compare">
            <field name="OP">NEQ</field>
            <value name="A">
              <block type="component_set_get">
                <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn1"></mutation>
                <field name="COMPONENT_SELECTOR">Btn1</field>
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
                    <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn1"></mutation>
                    <field name="COMPONENT_SELECTOR">Btn1</field>
                    <field name="PROP">Text</field>
                  </block>
                </value>
                <value name="B">
                  <block type="component_set_get">
                    <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn4"></mutation>
                    <field name="COMPONENT_SELECTOR">Btn4</field>
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
                        <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn4"></mutation>
                        <field name="COMPONENT_SELECTOR">Btn4</field>
                        <field name="PROP">Text</field>
                      </block>
                    </value>
                    <value name="B">
                      <block type="component_set_get">
                        <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn7"></mutation>
                        <field name="COMPONENT_SELECTOR">Btn7</field>
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
                            <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn1"></mutation>
                            <field name="COMPONENT_SELECTOR">Btn1</field>
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

      <block type="controls_if" id="win_258">
        <value name="IF0">
          <block type="logic_compare">
            <field name="OP">NEQ</field>
            <value name="A">
              <block type="component_set_get">
                <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn2"></mutation>
                <field name="COMPONENT_SELECTOR">Btn2</field>
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
                    <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn2"></mutation>
                    <field name="COMPONENT_SELECTOR">Btn2</field>
                    <field name="PROP">Text</field>
                  </block>
                </value>
                <value name="B">
                  <block type="component_set_get">
                    <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn5"></mutation>
                    <field name="COMPONENT_SELECTOR">Btn5</field>
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
                        <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn5"></mutation>
                        <field name="COMPONENT_SELECTOR">Btn5</field>
                        <field name="PROP">Text</field>
                      </block>
                    </value>
                    <value name="B">
                      <block type="component_set_get">
                        <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn8"></mutation>
                        <field name="COMPONENT_SELECTOR">Btn8</field>
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
                            <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn2"></mutation>
                            <field name="COMPONENT_SELECTOR">Btn2</field>
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

      <block type="controls_if" id="win_369">
        <value name="IF0">
          <block type="logic_compare">
            <field name="OP">NEQ</field>
            <value name="A">
              <block type="component_set_get">
                <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn3"></mutation>
                <field name="COMPONENT_SELECTOR">Btn3</field>
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
                    <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn3"></mutation>
                    <field name="COMPONENT_SELECTOR">Btn3</field>
                    <field name="PROP">Text</field>
                  </block>
                </value>
                <value name="B">
                  <block type="component_set_get">
                    <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn6"></mutation>
                    <field name="COMPONENT_SELECTOR">Btn6</field>
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
                        <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn6"></mutation>
                        <field name="COMPONENT_SELECTOR">Btn6</field>
                        <field name="PROP">Text</field>
                      </block>
                    </value>
                    <value name="B">
                      <block type="component_set_get">
                        <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn9"></mutation>
                        <field name="COMPONENT_SELECTOR">Btn9</field>
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
                            <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn3"></mutation>
                            <field name="COMPONENT_SELECTOR">Btn3</field>
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

      <block type="controls_if" id="win_159">
        <value name="IF0">
          <block type="logic_compare">
            <field name="OP">NEQ</field>
            <value name="A">
              <block type="component_set_get">
                <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn1"></mutation>
                <field name="COMPONENT_SELECTOR">Btn1</field>
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
                    <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn1"></mutation>
                    <field name="COMPONENT_SELECTOR">Btn1</field>
                    <field name="PROP">Text</field>
                  </block>
                </value>
                <value name="B">
                  <block type="component_set_get">
                    <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn5"></mutation>
                    <field name="COMPONENT_SELECTOR">Btn5</field>
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
                        <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn5"></mutation>
                        <field name="COMPONENT_SELECTOR">Btn5</field>
                        <field name="PROP">Text</field>
                      </block>
                    </value>
                    <value name="B">
                      <block type="component_set_get">
                        <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn9"></mutation>
                        <field name="COMPONENT_SELECTOR">Btn9</field>
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
                            <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn1"></mutation>
                            <field name="COMPONENT_SELECTOR">Btn1</field>
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

      <block type="controls_if" id="win_357">
        <value name="IF0">
          <block type="logic_compare">
            <field name="OP">NEQ</field>
            <value name="A">
              <block type="component_set_get">
                <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn3"></mutation>
                <field name="COMPONENT_SELECTOR">Btn3</field>
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
                    <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn3"></mutation>
                    <field name="COMPONENT_SELECTOR">Btn3</field>
                    <field name="PROP">Text</field>
                  </block>
                </value>
                <value name="B">
                  <block type="component_set_get">
                    <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn5"></mutation>
                    <field name="COMPONENT_SELECTOR">Btn5</field>
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
                        <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn5"></mutation>
                        <field name="COMPONENT_SELECTOR">Btn5</field>
                        <field name="PROP">Text</field>
                      </block>
                    </value>
                    <value name="B">
                      <block type="component_set_get">
                        <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn7"></mutation>
                        <field name="COMPONENT_SELECTOR">Btn7</field>
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
                            <mutation component_type="Button" set_or_get="get" property_name="Text" is_generic="false" instance_name="Btn3"></mutation>
                            <field name="COMPONENT_SELECTOR">Btn3</field>
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
  </next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block>
    </statement>
  </block>

  <block type="procedures_defnoreturn" id="proc_reset" x="2000" y="-400">
    <field name="NAME">ResetGame</field>
    <statement name="STACK">

      <block type="component_set_get">
        <mutation component_type="Button" set_or_get="set" property_name="Text" is_generic="false" instance_name="Btn1"></mutation>
        <field name="COMPONENT_SELECTOR">Btn1</field>
        <field name="PROP">Text</field>
        <value name="VALUE"><block type="text"><field name="TEXT">_</field></block></value>
        <next>

      <block type="component_set_get">
        <mutation component_type="Button" set_or_get="set" property_name="Text" is_generic="false" instance_name="Btn2"></mutation>
        <field name="COMPONENT_SELECTOR">Btn2</field>
        <field name="PROP">Text</field>
        <value name="VALUE"><block type="text"><field name="TEXT">_</field></block></value>
        <next>

      <block type="component_set_get">
        <mutation component_type="Button" set_or_get="set" property_name="Text" is_generic="false" instance_name="Btn3"></mutation>
        <field name="COMPONENT_SELECTOR">Btn3</field>
        <field name="PROP">Text</field>
        <value name="VALUE"><block type="text"><field name="TEXT">_</field></block></value>
        <next>

      <block type="component_set_get">
        <mutation component_type="Button" set_or_get="set" property_name="Text" is_generic="false" instance_name="Btn4"></mutation>
        <field name="COMPONENT_SELECTOR">Btn4</field>
        <field name="PROP">Text</field>
        <value name="VALUE"><block type="text"><field name="TEXT">_</field></block></value>
        <next>

      <block type="component_set_get">
        <mutation component_type="Button" set_or_get="set" property_name="Text" is_generic="false" instance_name="Btn5"></mutation>
        <field name="COMPONENT_SELECTOR">Btn5</field>
        <field name="PROP">Text</field>
        <value name="VALUE"><block type="text"><field name="TEXT">_</field></block></value>
        <next>

      <block type="component_set_get">
        <mutation component_type="Button" set_or_get="set" property_name="Text" is_generic="false" instance_name="Btn6"></mutation>
        <field name="COMPONENT_SELECTOR">Btn6</field>
        <field name="PROP">Text</field>
        <value name="VALUE"><block type="text"><field name="TEXT">_</field></block></value>
        <next>

      <block type="component_set_get">
        <mutation component_type="Button" set_or_get="set" property_name="Text" is_generic="false" instance_name="Btn7"></mutation>
        <field name="COMPONENT_SELECTOR">Btn7</field>
        <field name="PROP">Text</field>
        <value name="VALUE"><block type="text"><field name="TEXT">_</field></block></value>
        <next>

      <block type="component_set_get">
        <mutation component_type="Button" set_or_get="set" property_name="Text" is_generic="false" instance_name="Btn8"></mutation>
        <field name="COMPONENT_SELECTOR">Btn8</field>
        <field name="PROP">Text</field>
        <value name="VALUE"><block type="text"><field name="TEXT">_</field></block></value>
        <next>

      <block type="component_set_get">
        <mutation component_type="Button" set_or_get="set" property_name="Text" is_generic="false" instance_name="Btn9"></mutation>
        <field name="COMPONENT_SELECTOR">Btn9</field>
        <field name="PROP">Text</field>
        <value name="VALUE"><block type="text"><field name="TEXT">_</field></block></value>
        <next>

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
</next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block>
    </statement>
  </block>

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
          <!-- CORRECT -->
          <block type="controls_if" id="update_chain">
            <mutation elseif="8"></mutation>

            <value name="IF0">
              <block type="logic_compare" id="cmp_update1">
                <field name="OP">EQ</field>
                <value name="A"><block type="lexical_variable_get" id="get_pending1"><field name="VAR">global pending_move</field></block></value>
                <value name="B"><block type="text" id="text_pending1"><field name="TEXT">Btn1</field></block></value>
              </block>
            </value>
            <statement name="DO0">
              <block type="component_set_get" id="set_btn1">
                <mutation component_type="Button" set_or_get="set" property_name="Text" is_generic="false" instance_name="Btn1"></mutation>
                <field name="COMPONENT_SELECTOR">Btn1</field>
                <field name="PROP">Text</field>
                <value name="VALUE"><block type="lexical_variable_get" id="get_turn1"><field name="VAR">global turn</field></block></value>
              </block>
            </statement>

            <value name="IF1">
              <block type="logic_compare" id="cmp_update2">
                <field name="OP">EQ</field>
                <value name="A"><block type="lexical_variable_get" id="get_pending2"><field name="VAR">global pending_move</field></block></value>
                <value name="B"><block type="text" id="text_pending2"><field name="TEXT">Btn2</field></block></value>
              </block>
            </value>
            <statement name="DO1">
              <block type="component_set_get" id="set_btn2">
                <mutation component_type="Button" set_or_get="set" property_name="Text" is_generic="false" instance_name="Btn2"></mutation>
                <field name="COMPONENT_SELECTOR">Btn2</field>
                <field name="PROP">Text</field>
                <value name="VALUE"><block type="lexical_variable_get" id="get_turn2"><field name="VAR">global turn</field></block></value>
              </block>
            </statement>

            <value name="IF2">
              <block type="logic_compare" id="cmp_update3">
                <field name="OP">EQ</field>
                <value name="A"><block type="lexical_variable_get" id="get_pending3"><field name="VAR">global pending_move</field></block></value>
                <value name="B"><block type="text" id="text_pending3"><field name="TEXT">Btn3</field></block></value>
              </block>
            </value>
            <statement name="DO2">
              <block type="component_set_get" id="set_btn3">
                <mutation component_type="Button" set_or_get="set" property_name="Text" is_generic="false" instance_name="Btn3"></mutation>
                <field name="COMPONENT_SELECTOR">Btn3</field>
                <field name="PROP">Text</field>
                <value name="VALUE"><block type="lexical_variable_get" id="get_turn3"><field name="VAR">global turn</field></block></value>
              </block>
            </statement>

            <value name="IF3">
              <block type="logic_compare" id="cmp_update4">
                <field name="OP">EQ</field>
                <value name="A"><block type="lexical_variable_get" id="get_pending4"><field name="VAR">global pending_move</field></block></value>
                <value name="B"><block type="text" id="text_pending4"><field name="TEXT">Btn4</field></block></value>
              </block>
            </value>
            <statement name="DO3">
              <block type="component_set_get" id="set_btn4">
                <mutation component_type="Button" set_or_get="set" property_name="Text" is_generic="false" instance_name="Btn4"></mutation>
                <field name="COMPONENT_SELECTOR">Btn4</field>
                <field name="PROP">Text</field>
                <value name="VALUE"><block type="lexical_variable_get" id="get_turn4"><field name="VAR">global turn</field></block></value>
              </block>
            </statement>

            <value name="IF4">
              <block type="logic_compare" id="cmp_update5">
                <field name="OP">EQ</field>
                <value name="A"><block type="lexical_variable_get" id="get_pending5"><field name="VAR">global pending_move</field></block></value>
                <value name="B"><block type="text" id="text_pending5"><field name="TEXT">Btn5</field></block></value>
              </block>
            </value>
            <statement name="DO4">
              <block type="component_set_get" id="set_btn5">
                <mutation component_type="Button" set_or_get="set" property_name="Text" is_generic="false" instance_name="Btn5"></mutation>
                <field name="COMPONENT_SELECTOR">Btn5</field>
                <field name="PROP">Text</field>
                <value name="VALUE"><block type="lexical_variable_get" id="get_turn5"><field name="VAR">global turn</field></block></value>
              </block>
            </statement>

            <value name="IF5">
              <block type="logic_compare" id="cmp_update6">
                <field name="OP">EQ</field>
                <value name="A"><block type="lexical_variable_get" id="get_pending6"><field name="VAR">global pending_move</field></block></value>
                <value name="B"><block type="text" id="text_pending6"><field name="TEXT">Btn6</field></block></value>
              </block>
            </value>
            <statement name="DO5">
              <block type="component_set_get" id="set_btn6">
                <mutation component_type="Button" set_or_get="set" property_name="Text" is_generic="false" instance_name="Btn6"></mutation>
                <field name="COMPONENT_SELECTOR">Btn6</field>
                <field name="PROP">Text</field>
                <value name="VALUE"><block type="lexical_variable_get" id="get_turn6"><field name="VAR">global turn</field></block></value>
              </block>
            </statement>

            <value name="IF6">
              <block type="logic_compare" id="cmp_update7">
                <field name="OP">EQ</field>
                <value name="A"><block type="lexical_variable_get" id="get_pending7"><field name="VAR">global pending_move</field></block></value>
                <value name="B"><block type="text" id="text_pending7"><field name="TEXT">Btn7</field></block></value>
              </block>
            </value>
            <statement name="DO6">
              <block type="component_set_get" id="set_btn7">
                <mutation component_type="Button" set_or_get="set" property_name="Text" is_generic="false" instance_name="Btn7"></mutation>
                <field name="COMPONENT_SELECTOR">Btn7</field>
                <field name="PROP">Text</field>
                <value name="VALUE"><block type="lexical_variable_get" id="get_turn7"><field name="VAR">global turn</field></block></value>
              </block>
            </statement>

            <value name="IF7">
              <block type="logic_compare" id="cmp_update8">
                <field name="OP">EQ</field>
                <value name="A"><block type="lexical_variable_get" id="get_pending8"><field name="VAR">global pending_move</field></block></value>
                <value name="B"><block type="text" id="text_pending8"><field name="TEXT">Btn8</field></block></value>
              </block>
            </value>
            <statement name="DO7">
              <block type="component_set_get" id="set_btn8">
                <mutation component_type="Button" set_or_get="set" property_name="Text" is_generic="false" instance_name="Btn8"></mutation>
                <field name="COMPONENT_SELECTOR">Btn8</field>
                <field name="PROP">Text</field>
                <value name="VALUE"><block type="lexical_variable_get" id="get_turn8"><field name="VAR">global turn</field></block></value>
              </block>
            </statement>

            <value name="IF8">
              <block type="logic_compare" id="cmp_update9">
                <field name="OP">EQ</field>
                <value name="A"><block type="lexical_variable_get" id="get_pending9"><field name="VAR">global pending_move</field></block></value>
                <value name="B"><block type="text" id="text_pending9"><field name="TEXT">Btn9</field></block></value>
              </block>
            </value>
            <statement name="DO8">
              <block type="component_set_get" id="set_btn9">
                <mutation component_type="Button" set_or_get="set" property_name="Text" is_generic="false" instance_name="Btn9"></mutation>
                <field name="COMPONENT_SELECTOR">Btn9</field>
                <field name="PROP">Text</field>
                <value name="VALUE"><block type="lexical_variable_get" id="get_turn9"><field name="VAR">global turn</field></block></value>
              </block>
            </statement>

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

  <block type="component_event" id="reset_click" x="-1000" y="1000">
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
