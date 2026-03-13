products = [{'code': 101, 'name': 'Rice', 'price': 7.99, 'quantity': 10},
            {'code': 102, 'name': 'Soda', 'price': 5.43, 'quantity': 4},
            {'code': 103, 'name': 'Orange', 'price': 1.23, 'quantity': 42}]

codes_set = set([item['code'] for item in products])

available_categories = ('Food', 'Drinks')

def register_product():
    '''Checks unique products, stores product in a dictionary and adds product to the product list.'''
    try:
        code = int(input('Enter the product code: '))
        if code in codes_set:
            print('-------------------------------')
            print('Code already used. Try again.')
            return

        name = input('Enter the product name: ').capitalize()
        price = float(input('Enter the product price: '))
        quantity = int(input('Enter the product quantity: '))

        codes_set.add(code)

        # add items to dictionary
        product_dict = {}
        product_dict['code'] = code
        product_dict['name'] = name
        product_dict['price'] = price
        product_dict['quantity'] = quantity

        # add dictionary to list
        products.append(product_dict)

        print('-------------------------------')
        print('Product registered successfully!')

    except ValueError:
        print('-------------------------------')
        print('Entered value does not match the expected data type!')

def list_products():
    '''Lists all products in dictionary format.'''
    for item in products:
        print(item)

def search_product():
    '''Defines the product code and prints its attributes if the entered value matches a product'''
    try:
        code = int(input('Enter the product code: '))
        for product_dict in products:
            if product_dict['code'] == code:
                print('-------------------------------')
                print('Product found. \nInformation: ')
                for k,v in product_dict.items():
                    print(f'{k} : {v}')
                return

        print('-------------------------------')
        print('Product not found.')

    except ValueError:
        print('-------------------------------')
        print('Entered value does not match the expected data type!')

def update_product():
    '''Updates product attributes according to the chosen option'''
    try:
        code = int(input('Enter the code of the product you want to update: '))
        for product_dict in products:
            if product_dict['code'] == code:
                update_option = input('Which option do you want to update (code, name, price, quantity) : ').lower()
                if update_option == 'code':
                    print(f'Current code : {product_dict["code"]}')
                    verify_update(product_dict)
                    return

                elif update_option == 'name':
                    print(f'Current name : {product_dict["name"]}')
                    new_value = input('Enter new value: ').capitalize()
                    product_dict['name'] = new_value

                    print('-------------------------------')
                    print('Update successful!')
                    return

                elif update_option in ('price', 'preco'):
                    print(f'Current price : {product_dict["price"]}')
                    try:
                        new_value = float(input('Enter new value: '))
                        product_dict['price'] = new_value
                        print('-------------------------------')
                        print('Update successful!')
                    except ValueError:
                        print('-------------------------------')
                        print('Entered value does not match the expected data type!')
                    return

                elif update_option =='quantity':
                    print(f'Current quantity : {product_dict["quantity"]}')
                    try:
                        new_value = int(input('Enter new value: '))
                        product_dict['quantity'] = new_value
                        print('-------------------------------')
                        print('Update successful!')
                    except ValueError:
                        print('-------------------------------')
                        print('Entered value does not match the expected data type!')
                    return

                else:
                    print('-------------------------------')
                    print('Option not available in the system!')
                    return

        print('-------------------------------')
        print('Product code not found.')

    except ValueError:
        print('-------------------------------')
        print('Entered value does not match the expected data type!')

def verify_update(product_dict):
    '''Checks for unique code items; if duplicate, it is not updated'''
    try:
        new_code = int(input('Enter new code: '))
        if new_code in codes_set:
            print('-------------------------------')
            print('Code already used. Try again.')
            return
        else:
            product_dict['code'] = new_code
    except ValueError:
        print('-------------------------------')
        print('Entered value does not match the expected data type!')
        return

    print('-------------------------------')
    print('Update successful!')

def delete_product():
    '''Removes product from the product list by code'''
    try:
        code = int(input('Enter the code of the product you want to delete: '))
        for product_dict in products:
            if product_dict['code'] == code:
                products.remove(product_dict)
                print('-------------------------------')
                print('Product removed successfully!')
                return

            print('-------------------------------')
            print('Product code not found.')

    except ValueError:
        print('-------------------------------')
        print('Entered value does not match the expected data type!')


while True:
    print('-------------------------------')
    print('1- Register a product')
    print('2- List products')
    print('3- Search product')
    print('4- Update product')
    print('5- Delete product')
    print('0- Exit')
    print('-------------------------------')

    option = input('Choose an option: ')

    print('-------------------------------')

    if option == '1':
        register_product()
    elif option == '2':
        list_products()
    elif option == '3':
        search_product()
    elif option == '4':
        update_product()
    elif option == '5':
        delete_product()
    elif option == '0':
        print('System terminated!')
        break
    else:
        print('Option not available in our system! Choose another:')
