# -*- coding: utf-8 -*-

#pip install pytelegrambotapi
import telebot  
#pip install catboost
from catboost import CatBoostClassifier
import config


bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start','help'])
def start(message):
    start_message='''✌️✌️✌️✌️✌️Это бот-робот\n\
                 Он помогает определять фейковые новости\n\
                 пошлите ему сообщение в формате "Название новости",Автор,"Новость"\n\
                 и он определит фейк это или нет.✌️✌️✌️✌️✌️\n'''
    bot.send_message(message.chat.id,start_message)
    
    
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    str = message.text

    
    try:
        lst = str.split(",")
    except:
        print("can not parse input")    
    
    if len(lst) != 3:
        lst = '"aaa",nan,"sdsdsd"'.split(",")
    print(lst)
    
    # let s load trained model
    clf = CatBoostClassifier()
    clf.load_model('clf_cb04.cbm')
    
    answer = clf.predict_proba(lst)
    answer = int(answer[1])
    #answer_str = str(answer)
    #mess = "Рейтинг новости около 0 означает фейк, достоверные новости более 90 баллов. Рейтинг: "
    print(clf.predict(lst))

    bot.send_message(message.chat.id, answer)
if __name__ == '__main__':
    print('bot started.')
    bot.polling(none_stop=True)