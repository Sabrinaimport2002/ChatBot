#import kivy
from logging import exception
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pyttsx3
import speech_recognition as sr

class Manager(ScreenManager):
    pass

class MenuInitial(Screen):
    pass

class HomeScreen(Screen):

    bot = ChatBot(
            'Chatbot do Poderoso',
            logic_adapters=[
            'chatterbot.logic.BestMatch'],
        )
    
    list = ListTrainer(bot)
    list.train(
    [
        'Oi','Olá',
        'Tudo bem?','Tudo bem comigo, e com você?',
        'Como vai seu aprendizado?', 'Ainda em estágio inicial...',
        'Mas e seu coração?', 'Ainda machucado...',
        'Bro', 'Bro...',
        'tchau', 'Tchau!, Até a próxima :)',
        'Não Identificado', 'Diga Novamente!'
    ])

    speak = pyttsx3.init('sapi5')
    rec = sr.Recognizer()

    def __init__ (self, tarefas=[], **kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.box.add_widget(Message(text=tarefa))

    # método que utiliza o chatbot
    def mensagem(self, msg, *args):     
        self.ids.box.add_widget(Message(text=msg))   
        
        #sintetiza a voz e a reproduz
        resp = str(self.bot.get_response(msg))
        self.speak.say(resp)
        self.speak.runAndWait() 
        self.ids.box.add_widget(Message(text=resp))
        self.ids.texto.text = ''
    
    def mensagem_audio(self, *args):
        with sr.Microphone() as fonte:
            frase = self.rec.listen(fonte)
            texto = self.rec.recognize_google(frase, language='pt')            
        
        self.ids.box.add_widget(Message(text=texto)) 
        resp = str(self.bot.get_response(texto))
        self.speak.say(resp)
        self.speak.runAndWait() 
        self.ids.box.add_widget(Message(text=resp))
        self.ids.texto.text = ''

    #implementa o esc para voltar
    def on_pre_enter(self):
        Window.bind(on_keyboard=self.back)

    #implementa o esc para voltar
    def back(self, window, key, *args):
        if key == 27:
            App.get_running_app().root.current = 'menuinitial'
            return True

    #implementa o esc para sair da aplicação
    def on_pre_leave(self):
        return Window.unbind(on_keyboard=self.back)

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
class Main(App):
    def build(self):
        return Manager()

Main().run()
