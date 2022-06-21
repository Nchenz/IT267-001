class Customer:   #รับค่าจากลูกค่า
    def __init__(self) -> None:
        self.name = ''      #เตรียมตัวแปรให้มีค่าว่าง
        self.address = ''
        self.phone = ''

    def new_customer(self):
        self.name = input('Enter customer name: ')
        self.address = input('Enter customer  address: ')
        self.phone = input('Enter customer phone: ')

    def cus_info(self):
        return f'Name: {self.name}\nAddress: {self.address}\nPhone: {self.phone}'
