import json
import os
import typing

from PIL import Image, ImageDraw
from PIL.ImageFile import ImageFile
from datetime import datetime

from lib.qr_generator import QRGenerator
from apps.certificate.utils.certificate_utils import CertificateUtils
from apps.certificate.models import Certificate
from .certificate_generator import CertificateGenerator


class PillowCertificateGenerator(CertificateGenerator):

	__FULL_NAME_KEY = "full_name_position"
	__QR_POSITION_KEY = "qr_position"
	__QR_SIZE_KEY = "qr_size"

	def __init__(
			self,
			template_path: str,
			config_path: str,
			qr_generator: QRGenerator,
			tmp_path: str = "/tmp",
	):
		super().__init__()
		self.__template_path = template_path
		self.__qr_generator = qr_generator
		self.__tmp_path = tmp_path
		with open(config_path, "r") as file:
			self.__config: typing.Dict[str, typing.Any] = json.load(file)

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
		draw.text(self.__config[self.__FULL_NAME_KEY], name, fill="black", font_size=100, anchor="mm")

	def __place_qr_code(self, template: ImageFile, certificate: Certificate):
		qr = self.__generate_qr_code(certificate)
		qr = qr.resize(self.__config[self.__QR_SIZE_KEY])
		template.paste(qr, self.__config[self.__QR_POSITION_KEY])

	def generate(self, certificate: Certificate, export_path: str):
		template = self.__load_template()

		self.__place_full_name(template, certificate.full_name)
		self.__place_qr_code(template, certificate)

		template.save(export_path)
