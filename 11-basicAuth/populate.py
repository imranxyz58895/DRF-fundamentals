import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "basicAuth.settings")

import django
django.setup()

from testApp.models import Employee 
from random import randint

from faker import Faker 
fake = Faker()

def populate(number):
	for i in range(number):
		feno = randint(1001, 9999)
		fename = fake.name()
		fesal = randint(10000, 99999)
		feaddr = fake.city()
		emp = Employee.objects.get_or_create(
			eno=feno, esal=fesal, eaddr=feaddr, ename=fename
		)

populate(10)