import os

from PIL import Image, ImageDraw
from PIL.ImageFile import ImageFile
from datetime import datetime

from lib.qr_generator import QRGenerator
from apps.certificate.utils.certificate_utils import CertificateUtils
from apps.certificate.models import Certificate
from .certificate_generator import CertificateGenerator


class PillowCertificateGenerator(CertificateGenerator):

	__FULL_NAME_POSITION = (780, 560)
	__QR_POSITION = (1210, 800)
	__QR_SIZE = (200, 200)

	def __init__(
			self,
			template_path: str,
			qr_generator: QRGenerator,
			tmp_path: str = "/tmp"
	):
		super().__init__()
		self.__template_path = template_path
		self.__qr_generator = qr_generator
		self.__tmp_path = tmp_path

	def __load_template(self) -> ImageFile:
		template = Image.open(self.__template_path)
		return template

	def __generate_qr_code(self, certificate: Certificate) -> ImageFile:
		url = CertificateUtils.generate_certificate_url(certificate)
		path = os.path.join(self.__tmp_path, f"{datetime.now().timestamp()}.png")
		self.__qr_generator.generate(url, path)
		return Image.open(path)

	def __place_full_name(self, template: ImageFile, name: str):
		draw = ImageDraw.Draw(template)
		draw.text(self.__FULL_NAME_POSITION, name, fill="black", font_size=100, anchor="mm")

	def __place_qr_code(self, template: ImageFile, certificate: Certificate):
		qr = self.__generate_qr_code(certificate)
		qr = qr.resize(self.__QR_SIZE)
		template.paste(qr, self.__QR_POSITION)

	def generate(self, certificate: Certificate, export_path: str):
		template = self.__load_template()

		self.__place_full_name(template, certificate.full_name)
		self.__place_qr_code(template, certificate)

		template.save(export_path)
