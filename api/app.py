## referenced to https://github.com/egorsmkv/fail2ban-scripts/blob/master/unban.py
import sys
import json
from fail2ban.client.csocket import CSocket
from flask import Flask, redirect, url_for, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello World!"

@app.route('/ban/wp', methods=['POST'])
def ban_wp():
	if request.method == 'POST':
		ip = request.form.get('ip')
		cmd = ['set', 'rb-wordpress', 'banip', ip]
		data = send_command(cmd)
	return jsonify(data)

def error(reason):
    """
    A helper function to form an error response.

    :param reason: What happened wrong
    :return: Dict of the response
    """

    return {'error': True, 'reason': reason}


def send_command(command):
    """
    This function send a command to the Fail2ban socket server

    :param command: A command
    :return: Result or an error from the server
    """

    if not command:
        return error('empty command')

    socket_file = '/var/run/fail2ban/fail2ban.sock'

    try:
        # command to the socket and set timeout
        client = CSocket(socket_file, timeout=20)
        client.settimeout(20)

        # send the command
        ret = client.send(command)

        # there is an error
        if ret[0] != 0:
            return error('incorrect response code')

        return {'error': False, 'data': ret[1]}
    except Exception as e:
        return error('exception occurred: ' + str(e))

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000, debug=True)
