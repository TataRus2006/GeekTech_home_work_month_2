"""
     класс Компания: —> атрибуты (company_bank, company_name)
     Создать класс Человек: —> атрибуты (имя, фамилия, оклад) и наследовать его от Компания
     создает 2 метода для класса Лицо:
     1) get_salary —> при запросе сделать проверку на то, что если у компании недостаточно средств для выдачи зп
     сотруднику выводить: «У компании недостаточно средств!» или же: отнять от капитала комании(company_bank)
     зарплату сотрудника(Person.salary)
     2) person_info —> выводит информацию о сотруднике (имя, фамилия, оклад)
"""


class Company:
    def __init__(self, company_bank, company_name):
        self.company_bank = company_bank
        self.company_name = company_name


class Human(Company):
    def __init__(self, company_bank, company_name, name, last_name, person_salary):
        super().__init__(company_bank, company_name)
        self.name = name
        self.last_name = last_name
        self.person_salary = person_salary

    def get_salary(self):
        if self.company_bank <= self.person_salary:
            return "«У компании недостаточно средств!»"
        else:
            self.company_bank -= self.person_salary
            return self.person_salary

    def person_info(self):
        print(f"""
Name: {self.name}
Last_name: {self.last_name}
Person_salary: {self.get_salary()}
        """)


president_company = Human(1000000, "Optima Bank", "Sadyr", 'Zhaparov', 400000)
president_company.person_info()
president_company.person_info()
president_company.person_info()
