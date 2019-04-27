from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqldatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db = SQLAlchemy(app)

import random


def random_fairy_tale():
    START_WORDS = ['Однажды в тридевятом царстве , в тридедесятом государстве', 'Как-то раз',
                   'Давным-Давно', 'В некотором царстве, в некотором государстве',
                   'Давным-Давно']  # первоначальные слова
    is_men = random.choice([False, True])
    if is_men:
        ARTICLE = ['его']  # Обращения1
        ARTICLE_SECOND = ['ему']  # Обращения2
        ARTICLE_THRD = ['героя']
        ARTICLE_FOURTH = ['герою']
        COMPLIMENT = ['cильный и мужественный', 'смелый и крепкий', 'мудрый и отважный']  # Комплимент
        HEROES = ['Алеша Попович', ' Илья Муромец', 'Добрыня Никитич', 'Иван-Царевич']  # Имя героя
        ACT_FIRST = ['жил-был, да подвиги совершал, но в один день ']  # действие героя до начала событий

        WAY_SUB = [',но благодаря своей силе и мудрости {} с легкостью их преодолевал.',
                   ',но с помощью своего ума и ловкости {} справлялся со всеми испытаниями.']

        ENEMY_PLACE_SUB = ['Когда {} добрался до {} , где жил злодей , на него напал {}',
                           'Когда {} находился около {}, где жил разбойник, откуда не возьмись появился {}, и напал на него']
        END_START = [',но {} успел ускользнуть от него и одержал победу в нелегком бою и спас {}.',
                     ',но {} в ходе жестокого поединка смог победить злодея и освободил {}.']
        ANIMAL = ['И пошёл {} за волшебным клубком из ниток, который котился по дороге и указывал ему путь к логову, в котором жил {}.',
                  'И полетел {} на славном орле прямо к логову, в котором жил {}.']
    else:
        ARTICLE = ['её']  # Обращения1
        ARTICLE_SECOND = ['ей']  # Обращения2
        ARTICLE_THRD = ['героиню']
        ARTICLE_FOURTH = ['героине']
        COMPLIMENT = ['прекрасная', 'красавица', 'прелестная', 'редкой красоты']  # Комплимент
        HEROES = ['Царевна-Лягушка', ' Василиса-Премудрая']  # Имя героя
        ACT_FIRST = ['жила-была, да подвиги совершала, но в один день ']   # действие героя до начала событий
        WAY_SUB = [',но благодаря своей сообразительности и мудрости {} с легкостью их преодолевала.',
                   ',но в силу своего ума и смекалки {} справлялась со всеми испытаниями.']
        ENEMY_PLACE_SUB = ['Когда {} добралась до {} , где жил злодей , на неё напал {}',
                           'Когда {} находилась около {}, где жил разбойник, откуда не возьмись появился {}, и напал на неё']
        END_START = [',но {} успела увернуться ,и с помощью своего красноречия смогла уговорить его вернуть ей {}.']
        ANIMAL = ['И пошла {} за волшебным клубком из ниток, который котился по дороге и указывал ей путь к логову, в котором жил {}',
                  'И полетела {} на славном орле прямо к логову , в котором жил {}']

    RELATIONS = [',как вдруг ', ', но вдруг', ',но тут', ',но внезапно']  # связуещие звено
    INSULT = ['страшный и беспощадный', 'жестокий и грозный']  # оскорбление злодея
    ENEMY = ['Кащей бессмертный', 'Леший', 'Водяной', 'Чудо-Юдо', 'Соловей-разбойник', 'Змей Горыныч']  # имя злодея
    ACT_SECOND = ['украл', 'забрал', 'похитил']  # поступок злодея
    ACT_SECOND_SUB = ['царевну', 'принцессу', 'королевну']  # близкий родственик
    RELATIONS_SECOND = ['Тогда']  # связуещие звено 2
    ACT_THIRD = ['прославленный царь', 'правящий князь', 'разгневанный король']  # Родственик пославший
    ACT_THIRD_SUB = ['приказал', 'дал указ', 'повелел']  # Задание
    ACT_FOURTH = ['найти', 'вернуть', 'возратить']  # Задание
    WAY = ['В пути {} ждало множество опасностей', 'В пути {} ожидало много трудностей',
           'Во время столь опасного путешествия {} ждало великое множество припятствий']
    ENEMY_PLACE = ['вязкого и топкого болота', 'дремучего и непроходимого леса']
    END_END = ['Вот и сказочки конец , а кто слушал - молодец']

    start_words = random.choice(START_WORDS)  # рандомное первоночальное слово
    compliment = random.choice(COMPLIMENT)
    hero = random.choice(HEROES)  # рандомный герой
    act_first = random.choice(ACT_FIRST)  # первое действие
    insult = random.choice(INSULT)  # оскорбление злодея
    enemy = random.choice(ENEMY)  # рандомное первое действие
    relations = random.choice(RELATIONS)  # случайное связуещее
    act_second = random.choice(ACT_SECOND)  # действие злодея
    article = random.choice(ARTICLE)  # обращение
    family_name = random.choice(ACT_SECOND_SUB)  # имя члена семьи
    relations_second = random.choice(RELATIONS_SECOND)  # рандомное связуещее звено
    act_third = random.choice(ACT_THIRD)  # родственик пославший
    act_third_sub = random.choice(ACT_THIRD_SUB)
    article_second = random.choice(ARTICLE_SECOND)
    article_third = random.choice(ARTICLE_THRD)
    article_fourth = random.choice(ARTICLE_FOURTH)
    act_fourth = random.choice(ACT_FOURTH)
    animal = random.choice(ANIMAL)
    way = random.choice(WAY)
    way_sub = random.choice(WAY_SUB)
    enemy_place = random.choice(ENEMY_PLACE)
    enemy_place_sub = random.choice(ENEMY_PLACE_SUB)
    end_start = random.choice(END_START)
    end_end = random.choice(END_END)

    all_words = [start_words,
                 compliment,
                 hero,
                 act_first,

                 insult,
                 enemy,
                 act_second,
                 family_name + '.',
                 relations_second,
                 article,
                 act_third,
                 act_third_sub,
                 article_fourth,
                 act_fourth,
                 family_name + '.',
                 animal.format(hero,enemy),
                 way.format(article_third),
                 way_sub.format(hero),
                 enemy_place_sub.format(hero, enemy_place, enemy),
                 end_start.format(hero, family_name),
                 end_end]  # список всех слов
    title = [start_words, hero, act_first,  enemy, act_second,
             family_name + '.']  # список для названия

    text = ' '.join(all_words)
    return [text, ' '.join(title)]


