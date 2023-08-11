from pyLoraRFM9x import LoRa, ModemConfig
import time
# from alimentandofirebase import*
from testesprorasp import *
import struct
import ctypes as ct

class tipoDados(ct.Structure):
    _fields_ = (
            ("contador", ct.c_int),
            ("latitude", ct.c_int),
            ("longitude", ct.c_int),
            ("valuePh", ct.c_float)
    )


# This is our callback function that runs when a message is received
def on_recv(payload):
    print("From:", payload.header_from)
    print("Received:",payload.message)
    print("RSSI: {}; SNR: {}".format(payload.rssi, payload.snr))
    
    #Tratamento de dados recebidos do Arduino
    print('Messagem bruta', payload.message)
    msg = payload.message
    #print(msg)
    #print(msg[:9])
    unpacked_data = struct.unpack('ffi', msg)
    print(unpacked_data)
    dadoRecv = tipoDados()
    #fmt = "<fic"
    #fmt_size = struct.calcsize(fmt)
    #print('Tam: ', fmt_size)
    #dadoRecv.contador, dadoRecv.latitude, dadoRecv.longitude = struct.unpack(fmt, msg[:fmt_size])
    #print(dadoRecv)

    #dados = payload.message.decode('utf-8') #transformando em byte para sting/char
    #print(dados)
    #arrayData = dados.split(';')
    
    #Percorrer o array de dados e apenas pegar os numeros, removendo as strings
    '''
    for x in range(0,len(arrayData)):
        arrayData[x] = arrayData[x][2:]
        if x == len(arrayData) - 1:
            arrayData[x] = arrayData[x][:-1]
        print(arrayData[x])
    print(arrayData)
    
    
    arrayNomes = ['Turbidez', 'PH', 'Temperatura','TDS']
    for i in range(0,4):
       #feedFb(arrayNomes[i],arrayData[i])
       insert('PAI',arrayNomes[i],arrayData[i])
       #feedFbLastRecord('PAI')        
    
    print(len(payload.message))
    print("RSSI: {}; SNR: {}".format(payload.rssi, payload.snr))
    '''

# Lora object will use spi port 0 and use chip select 1. GPIO pin 5 will be used for interrupts and set reset pin to 25
# The address of this device will be set to 2
lora = LoRa(0, 1, 5, 2, 
        reset_pin = None, 
        freq=915, 
        tx_power=14,
        modem_config=ModemConfig.Bw125Cr45Sf128, 
        acks=False, 
        crypto=None, 
        receive_all=True
        )
lora.cad_timeout=2
lora.set_mode_rx()
lora.on_recv = on_recv

print("inicio")
print("inicio do banco")
#create_table()

# Send a message to a recipient device with address 10
# Retry sending the message twice if we don't get an  acknowledgment from the recipient
while(1):
    
    message = "ACK!\0"
    #status = lora.send_to_wait(message,255, retries=1)
    print('ouvindo...')
    #if status is True:
    #    print("Message sent!")
    #else:
    #    print("No acknowledgment from recipient")
    time.sleep(3)
    
lora.close()
