#The user will insert will insert the products that they have in their shopping basket along with their price. The program will then display all entered products in the order they were entered, with their prices. It will then add up the product price into a total price then also show how much VAT should is included in the total price and also display number of products.

# -----------PSUDECODE-----------
# 1. INSERT product name, item number and price.
# 2. ADD product prices into Total price.
# 3. Calculate 15% VAT of total price.
# 4. DISPLAY product number, Total price, VAT & and each entered product. 


numOfProducts = int(input('Enter number of products: '))
totalPrice = 0

product = []
price = [] 
itemCnt = []

for i in range(numOfProducts):

    print('\nyou are entering product number ' + str(i+1) + '\n')

    prod = input('Enter product name: ').upper()
    items = input('Enter item numbers: ')
    prodPrice = float(input('Enter product price: '))

    product.append(prod)
    price.append(prodPrice)
    itemCnt.append(items)

print('\n' +  '======= CUSTOMER TILL SLIP =======' + '\n')

print('Product' + '\t\t' + 'Items' + '\t\t' + 'Price\n')

for i in range(numOfProducts):
    print(product[i] + '\t\t' + str(itemCnt[i]) + '\t\t' + 'R' + str(price[i]))
    totalPrice += price[i]

vat = totalPrice * 0.15

print('\n''TOTAL PRICE' + '\t\t' + 'R' + str(totalPrice).expandtabs(4) + '\n' 'VAT (15%)' + '\t\t' + 'R' + str(round(vat, 2)))

print('\n' +  '======= END OF CUSTOMER TILL SLIP =======' + '\n' + 'thank you for choosing us'.center(38).upper())
