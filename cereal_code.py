# Control the position of a servo using PWM
from machine import Pin, PWM
import ssd1306
from time import sleep

#Servo motor
servo = PWM(Pin(14), freq=50)
servo.duty(80)

#Button
switch = Pin(1, Pin.IN, Pin.PULL_UP)

#Transistor
transistor = Pin(12, Pin.OUT)
transistor.value(0)

#External OLED Screen
i2c = I2C(1, sda=Pin(3), scl=Pin(38))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
#oled = OLED(i2c, Pin(18))

def dot_dot_dot_milk():
    
    for x in range (0,10):
        oled.fill(0)
        oled.text("Dispensing ", 0, 0)
        oled.text("milk.", 0, 10)
        oled.show()
        sleep(1)
        oled.fill(0)
        oled.text("Dispensing ", 0, 0)
        oled.text("milk..", 0, 10)
        oled.show()
        sleep(1)
        oled.fill(0)
        oled.text("Dispensing ", 0, 0)
        oled.text("milk...", 0, 10)
        oled.show()
        sleep(1)
    
    
    
def dot_dot_dot_cereal():
    oled.fill(0)
    oled.text("Dispensing ", 0, 0)
    oled.text("cereal.", 0, 10)
    oled.show()
    sleep(1)
    oled.fill(0)
    oled.text("Dispensing ", 0, 0)
    oled.text("cereal..", 0, 10)
    oled.show()
    sleep(1)
    oled.fill(0)
    oled.text("Dispensing ", 0, 0)
    oled.text("cereal...", 0, 10)
    oled.show()
    sleep(1)

# For a little SG90 micro-servos,
# 20 is full left, 130 is full right, 90 is about the middle
# you may need to troubleshoot and do you own calculations for your motor

while True:
    #Passive message
    oled.fill(0)
    oled.text("Press button to ", 0 , 0)
    oled.text("dispense cereal ", 0 , 10)
    oled.text("and milk!", 0, 20)
    oled.show()
    
    if not switch.value():
        
        #Actually dispensing milk
        transistor.value(1)
        dot_dot_dot_milk()
        transistor.value(0)
        
        #Printing cereal on screen
        oled.fill(0)
        oled.text("Done!", 0, 0)
        oled.show()
        sleep(2)
        
        #Actually dispensing cereal
        servo.duty(30)
        dot_dot_dot_cereal()
        servo.duty(80)
        
        #All done!
        oled.fill(0)
        oled.text("Enjoy!", 0, 0)
        oled.show()
                            
        #Finish sequence
        sleep(4)
        
        
    


