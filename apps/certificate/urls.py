from django.urls import path

from apps.certificate.views import CertificateDetailsView

urlpatterns = [
	path("certificate/details/", CertificateDetailsView.as_view())
]