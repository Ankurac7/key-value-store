import socket
import json

def send_command(command):
    with socket.create_connection(('localhost', 5000)) as sock:
        fileobj = sock.makefile('rwb')
        fileobj.write(json.dumps(command).encode('utf-8') + b'\n')
        fileobj.flush()
        response = fileobj.readline()
        return json.loads(response.decode('utf-8'))

print(send_command({"type": "SET", "key": "foo", "value": "bar"}))
print(send_command({"type": "GET", "key": "foo"}))
