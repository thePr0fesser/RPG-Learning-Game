Items_for_Sale = {'Healing Potion':2,'Agility Potion':5,'Strength Potion':5,'Cunning Potion':5,'Courage Potion':5}
activecart = []

def List_Items():
  print("Here is what we have in stock!")
  for keys in Items_for_Sale:
    print("%s for sale at %d silver shillings"%(keys,Items_for_Sale[keys]))
  print()

def Add_Items_For_Sale():
  while True:
    print("Currently Expanding our Stock")
    newitem = input(">")
    if newitem == 'exit' or newitem == 'Exit':
      return
    newprice = input(">")
    try:
      newprice = int(newprice)
      if newprice < 1:
        print("Please input positive value")
      else:
        Items_for_Sale[newitem]=newprice
    except:
        print("please input postive value")
  print()

def Remove_Items():
  List_Items
  print("What Item Do You Wish to Remove? Type exit to finish")
  while True:
    removeitem = input(">")
    if removeitem == 'exit' or removeitem == 'Exit':
      return
    try:
      Items_for_Sale.pop(removeitem)
      print("Removed "+removeitem)
    except:
      print("No Item Found")
  print() 
  return

def Add_Item_to_Cart():
  while True:
    print("What would you like to purchase?")
    cartitem = input(">")
    if cartitem == 'exit' or cartitem == 'Exit':
      print(activecart)
      return
    for_sale = False
    for keys in Items_for_Sale:
      if cartitem == keys:
        for_sale = True
        activecart.append(cartitem)
        print("Added "+cartitem)
        break
      if for_sale == False:
        print("Item Not Found")
  print()
  return

def Remove_Item_From_Cart():
  while True:
    print("What would you like to remove?")
    print(activecart)
    cartitem = input(">")
    if cartitem == 'exit' or cartitem == 'Exit':
      print(activecart)
      return
    item_in_cart = False
    for item in activecart:
      if cartitem == item:
        item_in_cart = True
        activecart.remove(cartitem)
        print("Removed "+cartitem)
        break
    if item_in_cart == False:
      print("Item Not in Cart")
  print()
  return

def Remove_all():
  while True:
    print("Would you like to get rid of your cart? Y or N")
    deletecart = input(">")
    if deletecart == "Y" or deletecart == "y":
      activecart.clear()
      print("Cart has been cleared")
    elif deletecart == "N" or deletecart =="n":
      print("Then why did you pick this option")
      return
    else:
      print("Please select yes or no")

def Carts_Total():
  myrange = 0
  print("This is the total cost of the items in your cart")
  for item in activecart:
    for keys in Items_for_Sale:
      if item == keys:
        print('%s : %d silver shillings'%(keys, Items_for_Sale[keys]))
        myrange += Items_for_Sale[keys]
  print("Total: %d silver shillings"%myrange)
  return

def mainmenu():
  while True:
    print("Welcome to Wilhelm's Wondrous, Wild, and Weird Elixers!")
    print("1) List Items for Sale")
    print("2) Add Items for Sale")
    print("3) Remove Items for Sale")
    print("4) Add Item to Cart")
    print("5) Remove Item from Cart")
    print("6) Remove All Items from Cart")
    print("7) Cart's Total")
    print("8) Exit")
    menunum = input(">")
    if menunum == "1":
      List_Items()
    elif menunum == "2":
      Add_Items_For_Sale()
    elif menunum == "3":
      Remove_Items()
    elif menunum == "4":
      Add_Item_to_Cart()
    elif menunum == "5":
      Remove_Item_From_Cart()
    elif menunum == "6":
      Remove_all()
    elif menunum == "7":
      Carts_Total()
    elif menunum == "8":
      print("Thank you for shopping at Wilhelm's Wondrous, Wild, and Weird Elixers")
      exit()
    else:
      print("git gud skrub {0} ".format(menunum))
mainmenu()
