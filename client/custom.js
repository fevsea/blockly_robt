var ws = null;
ws = new WebSocket("ws://127.0.0.1:5678/");
consoleData = ""

function updateConsoleData(){

}


function sendToServer(data) {
    console.log("Send: " + op);
    consoleData += "Send: " + op + "\n";
    ws.send(op);
}


ws.onopen = function (){
    op = JSON.stringify({
      op: "GET_STATUS",
      data: "foo"});
    ws.onopen = null;
    sendToServer(op);
};

ws.onerror = function (event) {
    console.log("ERROR: " + event.data)
  };

ws.onmessage = function (event) {
    console.log("Received: " + event.data);
    consoleData += "Received: " + event.data + "\n";
    updateConsoleData()
    response = JSON.parse(event.data);

    switch(response["op"]) {
    case "INVALID REQUEST":
        console.log("ERROR: Invalid request: " + response["data"]);
        break;
    case "CURRENT_STATUS":
        if(response["data"] != "nothing"){
            Code.workspace.clear();
            bdom = Blockly.Xml.textToDom(response["data"]);
            Blockly.Xml.domToWorkspace(bdom, Code.workspace);
        }
        break;
    case "CODE_SAVED":
        break;
    default:
        console.log("ERROR: Unknown response");
}
};

function saveCode(xml_code){
    op = JSON.stringify({
      op: "SAVE_CODE",
      data: xml_code});
    sendToServer(op);
}



function mirrorEvent(primaryEvent) {
    if (primaryEvent.type == Blockly.Events.UI) {
        return;  // Don't mirror UI events.
    }

    // Convert event to JSON.  This could then be transmitted across the net.
    var xmlDom = Blockly.Xml.workspaceToDom(Code.workspace);
    var xmlText = Blockly.Xml.domToPrettyText(xmlDom);
    saveCode(xmlText);
}

function setUp(){
    // Listen to events on primary workspace.
    Code.workspace.addChangeListener(mirrorEvent);
    Code.bindClick('runButton', sendRun);
}


function sendRun(){
    op = JSON.stringify({
      op: "RUN_CODE",
      data: Blockly.Python.workspaceToCode(Code.workspace)});
    sendToServer(op);
    Code.tabClick("console");
}
