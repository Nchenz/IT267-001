#from animalsubclass import Dog,Cat,Cow
from animalsubclass import *  #เรียกใช้ทุกตัว

#create object
dogobj = Dog('Fluffy',4)
catobj = Cat('Milo',2.5)
cowobj = Cow('Phil',5)

"""dogobj.info()
dogobj.make_sound()
catobj.info()
catobj.make_sound()
cowobj.info()
cowobj.make_sound()"""

#เขียนแบบใช้loop
for animal in (dogobj,catobj,cowobj):
    print('***********')
    animal.info()
    animal.make_sound()