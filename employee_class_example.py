user_list = []
user_dict = {'first_nam': 'sonu', 'last_name': 'tak','contact': '1234', 'email_id':'qw@gmail.com', 'age':'23',
             'first_name': 'ass', 'last_name': 'qww','contact': '533', 'email_id':'rtgv@gmail.com', 'age':'36',
                'first_name': 'vuj', 'last_name': 'yuj','contact': '8633', 'email_id':'vyu@gmail.com', 'age':'86',
                'first_name': 'fyh', 'last_name': 'kkm','contact': '9556', 'email_id':'vgh@gmail.com', 'age':'76',
                'first_name': 'etty', 'last_name': 'cgb','contact': '31564', 'email_id':'srr@gmail.com', 'age':'43'}
class Employee:
    def __init__(self, *args, **kwargs):
        self.initalize_object(kwargs)
        user_list.append(self)

    def initalize_object(self, emp_data):

        self.first_name = emp_data.get("first_name")
        self.last_name = emp_data.get("last_name")
        self.contact = emp_data.get("contact")
        self.email_id = emp_data.get("email_id")
        self.age = emp_data.get("age")

    @staticmethod
    def employee_greater_than_age(age = 30):
        new_emp_list = []
        for emp in user_list:
            if emp.age > age:
                new_emp_list.append(emp)
        return new_emp_list

    # below function to convert output (address) into human redable content
    def __repr__(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.first_name

if __name__ =="__main__":
        for emp_dict in user_dict:


            emp_obj = Employee(first_name = emp_dict.get("first_name"),
                               last_name = emp_dict.get("last_name"),
                               contact = emp_dict.get("contact"),
                               email_id = emp_dict.get("email_id")
                               age = emp_dict.get("age" )
            print(len(user_list))
            print("Employee having age more than 30")
            print(Employee.employee_greater_than_age())
            print(user_list[0])