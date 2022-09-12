import csv

class Item:
    # This is a class attribute
    pay_rate=0.8 # The pay rate after 20% discount
    all=[]

    def __init__(self,name:str,price:float,quantity=0):
        # Run validations to the received arguments
        assert price>=0,f"Price {price} is not greater than or equal to zero.."
        assert quantity>=0,f"Quantity {quantity} is not greater than or equal to zero.."

        # Assign to self objects (these are instance attribute)
        self.__name=name
        self.__price=price
        self.quantity=quantity

        # Actions to execute
        Item.all.append(self)
    
    @property # @property decorator == Read-Only Attribute || This is 'getter' in python
    def name(self):
        # print("You are trying to access a read-only variable 'name'...")
        return self.__name
    
    @name.setter # This is 'setter' in python
    def name(self, value):
        # print("Setter accessed to change the read-only variable 'name'...")
        if len(value)>10:
            raise Exception(f"The name '{value}' is too long!")
        else:
            self.__name=value
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        self.__price==value

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"

    def calculate_total_price(self):
        return self.__price*self.quantity
    
    def apply_discount(self):
        self.__price=self.__price*self.pay_rate
    
    def apply_increment(self,increment_value):
        self.__price=self.__price+self.__price*increment_value
    
    # Will be fetching data from a csv file
    # this method will be a class method
    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv","r") as f:
            reader=csv.DictReader(f)
            items=list(reader)
        for item in items:
            Item(
                name=item.get("name"),
                price=float(item.get("price")),
                quantity=int(item.get("quantity"))
            )
    
    # Will be checking if a received number is an integer or not
    # this method will be a static method
    @staticmethod
    def is_integer(num):
        # we will count out the floats that are point zero
        # For i.e.: 5.0, 10.0
        if isinstance(num,float):
            # Count otu the floats that are point zero
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False

    # below codes are just a simulation, not actual working codes
    # This is just an example of abstruction
    
    def __connect(self, smtp_server): # this is a private method and can only be accessed within the class
        pass
    
    def __prepare_body(self):
        return f"""
        Hello Someone.
        Wwe have {self.name} {self.quantity} times.
        Regards, ShouvikBajpayee
        """
    
    def __send(self):
        pass
    
    def send_email(self):
        self.__connect("smtp_server")
        self.__prepare_body()
        self.__send()
        print("Email sent!")
        