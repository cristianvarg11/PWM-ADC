#--------- Import modules -----------------------------------#
from machine import PWM, Pin, ADC
#--------- Declarations ------------------------------------#
Ledb = PWM(Pin(21), freq = 1000, duty = 512)  # duty 50% = 512 (0% = 0 & 1023 = 100%)
Ledg = PWM(Pin(22), freq = 1000, duty = 512)
Ledr = PWM(Pin(23), freq = 1000, duty = 512)
duty_b = 0  #  duty cicle led blue
duty_g = 0  #  de duty cicle led green
duty_r = 0  #  de duty cicle led red
#------------ Config ADC ------------------------------------#
adc_blue = ADC(Pin(32))
adc_green = ADC(Pin(33))
adc_red = ADC(Pin(34))

adc_blue.atten(ADC.ATTN_11DB)
adc_green.atten(ADC.ATTN_11DB)
adc_red.atten(ADC.ATTN_11DB)

ADC.width(ADC.WIDTH_10BIT)
# methood read() read values on range 0-4095 (resolution 12 bits esp32)
# 10 bits -> 0-1023
#------------------------------------------------------------#
#__________________ ADC and PWM Functions ___________________#
#--------- Func leds ADC read & config duty -----------------#
def adc_readead(color_adc, duty_col, Pin_pwm):
    while color_adc.read() <= 1023:
        duty_col = color_adc.read()
        if duty_col >= 1023:
            duty_col = 1023
        elif duty_col <= 0:
            duty_col = 0
        Pin_pwm.duty(duty_col)
        break
#-----------------------------------------------------------#
#---------- Func calc ADC & PWM ----------------------------#
def calc_adc_range(col_adc_1, col_adc_2, col_adc_3):
    value_adc_1 = ((col_adc_1.read())*3.3)/ 1023
    value_adc_2 = ((col_adc_2.read())*3.3)/ 1023
    value_adc_3 = ((col_adc_3.read())*3.3)/ 1023

    Val_ADC = []
    Val_ADC.extend([value_adc_1, value_adc_2, value_adc_3])
    return Val_ADC
#-----------------------------------------------------------#
