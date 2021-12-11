from django.shortcuts import render
from testapp.models import StudentModel

# Create your views here.
def index_page_view(request):
    return render(request,"testapp/index.html")

def student_info_view(request):
    students=StudentModel.objects.all().order_by('marks')
    return render(request,"testapp/studentinfo.html",{'students':students})
