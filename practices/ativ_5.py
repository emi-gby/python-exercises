from collections import Counter, defaultdict, namedtuple

def grade_greater7():
    dic_list = [{'Caio':3,},{'Jonas':7},{'Raeia':8}]
    for d in dic_list:
        for k, v in d.items():
            if v >= 7:
                print(k)

def word_count():
    phrase = "the house is yellow and the door of the house is brown"
    count_dic = {}
    for word in phrase.split():
        count_dic[word] = count_dic.get(word, 0) + 1
    print(count_dic)


def friends():
    work_friends = {"Ana", "Bruno", "Carlos"}
    college_friends = {"Ana", "Daniel", "Eva"}
    # All friends (union)
    print(f'Union: {list(work_friends | college_friends)}')
    # Friends from both groups (intersection)
    print(f'Intersection: {list(work_friends & college_friends)}')
    # Friends only from work (difference)
    print(f'Difference: {list(work_friends - college_friends)}')

def greater_smaller(lista):
    if not lista:   #error prevention
        print('Empty List')
        return
    greater_number, smaller_number = lista[0], lista[0]
    for num in lista[:1]:
        if num > greater_number:
            greater_number = num
        elif num < smaller_number:
            smaller_number = num
    print((greater_number,smaller_number))

def product_registry():
    """
    Product registration and consultation system with error handling.
    """
    products_dic = {}
    while True:
        user_response = input('1.Add new product\n 2.Check price\n q.Exit \nChoose an option : ').strip().lower()
        if user_response == '1':
            product = input('Enter the product name : ').strip().capitalize()
            price_str = input('Enter the product price : ').strip().replace(',','.')
            try:
                price = float(price_str)
                products_dic[product] = price
            except ValueError:
                print('Invalid price. Please enter a valid number.')
        elif user_response == '2':
            if not products_dic:
                print('No product registered yet.')
                continue
            print('Available products:', ', '.join(products_dic.keys()))
            query_product = input('Enter the name of a product : ').strip().capitalize()
            price = products_dic.get(query_product)
            if price is not None:
                print(f'Price - {query_product}: $ {price:.2f}')
            else:
                print(f'"{query_product}" is not in the product list.')
        elif user_response == 'q':
            print('Exiting the product registration system.')
            break
        else:
            print(f'Option "{user_response}" invalid. Try again.')


def total_sales():
    sales = [('productA', 10), ('productB', 5),('productA', 3), ('productB', 13)]
    result_dic = defaultdict(int)
    for product, quantity in sales:
        result_dic[product] += quantity
    print(dict(result_dic))


def tuple_config():
    # Defining the immutable configuration structure
    Configuration = namedtuple('Configuration', ['database_host', 'port', 'user'])

    # Creating the configuration
    config = Configuration(database_host="localhost", port=5432, user="admin")

    # Accessing the port value
    print(config.port)  # Output: 5432

def add_edge(v1, v2):
    graph = [{'a','b'},{'c','d'},{'d','e'}]
    if {v1,v2} not in graph:
        graph.append({v1,v2})
        print(graph)
    else:
        print('Edge already exists in the graph.')
