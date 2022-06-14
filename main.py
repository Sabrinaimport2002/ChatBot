#import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window


class Manager(ScreenManager):
    pass

class MenuInitial(Screen):
    pass

class HomeScreen(Screen):
    def __init__ (self, tarefas=[], **kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.box.add_widget(Message(text=tarefa))
    
    #implementa o esc para voltar
    def on_pre_enter(self):
        Window.bind(on_keyboard=self.back)

    #implementa o esc para voltar
    def back(self, window, key, *args):
        if key == 27:
            App.get_running_app().root.current = 'menuinitial'
            return True

    #implementa o esc para voltar
    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.back)

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
