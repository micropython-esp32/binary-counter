"""
Name: BinaryCounter.py
Purpose:  

Requirements: Micropython, ESP32 board, 4 LEDs

"""

from machine import Pin
from time import sleep_ms

    
def loop():
    b0 = Pin(32, Pin.OUT)
    b1 = Pin(33, Pin.OUT)
    b2 = Pin(12, Pin.OUT)
    b3 = Pin(13, Pin.OUT)
        
        
    print("Starting loop, use Ctrl-C to break out.")
    
    counter = 0
    
    while(1):
        print(counter)
        try:
            b0.value( counter & 0x01 ) # Assign bit position 0
            b1.value( counter & 0x02 ) # Assign bit position 1
            b2.value( counter & 0x04 ) # Assign bit position 2
            b3.value( counter & 0x08 ) # Assign bit position 3
            
            sleep_ms(1000)  # Sleep for 1000 milliseconds
            
            # Turn off all LEDs before moving to next binary number
            b0.off()
            b1.off()
            b2.off()
            b3.off()
            
            sleep_ms(1000)
            
        except KeyboardInterrupt: # Ctrl-C to come out of loop
            print("User Interruption, exiting loop")
            break
        
        counter = (counter + 1) % 16 # Loop for 1 to 15
        
loop()