class FairyTale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), unique=False, nullable=False)
    text = db.Column(db.String(5000), unique=False, nullable=False)
    like = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return "<FairyTale {} {} {} {}>".format(self.id, self.title, self.text, self.like)


def most_likefull():
    spisok = FairyTale.query.order_by(FairyTale.like.desc()).all()[:10]
    text = 'Вот список всех наиболее популярных сказок, для выбора сказки напишите :'
    list_id = []
    number = len(spisok)
    if number > 5:
        number = 5
    for i in range(number):
        list_id.append(spisok[i].id)
        text += '\n {}. {}'.format(spisok[i].id,
                                   spisok[i].title)
    return (list_id, text)


def get_fairy_tale_id(id):
    fairy_tale = FairyTale.query.filter_by(id=id).first()
    if fairy_tale:
        return fairy_tale.text
    else:
        return 'Такой сказки не найдено, возможно вы ошиблись с номером'


def like_fairy_tale(id):
    fairy_tale = FairyTale.query.filter_by(id=id).first()
    if fairy_tale:
        fairy_tale.like += 1
        db.session.commit()
    else:
        return


def add_fairy_tale():
    params = random_fairy_tale()
    user = FairyTale(title=params[1], text=params[0], like=0)
    db.session.add(user)
    db.session.commit()
    id = FairyTale.query.filter_by(text=params[0]).first().id
    return (id, params[0])


import logging
import json

db.create_all()
logging.basicConfig(level=logging.INFO)
first_text = 'Привет, ты попал в "Сказкогенератор". Сказкогенератор - это программа ' \
             'для генерации сказок. Если хочешь узнать больше информации напиши "Помощь"'
help = 'И снова здравствуй, давай я разъясню тебе все! В Сказкогенераторе ты можешь получить сказку двумя способами:' \
       '\n1)Сгенерировать её; \n 2)Получить наиболее понравившиеся людям сказки. ' \
       'Также ты можешь оценивать сказки, которые ты получил. Желаю тебе получить удовольствия от Сказкогенератора, удачи) '
what_i_can = 'Я могу генерировать сказки '
sessionStorage = {}


@app.route('/', methods=['POST'])
# Функция получает тело запроса и возвращает ответ.
# Внутри функции доступен request.json - это JSON,
# который отправила нам Алиса в запросе POST
def main():
    logging.info('Request: %r', request.json)

    # Начинаем формировать ответ, согласно документации
    # мы собираем словарь, который потом при помощи библиотеки json
    # преобразуем в JSON и отдадим Алисе
    response = {
        'session': request.json['session'],
        'version': request.json['version'],
        'response': {
            'end_session': False
        }
    }

    # Отправляем request.json и response в функцию handle_dialog.
    # Она сформирует оставшиеся поля JSON, которые отвечают
    # непосредственно за ведение диалога
    handle_dialog(request.json, response)

    logging.info('Response: %r', request.json)

    # Преобразовываем в JSON и возвращаем
    return json.dumps(response)


