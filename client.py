import sys
sys.path.insert(0, '/home/bassam2.ali/iotworksheet2')
import websockets
import json
import asyncio
from morse import morse

async def recv_message(websocket):
    message = json.loads(await websocket.recv())
    return message

async def recv_message2(websocket):
    message = json.loads(await websocket.recv())
    return message
    
async def send_echo(websocket, sender: str, msg: str, client_id) -> str:
    encoded_msg = morse.encode_ham(sender, 'echo', msg)
    outward_message = {'type':'morse_evt','client_id': client_id, 'payload': encoded_msg}
    await websocket.send(json.dumps(outward_message))

async def send_time(websocket, sender: str, client_id) -> str:
    encoded_msg = morse.encode_ham(sender, "time", 'hello world')
    outward_message = {'type':'morse_evt','client_id':client_id, 'payload': encoded_msg}
    await websocket.send(json.dumps(outward_message))


async def main():
    uri = "ws://localhost:10102"

    async with websockets.connect(uri) as websocket:
        
        message = json.loads(await websocket.recv())
        #print(message)

        if message['type'] == 'join_evt':
            client_id = message['client_id']
        else:
            print('Did not receive a correct join message')
            return 0

        print("Echo:")
        echo_sender = input("Enter sender name: ")
        echo_message = input("Enter the message to be sent to the server: ")        
        await send_echo(websocket, echo_sender, echo_message, client_id)
        echo_response = await recv_message(websocket)
        print("The server sent back:\n",echo_response['payload'])
        print(morse.decode_ham(echo_response['payload']))
        
        print("\nTime:")
        time_sender = "s"
        await send_time(websocket, time_sender, client_id)
        time_response = await recv_message2(websocket)
        print("The server sent back:\n",time_response['payload'])
        print(morse.decode_ham(time_response['payload']))
        

if __name__ == "__main__":
    asyncio.run(main())