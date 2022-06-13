# Проект команды BestArmFake на хакатоне
MoscowCityHack 11-13 июня 2022 года
сервис по выяслению фейковых новостей

## Состав команды:
- Бочаров Алексей (lead, Python developer, DS)
- Хомякова Мария (product-manager)
- Хамизов Руслан (backend developer)
контакт для связи скайп bam271074

## Идея проекта:

Разработан алгоритм на основе машинного обучения (бустинг catboost), который можно интегрировать с лэндинг информационного	портала,	и	который может выставлять	оценку	достоверности размещённых на портале новостей по шкале от 1 до 100 баллов.
Новость, которой можно верить получает более 95 баллов. Если у новости около нуля баллов, то это фейк.

## Техническая реализация проекта:

В качестве основного алгоритма для проверки достоперности новостей используется опен-сорсный проект Яндекса, бустинг catboost. В дальнейшем по мере развития проекта он может быть заменен на нейронные сети архитектуры Transformers.


## Технологический стек проекта:

За основу обучения модели машинного обучения catboost взят датасет с Кагл [https://www.kaggle.com/c/fake-news/data] в который были добавлены новости предоставленные организаторами. В итоге получена модель бинарной классификации (1-фейк, 0-норм) которая может по предоставленной информации в текстовом формате "Название новости", Автор, "Новость" выдавать рейтинг от 0 (новости можно доверять) до 100 (новость фейк). На основании обученной модели для демонстрации ее работоспособности реализован телеграм-бот.

# Как запустить проект:

ML-часть пректа разрабатывалась в облачном сервисе от Гугл Colab.
Разработка телеграм бота велась на masOS Big Sur (11.6.6)
Для запуска телеграм-бота необходимо скопировать с гитхаба [https://github.com/poisonpython2001/hackatone] в одну дирректорию файлы app.py, config.py, clf_cb04.cbm, убедиться счто у установлен Питон верси 3.9 и библиотеки:

- catboost (1.0.6)
- pytelegrambotapi

Перейти в папку проекта и запустить телеграм-бота командой python3 app.py

После этого бот доступен по адресу: @Robot_test_app_bot
