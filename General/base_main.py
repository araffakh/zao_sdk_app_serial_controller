#!/usr/bin/python3 -u

# Zao SDK Jetbot
# Pawana LLC.
# Khaldon Araffa
# 2023.07


import logging
import asyncio
import time
# from ps_input import PSInput
from communication import Communication
from heartbeatled import HeartbeatLed

#Using the pygame to read Joystic
import pygame

logging.basicConfig(level=logging.INFO)

VERSION = '1.0.0.0'

SERIAL_PORT = ''
BAUD = 115200

FREQUENCY = 50

HEARTBEAT_LED_GPIO_PIN_RX = 17 #ハートビート用LED RX
HEARTBEAT_LED_GPIO_PIN_TX = 27 #ハートビート用LED TX
BASE_BOARD_TYPE="desktop"


CONNECTINO_TIMEOUT = 2

class ZaoSDKController:
    def __init__(self,):
        #init Joystick
        pygame.init()
        print(pygame.joystick.get_count())
        self.throttle=0
        self.steering =0
        if pygame.joystick.get_count()>0:
            self.psinput = pygame.joystick.Joystick(0)
            self.psinput.init()
            print ('Initialized Joystick : %s' % self.psinput.get_name())
            self.joy_connected=True
        else:
            self.joy_connected=False
            
        self.led = HeartbeatLed(BASE_BOARD_TYPE,HEARTBEAT_LED_GPIO_PIN_RX, HEARTBEAT_LED_GPIO_PIN_TX)
        self.prev_hertbeat_sent_time = time.time()
        self.prev_hertbeat_received_time = time.time()

    def get_joy_details(self):
        # if pygame.joystick.get_count()>0:
        #     self.psinput = pygame.joystick.Joystick(0)
        #     self.psinput.init()
        #     print ('Initialized Joystick : %s' % self.psinput.get_name())
        #     self.joy_connected=True
        # else:
        #     self.joy_connected=False
            
        if self.joy_connected==True:
            joy_name= self.psinput.get_name()
            Joy_status= self.joy_connected  
        else:
            joy_name= "joystic not recognized"
            Joy_status= False 
        
        return joy_name,Joy_status              

            
    def handle_joypad_axis(self, stick0_val, stick1_val, stick2_val, stick3_val):
        self.com.add_write_data(f'{stick0_val},{stick1_val},{stick2_val},{stick3_val}')
        logging.debug(f'gamepad stick {stick0_val} {stick1_val} {stick2_val} {stick3_val}')    
    
    
    # def SetPort(self, port):
    #     SERIAL_PORT=port
    #     return SERIAL_PORT
    # def close_connection():
    #     self.com.close_connection()
    
    def get_direction(self):
        
        if self.throttle>0.3:
            text1="Backward"
        elif (self.throttle <- 0.3):
            text1="Farward"
        else:
          text1="stop"
        if self.steering>0.3:
            text2="Right"
        elif (self.steering <- 0.3):
            text2="Left"
        else:
          text2="stop"
        
        return text1,text2,self.throttle,self.steering
    
    
    def get_leds(self):
        return self.led.led_tx,self.led.led_rx
        
        
    async def start(self,port='COM9'):
        logging.info(f"Zao SDK Controller started. {VERSION}")
        self.com = Communication(port, BAUD, FREQUENCY)
        self.com.start()    
        
        while(True):
            # Obtain joysitc values 
            pygame.event.pump()
            self.throttle = self.psinput.get_axis(1) #Farward - Back
            self.steering = self.psinput.get_axis(0) #Right left
            stop= self.psinput.get_button(2) #stop X button
            # print("Throttle:", self.throttle)
            # print("Steering:", steering)
            # print ("stop:",stop)
            self.com.add_write_data(f'{-self.throttle},{self.steering}')
            

            
            #send hertbeat            
            if time.time() - self.prev_hertbeat_sent_time >= 1.0:
                self.com.add_write_data('h\n') #add hert beat
                self.prev_hertbeat_sent_time = time.time()
                self.led.sentIndicator()

            #offline check
            if CONNECTINO_TIMEOUT < time.time() - self.prev_hertbeat_received_time:
                logging.debug('heart beat timeout')
                self.led.waitingmodeIndicator()

            # received data
            if self.com.received_data:
                cmd = self.com.received_data.popleft()
                if cmd =='h':
                    self.led.receivedIndicator()
                    self.prev_hertbeat_received_time = time.time()
                    logging.debug('hertbeat received')
                    
           

            time.sleep(1/FREQUENCY)
            
if __name__ == '__main__':
    print('started')
    # zaosdkcontroller = ZaoSDKController()
    # asyncio.run(zaosdkcontroller.start())
    

    
    
