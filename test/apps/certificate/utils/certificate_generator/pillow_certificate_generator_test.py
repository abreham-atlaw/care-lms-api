import os
import unittest

from django.test import TestCase, TransactionTestCase, SimpleTestCase

from apps.certificate.models import Certificate
from apps.certificate.utils.certificate_utils import CertificateUtils
from care_api import settings
from di.utils_providers import UtilsProviders


class PillowCertificateGeneratorTest(SimpleTestCase):

	databases = settings.DATABASES

	def test_generate(self):
		EXPORT_PATH = settings.BASE_DIR / "tmp/certificates/01.png"

		certificate = Certificate.objects.create(
			full_name="John Doe",
		)

		generator = UtilsProviders.provide_certificate_generator()
		generator.generate(
			certificate=certificate,
			export_path=EXPORT_PATH
		)

		self.assertTrue(os.path.exists(EXPORT_PATH))

		url = CertificateUtils.generate_certificate_url(certificate)
		print(f"Certificate URL: {url}")
