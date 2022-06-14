#import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class Manager(ScreenManager):
    pass

class MenuInitial(Screen):
    pass

class HomeScreen(Screen):
    def __init__ (self, tarefas=[], **kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.box.add_widget(Message(text=tarefa))

    # método que permite adicionar labels dinamicamente
    def addWidget(self):
        texto = self.ids.texto.text
        self.ids.box.add_widget(Message(text=texto))
        self.ids.texto.text = ''

#define o espaço da mensagem na GUI + adiciona o X de exclusão de labels
class Message(BoxLayout):
    def __init__(self, text='', **kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text

#classe main
class Interface(App):
    def build(self):
        return Manager()
    
Interface().run()
