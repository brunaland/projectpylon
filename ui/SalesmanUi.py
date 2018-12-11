from services.CarService import CarService
from models.Car import Car
from services.CustomerService import CustomerService
from models.Customer import Customer
from models.Order import Order
from services.OrderService import OrderService
from datetime import datetime, timedelta
from models.Colors import Colors



class SalesmanUi:

    def __init__(self):
        self.__carService = CarService()
        self.__customerService = CustomerService()
        self.__orderService = OrderService()

    def mainMenu(self):

        action = ''
        while action != 'q':
            self.spaces()
            self.mainMenuPrint()
            action = self.chooseAction()

            if action == '1' or action == '2':
                self.spaces()
                typeAction = ''
                dateAvailable = datetime.now()
                if action == '1':
                    print(Colors.WHITE + "\nPath: Menu/Available_Cars/" + Colors.END)
                    self.allAvailableCars()
                elif action == '2':
                    print(Colors.WHITE + "\nPath: Menu/UnAvailable_Cars/" + Colors.END)
                    self.allUnAvilableCars()
                cars = self.__carService.getCars(action, typeAction, dateAvailable)
                self.displayAllCarsPrint(cars)
                self.showCarsByTypeMenu(action,dateAvailable)
            
            # elif action == '2':
                # print("\n\033[1;37mPath: Menu/Unavailable_cars/\033[1;m")

            elif action == '3':
                self.createOrder()

            elif action == '4':
                self.spaces()
                print(Colors.WHITE + "\nPath: Menu/Creating_Customer/\n" + Colors.END)
                name,age,ssn,address,number = self.createCustomer()
                newCustomer = Customer(name,age,ssn,address,number)
                self.__customerService.addCustomer(newCustomer)
                print(Colors.GREEN + "\nCustomer has been created!\n" + Colors.END)
                action = self.pressAnyKeyToContinue()

            elif action == '5':
                self.spaces()
                self.findCustomerMenu()

            elif action == '6':####WORKING ON THIS
                self.spaces()
                #search for order by number
                pass
            
            elif action == '7':#####WORKING ON THIS
                self.spaces()
                orders, nothing = self.__orderService.getAllOrders()
                self.displayAllOrders(orders)
                self.pressAnyKeyToContinue()
                #print all orders and options

            elif action == '8':
                self.returnCar()

# Register a car
            elif action == '10':
                self.spaces()
                newCar = self.createCar()
                self.__carService.addCar(newCar)

# Prints out the pricelist for cars.
            elif action == '11':
                self.spaces()
                print(open('./data/pricelist.txt').read())
                action = self.pressAnyKeyToContinue()

# Prints exit message and exits the program.
            elif action == 'q':
                self.spaces()
                self.exitPrint()
                exit()
# unwanted action gets recognized and gives feedback to the user.
            else:
                self.invalidAction(action)
                self.pressAnyKeyToContinue()
                self.mainMenu()

