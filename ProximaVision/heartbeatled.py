#!/usr/bin/python3 -u
# Zao SDK Jetbot
# Khaldon Araffa
# 2023.07

import time
from threading import Timer, Thread

class HeartbeatLed(Thread):
    def __init__(self,board_type ,gpiopin_rx, gpiopin_tx, waitspan = 0.3, min_flash_span_tx=0.5, min_flash_span_rx=1):
        Thread.__init__(self)
        self.setDaemon(True)

        self.lastupdate_rx = time.time()
        self.lastupdate_tx = time.time()
        self.waitspan = waitspan

        self.board=board_type
        self.led_rx=False
        self.led_tx=False
 

        self.min_flash_span_tx = min_flash_span_tx
        self.min_flash_span_rx = min_flash_span_rx
            
        if self.board=='desktop':
            self.led_rx=False
            self.led_tx=False
            

        # #reset all leds
        # for i in range(1,27):
        #     try:
        #         # GPIO.setup(i, GPIO.OUT)
        #         # GPIO.output(i, GPIO.LOW)    
        #         self.led_status(True,True,False)
        #         # self.led_status("Tx","LOW")            
        #         # self.led_status("Rx","LOW")            
        #         # self.led_rx=False
        #         # self.led_tx=False
        #     except Exception:
        #         pass
        
        time.sleep(0.2)

    def receivedIndicator(self):
        if self.lastupdate_rx + self.min_flash_span_rx <= time.time():
            self.lastupdate_rx = time.time()
            self.led_status(False,True,True)    
            received_t = Timer(self.waitspan, self.led_status, args=(False,True,False))
            received_t.start()

    def sentIndicator(self, waitspan = 0.1):
        if self.lastupdate_tx + self.min_flash_span_tx <= time.time():
            self.lastupdate_tx = time.time()
            self.led_status(True,False,True)    
            sent_t  = Timer(self.waitspan, self.led_status, args=(True,False,False))
            sent_t.start()

    def waitingmodeIndicator(self, waitspan = 0.1):
        self.lastupdate_rx = time.time()
        waiting_t = Timer(waitspan, self.flash, args=("RX"))
        waiting_t.start()

    def serverwaitingClientIndicator(self, waitspan=0.1):
        self.lastupdate_tx = time.time()
        waiting_t = Timer(waitspan, self.flash, args=("TX"))
        waiting_t.start()

    def flash(self, led, flashtime = 2, waitspan = 0.1):
        for i in range(2):
            if led=='RX':
                self.led_status(False,True,True)
                # print(f"the RX is","HIGH")            
                time.sleep(waitspan)    
                self.led_status(False,True,False)
                # print(f"the RX is","LOW")   
                time.sleep(waitspan)
            else:
                self.led_status(True,False,True)
                # print(f"the TX is","HIGH")            
                time.sleep(waitspan)    
                self.led_status(True,False,False)
                # print(f"the TX is","LOW")   
                time.sleep(waitspan)
            

    def led_status(self,tx,rx,status):
        if tx==True:
            self.led_tx=status
            # print(f"the {self.led_tx} is",status)
            
        elif rx==True:
            self.led_rx=status
            # print(f"the { self.led_rx} is",status)
            
        elif (tx==True)and (rx==True):
            self.led_tx=status
            self.led_rx=status
        
 
    def close(self):
        self.led_status(False,True,False)
        self.led_status(True,False,False)

