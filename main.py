from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
class MainApp(MDApp):
    def build(self):

        return MDRectangleFlatButton("home")
    
if __name__ == '__main__':
    MainApp().run()




