main_menu = '''\nМеню:
    1 - Показать все заметки
    2 - Добавить заметку
    3 - Редактировать заметку 
    4 - Поиск по дате
    5 - Поиск по id
    6 - Удалить заметку
    7 - Выход\n'''

input_choice = 'Введите команду: '

input_title = 'Введите заголовок новой заметки: '

input_body = 'Введите текст заметки: '

def add_note_success(note_title):
    return (f"Заметка {note_title} создана!")

input_edit_id = 'Введите id заметки, которую хотите изменить: '


# def input_what_to_edit():
#     param = input("Что хотите изменить? Введите 1 - для заголовка"
#                   "2 - для текста: ")
#     return param

input_what_to_edit= "Что хотите изменить? Введите 1 - для заголовка, 2 - для текста: "

input_new_title = 'Введите новый заголовок: '

input_new_body = 'Введите новый тект: '

input_error = 'Введено неправильное значение!'

changes_successful = "Изменения сохранены!"

input_date = "Введите дату: "

find_note_error = "Не удалось найти заметку"

input_id = "Введите id: "

delete_success = "Заметка удалена!"