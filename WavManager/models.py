from django.db import models
from scipy.fftpack import idstn

# Create your models here.
class FileWav(models.Model):
    ids = models.IntegerField(default=1)
    name = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    text = models.CharField(max_length=200, default='')

    def Save(self):
        self.save()
    
    @staticmethod
    def get_file_by_id(ids):
        try:
            return FileWav.objects.get(ids= ids)
        except:
            return False
    
    def isExists(self):
        if FileWav.objects.filter(name = self.name):
            return True
        return False
