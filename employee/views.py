from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,FormView,TemplateView,UpdateView
from employee.forms import UserRegistrationForm,LogInForm,EmployeeRegistrationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from employee.models import Employee
from django.utils.decorators import  method_decorator


def sign_required(fn):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            messages.error(request,"login first")
            return redirect("log-in")

    return wrapper




class UseregistrationView(CreateView):
    form_class = UserRegistrationForm
    template_name = "register.html"
    model = User
    success_url = reverse_lazy("log-in")



class LogInView(FormView):
    form_class = LogInForm
    template_name = "login.html"
    model = User
    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                print("success")
                login(request,user)
                return redirect("emp-list")
            else:
                messages.error(request,"login failed")
                return render(request,self.template_name,{"form":form})

@method_decorator(sign_required,name="dispatch")
class EmployeeCreateView(CreateView):
    form_class = EmployeeRegistrationForm
    template_name = "employeeregisteration.html"
    model = Employee
    success_url = reverse_lazy("emp-list")



    def form_valid(self, form):
        form.instance.user=self.request.user
        messages.success(self.request,"profile has been created")
        self.object = form.save()
        return super().form_valid(form)

@method_decorator(sign_required,name="dispatch")
class EmployeeListView(View):
    def get(self,request,*args,**kwargs):
        qs=Employee.objects.all()
        return render(request, "list.html", {"employee": qs})
@method_decorator(sign_required,name="dispatch")
class BaseView(TemplateView):
    template_name = "base.html"

@method_decorator(sign_required,name="dispatch")
class EmployeeDetailView(View):
    def get(self, request, *args, **kwargs):
        id=kwargs.get("emp_id")
        employee=Employee.objects.get(id=id)
        return render(request,"details.html",{"employee":employee})

@method_decorator(sign_required,name="dispatch")
class EmployeeEditView(UpdateView):
    model = Employee
    form_class = EmployeeRegistrationForm
    template_name = "update.html"
    success_url = reverse_lazy("emp-list")
    pk_url_kwarg = "emp_id"


@sign_required
def signout(request,*args,**kwargs):
    logout(request)
    return redirect("log-in")