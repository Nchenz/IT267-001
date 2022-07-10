from abc import ABC

class Bank(ABC):
    def __init__(self,bankname:str) -> None:
        super().__init__()
        self.bankname = bankname

    def flat_rate(self):
        pass