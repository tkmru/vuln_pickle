#!/usr/bin/env python2.7
# coding: UTF-8

import cPickle
import SocketServer


class TCPServer(SocketServer.TCPServer):

    def __init__(self, server_address, RequestHandlerClass):
        SocketServer.TCPServer.__init__(self, server_address, RequestHandlerClass)


class VulnerableTCPHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        self.request.sendall('connected\n')

        self.received = self.request.recv(1024).strip()
        print('Received:{0}\n'.format(self.received))

        self.result = cPickle.loads(self.received)
        self.request.sendall('Server received')
        print('Sent:    {0}\n'.format('Server received'))


if __name__ == "__main__":

    HOST, PORT = "localhost", 9997
    print('Vulnerable server starts...')
    print('Host:    {0}'.format(HOST))
    print('Port:    {0}'.format(PORT))

    server = TCPServer((HOST, PORT), VulnerableTCPHandler)
    server.serve_forever()
