import os
os.environ['KIVY_GL_BACKEND'] = 'gl'
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
import time
from kivy.clock import Clock
import db

db_value = db.get_parameter_values()
for x in db_value:
    # for key,value in x.items():
    print(x)
    if x["parameter_id"] == "parameter_83":
        temp = str(x["value"])
        print("TEmp is ", temp)
class Screen(FloatLayout):
    '''It is base layout that holds all our widgets'''
    cod_val = ObjectProperty(None)
    def temp_render(self):
        self.cod_val.text = temp
    def show_datetime(self, *arg):
        self.timestamp.text = time.asctime()


class Template2App(App):
    def build(self):
        obj = Screen()
        Clock.schedule_interval(obj.temp_render, 1)
        return obj


if __name__ == "__main__":
    Template2App().run()
