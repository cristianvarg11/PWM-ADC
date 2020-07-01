#--------- Import modules -----------------------------------#
import time
from machine import Pin
#------Locals modules ------#
import PWM_
import mqtt_
from mqtt_ import connect_and_sub, restart_and_reconn, message_interval, last_message
#--------- Declarations ------------------------------------#
botoncito = Pin(0, Pin.IN, Pin.PULL_UP)  #  BOOT on target esp32
#_____________________ RED _________________________________#
#============ WiFi ===================================#
mqtt_.start_wifi()
#============ MQTT ===================================#
#-------- Conection try ----------------------#
try:
    client = connect_and_sub()
except OSError as e:
    restart_and_reconn()
#---------------------------------------------#
#____________________________________________________________#

#/////////////////////////////// APP MAIN ////////////////////////////////////#
while True:
    PWM_.adc_readead(PWM_.adc_blue, PWM_.duty_b, PWM_.Ledb)
    PWM_.adc_readead(PWM_.adc_green, PWM_.duty_g, PWM_.Ledg)
    PWM_.adc_readead(PWM_.adc_red, PWM_.duty_r, PWM_.Ledr)
    time.sleep_ms(5)
    try:
        client.check_msg()
        if (time.time() - last_message) > message_interval:
            if not botoncito():
                time.sleep_ms(10)
                PWM_.calc_adc_range(PWM_.adc_blue, PWM_.adc_green, PWM_.adc_red)
                vall_adc = PWM_.calc_adc_range(PWM_.adc_blue, PWM_.adc_green, PWM_.adc_red)
                msg = b'-----------------------------'
                msg_1 = b'ADC 1 = %r\n' %vall_adc[0]
                msg_2 = b'ADC 2 = %r\n' %vall_adc[1]
                msg_3 = b'ADC 3 = %r\n' %vall_adc[2]
                msg_4 = b'-----------------------------'
                client.publish(mqtt_.topic_pub, msg)
                client.publish(mqtt_.topic_pub, msg_1)
                client.publish(mqtt_.topic_pub, msg_2)
                client.publish(mqtt_.topic_pub, msg_3)
                client.publish(mqtt_.topic_pub, msg_4)
                last_message = time.time()
    except OSError as e:
        restart_and_reconn()
#/////////////////////////////////////////////////////////////////////////////#
