import telegram

CHAT_ID = '180949865'
texter = telegram.Bot(token='1069887282:AAHDXB-4eqV7Y8-kUhzkj-z97ONZ_ktdX0c')

def push(message):
    texter.send_message(chat_id=CHAT_ID, text=message)