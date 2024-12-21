from machine import Pin, PWM
from time import sleep

# Initialize PWM on GPIO pin (e.g., Pin 15)
servo = PWM(Pin(38))
servo.freq(50)  # Set PWM frequency to 50Hz

# Function to move the servo
def set_angle(angle):
    # Calculate duty cycle for the given angle
    duty = int(40 + (angle / 180) * 115)
    servo.duty_u16(duty)

# Example usage
while True:
    set_angle(0)
    sleep(1)
    set_angle(90)
    sleep(1)
    set_angle(180)
    sleep(1)
