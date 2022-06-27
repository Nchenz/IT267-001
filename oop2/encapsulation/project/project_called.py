#crate object
from condo import Condo
condo1 = Condo('Ideo5',18,'Ladphrao','Condo 20 Floor',80)
condo1.show()


from project import Project
home = Project('Ladawan',15,'Bang Yai')
home.show()
home.update_budget(30)
print(f'Budget: {home.get_budget()} MB') #มันreturn ต้องสั่งprint