import socket

class Multimeter(object):
    def __init__(self, host, port, bufsize):
        self.host = host
        self.port = port
        self.bufsize = bufsize

    def Read_Voltage(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        r=''
        v = 0
        n = 0
        message=bytes('READ:VOL' ,'utf-8')
        while v==0:
            self.sock.send(message)
            r = self.sock.recv(self.bufsize)
            c = str(r)
            try:
                x = int(str(c[-3]))
                v=1
                n+=1
            except ValueError:
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.sock.connect((self.host, self.port))
                v=0
        self.sock.shutdown(2)
        self.sock.close()
        print('No. of tries for voltage='+str(n))
        return r
    
    def Read_Resistance(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        r=''
        message=bytes('READ:RES' ,'utf-8')
        self.sock.send(message)
        r = self.sock.recv(self.bufsize)
        self.sock.shutdown(2)
        self.sock.close()
        return r
    
    def Read_Current(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        r=''
        message=bytes('READ:CUR' ,'utf-8')
        self.sock.send(message)
        r = self.sock.recv(self.bufsize)
        self.sock.shutdown(2)
        self.sock.close()
        return r
    
    def Set_Current(self):
        k = 0
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        r=''
        while k<10: 
            try:
                mydata = float(input('Please enter desired Current (in Amp):'))
                if mydata>1.0:
                    print ('You are going to burn your instrument')
                    k+=1
                else:
                    message=bytes('SET:CUR'+str(mydata) ,'utf-8')
                    break
            except ValueError:
                print ('Current is a number, Moron')
                k+=1
        self.sock.send(message)
        r = self.sock.recv(self.bufsize)
        self.sock.shutdown(2)
        self.sock.close()
        return r
    
    def Meas_R_Single_Point(self):
        i = str(self.Set_Current())
        v = str(self.Read_Voltage())
        curr = float(i[11:-2])
        volt = float(v[11:-2])
        r = (volt/curr)
        return 'Measured Resistance:'+str(r)+'Ohm'