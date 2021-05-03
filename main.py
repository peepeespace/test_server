import zmq
import time
import json

pub_context = zmq.Context()
pub_socket = pub_context.socket(zmq.PUB)
pub_socket.bind('tcp://*:6000')

while True:
    time.sleep(0.3)
    pub_socket.send_string(json.dumps({
        'status': 'success',
        'data': 'test data'
    }))