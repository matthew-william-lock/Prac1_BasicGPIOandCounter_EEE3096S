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
import itertools
print("GPIO and imports successful")

# Use itertools to set up binary values for states of LEDs
binaryStates = list(itertools.product([0, 1], repeat=3))
print binaryStates

counter = 0

inputs = [16,18]
LED_counter=[29,31,33]
flashing=37

def updateLEDs(button):
    global counter
    if button:
        counter=counter+1
        if counter>7:
            counter = 0
    else:
        counter=counter-1
        if counter<0:
            counter=7
    # Prints binary state and displays on LEDs
    print(binaryStates[counter])
    GPIO.output(LED_counter, binaryStates[counter])


# Detects counter add button press and calls for LED update
def add_callback(channel):
    print("Counter add button pressed!")
    updateLEDs(True)

# Detects subtract add button press and calls for LED update
def subtract_callback(channel):
    print("Counter subtract button pressed!")
    updateLEDs(False)

def main():
    #Flashing LED to show program is running
    GPIO.output(flashing, 1)
    time.sleep(0.3)
    GPIO.output(flashing, 0)
    time.sleep(0.3)

# Only run the functions if
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        #Setup GPIO PINS
        GPIO.setup(LED_counter, GPIO.OUT)
        GPIO.setup(flashing,GPIO.OUT)
        GPIO.output(LED_counter,0)
        GPIO.setup(inputs, GPIO.IN)
        print("GPIO pins setup successful")

        #Setup interrupts
        GPIO.add_event_detect(16, GPIO.RISING, callback=add_callback,bouncetime=200)
        GPIO.add_event_detect(18, GPIO.RISING, callback=subtract_callback,bouncetime=200)
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
