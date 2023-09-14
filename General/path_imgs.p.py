import os 
import sys


image="logo_text.png"

class Zao_sdk_App():
    def __init__(self):
        super().__init__()
        print("start")
        aa=self.resource_path(image)
        print("path =   "+aa)
        aa=self.resource_path0(image)
        print("path0 =   "+aa)
        aa=self.resource_path1(image)
        print("path1 =   "+aa)
        aa=self.resource_path2(image)
        print("path2 =   "+aa)


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
    
if __name__ == '__main__':
    aa=Zao_sdk_App()
    print(f"{os.path.dirname(__file__)}\logo.png")
    print("myyyyyy"+ os.path.join(os.getcwd(),'ProximaVision',"logo.png"))