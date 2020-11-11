class Product:
    def __init__(self, id, title, rating, price, prod_cost, discount_price, description, image, category, brand=None, color=None):
        self.__id = id
        self.title = title
        self.rating = rating
        self.__price = price
        self.__prod_cost = prod_cost
        self.discount_price = price
        self.description = description
        self.image = image
        self.category = category
        self.brand = brand
        self.color = color
    
    def get_id(self):
        return self.__id
    
    def get_price(self):
        return self.__price
    
    def set_price(self, x):
        self.__price = x 
    
    def get_prod_cost(self):
        return self.__prod_cost
    
    def set_prod_cost(self, x):
        self.__prod_cost = x

    def set_discount_price(self, disc_type, disc_value):
        if disc_type == 'faiz':
            self.discount_price = self.get_price() - (self.price * disc_value) // 100
        elif disc_type == 'vahid':
            self.discount_price = self.get_price() - disc_value
        else:
            print('Parametrler duzgun daxil edilmeyib')
            return

    def get_name(self):
        return f'Mehsulun adi: {self.title}'



class Book(Product):
    def __init__(self, id, title, rating, price, prod_cost, discount_price, description, image, category, language, author, published_at, genre, page_count, publisher):
        super().__init__(id, title, rating, price, prod_cost, discount_price, description, image, category)
        self.language = language
        self.author = author
        self.published_at = published_at
        self.page_count = page_count
        self.genre = genre
        self.publisher = publisher

    def get_name(self):
        return f'Kitabin adi: {self.title} | Kitabin yazari: {self.author}'

class Clothes(Product):
    def __init__(self, size, material, id, title, rating, price, prod_cost, discount_price, description, image, category, brand, color):
        super().__init__(id, title, rating, price, prod_cost, discount_price, description, image, category, brand, color)
        # self.brand = brand
        self.size = size
        self.material = material
    
    def get_name(self):
        return f'Paltarin adi: {self.title} | Paltarin rengi: {self.color}'

class Electronic(Product):
    def __init__(self, power, id, title, rating, price, prod_cost, discount_price, description, image, category, brand, color):
        super().__init__(id, title, rating, price, prod_cost, discount_price, description, image, category, brand, color)
        self.power = power
    
class Phone(Electronic):
    def __init__(self, battery_capacity, power, id, title, rating, price, prod_cost, discount_price, description, image, category, brand, color):
        super().__init__(id, power, title, rating, price, prod_cost, discount_price, description, image, category, brand, color)
        self.battery_capacity = battery_capacity

class Notebook(Electronic):
    def __init__(self, screen_size, power, id, title, rating, price, prod_cost, discount_price, description, image, category, brand, color):
        super().__init__(id, power, title, rating, price, prod_cost, discount_price, description, image, category, brand, color)
        self.screen_size = screen_size


#check Clothes class and methods
tshirt = Clothes('XL', 'cotton', 1, 'tshirt', 'higth', 150, 100, 120, 'higth quality', 'tshirt icon', 'for man', 'flo', 'red')

print(f'Clothes object Brand: {tshirt.brand}')

print(f'Clothes object Initial discount price: {tshirt.discount_price}')

tshirt.set_discount_price('vahid', 10)

print(f'Clothes object After calling set_discount_price method discount price: {tshirt.discount_price}')

print(f'Clothes object Initial product cost: {tshirt.get_prod_cost()}')

tshirt.set_prod_cost(110)

print(f'Clothes object Next product cost: {tshirt.get_prod_cost()}')

print(f'Clothes object get_name method {tshirt.get_name()}')

print('-----------------------------------------')
# Book class check
book1 = Book(2, 'Makr Tveyn', 'perfect', 20, 15, 18, 'description', 'first page image', 'reading', 'english', 'Check London', '20.10.2020', 'adventure', '357', 'Maarif Neshriyyati')

print(f'Book class object author: {book1.author}')
print(f'Book object get_name method {book1.get_name()}')

elektro1 = Electronic('220 Watt', 11, 'Uz Qirxan', 'middle', '250', '225', '249', 'description', 'simple image', 'home', 'Philips', 'gray')

print(f'Elektronic class object color: {elektro1.color}')
print(f'Elektronic object get_name method {elektro1.get_name()}')

print('-----------------------------------------')
# Phone class check
phone1 = Phone('4500mAH', '12 Watt', 13, 'Mi A2', 'lower', 350, 280, 349, 'Description', 'phone icon', 'prestige', 'Xioami', 'blue')

print(f'Phone class object battery_capacity: {phone1.battery_capacity}')
print(f'Phone object get_name method {phone1.get_name()}')

print('-----------------------------------------')
# Notebook class check
notebook1 = Notebook('15 duym', '220 Watt', 14, 'ProBook', 'lower', 950, 875, 949, 'Description', 'laptop icon', 'office', 'Dell', 'black')

print(f'Notebook class object screen_size: {notebook1.screen_size}')
print(f'Notebook object get_name method {notebook1.get_name()}')
