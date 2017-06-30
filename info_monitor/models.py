from django.db import models

# Create your models here.
class Infos(models.Model):
    sites_info_obtained=(("retirement","RET"),("CARDING","CD"))
    search_result=(("found","yes"),("not_found","no"))

    zipcode=models.PositiveSmallIntegerField(null=False,blank=False)
    f_name = models.CharField(max_length=50, default="")
    l_name = models.CharField(max_length=50, default="")
    middlename=models.CharField(max_length=20,default="",blank=True)
    age=models.PositiveSmallIntegerField(default=0,blank=True,null=True)
    address = models.CharField(max_length=100,blank=True)
    links=models.TextField(blank=True)
    myfile=models.FileField(upload_to="media",null=True,blank=True)
    where=models.CharField(choices=sites_info_obtained,max_length=50,null=True)
    dob=models.DateField(null=True,blank=True)
    status=models.NullBooleanField(default=False)
    def __str__(self):
        return self.f_name

    class Meta:
        verbose_name="UsedInfo"
        verbose_name_plural="UsedInfos"





