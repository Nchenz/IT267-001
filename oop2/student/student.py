class Student:
    def __init__(self,stuid,name,major) -> None:
        self._stuid = stuid
        self._name = name
        self._major = major

    def _displaynameandmajor(self):
        print(f'Name: {self._name}')
        print(f'Major: {self._major}')