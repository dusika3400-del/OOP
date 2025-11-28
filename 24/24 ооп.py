from datetime import datetime
from typing import List, Dict, Any

# ===== ГЛОБАЛЬНЫЕ ПЕРЕМЕННЫЕ =====

# Текущее состояние документа
current_document = ""

# История снимков
document_history = []

# Текущая позиция в истории
current_history_index = -1

# Максимальный размер истории
MAX_HISTORY_SIZE = 10

# ===== ФУНКЦИИ ДЛЯ РАБОТЫ С ДОКУМЕНТОМ =====

def create_document():
    """Создает новый документ"""
    global current_document
    current_document = ""
    print("Создан новый текстовый документ")

def add_text(text: str):
    """Добавляет текст в документ"""
    global current_document
    if text:
        current_document += text
        print(f"Добавлен текст: '{text}'")
        return True
    else:
        print("Введен пустой текст")
        return False

def delete_text(length: int):
    """Удаляет текст с конца документа"""
    global current_document
    if length <= 0:
        print("Ошибка: длина должна быть положительной")
        return False
    
    if length > len(current_document):
        print("Ошибка: нельзя удалить больше символов, чем есть в документе")
        return False
    
    deleted_text = current_document[-length:]
    current_document = current_document[:-length]
    print(f"Удален текст: '{deleted_text}'")
    return True

def replace_text(old_text: str, new_text: str):
    """Заменяет текст в документе"""
    global current_document
    if old_text not in current_document:
        print(f"Текст '{old_text}' не найден в документе")
        return False
    
    current_document = current_document.replace(old_text, new_text)
    print(f"Заменен '{old_text}' на '{new_text}'")
    return True

def display_document():
    """Показывает текущий документ"""
    print(f"\nТЕКУЩИЙ ДОКУМЕНТ:")
    print(f"'{current_document}'")
    print(f"Длина: {len(current_document)} символов\n")

# ===== ФУНКЦИИ ДЛЯ РАБОТЫ СО СНИМКАМИ (MEMENTO) =====

def create_memento() -> Dict[str, Any]:
    """Создает снимок текущего состояния документа"""
    return {
        'content': current_document,
        'timestamp': datetime.now()
    }

def get_memento_info(memento: Dict[str, Any]) -> str:
    """Возвращает информацию о снимке"""
    content = memento['content']
    timestamp = memento['timestamp'].strftime("%Y-%m-%d %H:%M:%S")
    content_preview = content[:20] + "..." if len(content) > 20 else content
    return f"[{timestamp}] '{content_preview}'"

def restore_from_memento(memento: Dict[str, Any]):
    """Восстанавливает документ из снимка"""
    global current_document
    current_document = memento['content']

# ===== ФУНКЦИИ ДЛЯ УПРАВЛЕНИЯ ИСТОРИЕЙ (CARETAKER) =====

def backup_document():
    """Сохраняет текущее состояние в историю"""
    global document_history, current_history_index
    
    # Создаем новый снимок
    memento = create_memento()
    
    # Удаляем все состояния после текущей позиции
    if current_history_index + 1 < len(document_history):
        document_history = document_history[:current_history_index + 1]
    
    # Добавляем новое состояние
    document_history.append(memento)
    current_history_index = len(document_history) - 1
    
    # Ограничиваем размер истории
    if len(document_history) > MAX_HISTORY_SIZE:
        document_history.pop(0)
        current_history_index -= 1
    
    print(f"Состояние сохранено {get_memento_info(memento)}")

def undo_action() -> bool:
    """Отменяет последнее действие"""
    global current_history_index
    
    if current_history_index <= 0:
        print("Нет действий для отмены")
        return False
    
    # Переходим к предыдущему состоянию
    current_history_index -= 1
    previous_memento = document_history[current_history_index]
    restore_from_memento(previous_memento)
    
    print(f"Отменено действие. Восстановлено состояние: {get_memento_info(previous_memento)}")
    return True

def redo_action() -> bool:
    """Повторяет отмененное действие"""
    global current_history_index
    
    if current_history_index >= len(document_history) - 1:
        print("Нет действий для повтора")
        return False
    
    # Переходим к следующему состоянию
    current_history_index += 1
    next_memento = document_history[current_history_index]
    restore_from_memento(next_memento)
    
    print(f"Повторено действие. Восстановлено состояние: {get_memento_info(next_memento)}")
    return True

def show_history():
    """Показывает историю изменений"""
    if not document_history:
        print("История изменений пуста")
        return
    
    print("\nИСТОРИЯ ИЗМЕНЕНИЙ:")
    for i, memento in enumerate(document_history):
        current_indicator = " ← ТЕКУЩЕЕ" if i == current_history_index else ""
        print(f"{i+1}. {get_memento_info(memento)}{current_indicator}")
    
    print(f"\nВсего состояний: {len(document_history)}")
    print(f"Текущая позиция: {current_history_index + 1}")
    print()

# ===== ГЛАВНАЯ ФУНКЦИЯ ПРИЛОЖЕНИЯ =====

def main():
    """Главная функция текстового редактора"""
    
    # Инициализация документа
    create_document()
    
    menu = '''
=== ТЕКСТОВЫЙ РЕДАКТОР С СИСТЕМОЙ ОТМЕНЫ (ПРОЦЕДУРНЫЙ) ===

1. Добавить текст
2. Удалить текст (с конца)
3. Заменить текст
4. Показать текущий документ
5. Сохранить состояние (Backup)
6. Отменить действие (Undo)
7. Повторить действие (Redo)
8. Показать историю изменений
0. Выход

Выберите действие: '''
    
    while True:
        try:
            choice = input(menu).strip()
            
            if choice == '0':
                print("До свидания!")
                break
            
            elif choice == '1':
                text = input("Введите текст для добавления: ").strip()
                if add_text(text):
                    backup_document()
            
            elif choice == '2':
                try:
                    length = int(input("Сколько символов удалить с конца: ").strip())
                    if delete_text(length):
                        backup_document()
                except ValueError:
                    print("Ошибка: введите число")
            
            elif choice == '3':
                old_text = input("Какой текст заменить: ").strip()
                new_text = input("На какой текст заменить: ").strip()
                if old_text and replace_text(old_text, new_text):
                    backup_document()
                else:
                    print("Введите текст для замены")
            
            elif choice == '4':
                display_document()
            
            elif choice == '5':
                backup_document()
            
            elif choice == '6':
                if undo_action():
                    display_document()
            
            elif choice == '7':
                if redo_action():
                    display_document()
            
            elif choice == '8':
                show_history()
            
            else:
                print("Неверный выбор. Попробуйте снова.")
        
        except KeyboardInterrupt:
            print("\nПрограмма прервана пользователем")
            break
        except Exception as e:
            print(f"Произошла ошибка: {e}")
 
    # Запуск основного приложения
    main()