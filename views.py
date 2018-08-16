from django.views import generic
from . import models
from . import forms
from django import  urls
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django import http
from django.core.urlresolvers import reverse
from django.shortcuts import render

class Dashboard(generic.TemplateView):
    template_name = 'loggedin.html'

class StandardDisplay(generic.TemplateView):
    template_name = 'standard.html'
    def get_context_data(self, **kwargs):
        context=super(StandardDisplay,self).get_context_data(**kwargs)
        context['datas']=models.Standard.objects.all()
        return context

class DivisionDisplay(generic.TemplateView):
    template_name = 'div.html'
    def get_context_data(self, **kwargs):
        context=super(DivisionDisplay,self).get_context_data(**kwargs)
        context['divs']=models.Division.objects.all().order_by('division')
        return context

class StandardAdd(generic.TemplateView):
    template_name = 'addform.html'
    def get_context_data(self, **kwargs):
        context = super(StandardAdd, self).get_context_data(**kwargs)
        context['form']=forms.StdForm
        return  context
    def post(self,request,*args,**kwargs):
        form=forms.StdForm(request.POST)
        if form.is_valid():
            form.save()
        return http.HttpResponseRedirect(urls.reverse('newapp:standard_list'))

class AddDivision(generic.TemplateView):
    template_name='add_div_form.html'
    def get_context_data(self, **kwargs):
        context = super(AddDivision,self).get_context_data()
        context['formdiv']=forms.DivForm
        return context
    def post(self,request,*args,**kwargs):
        formdiv=forms.DivForm(request.POST)
        if formdiv.is_valid():
            formdiv.save()
        return http.HttpResponseRedirect(urls.reverse('newapp:div_list'))

class AddClass(generic.TemplateView):
    template_name = 'add_class_form.html'
    def get_context_data(self, **kwargs):
        context= super(AddClass, self).get_context_data()
        context['formclass']=forms.ClassForm
        return context

    def post(self,request,*args,**kwargs):
        formclass=forms.ClassForm(request.POST)
        if formclass.is_valid():
            formclass.save()
            return HttpResponseRedirect(urls.reverse('newapp:class_list'))

class ClassView(generic.TemplateView):
    template_name = 'class_list.html'
    def get_context_data(self, **kwargs):
        context = super(ClassView, self).get_context_data(**kwargs)
        context['classes'] = models.Classes.objects.all().order_by('classes')
        return context

class AddStudent(generic.TemplateView):
    template_name = 'addstudent.html'
    def get_context_data(self, **kwargs):
        context= super(AddStudent, self).get_context_data()
        context['addstud']=forms.StudentForm
        return context

    def post(self,request,*args,**kwargs):
        addstud=forms.StudentForm(request.POST)
        if addstud.is_valid():
            addstud.save()
            return HttpResponseRedirect(urls.reverse('newapp:add_student'))
        else:
            return HttpResponse("form is not validated")

class StudentList(generic.TemplateView):
    template_name = 'class_list.html'
    def get_context_data(self, **kwargs):
        context = super(StudentList, self).get_context_data(**kwargs)
        context['student'] = models.Classes.objects.all()
        return context

class StudentView(generic.TemplateView):
    template_name = 'student_detail_list.html'
    def get_context_data(self, **kwargs):
        context = super(StudentView, self).get_context_data(**kwargs)
        context['studs'] = models.Student.objects.all().order_by('classes')
        return context

class ClassDetails(generic.TemplateView):
    template_name = 'class_details.html'
    def get_context_data(self, **kwargs):
        context=super(ClassDetails,self).get_context_data(**kwargs)
        context['clas']=models.Student.objects.filter(classes_id=self.kwargs.get('pk')).order_by('name')
        context['tot']=models.Student.objects.filter(classes_id=self.kwargs.get('pk')).count()
        context['girls']=models.Student.objects.filter(classes_id=self.kwargs.get('pk')).filter(gender='female').count()
        context['boys']=models.Student.objects.filter(classes_id=self.kwargs.get('pk')).filter(gender='male').count()

        print(context)
        return context

