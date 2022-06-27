#create Bus Object
from bus import Bus

#create Motocycle Object
from motorcycle import Motorcycle

bus = Bus('Bus',4,120,'v1234')
bus.set_color('blue')  
bus.set_capacity(34)
bus.bus_detail() 

bike = Motorcycle('Motocycle',2,100,'v5678')
bike.set_cc(1200)
bike.bike_detail()