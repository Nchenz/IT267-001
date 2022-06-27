class Temperature:
    def setcelsius(self,celsius:float):
        self.celsius = celsius

    def getcelsius(self):
        return self.celsius

    def getfahrenheit(self):
        return self.celsius*1.8 + 32

    def getweather(self):
        if self.celsius <= 0:
            return f'freezing'
        elif self.celsius <= 18:
            return f'cold'
        elif self.celsius <= 28:
            return f'warm'
        else:
            return f'hot'