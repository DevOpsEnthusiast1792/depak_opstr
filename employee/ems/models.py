from django.db import models

# Create your models here.

class Employee(models.Model):
    Status = [
    ('manager', 'Manager'),
]
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    status = models.CharField(max_length=20,choices=Status,null=True,blank=True)

    class Meta:
        db_table = "employee"

    def  __str__(self):
        return self.name

class sample(models.Model):
    employee_name = models.ManyToManyField(Employee,related_name='employee_name')
    manager = models.ManyToManyField(Employee,related_name='manager')
