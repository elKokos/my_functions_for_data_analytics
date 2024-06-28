import pandas as pd
import requests
from abc import ABC, abstractmethod

class PaymentMethod(ABC):

	@abstractmethod
	def pay(self, security_code):
		pass



class DebitPayment(PaymentMethod):

	def pay(self, security_code):
		pass

