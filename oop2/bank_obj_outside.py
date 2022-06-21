#this file is outside package bank
#call module
#เรียกผ่านpackge แทน
from bank import customer,account

"""#from bank import customer
from bank.customer import Customer  
from bank.account import Account
cus1 = Customer()
cus1.new_customer()"""


cus1 = customer.Customer()
cus1.new_customer()

#เพราะอยู่คนละclass ต้องสร้างobject แยกกัน
cus1_acc = account.Account()
cus1_acc.open_account(cus1.name,'Saving','108-813-4567',500) #เอาข้อมูลจากอันหนึ่งมายังอีกอันหนึ่ง cus.name เรียกมาใช้
print('**** Open Bank Account Detail ****')
print(cus1.cus_info())
print(cus1_acc.display_balance())
#print(cus1.cus_info())