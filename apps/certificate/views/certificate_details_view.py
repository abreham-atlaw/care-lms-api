from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.certificate.models import Certificate
from apps.certificate.serializers import CertificateSerializer


class CertificateDetailsView(APIView):

	def get(self, request: Request, *args, **kwargs) -> Response:

		certificate = get_object_or_404(Certificate, id=request.query_params["id"])

		serializer = CertificateSerializer(instance=certificate)

		return Response(
			data=serializer.data,
			status=status.HTTP_200_OK
		)
