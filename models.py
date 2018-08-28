from django.db import models

FEE_STATUS=(
    ('paid', 'Paid'),
    ('not Paid','Not Paid'),
            )

GENDER=(
    ('male','Male'),
    ('female','Female'),
    ('others','Others')
)

class Standard(models.Model):
    standard=models.CharField(max_length=20)
    def __str__(self):
        return self.standard

class Division(models.Model):
    division=models.CharField(max_length=20)
    def __str__(self):
        return self.division

class Classes(models.Model):
    classes=models.CharField(max_length=10,blank=False,null=False)
    standard = models.ForeignKey(Standard, null=False)
    division = models.ForeignKey(Division, null=False)
    def __str__(self):
        return self.classes

class Fee(models.Model):
    fee_amount=models.CharField(max_length=20, null=False, blank=False)
    fee_type = models.CharField(max_length=20, null=False, blank=False)
    classes = models.ForeignKey(Classes, null=False)

    def __str__(self):
        return self.fee_type

class Student(models.Model):
     name=models.CharField(max_length=20)
     age=models.IntegerField(default=0)
     gender=models.CharField(max_length=20,choices=GENDER)
     classes=models.ForeignKey(Classes,null=False)

     def __str__(self):
         return self.name

class FeeDetails(models.Model):
    name=models.ForeignKey(Student,null=False)
    classes=models.ForeignKey(Classes,null=True)
    fee_type=models.ForeignKey(Fee,null=True,blank=True)
    fee_amt=models.CharField(max_length=20,null=True)




