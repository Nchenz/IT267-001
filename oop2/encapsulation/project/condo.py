from project import Project
class Condo(Project):
    def __init__(self, name, time, location,type,budget) -> None:
        super().__init__(name, time, location)
        self.type = type
        self.__budget = budget #ตัวแปรใหม่ของclassนี้เท่านั้น

    def show(self):
        super().show()
        print(f'Type: {self.type}')
        print(f'Condo Budget: {self.__budget}')
        print(f'Project Budget: {self.get_budget()} MB') #เอาตัวแปร budget ของclass project