from django.db import models

# Create your models here.
class Infos(models.Model):
    sites_info_obtained=("A","")
    zipcode=models.PositiveSmallIntegerField(null=False,blank=False)
    f_name = models.CharField(max_length=50, default="")
    l_name = models.CharField(max_length=50, default="")
    middlename=models.CharField(max_length=20,default="",blank=True)

    age=models.PositiveSmallIntegerField(default=0,blank=True,null=True)
    address = models.CharField(max_length=100,blank=True)
    links=models.URLField(blank=True)


    def __str__(self):
        return self.f_name

    class Meta:
        verbose_name="UsedInfo"
        verbose_name_plural="UsedInfos"