class StudentDetails(generic.TemplateView):
    template_name = 'student_detail.html'
    def get_context_data(self, **kwargs):
        context=super(StudentDetails,self).get_context_data(**kwargs)
        context['stud']=models.Student.objects.filter(id=self.kwargs.get('pk'))
        return context

def DeleteStudent(request, pk):
    j = get_object_or_404(models.Student, id=pk)
    j.delete()
    return redirect('newapp:student_details')

class EditStudent(generic.UpdateView):

    model = models.Student
    form_class = forms.StudentForm
    template_name = 'edit_student.html'

    def get_success_url(self):
        return reverse('newapp:student_details')

class AddFee(generic.TemplateView):
    template_name = 'add_fee_form.html'

    def get_context_data(self, **kwargs):
        context = super(AddFee, self).get_context_data()
        context['formfee'] = forms.FeeForm
        return context

    def post(self, request, *args, **kwargs):
        formfee = forms.FeeForm(request.POST)
        if formfee.is_valid():
            formfee.save()
            return HttpResponseRedirect(urls.reverse('newapp:class_list'))

class FeeList(generic.TemplateView):
    template_name = 'fee_list.html'
    def get_context_data(self, **kwargs):
        context=super(FeeList,self).get_context_data(**kwargs)
        context['clas']=models.Fee.objects.filter(classes_id=self.kwargs.get('pk'))
        return context

class PayFees(generic.TemplateView):
    template_name = 'pay_fees.html'
    model = models.FeeDetails

    def get_context_data(self, **kwargs):
        context = super(PayFees,self).get_context_data(**kwargs)
        context['form'] = forms.PayForm(classes_id=self.kwargs.get('pk'))
        return context

    def post(self, request,pk):
        #fee=get_object_or_404(models.FeeDetails,classes_id=pk)
        if request.method=="POST":
            print(request.POST)
            ids = models.Fee.objects.filter(classes_id=self.kwargs.get('pk'))
            i=list(ids)
            length=len(i)
            for j in i:
                f = models.FeeDetails.objects.create(name_id=request.POST.get('name'),fee_type_id=j.id, fee_amt=request.POST.get(j.fee_type),classes_id=request.POST.get('classes'))
                f.save()
        return HttpResponseRedirect(reverse('newapp:class_list'))

class FeeDisplay(generic.TemplateView):
    template_name = 'fee_display.html'
    def get_context_data(self, **kwargs):
        context=super(FeeDisplay,self).get_context_data(**kwargs)
        context['clas']=models.FeeDetails.objects.filter(classes_id=self.kwargs.get('pk')).distinct()
        return context





























# class AddFee(generic.TemplateView):
#     template_name = 'add_fee_form.html'
#     def get_context_data(self, **kwargs):
#         context= super(AddFee, self).get_context_data()
#         context['formfee']=forms.FeeForm
#         return context
#
#     def post(self,request,*args,**kwargs):
#         formfee=forms.FeeForm(request.POST)
#         if formfee.is_valid():
#             formfee.save()
#             return HttpResponseRedirect(urls.reverse('newapp:fee_list'))
#
# class FeeList(generic.TemplateView):
#     template_name = 'fee_list.html'
#     def get_context_data(self, **kwargs):
#         context = super(FeeList, self).get_context_data(**kwargs)
#         context['fees'] = models.Fees.objects.all()
#         return context
#
#
# class PayFee(generic.UpdateView):
#
#     model = models.Student
#     form_class = forms.PayForm
#     template_name = 'payform.html'
#
#
#     def get_success_url(self):
#         return reverse('newapp:student_details')
#
#
# def Search(request):
#     query = request.GET.get('q')
#     if query:
#         # There was a query entered.
#         results = models.Student.objects.filter(name=query)
#     else:
#         # If no query was entered, simply return all objects
#         results = models.Student.objects.all()
#     return render(request, 'loggedin.html', {'results': results})














