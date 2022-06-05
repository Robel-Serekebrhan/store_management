
import csv
class items:
         pay_rate = 0.8  # class attribute
         profit_margin = 3.2 # class attribute
         All = []
         
        # is called special funtion or magic methood and is used to initialize all the attributes of the innstances(objects)    
         def __init__(self, item_code, item_name, description, buying_price, quantity, selling_price=0): 
        
                # validate the data inputed  
                assert buying_price >= 0, f"buying_price{buying_price} can not be negative"
                assert quantity >= 0, f"quantity{quantity} can not be less than zero"

                # attributes for every created instance(object)
                self.item_code = item_code
                self.item_name =  item_name
                #self.phoeto = phoeto
                self.description = description
                self.buying_price = buying_price
                self.quantity = quantity
                self.selling_price = self.buying_price * items.profit_margin
              


        

        # to see all the attribute that bellong to the class or object using the magic attribute(not majic method) .__dict__
        #print(items.__dict__)
        #print(item1.__dict__)
                
         
        # add our instances to the empty list we name it All
                items.All.append(self)


        
        # an instance method to appy a discount from he payrate given as attribute of instance first if not found from attribute of class
         def apply_discount(self):
                 self.selling_price = self.selling_price * self.pay_rate



         #def selling_price():
                 #self.selling_price = self.buying_price * items.profit_margin

        
        
        # automate instantiating by reading from csv usig class method
                                                                                            
         @classmethod
         def ins_csv(cls):
                 with open('/home/robel/oop/storemanagement/Untitled.csv', 'r') as f:
                         reader = csv.DictReader(f)
                         items_list = list(reader)


                 for item in items_list:
                         items(
                                  item_code=item.get('item_code'),
                                  item_name=item.get('item_name'),
                                  description=item.get('description'),
                                  buying_price=float(item.get('buying_price')), 
                                  quantity=int(item.get('quantity'))    
                                )       
                                

        #static method

        #lets use the repr magic method to format all our instances in the All list in the way we insanciate our instances

         def __repr__(self):
                 return f"items('{self.item_code}', '{self.item_name}','{self.description}', {self.buying_price}', '{self.quantity}', '{self.selling_price}' )"


items.ins_csv()
print(items.All)


