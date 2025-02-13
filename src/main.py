import csv

items = []

sold_items = list()

file_path = "magazyn.csv"
file_sold_items = "sold_archive.csv"

def get_items():
    print("Name\t\tQuantity\t\tUnit\t\tUnit Price (PLN)")
    for item in items:
        print(f"{item['name']}\t{item['quantity']}\t\t\t{item['unit']}\t\t{item['unit_price']}")


def exit_program():
    print("Exiting program\nGoodbye")


def add_item():
    print("Adding item")
    name = input("name:\n")
    quantity = input("quantity:\n")
    unit = "amount"
    unit_price = input("unit price:\n")
    items.append({"name": name, "quantity": quantity, "unit": unit, "unit_price": unit_price})
    get_items()


def check_amount(quantity, quantity_to_sell):
    if quantity < quantity_to_sell:
        print("Not enough items")
    return quantity >= quantity_to_sell


def sell_item():
    get_items()
    quantity_to_sell = 0
    print("Selling item")
    name = input("name:\n")
    if any(product["name"] == name for product in items):
        matching_product = next((product for product in items if product["name"] == name), None)
        quantity = int(matching_product["quantity"])
        print(f"You have {quantity} item(s) to sell")
        quantity_to_sell = int(input("quantity:\n"))
        while check_amount(quantity, quantity_to_sell):
            print(f"You have sold {quantity_to_sell} item(s)")
            matching_product["quantity"] = quantity - quantity_to_sell
            sold_items.append({"name": matching_product["name"], "quantity": quantity_to_sell, "unit": matching_product["unit"], "unit_price": matching_product["unit_price"]})
            break
    else:
        print("There is no such a item")
    get_items()


def export_items_to_csv():
    with open(file_path, "w", newline="") as csvfile:
        fieldnames = ["name", "quantity", "unit", "unit_price"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in items:
            writer.writerow(item)
    with open(file_sold_items, "w", newline="") as csvsold:
        fieldnames = ["name", "quantity", "unit", "unit_price"]
        writer = csv.DictWriter(csvsold, fieldnames=fieldnames)
        writer.writeheader()
        for item in sold_items:
            writer.writerow(item)
        print("Data saved to file")


def load_items_from_csv():
    with open(file_path, mode='r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            items.append(row)
    with open(file_sold_items, mode='r', newline='') as soldfile:
        reader = csv.DictReader(soldfile)
        for row in reader:
            sold_items.append(row)


def init():
    try:
        load_items_from_csv()
    except FileNotFoundError:
        print("File not found")
    except csv.Error:
        print("Loading file failed. Check files forma")
    message = ""
    while message != "exit":
        message = input("""
        What would you like to do?
        exit - exit the program
        show - show the items
        add - add item
        sell - sell item
        save
        """).lower()
        if message == "show":
            get_items()
        elif message == "add":
            add_item()
        elif message == "sell":
            sell_item()
        elif message == "save":
            export_items_to_csv()
    exit_program()

init()