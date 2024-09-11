from abc import ABC


class Employee(ABC):
    def __init__(self, name: str, salary: int):
        self.__name = name
        self.__salary = salary

    def get_name(self) -> str:
        return self.__name

    def get_salary(self) -> int:
        return self.__salary


class Manager(Employee):
    def __init__(self, name: str, salary: int, department: str):
        Employee.__init__(self, name, salary)
        self.__department = department

    def get_department(self) -> str:
        return self.__department


class Developer(Employee):
    def __init__(self, name: str, salary: int, programming_language: str):
        Employee.__init__(self, name, salary)
        self.__programming_language = programming_language

    def get_programming_language(self) -> str:
        return self.__programming_language


class TeamLead(Manager, Developer):
    def __init__(self, name: str, salary: int, department: str, programming_language: str, team_size: int):
        Employee.__init__(self, name, salary)
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.__team_size = team_size

    def get_team_size(self) -> int:
        return self.__team_size