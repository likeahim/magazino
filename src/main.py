items = [
    {"name": "Round table", "quantity": 2, "unit": "amount", "unit_price": 2000},
    {"name": "Wood stool", "quantity": 4, "unit": "amount", "unit_price": 300},
    {"name": "Wood frame", "quantity": 10, "unit": "amount", "unit_price": 80}
]

sold_items = list()

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
        quantity = matching_product["quantity"]
        print(f"You have {quantity} item(s) to sell")
        quantity_to_sell = int(input("quantity:\n"))
        while check_amount(quantity, quantity_to_sell):
            print(f"You have sold {quantity_to_sell} item(s)")
            matching_product["quantity"] = quantity - quantity_to_sell
            break
    else:
        print("There is no such a item")
    get_items()


def init():
    message = ""
    while message != "exit":
        message = input("""
        What would you like to do?
        exit - exit the program
        show - show the items
        add - add item
        sell - sell item
        """).lower()
        if message == "show":
            get_items()
        elif message == "add":
            add_item()
        elif message == "sell":
            sell_item()
    exit_program()

init()