# Prints the mainMenuPage.
    def mainMenuPrint(self):
        print(Colors.BLUE + "___  ___     _       ___  ___")
        print("|  \/  |__ _(_)_ _   |  \/  |___ _ _ _  _ ")
        print("| |\/| / _` | | ' \  | |\/| / -_) ' \ || |")
        print(Colors.WHITE + "|_|  |_\__,_|_|_||_| |_|  |_\___|_||_\_,_|")
        print("\nPath: Menu/\n" + Colors.END)
        print(Colors.BLUE + "You can do the following:" + Colors.END)
        print(Colors.WHITE + "1.  List all available cars")
        print("2.  List all unavailable cars")
        print("3.  Create car reservation.")
        print("4.  Register customer.")
        print("5.  Find a customer.")
        print("6.  Look up an order.")
        print("7.  Show list of orders.")
        print("8.  Return a car.")
        print("9.  Edit order.")
        print("10. Register car")
        print("11. Prints out pricelist for cars."+Colors.END)
        print(Colors.BLUE+"Press q to quit\n"+Colors.END)
    

    '''----------Functions for repetitive code-----------'''
    def spaces(self):
        print('\n'*43)

    def chooseAction(self):
        action = input(Colors.BLUE + "\nChoose action: " + Colors.END)
        return action

    def pressAnyKeyToContinue(self):
        action = input(Colors.BLUE + "\nPress any key to continue: " + Colors.END)
        return action

    def actionsPrint(self):
        print("\n" + Colors.BLUE + "Actions: " + Colors.END)

    def customerFound(self):
        print(Colors.GREEN + "Customer found!" + Colors.END)

    def customerNotFound(self):
        print(Colors.RED + "Customer not found!" + Colors.END)

    def searchTermInput(self):
        searchTerm = input(Colors.BLUE + "Enter SSN or Customer number to find: " + Colors.END)
        return searchTerm

    def exitPrint(self):
        print(Colors.GREEN + "\nHave a nice day!"+ Colors.END)
        print(Colors.GREEN + "Exiting program.." + Colors.END)

    def allCustomersHeaderPrint(self):
        print(Colors.GREEN +
        "---------------------------------- ALL CUSTOMERS ----------------------------------\n"
         + Colors.END)

    def allDeletedCustomerHeaderPrint(self):
        print(Colors.RED +
        "------------------------------ ALL DELETED CUSTOMERS ------------------------------\n"
         + Colors.END)

    def allAvailableCars(self):
        print(Colors.GREEN +
        "---------------------------------------------- ALL AVAILABLE CARS ----------------------------------------------\n"
         + Colors.END)

    def allUnAvilableCars(self):
        print(Colors.RED +
        "--------------------------------------------- ALL UNAVAILABLE CARS ---------------------------------------------\n"
         + Colors.END)

    def creatingCustomerPrintHeader(self):
        print(Colors.GREEN + 
        "-----------Creating customer account-----------"
        + Colors.END)

    def invalidAction(self,action):
        print(Colors.RED+"\nAction "+Colors.WHITE+f"'{action}'"+Colors.RED+" is not a valid action!"+Colors.END)
        # else:
        # self.invalidAction(action)
        # self.pressAnyKeyToContinue()
        # self.showCarsByTypeMenu(typeAction,dateAvailable)

    ''' -------------------- Customer Functions -------------------- '''

    def findCustomerMenu(self):
        self.spaces()
        self.findCustomerMenuPrint()
        action = self.chooseAction()

# Redirects the user to the mainMenuPage.
        if action == '0':
            self.mainMenu()

# Search engine that finds the customer.
        elif action == '1':
            self.spaces()
            print(Colors.WHITE+"Path: Menu/Find_Customer/Search_Existing/"+Colors.END)
            self.searchCustomerHeaderPrint()
            searchTerm = self.searchTermInput()
            customer = self.__customerService.findCustomer(searchTerm)

# If the customer is not found it prints not found message.
            if customer == None:
                self.spaces()
                print(Colors.WHITE+"Path: Menu/Find_Customer/Not_Found/\n"+Colors.END)
                self.customerNotFound()
                self.pressAnyKeyToContinue()
                self.findCustomerMenu()
    
# If the customer is found it prints found message.
            else:
                self.spaces()
                print(Colors.WHITE+"Path: Menu/Find_Customer/Selected_Customer/\n"+Colors.END)
                self.customerFound()
                self.displayCustomerHeaderPrint()
                print(customer)
                self.afterCustomerIsFoundMenu(customer)
#show all customers
        elif action == '2':
            self.spaces()
            print(Colors.WHITE+"Path: Menu/Find_Customer/All_Customers/\n"+Colors.END)
            self.allCustomersHeaderPrint()
            customers = self.__customerService.getAllCustomers()
            self.displayAllCustomersPrint(customers)
            action = self.pressAnyKeyToContinue()
            self.findCustomerMenu()

# Shows all deleted customers.
        elif action == '3':
            self.spaces()
            print(Colors.WHITE+"Path: Menu/Find_Customer/All_Deleted_Customers/\n"+Colors.END)
            self.allDeletedCustomerHeaderPrint()
            customers = self.__customerService.getAllDeletedCustomers()
            self.displayAllCustomersPrint(customers)
            action = self.pressAnyKeyToContinue()
            self.findCustomerMenu()

# Search engine in the deleted customers dir.
        elif action == '4':
            self.spaces()
            print(Colors.WHITE+"Path: Menu/Find_Customer/Search_Deleted/\n"+Colors.END)
            self.searchCustomerHeaderPrint()
            searchTerm = self.searchTermInput()
            customer = self.__customerService.findDeletedCustomer(searchTerm)

