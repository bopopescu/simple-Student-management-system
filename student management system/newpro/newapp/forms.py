from django import  forms
from . import models

class StdForm(forms.ModelForm):
    class Meta:
        model = models.Standard
        fields=('standard',)

    def clean_standard(self):
        standard = self.cleaned_data['standard']
        if models.Standard.objects.filter(standard=standard).exists():
            raise forms.ValidationError('standard already exists')
        return standard



class DivForm(forms.ModelForm):
    class Meta:
        model=models.Division
        fields = ('division',)

    def clean_division(self):
        division = self.cleaned_data['division']
        if models.Division.objects.filter(division=division).exists():
            raise forms.ValidationError('standard already exists')
        return division


class ClassForm(forms.ModelForm):
  class Meta:
    model=models.Classes
    fields = ('classes','standard','division','tuitionfee','messfee','hostelfee','busfee')




class StudentForm(forms.ModelForm):
    class Meta:
        model=models.Student
        fields = ('name','age','gender','classes','feestatus')

    def clean(self):
        age = self.cleaned_data['age']
        if age < 0:
            raise forms.ValidationError("you can't go below zero", code="age", )
        return self.cleaned_data

class FeeForm(forms.ModelForm):
  class Meta:
    model=models.Fees
    fields = ('tuitionfee','messfee','busfee','hostelfee')

class PayForm(forms.ModelForm):
    class Meta:
        model=models.Student
        fields = ('tuition_fee','hostel_fee','mess_fee','bus_fee','feestatus')


#
#
# #
#
