import zmq
import json

data_context = zmq.Context()
data_socket = data_context.socket(zmq.SUB)
data_socket.connect('tcp://localhost:6000')
data_socket.setsockopt_string(zmq.SUBSCRIBE, '')

while True:
    data = data_socket.recv_string()
    print(json.loads(data))