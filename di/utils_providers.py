from apps.certificate.utils.certifcate_generator import CertificateGenerator, PillowCertificateGenerator
from care_api import settings
from lib.qr_generator import QRGenerator
from lib.qr_generator.basic_qr_generator import BasicQRGenerator


class UtilsProviders:

	@staticmethod
	def provide_qr_generator() -> QRGenerator:
		return BasicQRGenerator()

	@staticmethod
	def provide_certificate_generator() -> CertificateGenerator:
		return PillowCertificateGenerator(
			template_path=settings.CERTIFICATE_TEMPLATE_PATH,
			qr_generator=UtilsProviders.provide_qr_generator(),
			config_path=settings.CERTIFICATE_TEMPLATE_CONFIG_PATH
		)
