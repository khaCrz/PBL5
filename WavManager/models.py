from django.db import models

# Create your models here.
class FileWav(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    text = models.CharField(max_length=200, default='')

    def Save(self):
        self.save()
    
    @staticmethod
    def get_file_by_id(id):
        try:
            return FileWav.objects.get(id= id)
        except:
            return False
    
    def isExists(self):
        if FileWav.objects.filter(name = self.name):
            return True
        return False
