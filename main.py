#import kivy
from tkinter import Label
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class HomeScreen(BoxLayout):
    def __init__ (self, tarefas, **kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.add_widget(Label(text=tarefa))

class Interface(App):
    def build(self):
        return HomeScreen(["ChatBot"])
    
Interface().run()
