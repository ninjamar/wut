
import socket

class WebServer:
	def __init__(self,entrypoint,host='0.0.0.0',port=8080):
		self._start(host,port,entrypoint)

	def _start(self,host,port,entrypoint):
		ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		ss.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		ss.bind((host,port))
		ss.listen(1)
		print(f'Listening on {host}:{port}')
		while True:
			conn,addr = ss.accept()
			req = conn.recv(1024).decode('utf-8')
			header,content = entrypoint(req)
			conn.sendall(header.encode('utf-8'))
			conn.sendall(content.encode('utf-8'))
			
