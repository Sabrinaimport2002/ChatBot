#import ChatBot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pyttsx3
import speech_recognition as sr  

class Chatbot():
      
    #iniciando a engine que capta a voz do usuário
    rec = sr.Recognizer()

    #iniciando a engine que recogniza a voz do bot
    speak = pyttsx3.init('sapi5')

    
    def initBot():    
        #iniciando a engine do bot
        bot = ChatBot(
            'Chatbot do Poderoso',
            logic_adapters=[
            'chatterbot.logic.BestMatch'],
        )
        return bot

    def trainBot(bot):
        list = ListTrainer(bot)
        list.train(
        [
            'Oi','Olá',
            'Tudo bem?','Tudo bem comigo, e com você?',
            'Como vai seu aprendizado?', 'Ainda em estágio inicial...',
            'Mas e seu coração?', 'Ainda machucado...',
            'Bro', 'Bro...'
        ])

        return 0
    
    initBot()
    trainBot(initBot())








        

