class Order:
	name="";
	phno="";
	adress="";
	totalamt = 0;
	isdelivered=False;
	small=[]
	medium = []
	large = []
	1
	def getName(self):
		return self.name;
		
	def setName(self, name):
		self.name = name;
	
	def getPhno(self):
		return self.phno;
		
	def setPhno(self, phno):
		self.phno = phno;
	
	def getAdress(self):
		return self.adress;
		
	def setAdress(self, adress):
		self.adress = adress;

	def getTotalamt(self):
		return self.totalamt;
		
	def setTotalamt(self, totalamt):
		self.totalamt = totalamt;

	def isIsdelivered(self):
		return self.isdelivered;
		
	def setIsdelivered(self, isdelivered):
		self.isdelivered = isdelivered;

	def getSmall(self):
		return self.small;

	def setSmall(self, small):
		self.small = small;

	def getMedium(self):
		return self.medium;
		
	def setMedium(self, medium):
		self.medium = medium;

	def getLarge(self):
		return self.large;
		
	def setLarge(self, large):
		self.large = large;


class Smallpizza:
  c=0;
  to=[];
  amt=[];
  amount=0;
    
  def pizzaorder(self):
    self.to.append("A Small Pizza with toppings: Tomato ,  Cheese ");
    print("We provide tomato base by default with cheese toppings for free");
        
    a=True;
    while(a):

      print("Do you want to append more toppings ? Press '1' else Press '2'");
          
      ch=int(input());

      if(self.c>3):
          print("Cant append more than 4 toppings");
          break;
	        
      if(ch==1):
        print("Extra toppings:");
        print("1. Bacons");
        print("2. Olives");
        print("3. Ham");
        print("4. Mushrooms");
        print("5. Pineapple");
        print("6. Salami");
        print("7. Anchovies");
        top=int(input());
        
        if(top==1):
          self.to.append(" Bacons ");
          self.c+=1;
                
        elif(top==2):
          self.to.append(" Olives ");
          self.c+=1;
              
        elif(top==3):
          self.to.append(" Ham ");
          self.c+=1;
              
        elif(top==4):
          self.to.append(" Mushrooms ");
          self.c+=1;
              
        elif(top==5):
          self.to.append(" Pineapple ");
          self.c+=1;
            
        elif(top==6):
          self.to.append(" Salami ");
          self.c+=1;
              
        elif(top==7):
          self.to.append(" Anchoives ");
          self.c+=1;
			        
      elif(ch==2):
        a=False;
            
    self.amt.append(self.c+5);
    self.amount=self.c+5;
    
  def getCost(self):
    return self.amount;

  def getToppings(self):
    return self.to;
      
  def getAmount(self):
    return self.amt;


class Mediumpizza:
  amount1=0;
  c=0;
	
	#static
  to1 = [];
  amt1 = [];
	
  def pizzaorder1(self):
    self.to1.append("A Medium pizza with toppings: Tomato , Cheese ");
    print("We provide tomato base by default with cheese toppings for free");
    
    a=True;
    while(a):
      print("Do you want to append more toppings ? Press '1' else Press '2'");
      ch=int(input());
		  
      if(self.c>3):
          print("Cant append more than 4 toppings");
          break;

      if(ch==1):
        print("Extra toppings:");
        print("1. Bacons");
        print("2. Olives");
        print("3. Ham");
        print("4. Mushrooms");
        print("5. Pineapple");
        print("6. Salami");
        print("7. Anchovies");
        top=int(input());
        
        if(top==1):
          self.to1.append(" Bacons ");
          self.c+=1;
          
        elif(top==2):
          self.to1.append(" Olives ");
          self.c+=1;
          
        elif(top==3):
          self.to1.append(" Ham ");
          self.c+=1;
          
        elif(top==4):
          self.to1.append(" Mushrooms ");
          self.c+=1;
          
        elif(top==5):
          self.to1.append(" Pineapple ");
          self.c+=1;
          
        elif(top==6):
          self.to1.append(" Salami ");
          self.c+=1;
          
        elif(top==7):
          self.to1.apend(" Anchoives ");
          self.c+=1;
          
        
          
      elif(ch==2):
        a=False;
        
    self.amt1.append(self.c+8);
    self.amount1=self.c+8;
    
  def getCost1(self):
    return self.amount1;
    
  def getToppings1(self):
    return self.to1;
    
  def getAmount1(self):
    return self.amt1;