# If the customer is not found it prints not found message.
            if customer == None:
                self.spaces()
                self.customerNotFound()
                self.pressAnyKeyToContinue()
                self.findCustomerMenu()
            
# If the customer is found it prints found message.
            else:
                self.spaces()
                self.customerFound()
                self.displayCustomerHeaderPrint()
                print(customer)
                self.afterDeletedCustomerIsFoundMenu(customer)

# After the customer is found the user can go back or reinstate the customer.
    def afterDeletedCustomerIsFoundMenu(self,customer):
        self.afterDeletedCustomerIsFoundPrint()
        action = self.chooseAction()
        if action == '0':
            self.findCustomerMenu()
        elif action == '1':
            self.reinstatingWarningMessageMenu(customer)
        else:
            self.invalidAction(action)
            self.pressAnyKeyToContinue()
            self.afterDeletedCustomerIsFoundMenu(customer)

    def reinstatingWarningMessageMenu(self,customer):
        self.spaces()
        self.reinstatingWarningMessagePrint(customer)
        action = self.chooseAction()
        while action:
            if action == '1':
                customerNumber = customer.getNumber()
                self.__customerService.restoringCustomer(customerNumber)
                self.spaces()
                print(Colors.GREEN+"Customer "+Colors.WHITE+f"'{customer.getName()}'"+Colors.GREEN+" has been reinstated."+Colors.END)  # Customer reinstated
                self.pressAnyKeyToContinue()
                self.spaces()
                self.findCustomerMenu()
            elif action == '2':
                self.spaces()
                self.afterDeletedCustomerIsFoundMenu(customer)
            else:
                self.invalidAction(action)
                self.pressAnyKeyToContinue()
                self.reinstatingWarningMessageMenu(customer)

    def reinstatingWarningMessagePrint(self,customer):
        print(Colors.WHITE+"Path: Menu/Find_Customer/Selected_Customer/Reinstate_Selected_Customer/"+Colors.END)
        print(Colors.GREEN + "\nSelected customer: " + Colors.END)
        self.displayCustomerHeaderPrint()
        print(customer)
        print(Colors.RED + "\nWarning: " + Colors.BLUE + "Are you sure you want to reinstate this customer?" + Colors.END)
        print(Colors.WHITE+"1. Yes, reinstate this customer")
        print("2. No, do not reinstate this customer"+Colors.END)
        
# After the customer is found the user can go back and search another, edit or delete the customer.
    def afterCustomerIsFoundMenu(self, customer):
        self.afterCustomerIsFoundPrint()
        action = self.chooseAction()
        self.spaces()
        if action == '0':
            self.findCustomerMenu()
        elif action == '1':
            self.editCustomerInfo(customer)
        elif action == '2':
            self.warningMessageMenu(customer)
        else:
            self.invalidAction(action)
            self.pressAnyKeyToContinue()
            self.afterCustomerIsFoundMenu(customer)
    
            
# The menu for editing the customer information, Number stays the same
    def editCustomerInfo(self,customer):
        self.spaces()
        self.editCustomerInfoPrint()
        cs = CustomerService()
        action = self.chooseAction()
        self.spaces()
        name = customer.getName()
        age = customer.getAge()
        ssn = customer.getSsn()
        address = customer.getAddress()
        number = customer.getNumber()
        if action =='0':
            self.afterCustomerIsFoundMenu(customer)
# Edit customer name
        elif action =='1':
            print(Colors.WHITE+"Path: Menu/Find_Customer/Selected_Customer/Edit_Customer/Name/\n"+Colors.END)
            print(Colors.BLUE+"Editing customers name:"+Colors.END)
            name = cs.inputNameCheck()
            newCustomer = Customer(name,age,ssn,address,number)
            cs.customerEdit(newCustomer)
            print(Colors.GREEN+"\nCustomer name has been changed from "\
            +Colors.WHITE+f"'{customer.getName()}'"+Colors.END+Colors.GREEN+" to "+Colors.WHITE+f"'{name}'"+Colors.END)
            self.pressAnyKeyToContinue()
            self.editCustomerInfo(customer)
