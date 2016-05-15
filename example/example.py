from ctypes  import get_errno
from multiprocessing import Process
import os
import sys
import signal
import socket

# The MIME for the type of data supported

extn = {  "gif":"image/gif" , "jpg":"image/jpg" , "jpeg":"image/jpeg", "png":"image/png", "ico":"image/ico", "zip":"image/zip",  
        "gz":"image/gz" , "tar":"image/tar", "htm":"text/html", "html":"text/html", "txt":"text/text",  
        chr(0):chr(0) };

# directories which cannot be used to host the web server

unsupported =["/","/etc","/bin","/lib","/tmp","/usr","/dev","/sbin"]

# some constants used throughout the program 

BUFSIZE=8192
ERROR=42
LOG=44
FORBIDDEN=403
NOTFOUND=404

# list of custom interrupts
def customSIGINT(foo,bar):
	exit(0)

def Log(type,s1,s2,sock):
	logbuffer=""
	if type == ERROR:
		logbuffer+="ERROR: {0}:{1} Errno={2} exiting pid={3}".format(s1,s2,get_errno(),os.getpid())
	elif type == FORBIDDEN:
		sock.sendall("HTTP/1.1 403 Forbidden\nContent-Length: 185\nConnection: close\nContent-Type: text/html\n\n<html><head>\n<title>403 Forbidden</title>\n</head><body>\n<h1>Forbidden</h1>\nThe requested URL, file type or operation is not allowed on this simple static file webserver.\n</body></html>\n")
		logbuffer+="FORBIDDEN: {0}:{1}".format(s1,s2)
	elif type == NOTFOUND:
		sock.sendall("HTTP/1.1 404 Not Found\nContent-Length: 136\nConnection: close\nContent-Type: text/html\n\n<html><head>\n<title>404 Not Found</title>\n</head><body>\n<h1>Not Found</h1>\nThe requested URL was not found on this server.\n</body></html>\n")
		logbuffer+="NOT FOUND: {0}:{1}".format(s1,s2)
	elif type == LOG:
		logbuffer+="INFO: {0}:{1}:{2}".format(s1,s2,sock)
	fd=os.open("server.log",os.O_CREAT| os.O_WRONLY | os.O_APPEND)
	if fd>0:
		os.write(fd,logbuffer)
		os.write(fd,"\n")
		os.close(fd)
	if(type ==ERROR or type == NOTFOUND or type == FORBIDDEN):
		exit(3)


def server(sock,hit):
	browserReq=sock.recv(BUFSIZE)
	info=len(browserReq)
	if info==0:
		Log(FORBIDDEN,"failed to read browser request","",sock)
	browserReq=browserReq.replace('\r','*').replace('\n','*')
	Log(LOG,"request",browserReq,hit)
	if (not browserReq.startswith("GET ")) and (not browserReq.startswith("get ")):
		Log(FORBIDDEN,"Only simple GET operation supported",browserReq,sock) 
	buffer= browserReq.split()
	if '..' in buffer[0] or '..' in buffer[1]:
		Log(FORBIDDEN,"Parent directory (..) path names not supported",browserReq,sock);			
	if buffer[1] is '/':
		buffer[1]='/index.html'
	extension="Not Supported"
	for x in extn:
		if buffer[1].endswith(x):
			extension=x
			break
	if extension is "Not Supported":
		Log(FORBIDDEN,"file extension type not supported",buffer[1],sock)
	
	filed=os.open(buffer[1][1:],os.O_RDONLY)
	if(filed<=0):
		print buffer[1][1:]
		Log(NOTFOUND, "failed to open file",buffer[1],sock)
	Log(LOG,"SEND",buffer[1],hit)
	filesize=os.lseek(filed,0,os.SEEK_END)
	os.lseek(filed,0,os.SEEK_SET)
	reply="HTTP/1.1 200 OK\nServer: web/{0}.0\nContent-Length: {1}\nConnection: close\nContent-Type: {2}\n\n".format(1,filesize,extn[extension])
	Log(LOG,"Header ",reply,hit)
	sock.sendall(reply)
	r=os.read(filed,BUFSIZE)
	while(r!=''):
		sock.sendall(r)
		r=os.read(filed,BUFSIZE)
	os.close(filed)
	exit(1)

if __name__ == '__main__':
	length = len(sys.argv)
	exten=""
	if length < 3 or length >4 or ( (sys.argv[1] is '-h') or (sys.argv[1] is '--help')):
		print "python web.py <port> <top-directory> [-d]"
		print "Web is a small mini web server written in python "
		for x in extn:
			exten+="*."+str(x)+' '
		print "Supported extensions are "
		print exten
		print "Not Supported: URLs include \"..\", Java, Javascript, CGI"
		print "Not Supported: directories / /etc /bin /lib /tmp /usr /dev /sbin"
		print "The -d flag runs the server as a daemon"
		print "No warranty given or implied"
		print "Sujay Raj sujayraaj@gmail.com"
		exit(0)
	if sys.argv[2] in unsupported:
		print "ERROR: Bad top directory ",sys.argv[2]," '-h' for more detail"
		exit(1) 
	try:
		os.chdir(sys.argv[2])
	except:
		print "ERROR: Can't Change to directory ", sys.argv[2]
		exit(2)
	if length==4 and sys.argv[3] is "-d":
		if os.fork() != 0:
			exit(0)
	signal.signal(signal.SIGCLD, signal.SIG_IGN);	
	signal.signal(signal.SIGHUP, signal.SIG_IGN);
	signal.signal(signal.SIGINT, customSIGINT);
	os.setpgrp()
	Log(LOG,"web starting",sys.argv[1],os.getpid())
	lsocket= socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
	port=int(sys.argv[1])
	if port < 0 or port > 60000:
		Log(ERROR,"Invalid port number",argv[1],s)
	
	host="0.0.0.0"
	lsocket.bind((host,port))
	lsocket.listen(64)
	hit=0
	while(1):
		hit+=1
		sock, addr = lsocket.accept()
		pid=os.fork()
		if pid < 0:
			Log(ERROR,"system call","accept",lsocket)
		elif pid is 0:
			lsocket.close()
			server(sock,hit)
		else:
			sock.close()
