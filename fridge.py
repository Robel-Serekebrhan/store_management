from store_management import items
#child class( needed as all the items are not nessarity to have same attribute and methods to execute)
class fridge(items):
        def __init__(self, item_code, item_name, description, buying_price, quantity, selling_price=0, defected_qty=1):
                #call to supper funtion to have acess to all atributes and methods of the parent class item
                super().__init__(item_code, item_name, description, buying_price, quantity, selling_price=0)

                #run validation to the argument created in this class only the rest will inhrited from the parent
                assert defected_qty >= 0, f"defected_qty{defected_qty} is not less than zero"


                #attribute to assign to the self object

                self.defected_qty = defected_qty
                self.net_quantiy = net_quantity


        def net_quantiy():

            self.net_quantity=items.quantiy - self.defected_qty

    



fridge.net_quantiy
        