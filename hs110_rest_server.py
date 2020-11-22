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


@api.route('/api/v1/energy', methods=['GET'])
def get_energy_data():
    return communicate('{"emeter":{"get_realtime":{}}}')


@api.route('/api/v1/monthly', methods=['GET'])
def get_monthly_stats():
    year = request.args.get('year')
    return communicate('{"emeter":{"get_monthstat":{"year":' + year + '}}}')



def communicate(cmd):
    ip = request.args.get('ip')
    port = request.args.get('port')
    sock_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_tcp.connect((ip, int(port)))
    sock_tcp.send(encrypt(cmd))
    data = sock_tcp.recv(1024)
    sock_tcp.close()
    decrypted = decrypt(data[4:])

    return decrypted


def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True


if __name__ == '__main__':
    api.run(host='0.0.0.0', port=1337)
