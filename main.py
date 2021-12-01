from random import randrange
import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.upload import VkUpload
import bs4
import requests
from contactsdb import DBclass
from shabuservk import VKpop
import photolu


user_id = '670053379'
token_b = '1063ed953c64645f57a2bd8dd5e43d58936e059c8003b9cf8f00c56b4cb8de18ffef06a99d927ed5642e7'
db_file = 'vk_users.db'
db_c = DBclass(db_file)
vk_b = vk_api.VkApi(token=token_b)
longpoll = VkLongPoll(vk_b)
upload = VkUpload(vk_b)
token_vk = '2ed4994139addec3f51843643fe25f35b8251b197bef321c715a18ce998c5b61f6e1c859cc10ec2f9c7dd'
downloader = VKpop(token_vk)

bot_menu = {'f0': ['Я Бот ИскуН. Чем могу помочь?', {'Поиск': 1, 'Просмотр': 2, 'Инфо': 3, 'Выход': 0}],
        'f1': ['Выберите параметр поиска', {'Пол': 11, 'Возраст': 12, 'Город': 13, 'Семейное положение': 14,
                                            'Покажи': 15, 'Найти': 16, 'Отмена': 0}],
        'f12': ['Введите возраст в интервале', {'20-29': 2, '30-39': 3, '40-49': 4, '50-59': 5, 'Все равно': 0}],
        'f13': ['Введите город', {'Отмена': 0}],
        'f11': ['Введите пол', {'Муж': 2, 'Жен': 1, 'Все равно':0}],
        'f14': ['Введите семейное положение', {'Женат (замужем)': 4, 'Не женат (не замужем)': 1, 'Все равно': 0}],
        'f2': ['Просмотр информации о пользователе ВК', {'Одобрить': 21, 'Отклонить': 22, 'Смотреть фото': 23,
                                                         'Отмена': 24}],
        'f3': ['Информация', {'База данных': 1, 'Отмена': 0}]}


def def_keyboard(menu, cur_pos, cur_keyboard):
    but_color = ['primary', 'secondary', 'positive', 'negative']
    cp = 'f' + str(cur_pos)
    if cp in menu.keys():
        pm = menu[cp]
        msg = pm[0]
        pc = len(pm[1]) - 1
        i = 0
        for kb in pm[1].keys():
            cur_keyboard.add_button(kb, color=but_color[i])
            if i % 2 and i < pc:
                cur_keyboard.add_line()
            i = i + 1
            if i > 3:
                i = 0


def write_msg(vk_c, id_type, id_val, message=None, attachments=None, keyboards=None):
    vk_c.method('messages.send',
                {id_type: id_val, 'random_id': randrange(10 ** 7),
                 'message': message, 'attachment': attachments, 'keyboard': keyboards})
#                                'peer_id': user_id, 'message': message})


def create_empty_keyboard():
    keyboards = VkKeyboard.get_empty_keyboard()
    return keyboards


write_msg(vk_b, 'user_id', user_id, f"Привет", keyboards=create_empty_keyboard())
keyboard_0 = VkKeyboard(one_time=True)
def_keyboard(bot_menu, 0, keyboard_0)
keyboard_1 = VkKeyboard(one_time=True)
def_keyboard(bot_menu, 1, keyboard_1)
keyboard_11 = VkKeyboard(one_time=True)
def_keyboard(bot_menu, 11, keyboard_11)
keyboard_12 = VkKeyboard(one_time=True)
def_keyboard(bot_menu, 12, keyboard_12)
keyboard_13 = VkKeyboard(one_time=True)
def_keyboard(bot_menu, 13, keyboard_13)
keyboard_14 = VkKeyboard(one_time=True)
def_keyboard(bot_menu, 14, keyboard_14)
keyboard_2 = VkKeyboard(one_time=True)
def_keyboard(bot_menu, 2, keyboard_2)
keyboard_3 = VkKeyboard(one_time=True)
def_keyboard(bot_menu, 3, keyboard_3)

