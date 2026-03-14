from rest_framework import serializers

from apps.certificate.models import Certificate


class CertificateSerializer(serializers.ModelSerializer):

	class Meta:
		model = Certificate
		fields = ("full_name", "date")
