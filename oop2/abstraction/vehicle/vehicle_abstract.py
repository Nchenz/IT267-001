from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self,brand,speed) -> None:
        super().__init__()
        self.brand = brand
        self.speed = speed
        self.gear = 0
        self.seat = 0

    @abstractmethod  #เฉพาะmethod ร่วมที่ทุกตัวต้องใช้เท่านั้น ถ้าเอาmethodทั้งหมดมาใส่ ทุกตัวต้องใช้ที่มีทั้งหมด
    def show_detail(self):
        pass