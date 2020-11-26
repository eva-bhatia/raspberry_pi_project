#Eva Bhatia's LED Signal Project

from time import sleep
#from gpiozero import LED


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
sleep(2)


#led_blink(5)
#sleep(2)
#led_blink(22)
#sleep(2)
#led_blink(1)

"""
while True:
    led.on()    # turn on LED
    print ('led turned on >>>')  # print message on terminal
    sleep(1)    # wait 1 second
    led.off()   # turn off LED 
    print ('led turned off <<<')
    sleep(1)    # wait 1 second
"""
