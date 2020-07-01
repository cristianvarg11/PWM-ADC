#---------- Import modules ------------------#
import time
import machine
import network
from umqtt.simple import MQTTClient
#---------- Declarations  -------------------#
mqtt_server = '192.168..'  # broker direction
puerto = 1883  # broker port
client_id = b'user'
topic_sub = b'PWM_ADC'
topic_pub = b'PWM_ADC'
last_message = 0  
message_interval = 10  # in seconds
ssid = 'AP ssid'
password = 'AP passqord'
#---------------------------------------------#
def start_wifi():
    estacion = network.WLAN(network.STA_IF)  # instanciar obj estacion
    estacion.active(True)
    estacion.connect(ssid, password)
    while not estacion.isconnected():
        pass
    print('Conexion establecida con AP')
    print(estacion.ifconfig())

#============= MQTT ==================================#
#---------- Func CallBack --------------------#
def call_back(topic, mnsg):
    print('Han publicado: ')
    print((topic, mnsg))
#---------------------------------------------#

#---------- Func connect & subscribe ---------#
def connect_and_sub():
    cliente = MQTTClient(client_id, mqtt_server, puerto)
    cliente.set_callback(call_back)  # func call back
    cliente.connect()  # conection
    cliente.subscribe(topic_sub)  # subscription
    return cliente
#---------------------------------------------#
#--------- Func restar -----------------------#
def restart_and_reconn():
    print('No fue posible conectarse al broker MQTT\nReconectando ...')
    time.sleep(10)
    machine.reset()
#---------------------------------------------#
#=====================================================#