cur_menu_ref = 0
cur_menu_key = 'f' + str(cur_menu_ref)
#def_keyboard(bot_menu, cur_menu_ref, keyboard_1)
dial_n = 0
age_f = 0
age_t = 0
male = 0
male_s = ''
status = 0
status_s = ''
hometown = ''
write_msg(vk_b, 'user_id', user_id, bot_menu[cur_menu_key][0], keyboards=keyboard_0.get_keyboard())
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        print(event.from_user, event.user_id, event.text, event.to_me, event.from_me)
        if event.from_user and event.to_me:
            request = event.text
            if cur_menu_ref == 0:
                if request == "Поиск":
                    cur_menu_ref = 1
                    cur_menu_key = 'f' + str(cur_menu_ref)
                    write_msg(vk_b, 'user_id', event.user_id, bot_menu[cur_menu_key][0],
                              keyboards=keyboard_1.get_keyboard())
                elif request == "Просмотр":
                    cur_menu_ref = 2
                    cur_menu_key = 'f' + str(cur_menu_ref)
                    write_msg(vk_b, 'user_id', event.user_id, bot_menu[cur_menu_key][0],
                              keyboards=keyboard_2.get_keyboard())
                elif request == "Инфо":
                    cur_menu_ref = 3
                    cur_menu_key = 'f' + str(cur_menu_ref)
                    write_msg(vk_b, 'user_id', event.user_id, bot_menu[cur_menu_key][0],
                              keyboards=keyboard_3.get_keyboard())
                elif request == "Выход":
                    write_msg(vk_b, 'user_id', event.user_id, "Пока((")
                    exit(0)
                else:
                    write_msg(vk_b, 'user_id', event.user_id, "Не понял вашего ответа...")

            elif cur_menu_ref == 1:                 # меню 'Поиск'
                if request == 'Найти':
                    write_msg(vk_b, 'user_id', event.user_id, "Поиск...")
                    db_c.connect()
                    # if db_c.get_count_contacts()[0] != 0:
                    #     write_msg(vk_b, 'user_id', event.user_id, "Можно поискать!",
                    #               keyboards=keyboard_3.get_keyboard())
                    find_data = downloader.user_search(age_f, age_t, male, status, hometown)
                    print(find_data)
                    db_c.add_contact(find_data)
                elif request == 'Пол':
                    cur_menu_ref = 11
                    cur_menu_key = 'f' + str(cur_menu_ref)
                    write_msg(vk_b, 'user_id', event.user_id, bot_menu[cur_menu_key][0],
                              keyboards=keyboard_11.get_keyboard())
                elif request == 'Возраст':
                    cur_menu_ref = 12
                    cur_menu_key = 'f' + str(cur_menu_ref)
                    write_msg(vk_b, 'user_id', event.user_id, bot_menu[cur_menu_key][0],
                              keyboards=keyboard_12.get_keyboard())
                elif request == 'Город':
                    cur_menu_ref = 13
                    cur_menu_key = 'f' + str(cur_menu_ref)
                    write_msg(vk_b, 'user_id', event.user_id, bot_menu[cur_menu_key][0],
                              keyboards=keyboard_13.get_keyboard())
                elif request == 'Семейное положение':
                    cur_menu_ref = 14
                    cur_menu_key = 'f' + str(cur_menu_ref)
                    write_msg(vk_b, 'user_id', event.user_id, bot_menu[cur_menu_key][0],
                              keyboards=keyboard_14.get_keyboard())
                elif request == 'Покажи':
                    cur_menu_key = 'f' + str(cur_menu_ref)
                    part_mes = 'Возраст от ' + str(age_f) + ' до ' + str(age_t) if age_f else ''
                    part_mes += ' Пол: ' + male_s if len(male_s) else ''
                    part_mes += ' Город: ' + hometown if len(hometown) else ''
                    part_mes += ' Семейное положение: ' + status_s if len(status_s) else ''
                    write_msg(vk_b, 'user_id', event.user_id, "Критерии поиска: " + part_mes if len(part_mes) else 'Пусто')
                    cur_menu_ref = 1
                    cur_menu_key = 'f' + str(cur_menu_ref)
                    write_msg(vk_b, 'user_id', event.user_id, bot_menu[cur_menu_key][0],
                              keyboards=keyboard_1.get_keyboard())
                elif request == 'Отмена':
                    cur_menu_ref = 0
                    cur_menu_key = 'f' + str(cur_menu_ref)
                    write_msg(vk_b, 'user_id', event.user_id, bot_menu[cur_menu_key][0],
                              keyboards=keyboard_0.get_keyboard())
                else:
                    write_msg(vk_b, 'user_id', event.user_id, "Не понял вашего ответа...")
            elif cur_menu_ref == 11:
                cur_menu_key = 'f' + str(cur_menu_ref)
                if request in bot_menu[cur_menu_key][1]:
                    male = int(bot_menu[cur_menu_key][1][request])
                    male_s = request
                else:
                    write_msg(vk_b, 'user_id', event.user_id, "Не понял вашего ответа...")
                cur_menu_ref = 1
                cur_menu_key = 'f' + str(cur_menu_ref)
                write_msg(vk_b, 'user_id', event.user_id, bot_menu[cur_menu_key][0],
                          keyboards=keyboard_1.get_keyboard())

            elif cur_menu_ref == 12:
                cur_menu_key = 'f' + str(cur_menu_ref)
                if request in bot_menu[cur_menu_key][1]:
                    age_b = int(bot_menu[cur_menu_key][1][request])
                    age_f = age_b * 10
                    age_t = age_f + 9
                else:
                    write_msg(vk_b, 'user_id', event.user_id, "Не понял вашего ответа...")
                cur_menu_ref = 1
                cur_menu_key = 'f' + str(cur_menu_ref)
                write_msg(vk_b, 'user_id', event.user_id, bot_menu[cur_menu_key][0],
                          keyboards=keyboard_1.get_keyboard())
            elif cur_menu_ref == 13:
                hometown = request
                write_msg(vk_b, 'user_id', event.user_id, "Принято")
                cur_menu_ref = 1
                cur_menu_key = 'f' + str(cur_menu_ref)
                write_msg(vk_b, 'user_id', event.user_id, bot_menu[cur_menu_key][0],
                          keyboards=keyboard_1.get_keyboard())
            elif cur_menu_ref == 14:
                cur_menu_key = 'f' + str(cur_menu_ref)
                if request in bot_menu[cur_menu_key][1]:
                    status = int(bot_menu[cur_menu_key][1][request])
                    status_s = request
                else:
                    write_msg(vk_b, 'user_id', event.user_id, "Не понял вашего ответа...")
                cur_menu_ref = 1
                cur_menu_key = 'f' + str(cur_menu_ref)
                write_msg(vk_b, 'user_id', event.user_id, bot_menu[cur_menu_key][0],
                          keyboards=keyboard_1.get_keyboard())
            elif cur_menu_ref == 15:
                cur_menu_key = 'f' + str(cur_menu_ref)
                part_mes = 'Возраст от ' + str(age_f) + ' до ' + str(age_t) if age_f else ''
                part_mes += ' Пол: ' + male_s if len(male_s) else ''
                part_mes += ' Город: ' + hometown if len(hometown) else ''
                part_mes += ' Семейное положение: ' + status_s if len(status_s) else ''
                write_msg(vk_b, 'user_id', event.user_id, "Критерии поиска: " + part_mes)
                cur_menu_ref = 1
                cur_menu_key = 'f' + str(cur_menu_ref)
                write_msg(vk_b, 'user_id', event.user_id, bot_menu[cur_menu_key][0],
                          keyboards=keyboard_1.get_keyboard())
            elif cur_menu_ref == 16:
                pass

            elif cur_menu_ref == 2:             # Меню 'Просмотр'
                if request == 'Отмена':
                    cur_menu_ref = 0
                    cur_menu_key = 'f' + str(cur_menu_ref)
                    write_msg(vk_b, 'user_id', event.user_id, bot_menu[cur_menu_key][0],
                              keyboards=keyboard_0.get_keyboard())
                elif request == 'Одобрить':
                    pass
                elif request == 'Отклонить':
                    pass
                elif request == 'Фото':
                    pass
                else:
                    write_msg(vk_b, 'user_id', event.user_id, "Не понял вашего ответа...")

            elif cur_menu_ref == 3:
                pass
            elif request == 'Просмотр':
                url = 'https://sun9-81.userapi.com/c10306/u7312303/d_32503c9d.jpg'
                attachment = photolu.send_photo(*photolu.upload_photo(upload, url))
                write_msg(vk_b, 'user_id', event.user_id, "Посмотрите фото...",
                          attachments=attachment)

            else:
                write_msg(vk_b, 'user_id', event.user_id, "Не понял вашего ответа...")
