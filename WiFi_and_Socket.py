from wireless import Wireless
import wifi
import socket
from socket import error
import os
import time
import binascii
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='[ %(asctime)s ] - %(levelname)s:  %(message)s',
                    datefmt='%H:%M:%S %m-%d-%y')
 

logging.debug('Main application is running!')

def check_root():
    if not os.geteuid() == 0:
        print("Run as root.")
        exit(1)


def application():

    ssid_list = []
    check_root()

    for cell in wifi.Cell.all('wlan0'):
        ssid = cell.ssid
        ssid_list.append(ssid)

    cont = 0
    print('Redes Wi-Fi disponiveis:')
    for ssid_names in ssid_list:
        print('(',cont,'): ', ssid_names)
        cont = cont + 1

if __name__ == '__main__':
    application()
    SSID_connect = input('Entre com o nome da rede Wi-Fi (SSID): ')
    PASSWORD_connect = input('Entre com a senha da rede Wi-Fi (Password): ')
    wireless = Wireless()
    try:
        wireless.connect(ssid=SSID_connect, password=PASSWORD_connect)   
        time.sleep(3)
        HOST = '192.168.0.1'
        PORT = 80
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        destino = (HOST, PORT)
        try:
            tcp.connect(destino)
        except error as erro:
            logging.error(erro)
            while True:
                pass
            
        msg = 'POST / HTTP/1.1\r\n\r\nnet_ssid=MSF&net_sec=true&net_pass=msfTeste123&net_tls=true&wlan_ip=192.168.0.57&wlan_mask=255.255.255.0&serial_baud1=9600&serial_baud2=&serial_parity=N&serial_stop=1'
        resp = msg.encode()
        print('------------------------------------')
        print(resp)
        print('----------------binario--------------------')
        x = binascii.hexlify(resp)
        print(x)
        print('------------------------------------')
        tcp.send(resp)
        time.sleep(2)
        tcp.close()
    except:
        print("Falha de coneção")



           
