import os
os.environ['KIVY_GL_BACKEND'] = 'gl'
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
import time
from kivy.clock import Clock
import db
from kivy.uix.videoplayer import VideoPlayer
from asci import serial_connection
from kivy.uix.screenmanager import ScreenManager, Screen


class VideoScreen(Screen):
    def video_player(self):
        self.player= VideoPlayer(source='opruss.mp4',  state='play', options={'allow_stretch': True})
        return self.player

    def run_home(self, *args):
        self.manager.current = 'home'

class MyScreen(Screen):
    '''It is base layout that holds all our widgets'''
    cod_val = ObjectProperty(None)
    bod_val = ObjectProperty(None)
    tss_val = ObjectProperty(None)
    ph_val = ObjectProperty(None)
    flow_val = ObjectProperty(None)
    timestamp = ObjectProperty(None)
    def calibrate(self):
        print("Initializing Calibration")
        serial_connection()
        ser.write('#W03%OPRUSS%')
        response  = ser.readline()
        print(ser)
        print(response)

    def show_datetime(self, *arg):
        self.timestamp.text = time.asctime()

    def sync(self):
        print("Syncing")

    def temp_render(self, *arg):
        cod = "N/A"
        bod = "N/A"
        tss = "N/A"
        ph = "N/A"
        flow = "N/A"
        db_value = db.get_parameter_values()
        print(db_value)
        for x in db_value:
            print("X is : ", x)
            # for key,value in x.items():
            if x["parameter_id"] == "parameter_83":
                cod = str(x["value"])
            if x["parameter_id"] == "parameter_84":
                bod = str(x["value"])
            if x["parameter_id"] == "parameter_85":
                tss = str(x["value"])
            if x["parameter_id"] == "parameter_80":
                ph = str(x["value"])
            if x["parameter_id"] == "parameter_81":
                flow = str(x["value"])
        if cod:
            self.cod_val.text = cod+" [size=15]mg/l[/size]"
        if bod:
            self.bod_val.text = bod+" [size=15]mg/l[/size]"
        if tss:
            self.tss_val.text = tss+" [size=15]mg/l[/size]"
        if ph:
            self.ph_val.text = ph
        if flow:
            self.flow_val.text = flow+" [size=15]m3/h[/size]"
    def show_datetime(self, *arg):
        self.timestamp.text = time.asctime()




class Template2App(App):

    def build(self):
        sm = ScreenManager()
        obj = MyScreen(name="home")
        vdo = VideoScreen(name="orpuss")
        sm.add_widget(vdo)
        sm.add_widget(obj)
        # video = obj.video_player()
        Clock.schedule_interval(obj.temp_render, 1)
        Clock.schedule_interval(obj.show_datetime, 1)
        Clock.schedule_interval(vdo.run_home, 12)
        return sm
    def on_start(self):
        sm = ScreenManager()
        sm.add_widget(MyScreen(name="home"))



if __name__ == "__main__":
    Template2App().run()
