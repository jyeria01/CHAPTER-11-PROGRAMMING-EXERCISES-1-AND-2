# Define the Employee class
class Employee:

    # Initialize the Employee object with name and id_number
    def __init__(self, name, id_number):
        self.__name = name
        self.__id_number = id_number
        
    # Mutator method for setting the employee's name
    def set_name(self, name):
        self.__name = name

    # Mutator method for setting the employee's id_number
    def set_id_number(self, id_number):
        self.__id_number = id_number

    # Accessor method for getting the employee's name
    def get_name(self):
        return self.__name

    # Accessor method for getting the employee's id_number
    def get_id_number(self):
        return self.__id_number

# Define the ProductionWorker class, a subclass of Employee
class ProductionWorker(Employee):
    
    # Initialize the ProductionWorker class object
    def __init__(self, name, id_number, shift_number, pay_rate):
        Employee.__init__(self, name, id_number)
        self.__shift_number = shift_number
        self.__pay_rate = pay_rate

    # Mutator method for setting the employee's shift_number
    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    # Mutator method for setting the employee's pay_rate
    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate

    # Accessor method for getting the employee's shift_number
    def get_shift_number(self):
        return self.__shift_number

    # Accessor method for getting the employee's pay_rate
    def get_pay_rate(self):
        return self.__pay_rate