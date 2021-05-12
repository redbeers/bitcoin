import telegram
from telegram.ext import Updater, MessageHandler, Filters
from team_01_시연.modules.main import GoogleWeather
   

# bot.sendPhoto(chat_id=chat_id, photo=img_url, caption="텍스트"
# 사용자가 전달한 메시지를 핸들링하는 코드
def get_message(bot, update): # 콜백함수
    chat_id = bot.message.chat.id
    msg = bot.message.text
#   종목이름 넣는곳
    if msg == '/start':
#         update.bot.send_photo(
#                                 chat_id, 
#                                 photo='https://t1.daumcdn.net/cfile/tistory/99559F435DEEDFCB1D', 
#                                 caption='최첨단 날씨알림봇'
#                             )
        update.bot.send_message(chat_id, '주인님 로봇이 작동 합니다.')
        return
      
    crawler.set_keyword(msg + ' 날씨')
    crawler.run()
    r = crawler.get_result()
    print(r)
    
    #  조건넣고 종목가격 보내는곳
    if r and r['loc']:
        send_msg = []
        for k, v in r.items():
            if k == 'loc':
                send_msg.append(f'지역명 : {v}')
            elif k == 'time':
                send_msg.append(f'시간대 : {v}')
            elif k == 'status':
                send_msg.append(f'날씨 : {v}')
        update.bot.send_message(chat_id, '\n'.join(send_msg))
    else:
        update.bot.send_message(chat_id,'무슨말인지 몰라.\n다시!')
#         update.bot.send_message(chat_id, '검색 결과가 없습니다.')
#         update.bot.send_message(chat_id, '지역명을 입력하세요.')
    
if __name__ == '__main__':
    print('start telegram chat bot')
    token = '1799768876:AAE-r9m6KcI4TCmBtG1zgXWArF_44mZSQ_U'
    bot = telegram.Bot(token)
    crawler = GoogleWeather()
        
    token = '1799768876:AAE-r9m6KcI4TCmBtG1zgXWArF_44mZSQ_U'
    updater = Updater(token, use_context=True)
    message_handler = MessageHandler(Filters.text, get_message)
    updater.dispatcher.add_handler(message_handler)
    updater.start_polling()
    updater.idle()
      
     
     