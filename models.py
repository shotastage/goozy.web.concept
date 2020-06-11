

class Gooz(models.Model):
  name = models.CharField(max_length = 255)
  type = models.CharField(max_length = 255)
  registered_by = models.CharField(max_length = 255)
