from empit import EmpIT

#create object employee it
mike = EmpIT('001','Milk',60000)
mike.add_skill('Python,JavaScript')
mike.add_experience(5)
mike.emp_detail()
mike.it_salary()

#create object employee marketing
from empmkt import EmpMKT
anna = EmpMKT('002','Anna',35000)
anna.emp_detail()
anna.mkt_salary()

#พนักงานการตลาด ชื่อ Paul เงินเดือน 45000 ได้คอมมิชชั่น 35% ทำงานอยู่เชี่ยงใหม่
from empmkt import EmpMKT
paul = EmpMKT('003','Pual',45000)
paul.add_location('Chaing Mai')
paul.add_commission(35)
paul.emp_detail()
paul.mkt_salary()