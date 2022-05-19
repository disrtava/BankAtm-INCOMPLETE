class atm(object):
    def __init__(self,cardno,pinno,cash,withdrawlMoney):
        self.cardno = cardno
        self.pinno = pinno
        self.cash = cash 
        self.withdrawlMoney = withdrawlMoney
    

    def navigation(self):
        navigationinput =int(input("If you want to withdraw cash enter 1, if you want to check your balance enter 2, if you want to add cash enter 3 "))
        if(navigationinput == 1):
            self.cashWithdrawl()
        elif(navigationinput == 2):
            self.balanceEnquiry()
        elif(navigationinput == 3):
            self.addToBalance()

    def cashWithdrawl(self,cash):
        input("Enter your atm card no.")
        input("Enter your pin no.")
        withdrawlMoney = int(input("Enter the amoutn you want to withdraw"))
        cash = cash - withdrawlMoney

    def balanceEnquiry(self,cash):
        input("Enter your atm card no.")
        input("Enter your pin no.")
        print("Your balance is :- ",cash)

    def addToBalance(self,cash):
        input("Enter your atm card no.")
        input("Enter your pin no.")
        moneyAdded = int(input("Enter the amount you want to add"))
        cash = cash + moneyAdded

