from item import Item

class Phone(Item):
    pay_rate=0.5
    
    def __init__(self,name:str,price:float,quantity=0,broken_phones=0):
        # Call to super function to have access to all attributes/methods
        super().__init__(
            name,price,quantity
        )
        
        # Run validations to the received arguments
        assert price>=0,f"Price {price} is not greater than or equal to zero.."
        assert quantity>=0,f"Quantity {quantity} is not greater than or equal to zero.."
        assert broken_phones>=0,f"Broken phones {broken_phones} is not greater than or equal to zero.."

        # Assign to self objects (these are instance attribute)
        self.broken_phones=broken_phones