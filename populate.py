# This is the script which is used to setup the django with our project settings.
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','studentInfo_project.settings')
django.setup()

from testapp.models import StudentModel
from faker import Faker

fake =Faker()

def populate(n):
    for i in range(n):
        fname=fake.first_name()
        fmarks=fake.random_element(elements=(10,20,30,40,100))
        student_records=StudentModel.objects.get_or_create(name=fname,marks=fmarks)
populate(5)
