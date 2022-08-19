from django.urls import path
from employee import views


urlpatterns=[
    path("account/signup",views.UseregistrationView.as_view(),name="sign-up"),
    path("account/login",views.LogInView.as_view(),name="log-in"),
    path("user/reg",views.EmployeeCreateView.as_view(),name="emp-reg"),
    path("user/list",views.EmployeeListView.as_view(),name="emp-list"),
    path("base",views.BaseView.as_view(),name="emp-base"),
    path("user/detail/<str:emp_id>",views.EmployeeDetailView.as_view(),name="emp-view"),
    path("user/edit/<str:emp_id>",views.EmployeeEditView.as_view(),name="emp-edit"),
    path("account/signout",views.signout,name="sign-out")

]