# -*- coding: ISO-8859-1 -*-
#import codecs

#After Simon Long <kudata@btinternet.com>

import unicodedata
import re
import itertools
import collections
import time
import string
import numpy
import pprint


from os import environ
from math import comb
from functools import (reduce, partial)
#from functools import partial

import kivy
from kivy.utils import escape_markup
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.effects.scroll import ScrollEffect
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen


from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty, StringProperty, ListProperty
)

class HelloWorld(App):
  Builder.load_string("""
<HelpScreen>:
  BoxLayout:
    orientation: 'vertical'
    spacing: 5
    ScrollView:
      size_hint: 1,9
      #size: 1400,2600
      #pos_hint: {'center_x': .5, 'center_y': .5}
      do_scroll_x: False
      spacing: 20
      GridLayout:
        spacing: 20
        id: help
        cols: 1
        size_hint: 1,None
        height: self.minimum_height
    Button:
      size_hint: .2,.3
      pos_hint: {'center_x':.9, 'center_y':2}
      font_size: '15dp'
      text: 'Help Screen'
      on_release: root.manager.current = 'help'
""")


  class HelpScreen(Screen):

    class HelpLabel(Label):
      def __init__(self):
        super().__init__()

    class WrappedLabel(Label):
    # Based on Tshirtman's answer
      def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(
          width=lambda *x:
          self.setter('text_size')(self, (self.width, None)),
          texture_size=lambda *x: self.setter('height')(self, self.texture_size[1]))

    def on_pre_enter(self, *args):
      self.write_help()
    
    def create_label(self,t):
      l = self.HelpLabel()
      setattr(l, "text",t)
      return l
    
    def write_help(self):
      self.ids.help.add_widget(self.create_label("Hello World"))


  def build(self):
    sm = ScreenManager()
    #ms = self.MainScreen()
    sm.add_widget(self.HelpScreen(name='help'))
    sm.current = "help"

    return sm


if __name__ == '__main__':
  HelloWorld().run()