#Edit customer ssn
        elif action =='2':
            print(Colors.WHITE+"Path: Menu/Find_Customer/Selected_Customer/Edit_Customer/Ssn/\n"+Colors.END)
            print(Colors.BLUE+"Editing customers ssn:"+Colors.END)
            ssn,age = cs.inputSsnCheck()
            newCustomer = Customer(name,age,ssn,address,number)
            cs.customerEdit(newCustomer)
            print(Colors.GREEN+"\nCustomer address has been changed from "\
            +Colors.WHITE+f"'{customer.getSsn()}'"+Colors.END+Colors.GREEN+" to "+Colors.WHITE+f"'{ssn}'"+Colors.END)
            self.pressAnyKeyToContinue()
            self.editCustomerInfo(customer)
#Edit customer address
        elif action =='3':
            print(Colors.WHITE+"Path: Menu/Find_Customer/Selected_Customer/Edit_Customer/Address/\n"+Colors.END)
            print(Colors.BLUE+"Editing customers address:"+Colors.END)
            address = cs.inputAddressCheck()
            newCustomer = Customer(name,age,ssn,address,number)
            cs.customerEdit(newCustomer)
            print(Colors.GREEN+"\nCustomer address has been changed from "\
            +Colors.WHITE+f"'{customer.getAddress()}'"+Colors.END+Colors.GREEN+" to "+Colors.WHITE+f"'{address}'"+Colors.END)
            self.pressAnyKeyToContinue()
            self.editCustomerInfo(customer)

#Edit all customer information
        elif action == '4':
            print(Colors.WHITE+"Path: Menu/Find_Customer/Selected_Customer/Edit_Customer/All_Customer_Info/\n"+Colors.END)
            print(Colors.BLUE+"Editing customers name, ssn and address:"+Colors.END)
            cs = CustomerService()
            name = cs.inputNameCheck()
            ssn,age = cs.inputSsnCheck()
            address = cs.inputAddressCheck()
            newCustomer = Customer(name,age,ssn,address,number)
            cs.customerEdit(newCustomer)
# Name changed
            print(Colors.GREEN+"\nCustomer address has been changed from "\
            +Colors.WHITE+f"'{customer.getName()}'"+Colors.END+Colors.GREEN+" to "+Colors.WHITE+f"'{name}'"+Colors.END)
# Ssn changed
            print(Colors.GREEN+"\nCustomer address has been changed from "\
            +Colors.WHITE+f"'{customer.getSsn()}'"+Colors.END+Colors.GREEN+" to "+Colors.WHITE+f"'{ssn}'"+Colors.END)
# Address changed
            print(Colors.GREEN+"\nCustomer address has been changed from "\
            +Colors.WHITE+f"'{customer.getAddress()}'"+Colors.END+Colors.GREEN+" to "+Colors.WHITE+f"'{address}'"+Colors.END)
            self.pressAnyKeyToContinue()
            self.editCustomerInfo(customer)
        else:
            self.invalidAction(action)
            self.pressAnyKeyToContinue()
            self.editCustomerInfo(customer)

# Safety function that asks the user if he is certain that he wants to delete the selected customer.
    def warningMessageMenu(self,customer):
        self.spaces()
        self.warningMessagePrint(customer)
        action = self.chooseAction()
        while action:
            if action == '1':
                customerNumber = customer.getNumber()
                self.__customerService.deletingCustomer(customerNumber)
                self.spaces()
                print(Colors.RED+"Customer "+Colors.WHITE+f"'{customer.getName()}'"+Colors.RED+" has been deleted."+Colors.END) # Customer Deleted
                self.pressAnyKeyToContinue()
                self.spaces()
                self.findCustomerMenu()
            elif action == '2':
                self.spaces()
                self.afterCustomerIsFoundMenu(customer)
            else:
                self.invalidAction(action)
                self.pressAnyKeyToContinue()
                self.warningMessageMenu(customer)

        
# Creates a customer, calls a function in the service class to validate the input.
    def createCustomer(self):
        self.spaces()
        self.creatingCustomerPrintHeader()
        cs = CustomerService()
        name = cs.inputNameCheck()
        ssn, age = cs.inputSsnCheck()
        address = cs.inputAddressCheck()
        number = cs.getSumOfAllCustomers()
        return name,age,ssn,address,number


    '''-------------------------- CUSTOMER PRINT FUNCTIONS -----------------------'''
