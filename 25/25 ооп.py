from datetime import datetime

# ===== ГЛОБАЛЬНЫЕ ПЕРЕМЕННЫЕ =====

# Все переменные храним глобально без какой-либо структуры
current_text = ""  # Текущий текст документа

# Для истории просто храним кучу отдельных переменных
saved_text_1 = ""
saved_text_2 = "" 
saved_text_3 = ""
saved_text_4 = ""
saved_text_5 = ""
saved_time_1 = ""
saved_time_2 = ""
saved_time_3 = ""
saved_time_4 = ""
saved_time_5 = ""
history_count = 0
current_position = 0

# ===== ФУНКЦИИ БЕЗ ПОВТОРНОГО ИСПОЛЬЗОВАНИЯ КОДА =====

def create_new_document():
    """Создает документ - каждая функция уникальна, не переиспользуем код"""
    global current_text
    current_text = ""
    print("Создан новый документ")

def add_some_text():
    """Добавляет текст - полностью самостоятельная функция"""
    global current_text
    user_input = input("Введите текст для добавления: ").strip()
    if user_input:
        current_text = current_text + user_input  # Не используем +=
        print(f"Добавлен текст: '{user_input}'")
        save_current_state()  # Вызываем сохранение отдельно
    else:
        print("Пустой текст не добавлен")

def remove_some_text():
    """Удаляет текст - своя уникальная реализация"""
    global current_text
    try:
        number = int(input("Сколько символов удалить с конца: ").strip())
        if number <= 0:
            print("Число должно быть положительным")
            return
            
        if number > len(current_text):
            print("Нельзя удалить больше чем есть")
            return
            
        # Удаляем символы по-своему, не как в других функциях
        temp_text = ""
        for i in range(len(current_text) - number):
            temp_text = temp_text + current_text[i]
        removed_part = current_text[len(current_text) - number:]
        current_text = temp_text
        print(f"Удалено: '{removed_part}'")
        save_current_state()
        
    except:
        print("Нужно ввести число")

def change_some_text():
    """Заменяет текст - полностью изолированная функция"""
    global current_text
    old_part = input("Какой текст заменить: ").strip()
    new_part = input("На какой текст заменить: ").strip()
    
    if not old_part:
        print("Нужно указать что заменять")
        return
        
    # Своя реализация замены без использования replace()
    if old_part in current_text:
        result_text = ""
        i = 0
        while i < len(current_text):
            if current_text[i:i+len(old_part)] == old_part:
                result_text = result_text + new_part
                i = i + len(old_part)
            else:
                result_text = result_text + current_text[i]
                i = i + 1
        current_text = result_text
        print(f"Заменен '{old_part}' на '{new_part}'")
        save_current_state()
    else:
        print(f"Текст '{old_part}' не найден")

def show_document():
    """Показывает документ - без переиспользования кода"""
    global current_text
    print("\n--- ТЕКУЩИЙ ДОКУМЕНТ ---")
    print(current_text)
    print(f"Всего символов: {len(current_text)}")
    print("------------------------\n")

def save_current_state():
    """Сохраняет состояние - уникальная реализация без общих функций"""
    global current_text, history_count, current_position
    global saved_text_1, saved_text_2, saved_text_3, saved_text_4, saved_text_5
    global saved_time_1, saved_time_2, saved_time_3, saved_time_4, saved_time_5
    
    now_time = datetime.now().strftime("%H:%M:%S")
    
    # Каждый случай обрабатываем отдельно
    if history_count == 0:
        saved_text_1 = current_text
        saved_time_1 = now_time
        history_count = 1
        current_position = 1
        print(f"Сохранено состояние 1 в {now_time}")
        
    elif history_count == 1:
        saved_text_2 = current_text
        saved_time_2 = now_time
        history_count = 2
        current_position = 2
        print(f"Сохранено состояние 2 в {now_time}")
        
    elif history_count == 2:
        saved_text_3 = current_text
        saved_time_3 = now_time
        history_count = 3
        current_position = 3
        print(f"Сохранено состояние 3 в {now_time}")
        
    elif history_count == 3:
        saved_text_4 = current_text
        saved_time_4 = now_time
        history_count = 4
        current_position = 4
        print(f"Сохранено состояние 4 в {now_time}")
        
    elif history_count == 4:
        saved_text_5 = current_text
        saved_time_5 = now_time
        history_count = 5
        current_position = 5
        print(f"Сохранено состояние 5 в {now_time}")
        
    else:  # history_count == 5
        # Сдвигаем историю вручную
        saved_text_1 = saved_text_2
        saved_text_2 = saved_text_3
        saved_text_3 = saved_text_4
        saved_text_4 = saved_text_5
        saved_text_5 = current_text
        saved_time_1 = saved_time_2
        saved_time_2 = saved_time_3
        saved_time_3 = saved_time_4
        saved_time_4 = saved_time_5
        saved_time_5 = now_time
        current_position = 5
        print(f"Сохранено состояние 5 в {now_time} (старые данные сдвинуты)")

