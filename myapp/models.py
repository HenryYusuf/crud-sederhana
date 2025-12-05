from django.db import models

# Create your models here.
class Dokumen(models.Model):
    judul = models.CharField(max_length=200)
    file = models.FileField(upload_to='uploads/') # Akan masuk ke folder 'uploads/' di R2
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.judul