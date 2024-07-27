from gevent import monkey; monkey.patch_all()
from gevent.server import StreamServer
import json

data_store = {}

def handle_client(socket, address):
    print(f"New connection from {address}")
    fileobj = socket.makefile('rwb')
    while True:
        line = fileobj.readline()
        if not line:
            break
        command = json.loads(line.decode('utf-8'))
        response = process_command(command)
        fileobj.write(json.dumps(response).encode('utf-8') + b'\n')
        fileobj.flush()
    fileobj.close()

def process_command(command):
    cmd_type = command.get("type")
    key = command.get("key")
    value = command.get("value")
    if cmd_type == "GET":
        return data_store.get(key, None)
    elif cmd_type == "SET":
        data_store[key] = value
        return "OK"
    elif cmd_type == "DELETE":
        return data_store.pop(key, None)
    elif cmd_type == "FLUSH":
        data_store.clear()
        return "OK"
    elif cmd_type == "MGET":
        return {k: data_store.get(k, None) for k in key}
    elif cmd_type == "MSET":
        data_store.update(value)
        return "OK"
    return "UNKNOWN COMMAND"

server = StreamServer(('0.0.0.0', 5000), handle_client)
server.serve_forever()
