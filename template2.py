import kivy
kivy.require('2.0.0')
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
import time
from kivy.clock import Clock


class Screen(FloatLayout):
    '''It is base layout that holds all our widgets'''
    # timestamp = ObjectProperty(None)
    def show_datetime(self, *arg):
        self.timestamp.text = time.asctime()


class Template2App(App):
    def build(self):
        return Screen()


if __name__ == "__main__":
    Template2App().run()
