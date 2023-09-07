import customtkinter

from tkinter import Canvas
from PIL import Image, ImageTk



class Joystick_virtual(customtkinter.CTk):
    def __init__(self, app,width_frame,height_frame,r_C1,r_C2):
        super().__init__()
        
        self.my_canvas=app
        self.x_center= width_frame/2
        self.y_center=height_frame/2
        self.r_C1=r_C1
        self.r_C2=r_C2
        points_C2 = (
            (self.x_center-self.r_C2, self.y_center-self.r_C2),
            (self.x_center+self.r_C2, self.y_center+self.r_C2)
        )
        points_C1 = (
            (self.x_center-self.r_C1, self.y_center-self.r_C1),
            (self.x_center+self.r_C1, self.y_center+self.r_C1)
        )
        
        # frame1 = customtkinter.CTkFrame(master=app,width=500,height=500)
        # frame1.grid(row=0,column=0,sticky="nesw")
        
        self.C2=self.my_canvas.create_oval(*points_C2, width =2,fill='white')
        self.C1=self.my_canvas.create_oval(*points_C1, width =2,fill='green')
        self.my_canvas.grid(row=0, column=0,sticky="nesw")
        # self.my_canvas.pack(anchor=customtkinter.CENTER, expand=True)

        # self.my_canvas.pack(padx=50,pady=50)
        # print(app.winfo_screenwidth())


        self.my_canvas.tag_bind(self.C1,"<Button1-Motion>", self.move, add="+")
        self.my_canvas.bind("<Button-3>", self.scan)
        self.my_canvas.bind("<Button3-Motion>",self.drag)
        self.my_canvas.bind("<ButtonRelease-1>",self.move_center)



        #Provides X-Y coordinates of mouse cursor when canvas object is selected
        self.my_label = customtkinter.CTkLabel(master=self.my_canvas, text="X: None Y: None",bg_color="white")
        self.my_label.pack(padx="10px", pady="10px", anchor="se")
        self.my_canvas.tag_bind(self.C1, "<Button1-Motion>",  self.display_coords, add="+")
        



        # self.my_canvas.configure(scrollregion=self.my_canvas.bbox(self.C1))
        # self.my_canvas = Canvas(master=frame1, height=500, width=500)

  
    
    def move(self, event):    
        if (event.y >self.y_center-self.r_C2) and (event.y <self.y_center+self.r_C2)and (event.x >self.x_center-self.r_C2) and (event.x <self.x_center+self.r_C2):
            self.my_canvas.moveto(self.C1,event.x-self.r_C1,event.y-self.r_C1)
            
    def scan(self,event):
        self.my_canvas.scan_mark(event.x, event.y)

    def drag(self, event):
        self.my_canvas.scan_dragto(event.x, event.y, gain=2)

    def display_coords(self, event):
        self.my_label.configure(text=f"X: {event.x} Y:{event.y}",fg_color="white")

    def move_center(self,event):
        self.my_canvas.moveto(self.C1,self.x_center-self.r_C1,self.y_center-self.r_C1)
        print(self.x_center-self.r_C1)

    def move_joystick(self, J_x=200,J_y=200):    
        self.my_canvas.moveto(self.C1,J_x-self.r_C1,J_y-self.r_C1)
            
    
# if __name__ == '__main__':
#     app1=customtkinter.CTk()
#     app1.geometry(f'{width_frame}x{height_frame}')
#     app1.resizable(width=False, height=False)
#     app1.grid_columnconfigure(0, weight=1)
#     app1.grid_rowconfigure(0, weight=1)       
#     my_canvas = customtkinter.CTkCanvas(app1, background="grey")
#     # frame1 = customtkinter.CTkFrame(master=app1,width=400,height=600)
#     # frame1.grid(row=0,column=0,sticky="nesw")
#     Joystick_virtual(my_canvas)
#     app1.mainloop()

