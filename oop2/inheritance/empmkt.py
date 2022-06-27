from employee import Employee
class EmpMKT(Employee):
    def __init__(self, id, name, salary) -> None:
        super().__init__(id, name, salary)
        self.location = 'Bangkok'
        self.commission = 30
        self.department = 'Marketing'

    def add_location(self,location):
        self.location = location

    def add_commission(self,commission):
        self.commission = commission

    def emp_tail(self):
        print('===== Employee Marketing Detail =====')
        super().emp_detail()  #เรียกใช้method emp_detail ในclassแม่มาใช้ จะแสดงid,name
        print(f'Location: {self.location}')  #overide
        print(f'Commission: {self.commission} %')

    def mkt_salary(self):
        self._emp_salary()