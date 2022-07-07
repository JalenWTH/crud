from django.db import models
import uuid

# Create your models here.

class Post(models.Model):
	post_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	title=models.CharField(max_length=50)
	body=models.CharField(max_length=300)
	created_at=models.DateField(auto_now_add=True)
	updated_at=models.DateField(auto_now=True)