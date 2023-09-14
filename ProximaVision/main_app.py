import threading
import customtkinter
from PIL import ImageTk, Image
import os 
from base_main import * 
import sys
import serial.tools.list_ports

APP_TITLE = "ProximaVision Controller"

#APP parameters
WIDTH =600
HIGHT =400

#Logo 
LOGO_IMG= "logo.png"
LOGO_WIDTH=100
LOGO_HIGHT=100
ports = serial.tools.list_ports.comports()


class zao_app_controoler(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
    #Variable 
        #for list of port     
        self.var = customtkinter.StringVar(self,value="selected port")
        self.PortsList=[]

    #call external files 
        self.zaosdkcontroller = ZaoSDKController()
        t1= threading.Thread()

        

                      
        self.title(APP_TITLE)
        #size window and fix the size 
        self.geometry(f'{WIDTH}x{HIGHT}')
        self.resizable(width=False, height=False)
        self._set_appearance_mode("light")

        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        #style 
        self.font_H1=customtkinter.CTkFont("",15,"bold")
        self.font_H2=customtkinter.CTkFont("",14)
        self.font_defult=customtkinter.CTkFont("",12)
        self.font_defult_bold=customtkinter.CTkFont("",13,"bold")
        self.text_color_defualt="black"
        self.text_color_success="green"
        self.text_color_error="red"
        self.text_color_alert="orange"
        

        
        Top_frame=customtkinter.CTkFrame(self,border_width=0,fg_color="#ffffff")
        Top_frame.grid(row=0, column=0, padx=5, pady=5, sticky="news",columnspan=3)
              
        Left_frame=customtkinter.CTkFrame(self,border_width=0,fg_color="#ffffff")
        Left_frame.grid(row=1, column=0, padx=5, pady=5, sticky="news")
        
        Right_frame=customtkinter.CTkFrame(self,border_width=0,fg_color="#ffffff")
        Right_frame.grid(row=1, column=1, padx=5, pady=5, sticky="news")
        
        bottom_frame=customtkinter.CTkFrame(self,border_width=0,fg_color="#ffffff")
        bottom_frame.grid(row=2, column=0, padx=5, pady=5, sticky="news",columnspan=3)
        
    #Top_frame    
        #logo top 
        my_image = customtkinter.CTkImage(light_image=Image.open(f"{os.path.dirname(__file__)}\{LOGO_IMG}"),
                                  dark_image=Image.open(f"{os.path.dirname(__file__)}\{LOGO_IMG}"),
                                  size=(LOGO_HIGHT, LOGO_WIDTH))
        
        label_logo=customtkinter.CTkLabel(Top_frame, image=my_image, text='')
        label_logo.grid(row=0, column=0, padx=(WIDTH-LOGO_WIDTH)/2, pady=0, sticky="ws" )
        
        #Slogan Frame
        label_slogan=customtkinter.CTkLabel(Top_frame,text='Proximavision Controller',font=self.font_H1, text_color=self.text_color_defualt)
        label_slogan.grid(row=2, column=0, padx=0, pady=0, sticky="NS" )
        
        
        
        
        
        
    #Left_frame
        IPADX_STATUS=30

        # label_title_LF=customtkinter.CTkLabel(Left_frame,text='Serial Ports',font=self.font_defult, text_color=self.text_color_defualt)
        # label_title_LF.grid(row=0, column=0, padx=0, pady=0, sticky="ew" ) 
        
        #Menu list of ports
        self.listbox=customtkinter.CTkOptionMenu(Left_frame,variable=self.var, values=self.Get_Port_List(),width=100)
        self.listbox.grid(row=1, column=0, padx=(5,5), pady=10, sticky="ew",)
        #connect to port button
        self.BT_connect=customtkinter.CTkButton(Left_frame,text="connect",command=  lambda: self.items_selected(True))
        self.BT_connect.grid(row=1, column=1, padx=0, pady=0, sticky="ew")
        

        label_title_RF=customtkinter.CTkLabel(Left_frame,text='System Status',font=self.font_H2, text_color=self.text_color_defualt)
        label_title_RF.grid(row=3, column=0, sticky="w" )    
        
        #port lable 
        label_port=customtkinter.CTkLabel(Left_frame,text='Port : ',font=self.font_defult_bold, text_color=self.text_color_defualt)
        label_port.grid(row=4, column=0, ipadx=IPADX_STATUS, sticky="w" )  
        
        self.label_port_value=customtkinter.CTkLabel(Left_frame,text='Not Selected',font=self.font_defult, text_color=self.text_color_defualt)
        self.label_port_value.grid(row=4, column=1, sticky="w" )  
        
        #Baud lable 
        label_port=customtkinter.CTkLabel(Left_frame,text='Baud : ',font=self.font_defult_bold, text_color=self.text_color_defualt)
        label_port.grid(row=5,ipadx=IPADX_STATUS, column=0, sticky="w" )  
        
        label_port_value=customtkinter.CTkLabel(Left_frame,text='115200',font=self.font_defult, text_color=self.text_color_defualt)
        label_port_value.grid(row=5, column=1, sticky="w" ) 
        
        #Freq lable 
        label_port=customtkinter.CTkLabel(Left_frame,text='Freq : ',font=self.font_defult_bold, text_color=self.text_color_defualt)
        label_port.grid(row=6,ipadx=IPADX_STATUS, column=0, sticky="w" )  
        
        label_port_value=customtkinter.CTkLabel(Left_frame,text=FREQUENCY,font=self.font_defult, text_color=self.text_color_defualt)
        label_port_value.grid(row=6, column=1, sticky="w" ) 
        
        #Joystick Frame    
        label_joystick_type=customtkinter.CTkLabel(Left_frame,text='Joystick Type :',font=self.font_defult_bold, text_color=self.text_color_defualt)
        label_joystick_type.grid(row=7, ipadx=IPADX_STATUS,column=0, sticky="w" )
        
        self.label_joystick_type_value=customtkinter.CTkLabel(Left_frame,text='Not Connected ',font=self.font_defult, text_color=self.text_color_defualt)
        self.label_joystick_type_value.grid(row=7, column=1,sticky="w" )
        
    #Right Frame
     
        #throttle   
        self.lable_throttle=customtkinter.CTkLabel(Right_frame,text='Joystick  :',font=self.font_defult_bold, text_color=self.text_color_defualt)
        self.lable_throttle.grid(row=0, ipadx=IPADX_STATUS,column=0, sticky="w" )
        
        #TX RX     
       
        
        self.label_tx_value=customtkinter.CTkLabel(Right_frame,text='   TX not Active    ',font=self.font_defult, text_color=self.text_color_defualt)
        self.label_tx_value.grid(row=2, column=0 ,pady=20 )
        
        self.label_rx_value=customtkinter.CTkLabel(Right_frame,text='   RX not Active    ',font=self.font_defult, text_color=self.text_color_defualt)
        self.label_rx_value.grid(row=3, column=0,  )
        
        self.BT_connect_exit=customtkinter.CTkButton(Right_frame,text="Exit",command= lambda:self.exit_app())
        self.BT_connect_exit.grid(row=4, column=0,  pady=10 )
             
        
        txt='Zao SDK Controller App for JetRacer ROS(ProximaVision) - V1.1.0.0\n Khaldon Araffa 2023'
    #Bottom_frame
        label_title_BF=customtkinter.CTkLabel(bottom_frame,text=txt,font=self.font_defult, text_color=self.text_color_defualt)
        paddx=WIDTH/2-len(txt)-50
        print(len(txt))
        
        label_title_BF.grid(sticky='ew', ipadx=paddx) 
    





# #Functions    
#     #get path to image
#     # multi fuctions to use it with py to exe
#     def resource_path(self, relative):
#             return os.path.join(
#                 os.environ.get(
#                     "_MEIPASS2",
#                     os.path.abspath(".")
#                 ),
#                 relative
#             )
            
#     def resource_path0(self,relative_path):
#             """ Get absolute path to resource, works for dev and for PyInstaller """
#             base_path = getattr(
#                 sys,
#                 '_MEIPASS',
#                 os.path.dirname(os.path.abspath(__file__)))
#             return os.path.join(base_path, relative_path)
        
#     def resource_path1(self,relative):
#             return os.path.join(
#                 os.environ.get(
#                     "_MEIPASS2",
#                     os.path.abspath(".")
#                 ),
#                 relative
#             )
#     def resource_path2(self,relative_path):
#             """ Get absolute path to resource, works for dev and for PyInstaller """
#             try:
#                 # PyInstaller creates a temp folder and stores path in _MEIPASS
#                 base_path = sys._MEIPASS
#             except Exception:
#                 base_path = os.path.abspath(".")
#             return os.path.join(base_path, relative_path)
    
#     #stop connection and exit app  
    def exit_app(self):
            # self.start_new_thread('False',self.selected_port)
            for proc in psutil.process_iter():
            # check whether the process name matches
                
                if proc.name() ==  APP_TITLE:
                    proc.kill()
            # raise Exception('Stop now!')
        
            # self.destroy()   
            # self.zaosdkcontroller.close()
            # sys.exit()
     
            
#     #open port and start connection 
    def start_new_thread(self,stop_connection, selected_port):
                t1 = threading.Thread(target = self.run_connection, args =(stop_connection,selected_port))
                t1.start()

    def run_connection(self,stop_connection,port):        
                # print(f'333333{stop_connection}')
                while True:
                    if stop_connection=='False':
                        asyncio.run(self.zaosdkcontroller.start(port))
                        time.sleep(1)
                    else:
                        self.zaosdkcontroller.close_connection()
                        print('Closing thread')
                        # self.zaosdkcontroller.close_connection()
                        # raise Exception('Stop this thing')
                        # time.sleep(1)
                        break                
#     # Select port                 
    def items_selected(self,connect):
            self.selected_port = self.listbox.get()
            print(f"The Item selected {self.selected_port}")
            if len(self.selected_port)<7:
                Selected=True
            else:
                Selected=False
            
            print("Selected="+str(Selected) +self.selected_port)
        
            #   check if connected to selected port
            if (connect == True) and (Selected ):
                # self.label_port_value.configure(text=self.selected_port,fg_color="green")
                self.label_port_value.configure(text=f'Connected to {self.selected_port} ', fg_color="Green")
                self.listbox.configure(state='disabled')
                self.BT_connect.configure(state='disabled')
                self.start_new_thread('False',self.selected_port)


            elif not Selected:
                self.label_port_value.configure(text="Not Selected",fg_color="red")
            
            else:
                self.label_port['text']['text']=f'Not Connect'
                self.listbox['state']='normal'
                self.button_connect['state']='normal'
    

# 
# #get ports list



    def Get_Port_List(self):
            for  port, desc, hwid in sorted(ports):
                self.PortsList.append(port)
                # print(port)
            return self.PortsList

#     #update lables text
    def update_lables(self):
            self.label_joystick_type_value.configure(text=self.zaosdkcontroller.get_joy_details()[0])
            if self.zaosdkcontroller.get_joy_details()[1]==1:
                self.label_joystick_type_value.configure(fg_color="green")
                # self.throttle1 =self.num_to_range(self.zaosdkcontroller.get_direction()[2],'y')
                # self.Steering1 =self.num_to_range(self.zaosdkcontroller.get_direction()[3],'x')
                self.throttle1 =self.zaosdkcontroller.get_direction()[2]
                self.Steering1 =self.zaosdkcontroller.get_direction()[3]
                self.lable_throttle.configure(text=f'Throttle =  :{ float("{:.2f}".format(self.throttle1))} | Steering ={ float("{:.2f}".format(self.Steering1))}')
                               
                # print(f"before {self.zaosdkcontroller.get_direction()[2]} after {self.throttle1}")
                # self.VJ.move_joystick(self.throttle1,self.Steering1)
                if self.zaosdkcontroller.get_leds()[0]==True:
                    self.label_tx_value.configure(text="   TX   ",fg_color="green")
                else:
                    self.label_tx_value.configure(fg_color="red")

                if self.zaosdkcontroller.get_leds()[1]==True:
            #         # self.label_tx_value._image(Image.open(f"{os.path.dirname(__file__)}\logo.png"))
                    self.label_rx_value.configure(text="   RX   ",fg_color="green")
                else:
                    self.label_rx_value.configure(fg_color="red")

            else:
                self.label_Joy_value.configure(text="Disconnected", fg_color="red") 
            self.after(50, self.update_lables) # run itself again after 1000 ms

#     #mapping range        
    # def num_to_range(self,num, axis='x'):
    #         if axis=='x':
    #             inMin=-1
    #             inMax=1
    #             outMin=-100
    #             outMax=100
    #         elif axis=='y':
    #             inMin=-1
    #             inMax=1
    #             outMin=160
    #             outMax=79
    #         return outMin + (int(num - inMin) / float(inMax - inMin) * (outMax- outMin))





            
if __name__ == '__main__':
    app = zao_app_controoler()
    app.update_lables()
    app.mainloop()
    
    