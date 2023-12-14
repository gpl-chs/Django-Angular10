from django.test import TestCase, Client
from django.urls import reverse

from EmployeeApp.models import Departments,Employees
from EmployeeApp.serializers import DepartmentSerializer, EmployeeSerializer
import datetime
#Arrange Act Assert
class DepartmentAPITests(TestCase):
    def setUp(self):
        self.department = Departments.objects.create(DepartmentName='Test Department')
        self.department1 = Departments.objects.create(DepartmentName='Test Department 1')
        self.department2 = Departments.objects.create(DepartmentName='Test Department 2')
            
        self.client = Client()
        self.url = reverse('department-api')     

    def test_get_departments(self):
        # Test GET request to retrieve departments
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        actual_data = response.json()
        except_data = DepartmentSerializer([self.department, self.department1, self.department2], many=True).data
        #print(except_data)
        self.assertEqual(actual_data, except_data)

    def test_create_departments(self):
        data = {'DepartmentName':'IT'}
        response = self.client.post(self.url, data, content_type='application/json')  
        #print(response.json())   Added successfully   
        self.assertEqual(response.status_code, 200)
        # Verify that the department has been created
        created_department = Departments.objects.get(DepartmentName='IT')
        self.assertEqual(created_department.DepartmentName, 'IT') 

    def test_update_departments(self):
        updated_data = {'DepartmentId':self.department1.DepartmentId, 'DepartmentName':'HR'}
        response = self.client.put(self.url, updated_data, content_type='application/json')  
        self.assertEqual(response.status_code, 200)
        updated_department = Departments.objects.get(DepartmentId=self.department1.DepartmentId)
        self.assertEqual(updated_department.DepartmentName, 'HR')

    def test_delete_departments(self):
        url = reverse('department-api-detail', args=[self.department.DepartmentId])
        response = self.client.delete(url, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        with self.assertRaises(Departments.DoesNotExist):
            Departments.objects.get(DepartmentId=self.department.DepartmentId)


class EmployeeAPITests(TestCase):
    def setUp(self):
        self.employee = Employees.objects.create(EmployeeName='Chs',Department='IT',DateOfJoining='2023-12-12',PhotoFileName='Anonymous.png')
        self.employee1 = Employees.objects.create(EmployeeName='Michx',Department='HR',DateOfJoining='2022-07-07',PhotoFileName='Anonymous.png')
        self.employee2 = Employees.objects.create(EmployeeName='Bea',Department='HR',DateOfJoining='2022-01-01',PhotoFileName='Anonymous.png')
        self.client = Client()
        self.url = reverse('employee-api')     

    def test_get_employees(self):
        # Test GET request to retrieve employees
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        actual_data = response.json()
        except_data = EmployeeSerializer([self.employee, self.employee1, self.employee2], many=True).data
        #print(except_data)
        self.assertEqual(actual_data, except_data)

    def test_create_employees(self):
        data = {'EmployeeName':'chs','Department':'IT','DateOfJoining':'2022-07-07','PhotoFileName':'Anonymous.png'}
        response = self.client.post(self.url, data, content_type='application/json')  
        #print(response.json())   Added successfully   
        self.assertEqual(response.status_code, 200)
        # Verify that the employee has been created
        created_employee = Employees.objects.get(EmployeeName='chs')
        self.assertEqual(created_employee.EmployeeName, 'chs') 
        self.assertEqual(created_employee.Department, 'IT') 
        self.assertEqual(created_employee.DateOfJoining, datetime.date(2022, 7, 7))
        self.assertEqual(created_employee.PhotoFileName, 'Anonymous.png') 

    def test_update_employees(self):
        updated_data = {'EmployeeId':self.employee1.EmployeeId, 'EmployeeName':'fritz','Department':'IT','DateOfJoining':'2022-08-08','PhotoFileName':'fritz.png'}
        response = self.client.put(self.url, updated_data, content_type='application/json')  
        self.assertEqual(response.status_code, 200)
        updated_employee = Employees.objects.get(EmployeeId=self.employee1.EmployeeId)
        self.assertEqual(updated_employee.EmployeeName, 'fritz')
        self.assertEqual(updated_employee.Department, 'IT')
        self.assertEqual(updated_employee.DateOfJoining, datetime.date(2022, 8, 8))
        self.assertEqual(updated_employee.PhotoFileName, 'fritz.png') 

    def test_delete_employees(self):
        url = reverse('employee-api-detail', args=[self.employee.EmployeeId])
        response = self.client.delete(url, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        with self.assertRaises(Employees.DoesNotExist):
            Employees.objects.get(EmployeeId=self.employee.EmployeeId)



    











    






