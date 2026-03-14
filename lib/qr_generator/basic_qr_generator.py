import qrcode

from .qr_generator import QRGenerator


class BasicQRGenerator(QRGenerator):

	def generate(self, content: str, export_path: str):
		qrcode.make(content).save(export_path)