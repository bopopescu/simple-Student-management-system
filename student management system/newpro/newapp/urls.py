from django.conf.urls import url
from django.views.generic import TemplateView,DetailView
from  . import views
# from .views import AddDivision,AddStandard,StandardDisplay,student
# from .models import Standard,Division

urlpatterns = [
    url(r'^$',views.Dashboard.as_view(),name='loggedin'),
    url(r'^standard/$',views.StandardDisplay.as_view(),name='standard_list'),
    url(r'^standard/add/$',views.StandardAdd.as_view(),name='standard_add'),
    url(r'^division/create/$',views.AddDivision.as_view(),name='add_division'),
    #  #division details
    url(r'^division/$',views.DivisionDisplay.as_view(),name='div_list'),
    # add class
    url(r'^class/create/$',views.AddClass.as_view(),name='add_class'),
    #view class
    url(r'^class/$',views.ClassView.as_view(),name='class_list'),
    #add stud
    url(r'^student/add/$',views.AddStudent.as_view(),name='add_student'),
    #students_detail
    url(r'^student/detail/$',views.StudentView.as_view(),name='student_details'),
    #class details
    url(r'^class/(?P<pk>\d+)/$',views.ClassDetails.as_view(),name='class_details'),
    #student's detail
    url(r'^student/(?P<pk>\d+)/$', views.StudentDetails.as_view(), name='student'),
    #delete student
    url(r'^student/delete/(?P<pk>\d+)/$', views.DeleteStudent, name='delete_student'),
    #edit Student
    url('student/edit/(?P<pk>\d+)/$', views.EditStudent.as_view(), name='edit_student'),
    #add fee
    url(r'^student/add/fee$',views.AddFee.as_view(),name='add_fee'),
    #fee list
    url(r'^fee/$',views.FeeList.as_view(),name='fee_list'),
    #pay
    url('student/pay/(?P<pk>\d+)/$', views.PayFee.as_view(), name='pay_fee'),
]


