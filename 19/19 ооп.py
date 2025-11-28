class Sportsman:

    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return f'{self.name}'
    
    def __str__(self) -> str:
        return f'ФИО спортсмена: {self.name}.'
    
class Team:

    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return f'{self.name}'
    
    def __str__(self) -> str:
        return f'Название команды: {self.name}.'
    
class Schedule:
    def __init__(self, team: Team, sportsmen: list[Sportsman], event_name: str, date: str):
        self.team = team
        self.sportsmen = sportsmen
        self.event_name = event_name
        self.date = date
        

    def get_name(self) -> str:
        return self.event_name

    def __str__(self) -> str:
        sportsmen_names = [s.get_name() for s in self.sportsmen]
        return f'Соревнование: "{self.event_name}". Дата: {self.date}. Команда: {self.team.get_name()}. Спортсмены: ({", ".join(sportsmen_names)})'
    

def main():
    all_objects = []
    menu = '''
    1. Создание нового объекта "Расписание".
    2. Вывод объектов.
    3. Вывод конктреного объекта.
    0. Завершение работы программы.
    '''

    while True:
        print(menu)
        menu_item = int(input("Введите номер команды: ").strip())

        if not (0 <= menu_item <= 4):
            print("Вы ввели неверную команду, попробуйте ещё раз.")
            continue
        
        
        match menu_item:
            case 0:
                print("Программа завершила свою работу.")
                break

            case 1:
                team_input = input("Введите название команды: ").strip()
                if not team_input:
                    print("Ошибка: название команды не может быть пустым.")
                    continue
                
                # Ввод данных о соревновании
                event_name = input("Введите название соревнования: ").strip()
                date = input("Введите дату соревнования: ").strip()
                
                # Ввод данных о спортсменах
                sportsmen_input = input("Введите ФИО спортсменов через запятую (формат: Иванов, Петров, Сидоров): ").strip().split(',')
                
                if len(sportsmen_input) == 0:
                    print("Должен быть указан хотя бы один спортсмен. Попробуйте ещё раз.")
                    continue
                
                # Создание объектов спортсменов
                sportsmen = []
                for s in sportsmen_input:
                    name = s.strip()
                    if name:  # проверяем, что имя не пустое
                        sportsmen.append(Sportsman(name))
                
                if not sportsmen:
                    print("Не удалось создать ни одного спортсмена. Проверьте ввод.")
                    continue
                
                # Создание объектов команды и расписания
                team = Team(team_input)  
                schedule = Schedule(team, sportsmen, event_name, date)
                all_objects.append(schedule)

                print("Объект успешно создан!")
                continue

            case 2:
                if len(all_objects) == 0:
                    print('Нет ни одного созданного объекта. Попробуйте для начала ввести команду 1.')
                    continue
                
                print("Вывод содержимого всех объектов:")
                for i, obj in enumerate(all_objects):
                    print(f"--- Объект {i} ---")
                    print(obj)
                    print()
                
                continue

            case 3:
                inx = int(input("Введите индекс интересующего объекта: ").strip())

                if not(0 <= inx <= len(all_objects)):
                    print("Индекс выходит за допустимы диапазон. Попробуйте ещё раз.")
                    continue

                print(f'--- Детальная информация об объекте {inx} ---')
                print(f'Соревнование: {all_objects[inx].get_name()}')
                print(f'Дата: {all_objects[inx].date}')
                print(f'{all_objects[inx].team.__str__()}')
                print('Спортсмены:')
                for s in all_objects[inx].sportsmen:
                    print(f'  - {s.__str__()}')
                
                continue
                
if __name__ == "__main__":
    main()