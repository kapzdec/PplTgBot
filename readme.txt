Для создания бота нужно найти в телеграмме бота @BotFather, ввести команды /start и /newbot и следовать инструкциям.
В конце будет выдан токен, который нужно вставить в код программы.

Перед запуском программ установите необходимые библиотеки, введя в terminal поочерёдно:
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117
pip install -r https://raw.githubusercontent.com/ultralytics/yolov5/master/requirements.txt
pip install pyTelegramBotAPI
