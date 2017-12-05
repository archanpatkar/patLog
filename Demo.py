from patlog.Logger import Logger
from patlog.Factory import LogFactory

class PiggyBank:
   def __init__(self,logger):
       self.logger = logger
       self.logger.log("INFO","Entering __init__ of PiggyBank")
       self.balance = 0
       self.lt = 0
       self.logger.log("INFO","Created an Instance of PiggyBank")
       self.logger.log("INFO","Leaving __init__ of PiggyBank")

   def deposit(self,v):
       self.logger.log("INFO","Entering Deposit")
       self.logger.log("INFO","v = {}".format(v))
       if v > 0:
           self.logger.log("INFO","v > 0 == true")
           self.balance += v
           lt = v
           self.logger.log("INFO","Updated Balance and LT")
       self.logger.log("INFO","Leaving Deposit")

   def withdraw(self,v):
       self.logger.log("INFO","Entering Withdraw")
       self.logger.log("INFO","v = {}".format(v))
       if v > 0 and v <= self.balance:
           self.logger.log("INFO","v > 0 == true && v <= {}".format(self.balance))
           self.balance -= v
           lt = -v
           self.logger.log("INFO","Updated Balance and LT")
       self.logger.log("INFO","Leaving Withdraw")

   def statment(self):
       self.logger.log("INFO","Entering Statment")
       print("Balance = {}".format(self.balance))
       print("Last Transaction = {}".format(self.balance))
       self.logger.log("INFO","Leaving Statment")



pg1 = PiggyBank(LogFactory.getFileLogger("./p1.log"))

pg1.deposit(100)
pg1.deposit(75)
pg1.deposit(150)

pg1.statment()

pg1.withdraw(50)
pg1.withdraw(80)

pg1.statment()


pg2 = PiggyBank(LogFactory.getConsoleLogger())

pg2.deposit(1000)
pg2.deposit(754)
pg2.deposit(553)

pg2.statment()

pg2.withdraw(550)
pg2.withdraw(890)

pg2.statment()
