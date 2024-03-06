import notes_app
def start():
    while True:
        choice = notes_app.show_main_menu()

        match choice:
            case 1: # Показать все заметки
                notes_app.show_notes()

            case 2: # Добавить заметку
                notes_app.add_note()

            case 3: # Редактировать заметку
                notes_app.edit_note()

            case 4: # Поиск по дате
                notes_app.find_note_by_date()

            case 5: # Поиск по id
                notes_app.find_note_by_id()

            case 6: # Удалить заметку
                notes_app.delete_note()

            case 7:
                break