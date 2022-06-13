#import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView


class HomeScreen(ScrollView):
    def __init__ (self, tarefas, **kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.box.add_widget(Message(text=tarefa))

class Message(BoxLayout):
    def __init__(self, text='', **kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text

class Interface(App):
    def build(self):
        return HomeScreen(["ChatBot", "ChatBot", "ChatBot", "ChatBot"])
    
Interface().run()
