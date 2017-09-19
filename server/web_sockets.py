import asyncio
import os
import random

import websockets
import json
from task import ExecutionManager


async def handler(websocket, path):
    consumer_task = asyncio.ensure_future(consumer_handler(websocket))
    producer_task = asyncio.ensure_future(producer_handler(websocket))
    done, pending = await asyncio.wait(
        [consumer_task, producer_task],
        return_when=asyncio.FIRST_COMPLETED,
    )

    for task in pending:
        task.cancel()


def updateQ():
    files = os.listdir("out/")
    files.sort()
    q = []
    for file in files:
        f = open("out/" + file, "r")
        d = f.read()
        q.append(d)
        f.close()
        os.remove("out/" + file)
    return q


async def producer_handler(websocket):
    q = []
    while True:
        while q:
            response = q.pop(0)
            await websocket.send(response)
            print("> {}".format(response))
        try:
            q = updateQ()
        except:
            pass
        await asyncio.sleep(random.random())



async def consumer_handler(websocket):
    try:
        f = open("test", "r")
        saved_xml = f.read()
        f.close()
    except:
        saved_xml = None

    tk = ExecutionManager()

    while True:
        name = await websocket.recv()
        command = json.loads(name)
        response = None
        if not "op" in command:
            response = json.dumps({'op': 'INVALID REQUEST', 'data': 'Cannot find "op" on request'})
        elif command["op"] == "GET_STATUS":
            response = json.dumps({'op': 'CURRENT_STATUS', 'data': saved_xml if saved_xml else 'nothing'})
        elif command["op"] == "RUN_CODE":
            tk.runF(command.get("data"))
        elif command["op"] == "SAVE_CODE":
            saved_xml = command.get("data", None)
            f = open("test", "w")
            f.write(saved_xml)
            f.close()
            response = json.dumps({'op': 'CODE_SAVED'})
        else:
            response = json.dumps({'op': 'INVALID REQUEST', 'data': 'Unreconized command: ' + command["op"]})

        print("< {}".format(command.get("op", "NO OP")))
        if response is not None:
            await websocket.send(response)
        print("> {}".format(response))

start_server = websockets.serve(handler, '0.0.0.0', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()