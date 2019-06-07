from wireless import Wireless
import os
import wifi

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
    wireless.connect(ssid=SSID_connect, password=PASSWORD_connect)    
