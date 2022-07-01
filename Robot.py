import serial
import getch
serialport = serial.Serial ("/dev/ttyS0")
serialport.baudrate = 115200
x = ''
while(x != 'q'):
    x = getch.getch() 
    print(x)
    if x == 'w':
        command = '+100+100+1500'
    elif x == 'a':
        command = '-100+100+1500'
    elif x == 'd':
        command = '+100-100+1500'
    elif x == 's':
        command = '-100-100+1500'
    elif x == 'o':
        command = '+000+000+1500'
    serialport.write(command.encode())