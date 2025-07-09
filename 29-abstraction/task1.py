"""1. PaymentProcessor nomli abstract class yozing va uni process_payment
   nomli method bor bo'lsin va u amount qabul qilsin
   Undan 3 ta subclass yarating, click, payme, uzum nomli
   method ni ichida shunchaki string qaytarib qo'ysangiz bo'ladi
"""

from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(amount):
        pass



class Click:
    def click():
        return "Click"


class Uzum:
    def uzum():
        return "Uzum"


class Payme:
    def payme():
        return "Payme"
