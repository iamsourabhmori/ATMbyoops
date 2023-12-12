
class Bank:
    def __init__(self,name,bname,pin,bal):
        self.name = name
        self.bname = bname
        # self.kppin = kppin
        # self.spin = spin
        self.pin= pin
        self.bal= bal
      
    def deposite(self,bal):
            deb = int(input("How Much Amount you want to Deposite   : "))                         
            self.a = self.bal + deb
            self.bal = self.a
            print("Balance after debit : ",  self.bal) 
            return  self.bal
        
    def withdrawal(self,bal):
            cre = int(input("How Much Amount you want to Withdrawl : "))                              
            self.b = self.bal - cre
            self.bal = self.b
            print("Balance after withdrawal : ",self.bal)
            return self.bal    

with open("Kppin.txt", "r") as f:
   pin = f.read()
   kppin = int(pin)
   f.close()

with open("KpBalance.txt", "r") as f:
   kpfbal = f.read()
   kpbal = int(kpfbal)
   f.close()

with open("Sourabhpin.txt", "r") as f:
   pin = f.read()
   spin = int(pin)
   f.close()

with open("SourabhBalance.txt", "r") as f:
   sfbal = f.read()
   Sbal = int(sfbal)
   f.close()

while True:  
                  
        kapil = Bank("Kapil","SBI", kppin,kpbal)
        sourabh = Bank("Sourabh","PNB",spin,Sbal)
       
        try:
            with open("Kppin.txt", "r") as f:
               pin = f.read()
               kppin = int(pin)
               f.close()

            with open("Sourabhpin.txt", "r") as f:
               pin = f.read()
               spin = int(pin)
               f.close()
            
        
            user_pin = int(input("Enter your pin : "))
            if user_pin == kppin : 
                   print("Welcom kapil")
                   print("Your Balance is : ",kpbal)
                   print("your Bank is : ",kapil.bname)
                   
                   
                   while True:  
                       
                      
                       choice = int(input("Choose Operations: 1)Deposit 2)Withdrawl 3)Check Balance 4)change Pin 5)Exit"))
                                    
                       if choice == 1:
                             
                             kapil.bal = kapil.deposite(kpbal)
                             with open("KpBalance.txt", "w") as f:
                                kpfbal = f.write(str(kapil.bal))
                                f.close()
                                   
                       elif choice == 2 :
                              
                             kapil.bal = kapil.withdrawal(kpbal)
                             with open("KpBalance.txt", "w") as f:
                                kpfbal = f.write(str(kapil.bal))
                                f.close()
                        
                       elif choice == 3 :
                           with open("KpBalance.txt", "r") as f:
                               kpfbal = f.read()
                               kpbal = int(kpfbal)
                               f.close()
                                                   
                           print("Remaining Balance: ", kpbal)
                           
                       
                       elif choice == 4 :
                            pin = input("Enter your New Pin :")
                            with open("Kppin.txt","w") as f: 
                                kpin = f.write(pin)
                                f.close()
                                print("your pin has been successfully changed !")
                            break
                
                       elif choice == 5 :
                            
                            break
        
                       else:
                            print("Please Enter the Valid Choice !!!")
                
            elif user_pin ==  spin :
                
                   print("Welcom Sourabh")
                   print("Your Balance is : ",Sbal)
                   print("your Bank is : ",sourabh.bname)
                   
                   while True:
                       
                       choice = int(input("Choose Operations: 1)Deposit 2)Withdrawl 3)Check Balance 4)change Pin 5)Exit"))
                       if choice == 1:
                              sourabh.bal = sourabh.deposite(Sbal)
                              with open("SourabhBalance.txt", "w") as f:
                                  sfbal = f.write(str(sourabh.bal))
                                  f.close()                     
                       elif choice == 2 :
                              sourabh.bal = sourabh.withdrawal(Sbal)
                              with open("SourabhBalance.txt", "w") as f:
                                  sfbal = f.write(str(sourabh.bal))
                                  f.close()             
                                                          
                       elif choice == 3 :
                            with open("SourabhBalance.txt", "r") as f:
                               sfbal = f.read()
                               Sbal = int(sfbal)
                               f.close()
                            print("Remaining Balance: ", Sbal)    
        
                    
                       elif choice == 4 :
                            pin = input("Enter your New Pin :")
                            with open("Sourabhpin.txt","w") as f: 
                                smpin = f.write(pin)
                                f.close()
                                print("your pin has been successfully changed !")
                            break
                           
                       elif choice == 5 :
                            
                            break
        
                       else:
                            print("Please Enter the Valid Choice !!!")
        
                
            else:
                print("Please Enter the Correct Pin !!!")

        except Exception as e:
                # print(str(e))
                print(e)
                print("characters and special symbols are not allowed")
# bal = int(input("Enter your balance :"))
# kapil = Bank("Kapil","SBI", kpin,bal)

# sourabh = Bank("Sourabh","PNB",spin,bal)
# kapil.Getinfo()




