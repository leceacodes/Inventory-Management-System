class Product:
    """Class is the product in the store."""
    
    def __init__(self, product_id, name, category, price, quantity):
        """
        Initialize a new Product object.

        Args:
            product_id (int): Unique identifier for the product.
            name (str): Name of the product.
            category (str): Category of the product.
            price (float): Price of the product.
            quantity (int): Quantity of the product in stock.
        """
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity


class Inventory:
    """Class is the store's inventory."""

    def __init__(self):
        self.products = {}  # Store products with their IDs as keys

    def add_product(self, product):
        """Add a product inventory."""
        if product.product_id in self.products:
            print("Product with the same ID already exists.")
        else:
            self.products[product.product_id] = product

    def update_stock(self, product_id, quantity):
        """Update stock levels."""
        if product_id in self.products:
            self.products[product_id].quantity += quantity
        else:
            print("Product could'nt be found in the inventory.")

    def get_product_info(self, product_id):
        """Get product information by product ID."""
        return self.products.get(product_id, None)


class Transaction:
    """Class is the sales transaction."""
    
    def __init__(self):
        self.products_sold = [] 
        self.total_amount = 0

    def add_product(self, product, quantity):
        """Add a product to transaction."""
        if product.quantity >= quantity:
            self.products_sold.append((product, quantity))
            self.total_amount += product.price * quantity
            product.quantity -= quantity
        else:
            print("NOT ENOUGH stock for the product:", product.name)

    def finalize_transaction(self):
        """Finish the transaction."""
        pass


class ReportGenerator:
    """Class for generating reports."""
    
    def generate_stock_report(self, inventory):
        """Generate a stock report."""
        print("Stock Report:")
        for product_id, product in inventory.products.items():
            print(f"Product ID: {product_id}, Name: {product.name}, Quantity: {product.quantity}")

    def generate_sales_report(self, transactions):
        """Generate a sales report."""
        print("Sales Report:")
        for i, transaction in enumerate(transactions, start=1):
            print(f"Transaction {i}: Total Amount - ${transaction.total_amount}")


def main():
    inventory = Inventory()
    transactions = []
    report_generator = ReportGenerator()

    while True:
        print("The Store Inventory Management System:")
        print("\nOptions:")
        print("1. Products")
        print("2. Create a Sale")
        print("3. Put a Stock Report")
        print("4. Put a Sales Report")
        print("5. Leave")

        choice = input("Enter your choice (put either 1, 2, 3, 4, or 5): ")

        if choice == '1':
            try:
                product_id = int(input("Enter Product ID: "))
                name = input("Enter Product Name: ")
                category = input("Enter Product Category: ")
                price = float(input("Enter Product Price: "))
                quantity = int(input("Enter Initial Stock Quantity: "))
            except ValueError:
                print("Invalid input. Please enter a valid numeric value.")
                continue

            product = Product(product_id, name, category, price, quantity)
            inventory.add_product(product)
            print("Product added to inventory.")

        elif choice == '2':
            transaction = Transaction()
            while True:
                try:
                    product_id = int(input("Enter Product ID to sell (0 to finish): "))
                except ValueError:
                    print("Invalid input. Please enter a valid numeric value.")
                    continue

                if product_id == 0:
                    break

                quantity = int(input("Enter Quantity to sell: "))
                product = inventory.get_product_info(product_id)
                if product:
                    transaction.add_product(product, quantity)
                else:
                    print("Product not found in inventory.")
            transaction.finalize_transaction()
            transactions.append(transaction)
            print("Sale recorded.")

        elif choice == '3':
            report_generator.generate_stock_report(inventory)

        elif choice == '4':
            report_generator.generate_sales_report(transactions)

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()


