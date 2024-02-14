'''class LibraryItem:
    def _init_(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Publication Year: {self.publication_year}")

class Book(LibraryItem):
    def _init_(self, title, author, publication_year, isbn):
        super()._init_(title, author, publication_year)
        self.isbn = isbn

    def display_info(self):
        super().display_info()
        print(f"ISBN: {self.isbn}")

class Magazine(LibraryItem):
    def _init_(self, title, author, publication_year, issue_number):
        super()._init_(title, author, publication_year)
        self.issue_number = issue_number

    def display_info(self):
        super().display_info()
        print(f"Issue Number: {self.issue_number}")

class DVD(LibraryItem):
    def _init_(self, title, author, publication_year, duration):
        super()._init_(title, author, publication_year)
        self.duration = duration

    def display_info(self):
        super().display_info()
        print(f"Duration: {self.duration} minutes")

# Creating instances of the subclasses
book = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "978-3-16-148410-0")
magazine = Magazine("National Geographic", "National Geographic Society", 1888, "August 2023")
dvd = DVD("Inception", "Christopher Nolan", 2010, 148)

# Displaying information using the display_info() method
print("Book Information:")
book.display_info()
print("\nMagazine Information:")
magazine.display_info()
print("\nDVD Information:")
dvd.display_info()

'''



class Product:
    def _init_(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_cost(self):
        return self.price * self.quantity

class PhysicalProduct(Product):
    def _init_(self, name, price, quantity, weight):
        super()._init_(name, price, quantity)
        self.weight = weight

    def calculate_total_cost(self, shipping_cost_per_kg):
        product_cost = super().calculate_total_cost()
        shipping_cost = shipping_cost_per_kg * self.weight
        total_cost = product_cost + shipping_cost
        return total_cost

class DigitalProduct(Product):
    def _init_(self, name, price, quantity, file_size):
        super()._init_(name, price, quantity)
        self.file_size = file_size

# Creating instances of the subclasses
physical_product = PhysicalProduct("Book", 20, 2, 1)
digital_product = DigitalProduct("Ebook", 10, 3, "5 MB")

# Calculating total costs
shipping_cost_per_kg = 2.5
physical_total_cost = physical_product.calculate_total_cost(shipping_cost_per_kg)
digital_total_cost = digital_product.calculate_total_cost()

# Displaying total costs
print(f"Total cost of physical product: ${physical_total_cost:.2f}")
print(f"Total cost of digital product: ${digital_total_cost:.2f}")












