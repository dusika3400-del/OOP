class Organization:
    '''Абстрактный класс для организаций'''

    def __init__(self, name: str, type_org: str):
        self.name = name
        self.type_org = type_org

    def get_info(self) -> tuple[str, str]:
        return (self.name, self.type_org)

    def __str__(self) -> str:
        '''Метод который должен быть переопределён каждым наследником'''
        pass

    def calculate_budget(self) -> float:
        '''Абстрактный метод для расчета бюджета'''
        pass


class ClientOrganization(Organization):
    '''Организация клиента'''

    def __init__(self, name: str, contract_amount: float):
        super().__init__(name=name, type_org='клиентская организация')
        self.contract_amount = contract_amount
        
    def __str__(self) -> str:
        '''Реализация абстрактного метода для клиентской организации'''
        return f'Тип: {self.type_org}, Название: {self.name}, Сумма контракта: {self.contract_amount}.'
    
    def calculate_budget(self) -> float:
        '''Реализация метода расчета бюджета для клиентской организации'''
        return self.contract_amount * 0.9  # 10% комиссия


class ContractorOrganization(Organization):
    '''Подрядная организация'''

    def __init__(self, name: str, project_count: int, rate_per_project: float):
        super().__init__(name=name, type_org='подрядная организация')
        self.project_count = project_count
        self.rate_per_project = rate_per_project
    
    def __str__(self) -> str:
        '''Реализация абстрактного метода для подрядной организации'''
        return f'Тип: {self.type_org}, Название: {self.name}, Количество проектов: {self.project_count}, Ставка за проект: {self.rate_per_project}.'
    
    def calculate_budget(self) -> float:
        '''Реализация метода расчета бюджета для подрядной организации'''
        return self.project_count * self.rate_per_project


class Project:
    '''Класс проекта, объединяющий организации'''

    def __init__(self, client: ClientOrganization, contractors: list[ContractorOrganization], name: str):
        self.client = client
        self.contractors = contractors
        self.name = name

    def __str__(self) -> str:
        contractors = [c.get_info()[0] for c in self.contractors]
        return f'Проект: "{self.name}". Клиент: {self.client.get_info()[0]}. Подрядчики: ({", ".join(contractors)})"'
    
    def calculate_total_budget(self) -> float:
        '''Расчет общего бюджета проекта'''
        total = self.client.calculate_budget()
        for contractor in self.contractors:
            total += contractor.calculate_budget()
        return total


def main():
    all_objects = []
    menu = '''
    1. Создание нового объекта "Project".
    2. Вывод объектов.
    3. Вывод конкретного объекта.
    4. Расчет бюджетов (демонстрация полиморфизма).
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
                client_input = input("Введите название клиентской организации и сумму контракта через запятую: ").strip().split(', ')
                project_name = input("Введите название проекта: ").strip()
                contractors_input = input("Введите данные подрядчиков (название, кол-во проектов, ставка через запятую), разделяя подрядчиков точкой с запятой: ").strip().split('; ')

                if len(contractors_input) == 0:
                    print("Должен быть указан хотя бы один подрядчик. Попробуйте ещё раз.")
                    continue
                
                # Создаем клиентскую организацию
                client = ClientOrganization(client_input[0], float(client_input[1]))
                
                # Создаем подрядные организации
                contractors = []
                for contractor_str in contractors_input:
                    contractor_data = contractor_str.split(', ')
                    contractor = ContractorOrganization(
                        contractor_data[0], 
                        int(contractor_data[1]), 
                        float(contractor_data[2])
                    )
                    contractors.append(contractor)
                
                project = Project(client, contractors, project_name)
                all_objects.append(project)

                print("Объект успешно создан!")
                continue

            case 2:
                if len(all_objects) == 0:
                    print('Нет ни одного созданного объекта. Попробуйте для начала ввести команду 1.')
                    continue
                
                print("Вывод содержимого всех объектов.")
                for obj in all_objects:
                    print(obj)
                
                continue

            case 3:
                if len(all_objects) == 0:
                    print('Нет ни одного созданного объекта. Попробуйте для начала ввести команду 1.')
                    continue
                    
                inx = int(input("Введите индекс интересующего объекта: ").strip())

                if not(0 <= inx < len(all_objects)):
                    print("Индекс выходит за допустимый диапазон. Попробуйте ещё раз.")
                    continue
                    
                print(f'Название проекта: {all_objects[inx].name}')
                print(f'Клиент: {all_objects[inx].client.__str__()}')
                for contractor in all_objects[inx].contractors:
                    print(f'Подрядчик: {contractor.__str__()}')
                
                continue

            case 4:
                '''Демонстрация полиморфизма - расчет бюджетов для всех организаций'''
                if len(all_objects) == 0:
                    print('Нет ни одного созданного объекта. Попробуйте для начала ввести команду 1.')
                    continue
                
                print("Расчет бюджетов (демонстрация полиморфизма):")
                for i, project in enumerate(all_objects):
                    print(f"\nПроект {i}: {project.name}")
                    print(f"Бюджет клиента: {project.client.calculate_budget():.2f}")
                    
                    for j, contractor in enumerate(project.contractors):
                        print(f"Бюджет подрядчика {j+1}: {contractor.calculate_budget():.2f}")
                    
                    print(f"Общий бюджет проекта: {project.calculate_total_budget():.2f}")
                
                continue
                
if __name__ == "__main__":
    main()