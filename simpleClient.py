
import bluetooth

bd_addr = "04:C2:3E:65:AB:B0"

port = 1

sock=bluetooth.BluetoothSocket( bluetooth.L2CAP )
sock.connect((bd_addr, port))

sock.send("hello!!")

sock.close()
