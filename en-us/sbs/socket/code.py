import usocket
sock = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
sockaddr=usocket.getaddrinfo('www.tongxinmao.com',80)[0][-1]
sock.connect(sockaddr)

ret=sock.send('GET /News HTTP/1.1\r\nHost: www.tongxinmao.com\r\nAccept-Encoding:deflate\r\nConnection: keep-alive\r\n\r\n')
print('send %d bytes' % ret)

# 接收服务端的消息：
# ret=sock.send('GET /News HTTP/1.1\r\nHost: www.tongxinmao.com\r\nAccept-Encoding:
# deflate\r\nConnection: keep-alive\r\n\r\n')
# print('send %d bytes' % ret)
# data=sock.recv(1024)
# print('recv %s bytes:' % len(data))
# print(data.decode())