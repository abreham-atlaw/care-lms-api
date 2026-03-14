import os
import unittest

from care_api import settings
from lib.qr_generator.basic_qr_generator import BasicQRGenerator


class BasicQRGeneratorTest(unittest.TestCase):

	def test_generate(self):
		generator = BasicQRGenerator()

		CONTENT = "https://example.com"
		EXPORT_PATH = settings.BASE_DIR / "tmp/qr_codes/01.png"

		generator.generate(CONTENT, EXPORT_PATH)

		self.assertTrue(os.path.exists(EXPORT_PATH))