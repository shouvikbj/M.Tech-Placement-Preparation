from item import Item
from phone import Phone

item1=Item("Mouse",50,9)
print(item1.calculate_total_price())
phone1=Phone("jscPhoneV10",500,5,1)
print(phone1.calculate_total_price())
phone2=Phone("jscPhoneV20",700,5,1)
print(phone2.calculate_total_price())

print(Item.all)
print(Phone.all)

Item.instantiate_from_csv()
print(Item.all)

some_item=Item("MyItem",750)
print(some_item.name)

some_item.name="OtherItem" # this operation is not allowed if a 'setter' is not defined..
print(some_item.name)

some_item.name="ThisIsaVeryLongName" # this operation is not allowed if a 'setter' is not defined..
print(some_item.name)