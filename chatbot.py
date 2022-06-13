#import ChatBot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pyttsx3
import speech_recognition as sr  

class ChatBot():
      
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

    def initConversation(rec, bot, speak):

        #laço de repetição para uma conversa contínua
        print("Digite alguma coisa: ")
        while True:
            texto = input("Você: ")
            
            if(texto == "tchau"):
                break
            else:
                resp = bot.get_response(texto)
                print('Bot: ', resp)
                        
                #sintetiza a voz e a reproduz
                speak.say(resp)
                speak.runAndWait()
                  
            #with sr.Microphone() as fonte:
            #    rec.adjust_for_ambient_noise(fonte)
            #    frase = rec.listen(fonte)
            #    texto = rec.recognize_sphinx(frase, language='pt-Br')
            #    print("Você: ", texto)
            #    
            #    if(texto == "tchau"):
            #        break
            #    else:
            #        resp = bot.get_response(texto)
            #        print('Bot: ', resp)
            #            
            #        #sintetiza a voz e a reproduz
            #        speak.say(resp)
            #        speak.runAndWait()

        return 0
    
    initBot()
    trainBot(initBot())
    initConversation(rec, initBot(), speak)








        

