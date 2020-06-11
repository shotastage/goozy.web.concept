from django.db import models

# Create your models here.

class Gooz(models.Model):
  name = models.CharField(max_length = 255)
  serial = models.CharField(max_length = 255)
  photo = models.ImageField(upload_to='documents/', default='df_img')
  registered_by = models.CharField(max_length = 255)
  uploaded_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
        return self.name
