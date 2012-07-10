import socket
from itertools import imap


class MiniRedis(object):
    """A lightweight redis client"""

    def __init__(self, host="localhost", port=6379, timeout=30):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.settimeout(timeout)
        self.connection.connect((host, port))

    def encode(self, value):
        "From redis-py: Return a bytestring representation of the value"
        if isinstance(value, unicode):
            return value.encode('utf-8', 'strict')
        return str(value)

    def pack_command(self, *args):
        "From redis-py: Pack a series of arguments into a value Redis command"
        command = ['$%s\r\n%s\r\n' % (len(enc_value), enc_value)
                   for enc_value in imap(self.encode, args)]
        return '*%s\r\n%s' % (len(command), ''.join(command))

    def parse_response(self, reply):
        type, body = reply[0], reply[1:-2]
        if type == "-": raise Exception(body)
        elif type == "*": return body.split("\r\n")[::2][1:]
        elif type == "$": return body.split("\r\n")[1]
        return body

    def __getattr__(self, name, *args, **kwargs):
        def command(*args, **kwargs):
            self.connection.sendall(self.pack_command(name, *args))
            return self.parse_response(self.connection.recv(4096))
        return command
