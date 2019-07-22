#!/usr/bin/python3
"""
First Python Script
Names: Matthew Lock
Student Number: LCKMAT002
Prac: NA
Date: 20 July 2019
"""

def main():
    #print("Hello World!")
    if GPIO.input(16):
        print('Input was HIGH')
    else:
        print('Input was LOW')

if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:

        #GPIO imports
        import RPi.GPIO as GPIO
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(16, GPIO.IN)
        print("GPIO pins setup successfully")

        while True:
            main()

    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()

    #Catch GPIO import error
    except RuntimeError:
        print("Error importing RPi.GPIO!")

    except e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)

    except:
        print("Some other error occurred")

