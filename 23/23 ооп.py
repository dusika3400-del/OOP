from datetime import datetime
from typing import List

class DocumentMemento:
    """
    Класс Снимок (Memento) - хранит состояние документа в определенный момент времени.
    """
    
    def __init__(self, content: str):
        self._content = content
        self._timestamp = datetime.now()
    
    def get_content(self) -> str:
        return self._content
    
    def get_timestamp(self) -> str:
        return self._timestamp.strftime("%Y-%m-%d %H:%M:%S")
    
    def get_info(self) -> str:
        content_preview = self._content[:20] + "..." if len(self._content) > 20 else self._content
        return f"[{self.get_timestamp()}] '{content_preview}'"


class TextDocument:
    """
    Класс Создатель (Originator) - текстовый документ.
    """
    
    def __init__(self):
        self._content = ""
        print("Создан новый текстовый документ")
    
    def add_text(self, text: str) -> None:
        self._content += text
        print(f"Добавлен текст: '{text}'")
    
    def delete_text(self, length: int) -> None:
        if length <= 0:
            print("Ошибка: длина должна быть положительной")
            return
        
        if length > len(self._content):
            print("Ошибка: нельзя удалить больше символов, чем есть в документе")
            return
        
        deleted_text = self._content[-length:]
        self._content = self._content[:-length]
        print(f"Удален текст: '{deleted_text}'")
    
    def replace_text(self, old_text: str, new_text: str) -> None:
        if old_text not in self._content:
            print(f"Текст '{old_text}' не найден в документе")
            return
        
        self._content = self._content.replace(old_text, new_text)
        print(f"Заменен '{old_text}' на '{new_text}'")
    
    def get_content(self) -> str:
        return self._content
    
    def display(self) -> None:
        print(f"\nТЕКУЩИЙ ДОКУМЕНТ:")
        print(f"'{self._content}'")
        print(f"Длина: {len(self._content)} символов\n")
    
    def save(self) -> DocumentMemento:
        return DocumentMemento(self._content)
    
    def restore(self, memento: DocumentMemento) -> None:
        self._content = memento.get_content()


class History:
    """
    Класс Опекун (Caretaker) - управляет историей снимков документа.
    """
    
    def __init__(self, document: TextDocument, max_history_size: int = 10):
        self._document = document
        self._mementos: List[DocumentMemento] = []
        self._max_history_size = max_history_size
        self._current_index = -1  # Индекс текущего состояния в истории
    
    def backup(self) -> None:
        # Создаем новый снимок
        memento = self._document.save()
        
        # Удаляем все состояния после текущей позиции
        if self._current_index + 1 < len(self._mementos):
            self._mementos = self._mementos[:self._current_index + 1]
        
        # Добавляем новое состояние
        self._mementos.append(memento)
        self._current_index = len(self._mementos) - 1
        
        # Ограничиваем размер истории
        if len(self._mementos) > self._max_history_size:
            self._mementos.pop(0)
            self._current_index -= 1
        
        print(f"Состояние сохранено {memento.get_info()}")
    
    def undo(self) -> bool:
        """Переходит к предыдущему состоянию в истории"""
        if self._current_index <= 0:
            print("Нет действий для отмены")
            return False
        
        # Переходим к предыдущему состоянию
        self._current_index -= 1
        previous_memento = self._mementos[self._current_index]
        self._document.restore(previous_memento)
        
        print(f"Отменено действие. Восстановлено состояние: {previous_memento.get_info()}")
        return True
    
    def redo(self) -> bool:
        """Переходит к следующему состоянию в истории (если было отменено)"""
        if self._current_index >= len(self._mementos) - 1:
            print("Нет действий для повтора")
            return False
        
        # Переходим к следующему состоянию
        self._current_index += 1
        next_memento = self._mementos[self._current_index]
        self._document.restore(next_memento)
        
        print(f"Повторено действие. Восстановлено состояние: {next_memento.get_info()}")
        return True
    
    def show_history(self) -> None:
        """Показывает всю историю изменений с указанием текущей позиции"""
        if not self._mementos:
            print("История изменений пуста")
            return
        
        print("\nИСТОРИЯ ИЗМЕНЕНИЙ:")
        for i, memento in enumerate(self._mementos):
            current_indicator = " ← ТЕКУЩЕЕ" if i == self._current_index else ""
            print(f"{i+1}. {memento.get_info()}{current_indicator}")
        
        print(f"\nВсего состояний: {len(self._mementos)}")
        print(f"Текущая позиция: {self._current_index + 1}")
        print()


def main():
    """
    Главная функция приложения - текстовый редактор с системой отмены действий.
    """
    
    # Создаем объекты
    document = TextDocument()
    history = History(document)
    
    menu = '''
=== ТЕКСТОВЫЙ РЕДАКТОР С СИСТЕМОЙ ОТМЕНЫ ===

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
                if text:
                    document.add_text(text)
                    history.backup()
                else:
                    print("Введен пустой текст")
            
            elif choice == '2':
                try:
                    length = int(input("Сколько символов удалить с конца: ").strip())
                    document.delete_text(length)
                    history.backup()
                except ValueError:
                    print("Ошибка: введите число")
            
            elif choice == '3':
                old_text = input("Какой текст заменить: ").strip()
                new_text = input("На какой текст заменить: ").strip()
                if old_text:
                    document.replace_text(old_text, new_text)
                    history.backup()
                else:
                    print("Введите текст для замены")
            
            elif choice == '4':
                document.display()
            
            elif choice == '5':
                history.backup()
            
            elif choice == '6':
                if history.undo():
                    document.display()
            
            elif choice == '7':
                if history.redo():
                    document.display()
            
            elif choice == '8':
                history.show_history()
            
            else:
                print("Неверный выбор. Попробуйте снова.")
        
        except KeyboardInterrupt:
            print("\nПрограмма прервана пользователем")
            break
        except Exception as e:
            print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    # Запуск основного приложения
    main()