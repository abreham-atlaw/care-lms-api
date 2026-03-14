import os

from apps.certificate.models import Certificate
from care_api import settings


class CertificateUtils:

	@staticmethod
	def generate_certificate_url(certificate: Certificate) -> str:
		return os.path.join(settings.API_URL, f"api/certificates/verify?id={certificate.id.hex}")
