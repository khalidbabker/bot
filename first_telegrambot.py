import telebot

bot = telebot.TeleBot('1464134893:AAFoPzhUVL339JseiXrzEuVrzgXCEgXY1FU')
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id,'SupderAdmin',parse_mode='Markdown')

@bot.message_handler(regexp='^/hy')
def ab(message):
	te=message.text.split()[1]
	te1=message.text.split()[2]
	bot.send_message(message.chat.id,'[{}]({})'.format(te,te1),parse_mode='Markdown')	
@bot.message_handler(commands=['help'])
def send_wel(message):
	bot.send_message(message.chat.id,'/khalid /par /pr  /id ')

@bot.message_handler(commands=['id'])
def send_wec(message):
	bot.send_message(message.chat.id,text='id : '+str(message.chat.id) + '\n user name : @'+str(message.from_user.username)+'\n your message : '+str(message.text))
	
	
@bot.message_handler(commands=['khalid'])
def send_welc(message):
	bot.reply_to(message,text='welcome khalid')
	
@bot.message_handler(func=lambda message: message.text == "عمرك كم")
def func(message):
	bot.reply_to(message,text='5 ساعات و انت ؟؟')				


	
@bot.message_handler(commands=['par'])
def sn(message):
	bot.reply_to(message,text='**welcome khalid to my facebook account**',parse_mode='Markdown')

@bot.message_handler(func=lambda message: message.text == "Bika")
def fuc(message):
	bot.reply_to(message,text='عيونا ')

@bot.message_handler(func=lambda message: message.text == "ولد ولا بنت")
def fuhc(message):
	bot.reply_to(message,text='ولد و منتهي ما تناقشوني تاني ')
	bot.send_message(message.chat.id,'اسف على طريقه الكلام بس عصبتني ')
		
@bot.message_handler(func=lambda message: message.text == "كيفك")
def fuvc(message):
	bot.reply_to(message,text='تمام التمام الحمد لله وانت')
		
@bot.message_handler(commands=['pr'])
def sen(message):
	bot.reply_to(message,text='[welcome khalid to my facebook account](https://www.facebook.com/khalid.babker.54)',parse_mode='Markdown')

def id_ex(id):
	result = False
	file = open('/sdcard/users.txt','r')
	for line in file:
		if line.strip == id:
			result = True
	file.close()
	return result
	
	
@bot.message_handler(commands=['user'])
def son(message):
	if message.chat.type == 'private':
		idu = message.from_user.id
		f = open('/sdcard/users.txt','a')
		if (not id_ex(str(idu))):
			f.write('{}\n'.format(idu))
			f.close()
			bot.send_message(message.chat.id,'welcome new user')
		else:
			bot.send_message(message.chat.id,'yes u r 💙👌✨')
			
	
	
	
	
print('Running ...')
	
bot.polling()