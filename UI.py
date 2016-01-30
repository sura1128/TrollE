#User Interface

class UserInterface:

    def __init__(self, productList, controller):
        self._productList = productList


    def welcome(self):
        #set up controller here, get product list etc. 
        
        print("============================================")
        print("Hi. Welcome to Troll-E. Choose one of the following options to get started.")
        print("1. Budget Planning")
        print("2. Choose a Product!")
        print("3. Exit")
        action = input("Type 1, or 2. \n")
        if (action != 3 and action == 1 or action == 2):            
            self.chooseAction(action)
            action = input ("Your action is now completed. Type 5 to return to Menu.\n")
            if (action == 5):
                self.welcome()
            else:
                return
        else:
            print ("You have entered a wrong option. Please try again.")
            return
            

    def chooseAction(self, action):
        if (action==1):
            self.showBudgetPanel()
        elif(action==2):
            self.showProductPanel()
        else:
            return

    
    def showBudgetPanel(self):
        print("==================BUDGET PLANNING SYSTEM=================")
        print("Welcome to the Budget Planning System")
        print("=========================================================")
	print("What would you like to buy today?")

    def showProductPanel(self):
        print("PRODUCTS AVAILABLE")

ui = UserInterface({}, [])
ui.welcome()
