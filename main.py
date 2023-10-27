import torch
import telebot
import os
import shutil

# API токен от @BotFather
bot = telebot.TeleBot('6649613976:AAHTu6w5vq4_kKY76sh2oPwdOg7YNsVlS_o')

model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:/Users/robb/Desktop/test_ai_bot/yolov5/pantheras_two.pt', force_reload=True)

# Входная функция телеграма, просто реагирует на начальную команду /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}.')

# Функция получения фотографии от бота
@bot.message_handler(content_types=['photo'])
def get_photo(message):
    try:
        file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src = file_info.file_path
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
        send_photo(message, file_info, src)
    except Exception as e:
        bot.reply_to(message, e)

# Функция отправки обработанний фотографии со всеми рамками
def send_photo(message, file_info, src):
    number = file_info.file_path[file_info.file_path.find('_') + 1:]
    number = '.'.join(number.split('.')[:-1])
    model_file = ai_model_for_photo_processing(src, number)
    results = model_file.pandas().xyxy[0]
    send_src = f'photos/file_{number}/file_{number}.jpg'
    bot.reply_to(message, f'Фотография обработана!')
    remove_photo(number, src)

# Функция обработки фотографий с помощью YOLOv5s
def ai_model_for_photo_processing(src, number):
    model_file = model(src)
    model_file.save(labels=True, save_dir=f'photos/file_{number}')
    return model_file

# Функция удаления фотографий
def remove_photo(number, src):
    os.remove(src)
    shutil.rmtree(f'photos/file_{number}')

bot.polling(none_stop=True)