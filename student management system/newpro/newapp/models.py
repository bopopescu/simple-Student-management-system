from django.db import models

FEE_STATUS=(
    ('paid', 'Paid'),
    ('not Paid','Not Paid'),
            )

class Standard(models.Model):
    standard=models.CharField(max_length=20)
    def __str__(self):
        return self.standard

class Division(models.Model):
    division=models.CharField(max_length=20)
    def __str__(self):
        return self.division

class Fees(models.Model):
    tuitionfee=models.IntegerField(default=0,blank=False,null=False)
    messfee=models.IntegerField(default=0,blank=False,null=False)
    busfee=models.IntegerField(default=0,blank=False,null=False)
    hostelfee=models.IntegerField(default=0,blank=False,null=False)

    def __str__(self):
        template = '{0.tuitionfee} tuition fee/{0.messfee} mess fee/{0.busfee} bus fee/{0.hostelfee} hostel fee'
        return template.format(self)





class Classes(models.Model):
    classes=models.CharField(max_length=10,blank=False,null=False)
    standard = models.ForeignKey(Standard, null=False)
    division = models.ForeignKey(Division, null=False)
    tuitionfee = models.ForeignKey(Fees,related_name='fee1', null=False)
    messfee = models.ForeignKey(Fees,related_name='fee2',null=False)
    busfee = models.ForeignKey(Fees,related_name='fee3',null=False)
    hostelfee = models.ForeignKey(Fees,related_name='fee4',null=False)

    def __str__(self):
        return self.classes


class Student(models.Model):
     name=models.CharField(max_length=20)
     age=models.IntegerField(default=0)
     gender=models.CharField(max_length=20)
     classes=models.ForeignKey(Classes,null=False)
     feestatus=models.CharField(max_length=20,choices=FEE_STATUS)
     tuition_fee=models.CharField(max_length=20,null=False,blank=False)
     hostel_fee=models.CharField(max_length=20,null=False,blank=False)
     mess_fee=models.CharField(max_length=20,null=False,blank=False)
     bus_fee=models.CharField(max_length=20,null=False,blank=False)
     def __str__(self):
         return self.name