def go_back():
    """Отмена действия - своя уникальная реализация"""
    global current_text, current_position
    
    if current_position <= 1:
        print("Нельзя отменить - история пуста")
        return False
        
    # Каждый случай обрабатываем отдельно
    if current_position == 2:
        current_text = saved_text_1
        current_position = 1
        print(f"Отменено. Восстановлено состояние 1 из {saved_time_1}")
        
    elif current_position == 3:
        current_text = saved_text_2
        current_position = 2
        print(f"Отменено. Восстановлено состояние 2 из {saved_time_2}")
        
    elif current_position == 4:
        current_text = saved_text_3
        current_position = 3
        print(f"Отменено. Восстановлено состояние 3 из {saved_time_3}")
        
    elif current_position == 5:
        current_text = saved_text_4
        current_position = 4
        print(f"Отменено. Восстановлено состояние 4 из {saved_time_4}")
        
    show_document()
    return True

def go_forward():
    """Повтор действия - полностью изолированная функция"""
    global current_text, current_position, history_count
    
    if current_position >= history_count:
        print("Нельзя повторить - нет отмененных действий")
        return False
        
    # Каждый случай обрабатываем отдельно
    if current_position == 1 and history_count >= 2:
        current_text = saved_text_2
        current_position = 2
        print(f"Повторено. Восстановлено состояние 2 из {saved_time_2}")
        
    elif current_position == 2 and history_count >= 3:
        current_text = saved_text_3
        current_position = 3
        print(f"Повторено. Восстановлено состояние 3 из {saved_time_3}")
        
    elif current_position == 3 and history_count >= 4:
        current_text = saved_text_4
        current_position = 4
        print(f"Повторено. Восстановлено состояние 4 из {saved_time_4}")
        
    elif current_position == 4 and history_count >= 5:
        current_text = saved_text_5
        current_position = 5
        print(f"Повторено. Восстановлено состояние 5 из {saved_time_5}")
        
    show_document()
    return True

def display_history():
    """Показывает историю - без переиспользования кода"""
    global history_count, current_position
    global saved_text_1, saved_text_2, saved_text_3, saved_text_4, saved_text_5
    global saved_time_1, saved_time_2, saved_time_3, saved_time_4, saved_time_5
    
    if history_count == 0:
        print("История пуста")
        return
        
    print("\n=== ИСТОРИЯ ИЗМЕНЕНИЙ ===")
    
    # Каждый элемент выводим отдельно
    if history_count >= 1:
        marker = " ← ТЕКУЩЕЕ" if current_position == 1 else ""
        preview = saved_text_1[:15] + "..." if len(saved_text_1) > 15 else saved_text_1
        print(f"1. [{saved_time_1}] '{preview}'{marker}")
        
    if history_count >= 2:
        marker = " ← ТЕКУЩЕЕ" if current_position == 2 else ""
        preview = saved_text_2[:15] + "..." if len(saved_text_2) > 15 else saved_text_2
        print(f"2. [{saved_time_2}] '{preview}'{marker}")
        
    if history_count >= 3:
        marker = " ← ТЕКУЩЕЕ" if current_position == 3 else ""
        preview = saved_text_3[:15] + "..." if len(saved_text_3) > 15 else saved_text_3
        print(f"3. [{saved_time_3}] '{preview}'{marker}")
        
    if history_count >= 4:
        marker = " ← ТЕКУЩЕЕ" if current_position == 4 else ""
        preview = saved_text_4[:15] + "..." if len(saved_text_4) > 15 else saved_text_4
        print(f"4. [{saved_time_4}] '{preview}'{marker}")
        
    if history_count >= 5:
        marker = " ← ТЕКУЩЕЕ" if current_position == 5 else ""
        preview = saved_text_5[:15] + "..." if len(saved_text_5) > 15 else saved_text_5
        print(f"5. [{saved_time_5}] '{preview}'{marker}")
        
    print("=======================\n")

# ===== ГЛАВНАЯ ПРОГРАММА =====

def main_program():
    """Главная функция без использования паттернов"""
    
    create_new_document()

    menu_text = '''
=== ПРОСТОЙ ТЕКСТОВЫЙ РЕДАКТОР ===

1. Добавить текст
2. Удалить текст  
3. Заменить текст
4. Показать документ
5. Сохранить состояние
6. Отменить (Назад)
7. Повторить (Вперед)
8. Показать историю
0. Выход

Выберите действие: '''
    
    # Бесконечный цикл с кучей отдельных условий
    while True:
        try:
            user_choice = input(menu_text).strip()
            
            if user_choice == '0':
                print("Выход из программы")
                break
                
            elif user_choice == '1':
                add_some_text()
                
            elif user_choice == '2':
                remove_some_text()
                
            elif user_choice == '3':
                change_some_text()
                
            elif user_choice == '4':
                show_document()
                
            elif user_choice == '5':
                save_current_state()
                
            elif user_choice == '6':
                go_back()
                
            elif user_choice == '7':
                go_forward()
                
            elif user_choice == '8':
                display_history()
                
            else:
                print("Неизвестная команда")
                
        except KeyboardInterrupt:
            print("\nПрограмма прервана")
            break
        except Exception as error:
            print(f"Ошибка: {error}")

# Запуск программы
if __name__ == "__main__":
    main_program()