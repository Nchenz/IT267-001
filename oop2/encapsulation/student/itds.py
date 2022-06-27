from student import Student
class Itds(Student):
    def __init__(self, stuid, name, major) -> None:
        super().__init__(stuid, name, major)
    
    def _displaynameandmajor(self):
        print(f'ITDS Name: {self._name}')
        super()._displaynameandmajor()