def handle_dialog(req, res):
    user_id = req['session']['user_id']

    if req['session']['new']:
        sessionStorage[user_id] = {
            'suggests': [
                "Хочу сказку",
                "Хочу получить лучшие сказки",
                "Помощь",
            ],
            'last_message': 'none',
            'last_fairy_tale': 0,
            'is_last_fairy_tale': False,
            'is_last_fairy_tale_list': False,
            'fairy_tale_list': []
        }
        res['response']['text'] = first_text
        res['response']['buttons'] = get_suggests(user_id)
        # Получим подсказки
        return
    if req['request']['original_utterance'].lower() in [
        'хочу сказку', 'сказку'
    ]:
        sessionStorage[user_id]['last_message'] = req['request']['original_utterance']
        sessionStorage[user_id]['last_fairy_tale'], res['response']['text'] = add_fairy_tale()
        sessionStorage[user_id]['is_last_fairy_tale_list'] = False
        sessionStorage[user_id]['is_last_fairy_tale'] = True

        res['response']['text'] += '\n Вам понравилась эта сказка?'
        res['response']['buttons'] = get_suggests(user_id, 'лайкнуть')
        res['response']['end_session'] = False
        return
    elif req['request']['original_utterance'].lower() in [
        'хочу получить лучшие сказки', 'лучшие сказки']:
        sessionStorage[user_id]['is_last_fairy_tale'] = False
        sessionStorage[user_id]['is_last_fairy_tale_list'] = True
        sessionStorage[user_id]['fairy_tale_list'], res['response']['text'] = most_likefull()
        res['response']['buttons'] = get_suggests(user_id, 'лучшие сказки')
        return
    elif sessionStorage[user_id]['is_last_fairy_tale']:
        if req['request']['original_utterance'].lower() in ['понравилась', 'да']:
            like_fairy_tale(sessionStorage[user_id]['last_fairy_tale'])
            res['response']['buttons'] = get_suggests(user_id)
            res['response']['text'] = 'Спасибо за ваш отзыв'
            return
        elif req['request']['original_utterance'].lower() in ['нет', 'не понравилась']:
            res['response']['text'] = 'Спасибо за ваш отзыв'
            res['response']['buttons'] = get_suggests(user_id)
            return
    elif req['request']['original_utterance'].lower() == 'помощь':
        sessionStorage[user_id]['is_last_fairy_tale'] = False
        sessionStorage[user_id]['is_last_fairy_tale_list'] = False
        sessionStorage[user_id]['fairy_tale_list'] = []
        res['response']['text'] = help
        res['response']['buttons'] = get_suggests(user_id)
        return
    elif req['request']['original_utterance'].lower() == 'что я могу':
        sessionStorage[user_id]['is_last_fairy_tale'] = False
        sessionStorage[user_id]['is_last_fairy_tale_list'] = False
        sessionStorage[user_id]['fairy_tale_list'] = []
        res['response']['text'] = what_i_can
        res['response']['buttons'] = get_suggests(user_id)
        return
    elif req['request']['original_utterance'].isdigit() and sessionStorage[user_id]['is_last_fairy_tale_list']:
        res['response']['text'] = get_fairy_tale_id(int(req['request']['original_utterance']))
        if res['response']['text'] == 'Такой сказки не найдено, возможно вы ошиблись с номером':
            sessionStorage[user_id]['last_fairy_tale'] = 0
            res['response']['buttons'] = get_suggests(user_id)
            return
        sessionStorage[user_id]['is_last_fairy_tale'] = True
        sessionStorage[user_id]['is_last_fairy_tale_list'] = False
        res['response']['buttons'] = get_suggests(user_id, 'лайкнуть')
        sessionStorage[user_id]['last_fairy_tale'] = int(req['request']['original_utterance'])
        return

    res['response']['buttons'] = get_suggests(user_id)
    res['response']['text'] = 'Я не понимаю такой команды, вот список возможных команд:'


def get_suggests(user_id, param='сказка'):
    if param == 'сказка':
        sessionStorage[user_id]['suggests'] = [{'title': "Хочу сказку", 'hide': False},
                                               {'title': "Хочу получить лучшие сказки", 'hide': False},
                                               {'title': "Что я могу", 'hide': False},
                                               {'title': "Помощь", 'hide': False}]
    elif param == 'лайкнуть':
        sessionStorage[user_id]['suggests'] = [{'title': 'Понравилась', 'hide': True},
                                               {'title': 'не понравилась', 'hide': True}]
    elif param == 'лучшие сказки':
        spisok = sessionStorage[user_id]['fairy_tale_list']
        suggests = [{'title': str(suggest), 'hide': True}
                    for suggest in spisok]
        sessionStorage[user_id]['suggests'] = suggests

    return sessionStorage[user_id]['suggests']


if __name__ == '__main__':
    app.run()
