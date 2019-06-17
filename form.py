import kivy
kivy.require('2.0.0.dev0')
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
import time
from kivy.clock import Clock

# Window.clearcolor = (0, 1, 1, 1)
Window.size = (900, 600)



class Screen(FloatLayout):
    '''It is base layout that holds all our widgets'''
    timestamp = ObjectProperty(None)
    def send_to_usb(self):
        print("Readings send to USB")
        popup = Popup(content=Label(text="Readings send to USB"),
            title="Status OK",
            size_hint= [0.2, 0.2]
        )
        popup.open()
    def show_datetime(self, *arg):
        self.timestamp.text = time.asctime()


    def btn_touch_up(self):
        print("Opening SETTINGS")
        from subprocess import Popen, PIPE
        process = Popen(['python3', 'template2.py'], stdout=PIPE, stderr=PIPE)



class HMIApp(App):
    def build(self):
        ''' Returns our base Widget '''
        obj = Screen()
        Clock.schedule_interval(obj.show_datetime, 1)
        return obj



if __name__ == "__main__":
    HMIApp().run()