# Actions the user has after 5 is pressed on the mainPage.
    def findCustomerMenuPrint(self):
        print(Colors.WHITE+"Path: Menu/Find_Customer/"+Colors.END)
        self.actionsPrint()
        print(Colors.WHITE + "0. <-- Go back")
        print("1. Search for a customer")
        print("2. Show all customers")
        print("3. Show all deleted customers")
        print("4. Search for deleted customer"+Colors.END)

# The format which the customer is printed out on.
    def displayCustomerHeaderPrint(self):
        print("{:24} {:15} {:15} {:20} {:15}".format("Name", "Age", "SSN", "Address", "Number"))
        print("{:15} {:15} {:15} {:15} {:15}".format("-----------------------",\
        "---------------","---------------", "--------------------", "---------------"))
# Comes after the displayCustomerHeaderPrint, prints out all the customers.
    def displayAllCustomersPrint(self,customers):
        self.displayCustomerHeaderPrint()
        for customer in customers:
            print(customer)
    
# Header which is printed when user is searching for a customer.
    def searchCustomerHeaderPrint(self):
        print(Colors.YELLOW + 
        "--------------------------------------------Search for customer-------------------------------------------"
        + Colors.END)

# Prints the option to go back or reinstate the customer back into the main customer dir file.   VANTAR PATH
    def afterDeletedCustomerIsFoundPrint(self):
        self.actionsPrint()
        print(Colors.WHITE+"0. Go back")
        print("1. Reinstate selected customer"+Colors.END)

# 
    def afterCustomerIsFoundPrint(self):
        self.actionsPrint()
        print(Colors.WHITE+"0. Go back")
        print("1. Edit customer info")
        print("2. Delete customer"+Colors.END)

# Print function that displays users action choice.
    def editCustomerInfoPrint(self):
        print(Colors.WHITE+"Path: Menu/Find_Customer/Selected_Customer/Edit_Customer/"+Colors.END)
        self.actionsPrint()
        print(Colors.WHITE+"0. <-- Go back")
        print("1. Edit customer name")
        print("2. Edit customer SSN")
        print("3. Edit customer address")
        print("4. Edit All customer information"+Colors.END)

