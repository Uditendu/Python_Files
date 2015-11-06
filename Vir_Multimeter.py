import socket
import numpy as np
import matplotlib.pyplot as plt


class Multimeter(object):
    def __init__(self, host, port, bufsize):
        self.host = host
        self.port = port
        self.bufsize = bufsize
        
    def Cheak_Current_Val(self,A):
        k = 0
        while k<10: 
            try:
                mydata = float(input(A))
                if mydata>1.0:
                    print ('You are going to burn your instrument: Please enter a value between 0 to 1')
                    k+=1 
                elif mydata<0.0 or mydata==0:
                    print ('Please give a positive current between 0 to 1')
                else:
                    value = mydata
                    break
            except ValueError:
                print ('Current is a number, Moron')
                k+=1
        return value
    
    def Set_Current_Value(self,val):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        message=bytes('SET:CUR'+str(val) ,'utf-8')
        r = self.bypass_error(message,3)
        self.sock.shutdown(2)
        self.sock.close()
        return r
    
    def bypass_error(self,message,m):
        v = 0
        r = ''
        n = 0
        while v==0:
            self.sock.send(message)
            r = self.sock.recv(self.bufsize)
            c = str(r)
            try:
                x = int(str(c[-m]))
                v=1
                n+=1
            except ValueError:
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.sock.connect((self.host, self.port))
                v=0
        return r

    def Read_Voltage(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        message=bytes('READ:VOL' ,'utf-8')
        r = self.bypass_error(message,3)
        self.sock.shutdown(2)
        self.sock.close()
        #print('No. of tries for voltage='+str(n))
        return r
    
    def Read_Resistance(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        message=bytes('READ:RES' ,'utf-8')
        r = self.bypass_error(message,5)
        self.sock.shutdown(2)
        self.sock.close()
        return r
    
    def Read_Current(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        message=bytes('READ:CUR' ,'utf-8')
        r = self.bypass_error(message,3)
        self.sock.shutdown(2)
        self.sock.close()
        return r
    
    def Set_Current(self):
        val = self.Cheak_Current_Val('Please enter the desired value (in Amp):')
        cur = self.Set_Current_Value(val)
        return cur
    
    def Meas_R_Single_Point(self):
        i = str(self.Set_Current())
        v = str(self.Read_Voltage())
        curr = float(i[11:-2])
        volt = float(v[11:-2])
        r = (volt/curr)
        return 'Measured Resistance:'+str(r)+'Ohm'
    
    def Meas_R_Multi_Point(self):
        ini = self.Cheak_Current_Val('Please enter the initial current value (in Amp):')
        fin = self.Cheak_Current_Val('Please enter the final current value (in Amp):')
        diff = self.Cheak_Current_Val('Please enter the current step (in Amp):')
        
        current = ini
        X = []
        Y = []
        Z = []
        
        while (fin)>current:
            i = str(self.Set_Current_Value(current))
            v = str(self.Read_Voltage())
            r = float(v[11:-2])/float(i[11:-2])
            X.append(float(i[11:-2]))
            Y.append(float(v[11:-2]))
            Z.append(r)
            current+=diff
        
        plt.plot(X,Y,'.')
        plt.axis([(ini-diff), (fin+diff), (Y[0]-0.1), (Y[-1]+0.1)])
        plt.show()
        return Z
        