import os
os.environ['KIVY_GL_BACKEND'] = 'gl'
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
import time
from kivy.uix.popup import Popup
from kivy.clock import Clock
import db
from kivy.uix.videoplayer import VideoPlayer
from asci import serial_connection
from kivy.uix.screenmanager import ScreenManager, Screen


class DataScreen(Screen):
    pass

class SettingsScreen(Screen):
    def calibrate(self):
        try:
            print("Initializing Calibration")
            serial_connection()
            ser.write('#W03%OPRUSS%')
            response  = ser.readline()
            print(ser)
            print(response)
        except Exception as er:
            print(er)

class KeypadScreen(Screen):
    password = ObjectProperty(None)
    db_passwd = "1234"
    def on_key_press(self, text):
        if text == "1":
            # print("One is Pressed")
            self.password.text += "1"
        if text == "2":
            # print("Two is Pressed")
            self.password.text += "2"
        if text == "3":
            # print("Three is Pressed")
            self.password.text += "3"
        if text == "4":
            # print("Four is Pressed")
            self.password.text += "4"
        if text == "5":
            # print("Five is Pressed")
            self.password.text += "5"
        if text == "6":
            # print("Six is Pressed")
            self.password.text += "6"
        if text == "7":
            # print("Seven is Pressed")
            self.password.text += "7"
        if text == "8":
            # print("Eight is Pressed")
            self.password.text += "8"
        if text == "9":
            # print("Nine is Pressed")
            self.password.text += "9"
        if text == "Clear":
            # print("Clear is Pressed")
            self.password.text = ""
        if text == "0":
            # print("Zero is Pressed")
            self.password.text += "0"
        if text == "Enter":
            print("Value Entered is ", self.password.text)
            if self.password.text == self.db_passwd:
                print("PAssword match")
                self.manager.current = 'settings'


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

    # def open_settings(self):
    #     print("Opening Settings")
    #     popup = Popup(content=KeypadScreen())
    #     popup.open()



class Template2App(App):
    def build(self):
        sm = ScreenManager()
        obj = MyScreen(name="home")
        vdo = VideoScreen(name="orpuss")
        keypad = KeypadScreen(name="keypad")
        settings = SettingsScreen(name="settings")
        data = DataScreen(name="data")
        # sm.add_widget(vdo)  # uncomments leter
        sm.add_widget(obj)
        sm.add_widget(settings)
        sm.add_widget(keypad)
        sm.add_widget(data)
        # video = obj.video_player()
        Clock.schedule_interval(obj.temp_render, 1)
        Clock.schedule_interval(obj.show_datetime, 1)
        # Clock.schedule_interval(vdo.run_home, 12)     # uncomments leter
        return sm
    # def on_start(self):
    #     sm = ScreenManager()
    #     sm.add_widget(MyScreen(name="home"))



if __name__ == "__main__":
    Template2App().run()
