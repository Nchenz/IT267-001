import cafe 
#แสดงรายการขนมของร้าน
dessert_menu = cafe.Dessert()   #ชื่อโมดูล.ชื่อคลาส
print(dessert_menu.show_dessert())

#แสดงรายการเครื่องดื่มของร้าน
drink_menu = cafe.Drink()
print(drink_menu.show_drink())

#เพิ่มรายการเครื่องดื่ม
drink_menu.add_drink('Juice')
drink_menu.add_drink('Smoothy')
print(drink_menu.show_drink())