from bank_abstract import Bank

class Abank(Bank):
    def __init__(self, bankname: str) -> None:
        super().__init__(bankname)
        self.__loanamount:int = 0 
        self.__loanyear:int = 0 
        self.__loanrate:float = 0 
        self.interest:float = 0
        self.monthlypay:float= 0

    @property
    def loanamount(self):
        return self.__loanamount
    @loanamount.setter
    def loanamount(self,value):
        self.__loanamount = value
    
    @property
    def loanyear(self):
        return self.__loanyear
    @loanyear.setter
    def loanyear(self,value):
        self.__loanyear = value

    @property
    def loanrate(self):
        return self.__loanrate
    @loanrate.setter
    def loanrate(self,value):
        self.__loanrate = value

    def flat_rate(self):
        super().flat_rate()
        self.interest = ({self.loanamount}*({self.loanrate / 100})) * {self.loanyear}
        self.monthlypay = ({self.loanamount + self.interest}) / {self.loanyear*12}

    def display_interest(self):
        print(f'***** {self.bankname} Loan Info *****')
        print(f'Loan: {self.loanamount:,.2f} baht')
        print(f'Rate: {self.loanrate:.2f}%')
        print(f'Year: {self.loanyear}')
        print(f'Interest: {self.interest:,.2f} baht')
        print(f'Monthly Repayment: {self.monthlypay:,.2f} baht')