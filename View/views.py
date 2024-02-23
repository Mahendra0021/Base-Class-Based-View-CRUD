from typing import Any
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import StudentForm
from .models import Student
from django.views.generic.base import TemplateView,RedirectView,View

class MyCRUD(TemplateView):
    template_name = 'add_and_data_show.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        data = Student.objects.all()
        context = {'data':data}
        return context
    def post(self, request):
        Uname = request.POST['Uname']
        email = request.POST['email']
        password =request.POST['password']
        student = Student(Uname=Uname, email=email, password=password)
        student.save()
        return redirect('/')

class UserDeleteView(RedirectView):
    url = '/'
    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        Student.objects.get(pk = del_id).delete()
        return super().get_redirect_url(*args, **kwargs)

class UpdateDataView(View):
    def get(self, request,id):
        update_data = Student.objects.get(id=id)
        return render(request, 'update.html', {'update_data': update_data})
    def post(self, request,id):
        Uname = request.POST.get('Uname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        update_data = Student.objects.get(id=id)
        update_data.Uname = Uname
        update_data.email = email
        update_data.password = password
        update_data.save()
        return HttpResponseRedirect('/')





 