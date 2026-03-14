import os

from apps.certificate.models import Certificate
from care_api import settings


class CertificateUtils:

	@staticmethod
	def generate_certificate_url(certificate: Certificate) -> str:
		return os.path.join(settings.FRONT_END_URL, f"api/certificate/certificate/details/?id={certificate.id.hex}")
