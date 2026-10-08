from time import sleep
title = 'NX\'S SHOP PRODUCT/PRICE LIST '
print(title.center(50))
price = [40.0 , 20.0 , 9.0]
product = ['Shoes' , 'Shirt' , 'Hat']
while True:
    print(' 1. Add \n 2. Read \n 3. Update \n 4. Delete \n 5. Search \n 6. Exit ')
    try:
        opt = int(input('Type your option: '))
    except ValueError:
        print('-'*20)
        print('Invalid option!')
        print('Try a number between [1 - 6]')
        print('-'*20)
        sleep(3)
        continue
    print('-'*20)
    if opt == 1:
        add_product = input('Add product: ').capitalize().strip()
        if not add_product:
            print('Product name cannot be empty!')
            sleep(3)
            continue
        try:
            product_price = float(input('Price: '))
        except ValueError:
            print('-'*20)
            print('Invalid input!')
            print('Please enter a valid product name and a numeric price.')
            print('-'*20)
            sleep(3)
            continue
        if product_price < 0:
            print('Price cannot be negative!')
            sleep(3)
            continue
        product.append(add_product)
        price.append(product_price)
        print('The product has been successfully added!')
        print('-'*20)
    elif opt == 2:
        for i in range(len(product)):
            print(f'{product[i]} - R$ {price[i]}')
        print('-'*20)
        sleep(3)
    elif opt == 3:
        for i in range(len(product)):
            print(f'{i} - {product[i]}')
        update_product = input('Product to be updated: ').capitalize().strip()
        if update_product not in product:
            print('This product couldn\'t be found.')
        else:
            try:    
                update_price = float(input('New price: '))
            except ValueError:
                print('Invalid price! Please enter a number.')
                continue
            if update_price < 0:
                print('Price cannot be negative!')
                continue
            search_product = product.index(update_product)
            price[search_product] = update_price
            print('-'*20)
            print('Your product has been successfully updated!')
        print('-'*20)
        sleep(2)
    elif opt == 4:
            print('NOTE: WHEN YOU REMOVE A PRODUCT, ITS PRICE IS ALSO REMOVED!')
            print('-'*20)
            sleep(2)
            print('[ Y / N ]')
            agree = input('I agree: ').lower().strip()
            if agree == 'y':
                for i in range(len(product)):
                    print(f'{i} - {product[i]}')
                print('Name of the product to be removed. Ex: 0 - Shoes')
                remove_name = input('Answer: ').capitalize().strip()
                if remove_name not in product:
                    print('This product couldn\'t be found.')
                else:
                    remove_product = product.index(remove_name)
                    product.pop(remove_product)
                    price.pop(remove_product)
                    print('-'*20)
                    print('Your product has been successfully removed!')
                sleep(1)
            elif agree == 'n':
                print('Denied!')
            else:
                print('Invalid option!')
            print('-'*20)
    elif opt == 5:
        item = input('Type the product you\'re searching for: ').capitalize().strip()
        if item in product:
            index_search = product.index(item)
            print(f'Product: {product[index_search]}')
            print(f'Price: R$ {price[index_search]:.2f}')
            print(f'Index: {index_search}')
            print('-'*20)
            sleep(1.5)
        else:
            print('Product couldn\'t be found!')
    elif opt == 6:
        print('Closing...')
        sleep(3)
        break
    print('Loading...')
    print('-'*20)
    sleep(1.5)