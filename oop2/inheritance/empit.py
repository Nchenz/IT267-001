from employee import Employee
class EmpIT(Employee):
    def __init__(self, id, name, salary) -> None:
        super().__init__(id, name, salary)
        self.skill = None   #ไม่มีค่า
        self.experience = '' #มีสมาชิกเป้นเซ็ทว่าง
        self.department = 'IT'

    def add_skill(self,skill:str):
        self.skill = skill

    def add_experience(self,experience:int):
        self.experience = experience

    def emp_tail(self):
        print('===== Employee IT Detail =====')
        super().emp_detail()  #เรียกใช้method emp_detail ในclassแม่มาใช้ จะแสดงid,name
        print(f'Skill: {self.skill}')  #overide
        print(f'Experience: {self.experience} year(s)')

    def it_salary(self):
        self._emp_salary()
