from cgitb import text
import requests
import telebot

city=''
bot = telebot.TeleBot('5293190304:AAFzrDyUab2W1DyyEtD0FRiQu-SmAdfxvDE')
@bot.message_handler(commands=['start', 'help'])
def get_weather(message):
    bot.send_message(message.chat.id,'Привет, я бот прогноза погоды! \nНапиши любой город.')
@bot.message_handler(content_types=['text'])   
def rekuest(message):
    global city
    city = message.text        
    link1 = 'https://api.openweathermap.org/data/2.5/weather?q='
    link2 = '&units=metric&APPID=6bab4d6713adbf3a428b1f2a7454395d&lang=ru'
    link = link1 + city +link2
    data = requests.get(link).json()
    temperature = data['main']['temp']
    description_1 = data['weather'][0]['description']
    bot.send_message(message.chat.id,city+'\n'+str(round(temperature))+'°C '+description_1)

    icon_data = data['weather'][0]['icon']
     
    
    foto= open('weather_icons/'+icon_data+'.png','rb')
    bot.send_photo(message.chat.id,foto)
       

    print('Загружено!')
        


    if temperature < 0:
        bot.send_message(message.chat.id,'Одевайся тепло')


    if temperature > 0:

        bot.send_message(message.chat.id,'Незабудь очки и кепку')

    else:
        bot.send_message(message.chat.id,'Захвати с собой зонт')






bot.infinity_polling()
