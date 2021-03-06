import config
import biology_functions
import triplets_dictionary
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='''Здравствуйте. Меня зовут Lafy, я ваш помощник в мире биологии. Я умею обрабатывать цепочки ДНК. Для этого введите свою цепочку после специального символа /DNK. Если вам нужна помощь, я могу рассказать о себе /help.''')

def helpCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='''Я умею работать с цепью ДНК и по введенной Вами цепи рассчитывать множество важных параметров, а именно: длину ДНК, обратную комплиментарную цепь, иРНК, стоп-кодон, выделять триплеты и рассчитывать длину белка''')

def DNKCommand(bot, update, args):
    
    n = len(args[0])
    length_args = n * 0.34
    
    bot.send_message(chat_id=update.message.chat_id, text='''Длина ДНК (нм):''')
    bot.send_message(chat_id=update.message.chat_id, text = str(length_args))
    
    reverse_DNK = reverse_DNK(args[0], n)
    RNK = RNK(args[0], n)
    
    bot.send_message(chat_id=update.message.chat_id, text='''Обратная комплиментарная цепь:''')
    bot.send_message(chat_id=update.message.chat_id, text=reverse_DNK)
    bot.send_message(chat_id=update.message.chat_id, text='''иРНК:''')
    bot.send_message(chat_id=update.message.chat_id, text=RNK)
    
    i = 1;
    stop_codon = ""
    first_counter = n
    
    stop_codon = stop_codon (i, RNK, first_counter)
    
    if (stop_codon != ''):
        bot.send_message(chat_id=update.message.chat_id, text='''Стоп-кодон:''')
        bot.send_message(chat_id=update.message.chat_id, text=stop_codon)
    sub_string = ""
    k = n % 3
    i = k

    RNK = string_RNK (n, RNK, sub_string)
    n -= k
    first_counter -= k
    triplets = triplets(RNK, first_counter)
    new_number = len(triplets)

    i = 0
    
    string_triplets = string_triplets (new_number, triplets, i)
   

    bot.send_message(chat_id=update.message.chat_id, text='''Триплеты:''')
    bot.send_message(chat_id=update.message.chat_id, text=string_triplets)
    triplets_abs = []
    second_count = len(triplets)

    triplets_abs = triplets_abc(triplets, new_number)

    string_triplets_abc = string_triplets (new_number, triplets_abc, i)

    bot.send_message(chat_id=update.message.chat_id, text=string_triplets_abc)
    bot.send_message(chat_id=update.message.chat_id, text='''Длина белка (нм) :''')
    bot.send_message(chat_id=update.message.chat_id, text=str(len(triplets) * 0.3))

start_command_handler = CommandHandler('start', startCommand)
DNK_command_handler = CommandHandler('DNK', DNKCommand, pass_args = True)
help_command_handler = CommandHandler('help', helpCommand)

dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(DNK_command_handler)
dispatcher.add_handler(help_command_handler)

updater.start_polling(clean=True)

updater.idle()

if __name__ == '__main__':
    bot.polling(none_stop=True)
