import uuid
from datetime import datetime

from django.db import models


class Certificate(models.Model):

	id: uuid.UUID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	full_name: str = models.CharField()
	course: str = models.CharField()
	date: datetime = models.DateTimeField(auto_now_add=True)
