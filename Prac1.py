#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: Matthew Lock
Student Number: LCKMAT002
Prac: 1
Date: 04/08/2019
"""

# import Relevant Librares
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
import time
print("GPIO and imports successful")

LED1=False
LED2=False
LED3=False


def press_callback(channel):

    global LED1
    print("Button1 pressed!")

    if not LED1:
        GPIO.output(29,1)
        LED1 = True

    else:
        GPIO.output(29,0)
        LED1 = False

def main():
    #if GPIO.event_detected(16):
    #    print("Button pressed!")
    #else:
    #    print("Nothing pressed!")
    GPIO.output(37, 1)
    time.sleep(0.3)
    GPIO.output(37, 0)
    time.sleep(0.3)

# Only run the functions if
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        #Setup GPIO PINS
        inputs = [16,18]
        outputs=[29,31,33,37]
        GPIO.setup(outputs, GPIO.OUT)
        GPIO.output(outputs,0)
        GPIO.setup(inputs, GPIO.IN)
        print("GPIO pins setup successful")

        #Setup interrupts
        #GPIO.add_event_detect(16, GPIO.RISING,bouncetime=200)
        GPIO.add_event_detect(16, GPIO.RISING, callback=press_callback,bouncetime=300)
        print("Interrupts setup successful")

        while True:
            main()

    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except:
        GPIO.cleanup()
        print("Some other error occurred")
        #print(e.message)
