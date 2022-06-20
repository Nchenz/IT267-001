from cafe import Dessert,Drink
#แสดงรายการขนมของร้าน
dessert_menu = Dessert()
print(dessert_menu.show_dessert())

#แสดงรายการเครื่องดื่มของร้าน
drink_menu = Drink()
print(drink_menu.show_drink())

#เพิ่มรายการเครื่องดื่ม
drink_menu.add_drink('Juice')
drink_menu.add_drink('Smoothy')
print(drink_menu.show_drink())