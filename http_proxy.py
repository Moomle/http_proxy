import socket, urllib, urllib2

class HttpProxy(object):
	socket

	def __init__(self):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def receiveC