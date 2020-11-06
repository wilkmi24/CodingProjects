#Parent Class User
class User:
    username = 'jdoe88'
    password = 'qdw2%'

    def userLogin(self):
        entry_username = input("Enter your username:")
        entry_password = input("Enter your password:")
        if (entry_username == self.username and entry_password == self.password):
            print("Welcome back, {}!".format(entry_username))
        else:
                print("The username or passward entered to not match our records.")


#Child Class Customer
class Customer(User):
    email = "jdoe@hotmail.com"
    fName = "Jane"
    lName = "Doe"

    def userLogin(self):
        email = input("Enter your email:")
        entry_password = input("Enter your password:")
        if (email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(fName))
        else:
                print("The email or passward entered to not match our records.")
        

#Child Class Seles Reb
class SalesRep(User):
    employee_ID = 42365
    department = "Accounting"

    def userLogin(self):
        employee_ID = input("Enter your Employee Id:")
        entry_password = input("Enter your password:")
        if (employee_ID == self.emloyee_ID and entry_password == self.password):
            print("Welcome back, {}!".format(emloyee_ID))
        else:
                print("The employee ID or passward entered to not match our records.")





customer = User()
customer.userLogin()

employee = SalesRep()
employee.userLogin
    
                
