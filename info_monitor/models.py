from django.db import models

# Create your models here.
class Infos(models.Model):
    zipcode=models.PositiveSmallIntegerField(null=False,blank=False)
    middlename=models.CharField(max_length=20,default="")
    full_name=models.CharField(max_length=50,default="")
    age=models.PositiveSmallIntegerField(default=0)
    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name="UsedInfo"
        verbose_name_plural="UsedInfos"