class Largepizza:
  amount2=0
  c=0;
	
	#static
  to2=[];
  amt2=[];
  
  def pizzaorder2(self):
    self.to2.append("A Large Pizza with toppings: Tomato , Cheese ");
    print("We provide tomato base by default with cheese toppings for free");
    a=True;

    while(a):
      print("Do you want to append more toppings ? Press '1' else Press '2'");
      
      ch=int(input());
      
      if(self.c>3):
          print("Cant add more than 4 toppings");
          break;
      
      if(ch==1):
        print("Extra toppings:");
        print("1. Bacons");
        print("2. Olives");
        print("3. Ham");
        print("4. Mushrooms");
        print("5. Pineapple");
        print("6. Salami");
        print("7. Anchovies");
        top=int(input());
        
        if(top==1):
          self.to2.append(" Bacons ");
          self.c+=1;
          
        elif(top==2):
          self.to2.append(" Olives ");
          self.c+=1;
          
        elif(top==3):
          self.to2.append(" Ham ");
          self.c+=1;
          
        elif(top==4):
          self.to2.append(" Mushrooms ");
          self.c+=1;
          
        elif(top==5):
          self.to2.append(" Pineapple ");
          self.c+=1;
          
        elif(top==6):
          self.to2.append(" Salami ");
          self.c+=1;
          
        elif(top==7):
          self.to2.append(" Anchoives ");
          self.c+=1;
          
        
          
      elif(ch==2):
        a=False
        
    self.amt2.append(self.c+12);
    self.amount2=self.c+12;
    
  def getCost2(self):
    return self.amount2;
    
  def getToppings2(self):
    return self.to2;
    
  def getAmount2(self):
    return self.amt2;


class BookPizza:
  price = 0;
  a1 = 0;
  a2 = 0;
  a3 = 0;
  ob = Order();
  
  def calculate(self):
    a = True;
    while (a):
      print("Enter your Choice");
      print("1.---> For Small pizza");
      print("2.---> For Medium pizza");
      print("3.---> For Large pizza");
      print("4.---> Calculate bill");
      choice = int(input());
			
      if choice==1:
        p=Smallpizza();
        p.pizzaorder();
        self.ob.getSmall().append(p);
        self.price += p.getCost();
			
      elif choice==2:
        pa = Mediumpizza();
        pa.pizzaorder1();
        self.ob.getMedium().append(pa);
        self.price += pa.getCost1();
			
      elif choice==3:
        p1 = Largepizza();
        p1.pizzaorder2();
        self.ob.getLarge().append(p1);
        self.price += p1.getCost2();
			
      elif choice==4:
        print("Enter Name :");
        na = input();
        self.ob.setName(na);
				
        print("Enter Phone number :");
        ph = input();
        self.ob.setPhno(ph);
        
        print("Click '1' to Collect or '2' to get Delivered");
        chr = int(input());
        
        if(chr == 2):
          self.ob.setIsdelivered(True);
          print("Enter address :");
          ad = input();
          self.ob.setAdress(ad);
					
          if(self.price < 30):
            self.price += 8;
				
        self.ob.setTotalamt(self.price);
        print("------------ORDER ACCEPTED----------------");
        
        print("Name:",na);
        print("Phone number:",ph);
        
        if(chr==2):
          print("appendress:",ad);
        
        print("Orders: ");
			
        for small in self.ob.getSmall():
          print(small.getToppings());
          print("Cost: ",small.getCost());
          
        for medium in self.ob.getMedium():
          print(medium.getToppings1());
          print("Cost: ",medium.getCost1());
          
        for large in self.ob.getLarge():
          print(large.getToppings2());
          print("Cost: ",large.getCost2());
				
        print("Total Amount to be paid:", self.ob.getTotalamt());
        print();
        
        if(chr==2):
          print("Order To be delivered");
        elif(chr==1):
          print("Order to be collected");
			    
        print("------------------------------------------");
        a=False;
			
      else:
        print("Wrong choice");
        
  def getOb(self):
    return self.ob;
    
  def setOb(self, ob):
    self.ob = ob;
	
def takeOrder():
  q=0;
  orders=[];
  print("  ******************WELCOME TO PIZZA PARADISE******************");
  print("------------------------------------------------------------------");
  print(" Small PIZZA : $5      Medium PIZZA : $8         Large PIZZA : $12");
  print("------------------------------------------------------------------");
  print("Each topping costs : $1                 Delivery less than $30: $8");
  print("------------------------------------------------------------------");
  print();
  
  a = 0;
  while (True):
    print("1. -->  Order Pizza");
    print("2. -->  View Orders");
    print("0. -->  To exit");
    take = int(input());
    
    if take==1:
      b = BookPizza();
      b.calculate();
      orders.append(b.getOb());
      a+=1;
		
    elif take==2:
      print("--------------ORDER HISTORY-------------------------");
			
      for order in orders:
        print("ORDER ID :",(q+1));
        print("----------------------------------------");
        print("Name :",order.getName());
        print("Phone no. :",order.getPhno());
				
        if(order.isIsdelivered()):
          print("address :",order.getAdress());
				
        print();
        for small in order.getSmall():
          print("Cost: ",small.getToppings());
				
        for medium in order.getMedium():
          print("Cost: ",medium.getToppings1());
				
        for large in order.getLarge():
          print("Cost: ",large.getToppings2());
				
        print("Total Amount paid:",order.getTotalamt());
        print("---------------------------------------------------");
        print();
        q+=1;
		
    else:
      print("Thank You. You are now Logged Out");
      break;

takeOrder();
