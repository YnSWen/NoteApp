import json
import datetime
import random
import uuid

import text
def show_main_menu() -> int:
    print(text.main_menu)
    while True:
        choice = input(text.input_choice)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)


def show_notes():
    with open("notes.json", "r", encoding='utf-8') as file:
        notes = json.load(file)
        if len(notes) == 0:
            print('Список заметок пуст')
        else:
            for note in notes:
                print(f'id: {note["id"]}\nДата создания: {note["creation_date"]}\n'
                        f'Дата последнего изменения: {note["last_changes"]}\n'
                        f'{note["title"]}\n{note["body"]}\n ')



def add_note():
    with open("notes.json", "r", encoding= 'utf-8') as file:
        notes = json.load(file)

    id = random.randint(1, 100)
    while id in notes:
        id = random.randint(1, 100)

    creation_date = datetime.datetime.now().strftime("%Y-%m-%d")
    last_changes = datetime.datetime.now().strftime("%Y-%m-%d")
    title = input(text.input_title)
    body = input(text.input_body)
    new_note ={"id": id,
               "creation_date": creation_date,
               "last_changes": last_changes,
               "title": title,
               "body": body}

    notes.append(new_note)

    with open("notes.json", "w", encoding='utf-8') as file:
        json.dump(notes, file, indent=4)
    print(text.add_note_success(title))



def edit_note():
    with open("notes.json", "r", encoding='utf-8') as file:
        notes = json.load(file)

    edit_id = input(text.input_edit_id)
    param = input(text.input_what_to_edit)

    for note in notes:
        if edit_id.isdigit():
            if note["id"] == int(edit_id):
                if int(param) == 1:
                    new_title = input(text.input_new_title)
                    note["title"] = new_title
                elif int(param) == 2:
                    new_body = input(text.input_new_body)
                    note["body"] = new_body
                note["last_changes"] = datetime.datetime.now().strftime("%Y-%m-%d")
        else:
            print(text.input_error)
    with open("notes.json", "w") as file:
        json.dump(notes, file, indent=4)
    print(text.changes_successful)


def find_note_by_date():
    with open("notes.json", "r", encoding='utf-8') as file:
        notes = json.load(file)

    date_to_find = input(text.input_date)
    found = False
    for note in notes:
        if note["creation_date"] == str(date_to_find):
            print(f'id: {note["id"]}\nДата создания: {note["creation_date"]}\n'
                  f'Дата последнего изменения: {note["last_changes"]}\n'
                  f'{note["title"]}\n{note["body"]}\n ')
            found = True

    if not found:
        print(text.find_note_error)


def find_note_by_id():
    with open("notes.json", "r", encoding='utf-8') as file:
        notes = json.load(file)

    id_to_find = input(text.input_id)
    found = False
    for note in notes:
        if note["id"] == int(id_to_find):
            print(f'id: {note["id"]}\nДата создания: {note["creation_date"]}\n'
                  f'Дата последнего изменения: {note["last_changes"]}\n'
                  f'{note["title"]}\n{note["body"]}\n ')
            found = True

    if not found:
        print(text.find_note_error)



def delete_note():
    with open("notes.json", "r", encoding='utf-8') as file:
        notes = json.load(file)
    id_note_to_delete = input(text.input_id)

    for note in notes:
        if note["id"] == int(id_note_to_delete):
            notes.remove(note)

    with open("notes.json", "w") as file:
        json.dump(notes, file, indent=4)
    print(text.delete_success)










