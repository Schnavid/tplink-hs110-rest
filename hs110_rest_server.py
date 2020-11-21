#!/usr/bin/env python3

from flask import Flask, json, request
from struct import pack
import socket

api = Flask(__name__)

def encrypt(string):
    key = 171
    result = pack(">I", len(string))
    for i in string:
        a = key ^ ord(i)
        key = a
        result += bytes([a])
    return result


def decrypt(string):
    key = 171
    result = ""
    for i in string:
        a = key ^ i
        key = i
        result += chr(a)
    return result


@api.route('/energy', methods=['GET'])
def get_energy_data():
    ip = request.args.get('ip')
    port = request.args.get('port')
    sock_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_tcp.connect((ip, int(port)))
    sock_tcp.send(encrypt('{"emeter":{"get_realtime":{}}}'))
    data = sock_tcp.recv(2048)
    sock_tcp.close()
    decrypted = decrypt(data[4:])
    return decrypted

if __name__ == '__main__':
    api.run(host='0.0.0.0', port=1337)
