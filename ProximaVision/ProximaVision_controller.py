import threading
import customtkinter
from PIL import ImageTk, Image
import os 
from base_main import * 
import sys
import serial.tools.list_ports
ports = serial.tools.list_ports.comports()

class Zao_sdk_App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.PortsList=[]
        
        self.zaosdkcontroller = ZaoSDKController()
        t1= threading.Thread()
        
        self.title("ProximaVision Controller")
        self.geometry("600x400")
        self.resizable(width=False, height=False)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=4)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)


        #get the list of avible port 
        
        list_avaialble_ports=self.Get_Port_List()
        self.var = customtkinter.StringVar(self,value="selected port")
        # self.var=customtkinter.StringVar(value="sdfsdfsd")  # set initial value
        # self.var1=customtkinter.Variable(value=list_avaialble_ports)
        

        # self.checkbox_1 = customtkinter.CTkCheckBox(self, text="checkbox 1")
        # self.checkbox_1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        # self.checkbox_2 = customtkinter.CTkCheckBox(self, text="checkbox 2")
        # self.checkbox_2.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")
        # self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
        # self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
        
        Left=customtkinter.CTkFrame(self,width=200,height=400,border_width=1)
        Left.grid(row=0, column=0, padx=10, pady=20, sticky="nw",rowspan=8,)
                
        right_top=customtkinter.CTkFrame(self,width=400,height=50,border_width=1)
        right_top.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        right_middle=customtkinter.CTkFrame(self,width=400,height=150,border_width=1)
        right_middle.grid(row=1, column=1, padx=10, pady=10,sticky="nsew")
        
        right_bottom=customtkinter.CTkFrame(self,width=400,height=50,border_width=1)
        right_bottom.grid(row=2, column=1, padx=10, pady=10,sticky="nsew")
      
        my_image = customtkinter.CTkImage(light_image=Image.open(f"{os.path.dirname(__file__)}\logo.png"),
                                  dark_image=Image.open(f"{os.path.dirname(__file__)}\logo.png"),
                                  size=(100, 100))
        
        # my_image = customtkinter.CTkImage(light_image=Image.open(r"C:\\Users\\araff\Desktop\\zao_controller_app\\zao_sdk_controller_app-main\\logo.png"),
        #                           dark_image=Image.open(r'C:\\Users\\araff\Desktop\\zao_controller_app\\zao_sdk_controller_app-main\\logo.png'),
        #                           size=(70, 70))
        
        # path=self.resource_path("logo.png")
        # # print(path)
        # my_image = customtkinter.CTkImage(light_image=Image.open("logo.png"),
        #                           dark_image=Image.open(file=path),
        #                           size=(70, 70))
        
        label_logo=customtkinter.CTkLabel(Left, image=my_image, text='')
        # label_logo=customtkinter.CTkLabel(Left, text='')
        label_logo.grid(row=0, column=0, padx=0, pady=5, sticky="n" )
        

        self.listbox=customtkinter.CTkOptionMenu(Left,width=150,height=30,variable=self.var, values=list_avaialble_ports )
        self.listbox.grid(row=1, column=0, padx=20, pady=20, sticky="n" )

        self.label_connection=customtkinter.CTkLabel(Left,text='Not Connected',bg_color="red")
        self.label_connection.grid(row=3, column=0, padx=0, pady=2, sticky="n")
        # self.label_logo=customtkinter.CTkLabel(Left,text='sssss')
        # self.label_logo.grid(row=3, column=0, padx=0, pady=2, sticky="n")


        label_port=customtkinter.CTkLabel(right_middle,text='Port:')
        label_port.grid(row=1, column=1, padx=10, pady=2, sticky="w" )
        self.label_port_value=customtkinter.CTkLabel(right_middle,text='Not selected')
        self.label_port_value.grid(row=1, column=2, padx=15, pady=2)

      
        label_Baud=customtkinter.CTkLabel(right_middle,text='Baud:')
        label_Baud.grid(row=2, column=1, padx=10, pady=2, sticky="w" )
        label_Baud_value=customtkinter.CTkLabel(right_middle,text=BAUD)
        label_Baud_value.grid(row=2, column=2, padx=15, pady=2 )

        label_Freq=customtkinter.CTkLabel(right_middle,text='Freq.:')
        label_Freq.grid(row=3, column=1, padx=10, pady=2, sticky="w" )
        label_Freq_value=customtkinter.CTkLabel(right_middle,text=FREQUENCY)
        label_Freq_value.grid(row=3, column=2, padx=15, pady=2)

      
        
        self.label_tx=customtkinter.CTkLabel(right_middle,text='TX')
        self.label_tx.grid(row=5, column=1, padx=10, pady=2, sticky="w" )
        self.label_tx_value=customtkinter.CTkLabel(right_middle,text="none")
        self.label_tx_value.grid(row=5, column=2, padx=15, pady=2 )
        
        self.label_rx=customtkinter.CTkLabel(right_middle,text='RX')
        self.label_rx.grid(row=6, column=1, padx=10, pady=2, sticky="w" )
        self.label_rx_value=customtkinter.CTkLabel(right_middle,text="none")
        self.label_rx_value.grid(row=6, column=2, padx=15, pady=2 )

        self.BT_connect=customtkinter.CTkButton(Left,text="connect",command=  lambda: self.items_selected(True))
        self.BT_connect.grid(row=7, column=0, padx=0, pady=2, sticky="n" )
        
        self.BT_connect_exit=customtkinter.CTkButton(Left,text="Exit",command=self.quit)
        self.BT_connect_exit.grid(row=8, column=0, padx=0, pady=10, sticky="n" )

        label_Joy=customtkinter.CTkLabel(right_top,text='Joystick: ')
        label_Joy.grid(row=0, column=1, padx=10, pady=15, sticky='w' )
        self.label_Joy_value=customtkinter.CTkLabel(right_top,text='connected',fg_color='green')
        self.label_Joy_value.grid(row=0, column=2, padx=15, pady=15,sticky='w'  )

        label_Joy_type=customtkinter.CTkLabel(right_top,text='Type:')
        label_Joy_type.grid(row=0, column=3, padx=10, pady=15,sticky='e'  )
        self.label_Joy_type_value=customtkinter.CTkLabel(right_top,text=self.zaosdkcontroller.get_joy_details()[0])
        self.label_Joy_type_value.grid(row=0, column=4, padx=15, pady=15,sticky='e' )

        label_app_info=customtkinter.CTkLabel(right_bottom,text='Zao SDK Controller App for JetRacer - V1.0.0.0\n Khaldon Araffa 2023')
        label_app_info.grid(row=0, column=0, padx=65, pady=5,sticky="N")

        #get the list of available port    
        # canvas=customtkinter.CTkCanvas(right_middle)
        # self.VJ=Joystick_virtual(canvas,400,250, 25,50)
        # canvas.pack(expand=True, fill='both')
        # # canvas.grid(row=0, column=1, padx=10, pady=10, sticky="nw")
             
        self.lable_throttle=customtkinter.CTkLabel(right_middle,text=self.zaosdkcontroller.get_direction()[3])
        label_app_info.grid(row=4, column=1, padx=0, pady=5,sticky="N")

        
        # self.lable_throttle.grid(row=1, column=0, padx=2, pady=2,sticky='e' )

    def resource_path(self, relative):
        return os.path.join(
            os.environ.get(
                "_MEIPASS2",
                os.path.abspath(".")
            ),
            relative
        )
        
    def resource_path0(self,relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        base_path = getattr(
            sys,
            '_MEIPASS',
            os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)
    
    def resource_path1(self,relative):
        return os.path.join(
            os.environ.get(
                "_MEIPASS2",
                os.path.abspath(".")
            ),
            relative
        )
        return os.path.join(base_path, relative_path)
    def resource_path2(self,relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
    
    def start_new_thread(self,stop_connection, selected_port):
            t1 = threading.Thread(target = self.run_connection, args =(stop_connection,selected_port))
            t1.start()

    def run_connection(self,stop_connection,port):        
            print(f'333333{stop_connection}')
            while True:
                if stop_connection=='False':
                    asyncio.run(self.zaosdkcontroller.start(port))
                    time.sleep(1)
                else:
                    # self.zaosdkcontroller.close_connection()
                    print('Closing thread')
                    # self.zaosdkcontroller.close_connection()
                    # raise Exception('Stop this thing')
                    # time.sleep(1)
                    break                
                
    def items_selected(self,connect):
        self.selected_port = self.listbox.get()
        print(f"The Item selected {self.selected_port}")
        if len(self.selected_port)<7:
            Selected=True
        else:
            Selected=False
    
    #   check if connected to selected port
    
        if (connect == True) and (Selected ):
            self.label_port_value.configure(text=self.selected_port,fg_color="transparent")
            self.label_connection.configure(text="Connected", fg_color="Green")
            self.listbox.configure(state='disabled')
            self.BT_connect.configure(state='disabled')

            self.start_new_thread('False',self.selected_port)

            
        elif not Selected:

            self.label_port_value.configure(text="Not Selected",fg_color="red")
        
        else:
            self.label_port['text']['text']=f'Not Connect'
            self.listbox['state']='normal'
            self.button_connect['state']='normal'

      
    def update_lables(self):
        self.label_Joy_type_value.configure(text=self.zaosdkcontroller.get_joy_details()[0])
        if self.zaosdkcontroller.get_joy_details()[1]==1:
            self.label_Joy_value.configure(text="Connected", fg_color="green")
            self.throttle1 =self.num_to_range(self.zaosdkcontroller.get_direction()[2],'y')
            self.Steering1 =self.num_to_range(self.zaosdkcontroller.get_direction()[3],'x')
            self.lable_throttle.configure(text=f'the throttle is :{self.throttle1} the Steering is {self.Steering1}')
            
            
            # new_x=self.num_to_range(self.throttle1,'y')
            # new_y=self.num_to_range(self.Steering1,'x')
            print(f"before {self.zaosdkcontroller.get_direction()[2]} after {self.throttle1}")
            # self.VJ.move_joystick(self.throttle1,self.Steering1)
            if self.zaosdkcontroller.get_leds()[0]==True:
                self.label_tx_value.configure(text="On",fg_color="green")
            else:
                self.label_tx_value.configure(text="Off",fg_color="red")

            if self.zaosdkcontroller.get_leds()[1]==True:
                # self.label_tx_value._image(Image.open(f"{os.path.dirname(__file__)}\logo.png"))
                self.label_rx_value.configure(text="On",fg_color="green")
            else:
                self.label_rx_value.configure(text="Off",fg_color="red")

        else:
            self.label_Joy_value.configure(text="Disconnected", fg_color="red") 
        self.after(50, self.update_lables) # run itself again after 1000 ms

            
    def num_to_range(self,num, axis='x'):
        if axis=='x':
            inMin=-1
            inMax=1
            outMin=250
            outMax=150
        elif axis=='y':
            inMin=-1
            inMax=1
            outMin=160
            outMax=79
        return outMin + (int(num - inMin) / float(inMax - inMin) * (outMax- outMin))

    def Get_Port_List(self):
        for  port, desc, hwid in sorted(ports):
            self.PortsList.append(port)
            # print(port)
        return self.PortsList
        

        
if __name__ == '__main__':
    app = Zao_sdk_App()
    app.update_lables()
    app.mainloop()
    
    

