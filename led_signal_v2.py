#Eva Bhatia's LED Signal Project

from time import sleep
#from gpiozero import LED
import string

#led = LED(17) 

def led_blink(number=1):
    
    i=1
    
    while(i<=number):
        print('led_on')
        #led.on()
        sleep(0.5)
        print('led_off')
        #led.off()
        i=i+1
    print(i-1)



#led.off()
#sleep(2)
"""
led_blink(5)
sleep(2)
led_blink(22)
sleep(2)
led_blink(1)
"""

while True:
    val = input("Enter your value: ") 
    n = string.ascii_lowercase.index(val)
    led_blink(n+1)