# Prints when user chooses to delete a user.
    def warningMessagePrint(self,customer):
        print(Colors.WHITE+"Path: Menu/Find_Customer/Selected_Customer/Deleted_Selected_Customer/"+Colors.END)
        print(Colors.GREEN + "\nSelected customer: " + Colors.END)
        self.displayCustomerHeaderPrint()
        print(customer)
        print(Colors.RED + "\nWarning: " + Colors.BLUE + "Are you sure you want to delete this customer?" + Colors.END)
        print(Colors.WHITE+"1. Yes, delete this customer")
        print("2. No, do not deleted this customer"+Colors.END)
    
    
    
    ''' -------------------- CAR FUNCTIONS -------------------- '''

    def showCarsByTypeMenu(self, typeAction,dateAvailable):
        while True:
            self.findCarTypeMenuPrint()
            action = self.chooseAction()
            self.spaces()
            if action == '0':
                self.mainMenu()
            elif action == '1':
                if typeAction == '1':
                    self.allAvailableCars()
                elif typeAction == '2':
                    self.allUnAvilableCars()
                action = 'compact'
            elif action == '2':
                if typeAction == '1':
                    self.allAvailableCars()
                elif typeAction == '2':
                    self.allUnAvilableCars()
                action = 'comfort'
            elif action == '3':
                if typeAction == '1':
                    self.allAvailableCars()
                elif typeAction == '2':
                    self.allUnAvilableCars()
                action = 'CUV'
            elif action == '4':
                if typeAction == '1':
                    self.allAvailableCars()
                elif typeAction == '2':
                    self.allUnAvilableCars()
                action = 'highland'
            elif action == '5':
                if typeAction == '1':
                    self.allAvailableCars()
                elif typeAction == '2':
                    self.allUnAvilableCars()
                action = 'luxury'
            else:
                self.invalidAction(action)
                self.pressAnyKeyToContinue()
                self.showCarsByTypeMenu(typeAction,dateAvailable)
            cars = self.__carService.getCars(typeAction, action,dateAvailable)
            self.displayAllCarsPrint(cars)

    def createCar(self):
        self.spaces()
        self.createCarPrint()
        #car type
        carTypeInput = self.__carService.checkCarType()
        make = input('Make (f.x. Toyota Yaris): ').capitalize()
        color = input('Color: ').capitalize()
        passengers = self.__carService.checkPassengers()
        transmissionInput = self.__carService.checkTransmission()
        liecensePlate = self.__carService.checkLicenseplate()

        transmission = self.getTransmission(transmissionInput)
        rentCost, carType = self.getCarTypeVariables(carTypeInput)
        status = 'available'
        rentOutCar, unusedValue = self.getTimeOfOrder()
        returnCar = rentOutCar
        newCar = Car(carType,make,liecensePlate,color,passengers,transmission,rentCost,status,rentOutCar,returnCar)
        print(Colors.GREEN+"\nCar successfully created!"+Colors.END)
        self.printCarHeader()
        print(newCar)

        return newCar


    def getTransmission(self, transmissionInput):
        if transmissionInput == 1:
            transmission = 'Auto'
        else:
            transmission = 'Manual'
        return transmission

    def getCarTypeVariables(self,carTypeInput):
        if carTypeInput == '1':
            carType = 'Compact'
            rentCost = 14000
        elif carTypeInput == '2':
            carType = 'Comfort'
            rentCost = 20000
        elif carTypeInput == '3':
            carType = 'CUV'
            rentCost = 25000
        elif carTypeInput == '4':
            carType = 'Highland'
            rentCost = 30000
        elif carTypeInput == '5':
            carType = 'Luxury'
            rentCost = 35000
        return rentCost, carType

    '''----------------------------------CAR PRINT FUNCTIONS-----------------------------------------------'''
    def displayAllCarsPrint(self,cars):
        self.printCarHeader()
        for car in cars:
            print(car)

    def findCarTypeMenuPrint(self):
        self.actionsPrint()
        print(Colors.WHITE+"0. <-- Go back")
        print("1. Show only Compact")
        print("2. Show only Comfort")
        print("3. Show only CUV")
        print("4. Show only Highland")
        print("5. Show only Luxury"+Colors.END)

    def createCarPrint(self):
        print("\nSelect from Car Types:")
        print("\n1. Compact")
        print("\n2. Comfort")
        print("\n3. CUV")
        print("\n4. Highland")
        print("\n5. Luxury")

    def printCarHeader(self):
        LINE = '---------------'
        print("\n{:15} {:15} {:15} {:15} {:<15} {:15} {:15}".format('Type', 'Make', 'License Plate',\
        'Color', 'Passengers','Transmission','Rent Cost'))
        print("{:15} {:15} {:15} {:15} {:<15} {:15} {:15}".format(LINE, LINE, LINE, LINE, LINE, LINE, LINE))


    '''----------------------------------ORDER FUNCTIONS-----------------------------------------------'''
    def customerNotFoundMenu(self):
        self.spaces()
        self.customerNotFoundPrintMenu()
        action = self.chooseAction()
        if action == '0':
            self.mainMenu()
        elif action == '1':
            self.createOrder()
        else:
            self.invalidAction(action)
            self.pressAnyKeyToContinue()
            self.customerNotFound()

    def rentOutToCustomerMenu(self):
        self.rentOutToCustomerPrintMenu()
        action = self.chooseAction()
        if action == '0':
            self.mainMenu()
        elif action == '1':
            return
        else:
            self.invalidAction(action)
            self.pressAnyKeyToContinue()
            self.rentOutToCustomerMenu()

    def selectCarType(self):
        self.selectCarTypePrintMenu()

        action = self.__orderService.checkCarTypeSelection()
        rentCost, carType = self.getCarTypeVariables(action)

        return rentCost, carType

    def getCostOfOrder(self, rentOutCarTime, returnCarTime, rentCost):
        self.spaces()
        daysRented = returnCarTime - rentOutCarTime
        if daysRented.seconds > 00:
            daysRentedCount = daysRented + timedelta(days = 1)
            totalDaysRented = daysRentedCount.days
        else:
            totalDaysRented = daysRented.days

        print("\nPrice for {} days: ".format(totalDaysRented))         

        totalCost = int(totalDaysRented) * rentCost

        print("Price: {} ISK".format(totalCost))

        return totalCost, totalDaysRented

    def addInsurance(self, cost):
        self.addInsurancePrint()
        action = self.chooseAction()
        self.spaces()
        insurance = 0
        if action == '1':
            totalCost = cost * 1.05
            insurance = cost * 0.05
        elif action == '2':
            totalCost = cost
        else:
            self.invalidAction(action)
            self.pressAnyKeyToContinue()
            self.addInsurance()
        return int(totalCost), int(insurance)

    def getTimeOfOrder(self):
        year = datetime.now().year
        month = datetime.now().month
        day = datetime.now().day
        hour = datetime.now().hour
        minutes = datetime.now().minute
        timeOfOrder = datetime(year, month, day, hour, minutes)
        stringTimeOfOrder = '{}-{}-{}-{}-{}'.format(day, month, year, hour, minutes)
        return stringTimeOfOrder, timeOfOrder

    def areYouSure(self):
        self.spaces()
        self.areYouSurePrint()
        action = self.chooseAction()
        if action == '1':
            return True
        elif action == '2':
            return False
        else:
            self.invalidAction(action)
            self.pressAnyKeyToContinue()
            self.areYouSure()

    def finalStepOrder(self, order):
        self.finalStepOrderPrint()
        action = self.chooseAction()
        if action == '1':
            status = self.areYouSure()
            if status == True:
                self.__orderService.addOrder(order)
                print(Colors.GREEN+"Order complete!"+Colors.END)
            else:
                self.finalStepOrder(order)
        elif action == '2':
            status = self.areYouSure()
            if status == True:
                self.mainMenu()
            else:
                self.finalStepOrder(order)
        else:
            self.invalidAction(action)
            self.pressAnyKeyToContinue()
            self.finalStepOrder(order)

    def createOrder(self):
        self.spaces()
        print(Colors.WHITE + "\nPath: Menu/Create_Reservation/" + Colors.END)
        #Order Number
        self.searchCustomerForCarRentalHeaderPrint()
        searchTerm = self.searchTermInput()
        try:
            customer = self.__customerService.findCustomer(searchTerm)
            name = customer.getName()
            ssn = customer.getSsn()
            self.customerFound()
            self.displayCustomerHeaderPrint()
            print(customer)
            self.rentOutToCustomerMenu()
        except:
            self.customerNotFound()
            self.customerNotFoundMenu()
        nothing, orderNumber = self.__orderService.getAllOrders()
        rentOutCar, returnCar, rentOutCarTime, returnCarTime = self.__orderService.checkValidDate(True)
        self.pressAnyKeyToContinue
        rentCost, carType = self.selectCarType()
        #calculate direct costs
        carCost, totalDaysRented = self.getCostOfOrder(rentOutCarTime, returnCarTime, rentCost)
        #Add insurance
        totalCost, insurance = self.addInsurance(carCost)
        #Time of order
        stringTimeOforder, timeOfOrder = self.getTimeOfOrder()
        # Print out order
        # self.displayAllOrdersHeaderPrint()
        order = Order(orderNumber, name, carType, stringTimeOforder, rentOutCar, returnCar, totalCost, ssn)
        self.displayOrderInfo(order, insurance, totalDaysRented, carCost, rentOutCarTime, returnCarTime, timeOfOrder)  
        self.finalStepOrder(order)
        return 

    def displayAllOrders(self, orders):
        self.displayAllOrdersHeaderPrint()
        for order in orders:
            print(order) 
            #menu? 

    def returnCarPrint(self):
        print(Colors.GREEN+"Car has successfully been returned"+Colors.END)

    def returnCarAdditionalPricePrint(self,price):
        print("Additional price to be paid for late delivery: {} ISK".format(price))
    
    def returnCarAdditionalPrice(self, returnTimeDifference, searchedCar):
        hourPrice = int(searchedCar.getRentcost())/24*1.25
        hours = returnTimeDifference.seconds / 60 / 60
        price = hours * hourPrice
        self.returnCarAdditionalPricePrint(int(price))
    
    def returnCar(self):
        licenseplate = self.__carService.checkLicenseplate(False)
        self.printReturnMenu()
        action = input("Choose action: ")#error check
        if action == '0':
            self.returnCar()
        elif action == '1':
            timeOfReturn = self.__orderService.checkValidDate()
            timeOfreturnInputTimeFormat = self.__orderService.createDate(timeOfReturn)
            searchedCar = self.__carService.findCar(licenseplate, timeOfReturn)
            returnTimeDifference = timeOfreturnInputTimeFormat - searchedCar.getReturnCar()

            if returnTimeDifference.seconds > 0:
                self.returnCarAdditionalPrice(returnTimeDifference, searchedCar)
            self.returnCarPrint()

    '''--------------------------ORDER PRINT FUNCTIONS--------------------------'''
    def rentOutToCustomerPrintMenu(self):
        self.actionsPrint()
        print(Colors.WHITE+"0. Go back to main menu")
        print("1. Select customer"+Colors.END)

    def customerNotFoundPrintMenu(self):
        self.actionsPrint()
        print(Colors.WHITE+"0. Go back to main menu")
        print("1. Search again"+Colors.END)

    def rentOutToCustomerPrintMenu(self):
        self.actionsPrint()
        print(Colors.WHITE+"0. Go back to main menu")
        print("1. Select customer")

    def customerNotFoundPrintMenu(self):
        self.actionsPrint()
        print(Colors.WHITE+"0. Go back to main menu")
        print("1. Search again"+Colors.END)

    def selectCarTypePrintMenu(self):
        self.actionsPrint()
        print(Colors.WHITE+"0. <-- Go back")
        print("1. Compact")
        print("2. Comfort")
        print("3. CUV")
        print("4. Highland")
        print("5. Luxury"+Colors.END)

    def addInsurancePrint(self):
        self.actionsPrint()
        print(Colors.WHITE+"1. Add SCDW(Includes):\n\t{0}\n\t{1}\n\t{2}\n\t{3}".format("-Front window","-Sandstorm","-Chassis", "-Theft insurance"))
        print("2. No additional insurance"+Colors.END)

    def areYouSurePrint(self):
        print(Colors.WHITE+"\nAre you sure?")
        print("1. Yes")
        print("2. No, go back"+Colors.END)

    def finalStepOrderPrint(self):
        self.actionsPrint()
        print(Colors.GREEN+"1. Save and complete order")
        print(Colors.RED+"2. Cancel order"+Colors.END)

    def displayAllOrdersHeaderPrint(self):
        LINE = '---------------'
        print("\n{:15} {:15} {:15} {:15} {:17} {:17} {:17} {:15}".format('Order number', 'Customer', 'SSN', 'Car Type',\
        'Time of order', 'Start of order','End of order','Rent cost'))
        print("{:15} {:15} {:15} {:15} {:17} {:17} {:17} {:15}".format(LINE, LINE, LINE, LINE, LINE, LINE, LINE, LINE))

    def displayOrderInfo(self,order, insurance, totalDaysRented, carCost, rentOutCarTime, returnCarTime, timeOfOrder):
        print("\n-------------------------------------------------- Order Info --------------------------------------------------\n")
        print("Order Number: {}".format(order.getOrderNumber()))
        print("{} | {}".format(order.getCustomer(), order.getSSN()))
        print("Car type rented: {} | from: {} To: {} | Date rented: {}".format(order.getCarType(), rentOutCarTime, \
        returnCarTime, timeOfOrder))
        print("\nCost of {} days without VAT: {} ISK".format(totalDaysRented, carCost))
        if insurance != 0:
            print("Extra insurance: {} ISK".format(insurance))
            print("\nTotal cost of {} days without VAT: {} ISK".format(totalDaysRented, order.getRentCost()))

    def searchCustomerForCarRentalHeaderPrint(self):
        print("--------------------- Find customer for car rental ---------------------")
    
    def editOrderInfoMenu(self):
        self.actionsPrint()
        print(Colors.WHITE+"0. Go back")
        print("1. "+Colors.END)
        #edit time of order, cancel, add/discard insurance, 

    def editCar(self):
        self.editCarInfoMenu()
        print("----------------Return a Car----------------")

    def printReturnMenu(self):
        self.actionsPrint()
        print(Colors.WHITE+"0. Go back")
        print("1. Return selected car"+Colors.END)

    def listofOrdersMenu(self):
        self.actionsPrint()
        print(Colors.WHITE+"0. Go back")
        print("1. Search for an order by order number"+Colors.END)