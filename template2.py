import os
os.environ['KIVY_GL_BACKEND'] = 'gl'
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
import time
from kivy.clock import Clock
import db


class Screen(FloatLayout):
    '''It is base layout that holds all our widgets'''
    cod_val = ObjectProperty(None)
    bod_val = ObjectProperty(None)
    tss_val = ObjectProperty(None)
    ph_val = ObjectProperty(None)
    flow_val = ObjectProperty(None)
    def temp_render(self, *arg):
        cod = "N/A"
        bod = "N/A"
        tss = "N/A"
        ph = "N/A"
        flow = "N/A"
        db_value = db.get_parameter_values()
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
        obj = Screen()
        Clock.schedule_interval(obj.temp_render, 1)
        return obj


if __name__ == "__main__":
    Template2App().run()
