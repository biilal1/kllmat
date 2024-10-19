import telebot
import os

Tok = '7346446016:AAFmOeoMF-96SMLZOVAAQ1llsI2VvMHoegA'
bot = telebot.TeleBot(Tok)
OWNER_ID = 7291869416

def load_banned_words():
    if os.path.exists('klmat.txt'):
        with open('klmat.txt', 'r', encoding='utf-8') as file:
            return [line.strip() for line in file.readlines()]
    return []

def save_banned_word(word):
    with open('klmat.txt', 'a', encoding='utf-8') as file:
        file.write(word + '\n')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.from_user.id == OWNER_ID:
        bot.send_message(message.chat.id, "مرحبا بك أيها المالك! يمكنك إرسال الأمر 'delete' متبوعا بالكلمة التي تريد حذفها.")
    else:
        bot.send_message(message.chat.id, "مرحبًا بك في البوت!")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.from_user.id == OWNER_ID:
        if message.text.startswith('delete '):
            word_to_delete = message.text[len('delete '):].strip()
            save_banned_word(word_to_delete)
            bot.send_message(message.chat.id, f"تم حفظ الكلمة '{word_to_delete}' إلى القائمة المحظورة.")
    else:
        banned_words = load_banned_words()
        if any(banned_word in message.text for banned_word in banned_words):
            bot.delete_message(message.chat.id, message.message_id)

print('#####')
bot.polling()
