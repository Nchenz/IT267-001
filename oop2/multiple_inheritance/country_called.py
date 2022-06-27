from country import Conutry

#create countries object
#Thailand lat = 13.7649136 , long = 100.5360959 , population = 70078203 , area = 513120 , temperture = 32C

c1 = Conutry('Thailand',513120,70078203)
c1.setcordinate(13.7649136,100.5360959)
c1.setcelsius(32)
c1.showdetails()

#create 2 country
c2 = Conutry('Egypt',1001000,102300000)
c2.setcordinate(26.8205530,30.8024980)
c2.setcelsius(25)
c2.showdetails()

c3 = Conutry('Canada',9985000,38010000)
c3.setcordinate(56.1303660,-106.3467710)
c3.setcelsius(22)
c3.showdetails()