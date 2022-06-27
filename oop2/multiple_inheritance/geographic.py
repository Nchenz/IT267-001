class Geographic:
    def setcordinate(self,latitude:float,longitude:float):
        self.latitude = latitude
        self.longitude = longitude

    def getcordinate(self):
        return f'latitude: {self.latitude}, longitude: {self.longitude}'

    def gettimeZone(self):
        timezone = round(self.longitude/12 -1)
        if timezone > 0 :
            return f'+{timezone}'
        else:
            return f'{timezone}'

    def getclimate(self):
        if self. latitude <= -66.5 or self.latitude >= 66.5:
            return f'Polar zone'
        elif self.latitude <= -23.5 or self.latitude >= 23.5:
            return f'Temerate zone'
        else:
            return f'Tropical zone'