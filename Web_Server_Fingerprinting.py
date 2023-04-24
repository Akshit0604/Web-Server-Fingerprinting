import socket

ip= 'google.com'
'''
ip = 'ftp.dlptest.com'
'''
port=80

test1 = b'' #b prefix converts string to byte size data which is necessary for it to be sent through network protocols
test2 = b'GET / HTTP/1.0\r\n\r\n' # testing if server supports HTTP
test3 = b'OPTIONS / HTTP/1.0\r\n\r\n' 
test4 = b'HELP/1.0\r\n'  #ftp 
test5 = b'HELO\r\n'#smtp (587)

tests_list = [test1,test2,test3,test4,test5]
supported_protocols={'HTTP':0, 'FTP':0, 'SMTP':0}

for i, test in enumerate(tests_list):
    if i==3: port=21 
    if i==4: port=587
    try:
        sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        sock.connect((ip, port))

        sock.send(test)
        data= sock.recv(1024)

        if(i==1 or i==2):
            supported_protocols['HTTP']=1
        elif i==3:
            supported_protocols['FTP']=1
        elif i==4:
            supported_protocols['SMTP']=1
        
        print(f"Test {i+1}: ")
        print(data.decode().split('\r\n')[0]) #printing headers if reply to request successfull
        print(data.decode().split('\r\n')[1])
        print(data.decode().split('\r\n')[3])
        

    except socket.timeout as e:
        print(f"Test {i+1}: {e}") #timeout exception (if server doesn't respond on time)

    except Exception as e:
       print(f"Test {i+1}: {e}")

    finally:
        sock.close()

print("\nThe protocols supported by", ip, " are: ")
    
for key, value in supported_protocols.items():
    if value == 1:
        print(key)