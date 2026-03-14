import os
import unittest

from django.test import TestCase

from apps.certificate.models import Certificate
from care_api import settings
from di.utils_providers import UtilsProviders


class PillowCertificateGeneratorTest(TestCase):

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
