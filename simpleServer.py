from bluetooth import *
s = BluetoothSocket(L2CAP)
s.bind(("", 0x1001))
s.listen(1)
conn, addr = s.accept()
print("Connected by %s" % addr)
data = s.recv(1024)
print("Received: %s" % data)
conn.close()
s.close()

