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

    def __getattr__(self, name, *args, **kwargs):
        def command(*args, **kwargs):
            self.connection.sendall(self.pack_command(name, *args))
            print self.connection.recv(1024)
        return command
