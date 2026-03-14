from abc import ABC, abstractmethod


class QRGenerator(ABC):

	@abstractmethod
	def generate(self, content: str, export_path: str):
		pass
