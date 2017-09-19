Blockly.Blocks['robot_move'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("move")
        .appendField(new Blockly.FieldDropdown([["fordwards","fordwards"],
        ["stop","stop"], ["backwards","backwards"]]), "move");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(0);
 this.setTooltip("Tip: Toltip");
 this.setHelpUrl("Help urk");
  }
};

Blockly.Python['robot_move'] = function(block) {
  var dropdown_move =  block.getFieldValue('move');
  if(dropdown_move == "fordwards"){
    code = 'robot.fordwards()\n';
  } else if (dropdown_move == "stop") {
    code = 'robot.stop()\n';
  } else if (dropdown_move == "backwards") {
    code = 'robot.backwards()\n';
  }
  return code;
};



Blockly.Blocks['robot_turn'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("turn")
        .appendField(new Blockly.FieldDropdown([["right","right"], ["left","left"]]), "turn");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(0);
 this.setTooltip("Tip: Toltip");
 this.setHelpUrl("Help urk");
  }
};

Blockly.Python['robot_turn'] = function(block) {
  var dropdown_turn = block.getFieldValue('turn');
  if(dropdown_turn == "left"){
    code = 'robot.left()\n';
  } else if (dropdown_turn == "right") {
    code = 'robot.right()\n';
  }
  return code;
};


Blockly.Blocks['robot_rotate'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("rotate")
        .appendField(new Blockly.FieldDropdown([["right","right"], ["left","left"]]), "rotate");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(0);
 this.setTooltip("Tip: Toltip");
 this.setHelpUrl("Help urk");
  }
};

Blockly.Python['robot_rotate'] = function(block) {
  var dropdown_rotate = block.getFieldValue('rotate');
  if(dropdown_rotate == "left"){
    code = 'robot.rotateLeft()\n';
  } else if (dropdown_rotate == "right") {
    code = 'robot.rotateRight()\n';
  }
  return code;
};

/*Blockly.Blocks['robot_buzz'] = {
  init: function() {
    this.appendValueInput("ms")
        .setCheck("Number")
        .appendField("buzz (ms)");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(0);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Python['robot_buzz'] = function(block) {
  var number_ms = Blockly.Python.valueToCode(block, 'ms', Blockly.Python.ORDER_ATOMIC);
  var code = 'robot.buzzer(' + number_ms + ')\n';
  // TODO: Change ORDER_NONE to the correct strength.
  return code;
};*/





Blockly.Blocks['utils_wait'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("wait ")
        .appendField(new Blockly.FieldNumber(1, 0), "time")
        .appendField("seconds");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(40);
 this.setTooltip("Tip: Toltip");
 this.setHelpUrl("Help urk");
  }
};



Blockly.Python['utils_wait'] = function(block) {
  var number_time = block.getFieldValue('time');
    var code = 'time.sleep(' + number_time + ')\n';
  return code;
};

Blockly.Blocks['utils_run_code'] = {
  init: function() {
    this.appendValueInput("command")
        .setCheck("String")
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("run code ");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(40);
 this.setTooltip("Tip: Toltip");
 this.setHelpUrl("Help urk");
  }
};

Blockly.Python['utils_run_code'] = function(block) {
  var value_command = Blockly.Python.valueToCode(block, 'command', Blockly.Python.ORDER_ATOMIC);
  // TODO: Assemble Python into code variable.
  var code = value_command.substring(1, value_command.length-1); + '\n';
  return code;
};


Blockly.Blocks['read_distance'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("front distance");
    this.setOutput(true, null);
    this.setColour(0);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Python['read_distance'] = function(block) {
  // TODO: Assemble Python into code variable.
  var code = 'robot.readDistance()';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.Python.ORDER_NONE];
};