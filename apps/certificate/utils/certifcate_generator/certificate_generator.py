from abc import ABC, abstractmethod

from apps.certificate.models import Certificate


class CertificateGenerator(ABC):

	@abstractmethod
	def generate(self, certificate: Certificate, export_path: str):
		pass
