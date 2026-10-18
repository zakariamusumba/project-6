products = [
    ["P001", "Wireless Mouse",         "Electronics", 25.50, 40, 10],
    ["P002", "USB-C Cable 1m",         "Electronics",  8.99, 15,  5],
    ["P003", "Bluetooth Headphones",   "Electronics", 59.99, 12,  8],
    ["P004", "A4 Notebook",            "Stationery",   3.75, 100, 25],
    ["P005", "Ballpoint Pen (Blue)",   "Stationery",   1.20, 200, 50],
    ["P006", "Stapler",                "Stationery",   6.50,  8, 10],
    ["P007", "Coffee Mug",             "Kitchen",      9.99,  30, 10],
    ["P008", "Water Bottle 1L",        "Kitchen",     14.25,   5,  8],
    ["P009", "Desk Lamp",              "Home",        32.00,  18,  6],
    ["P010", "Phone Stand",            "Accessories",  7.49,  22,  10],
    ["P011", "Laptop Sleeve 14\"",     "Accessories", 18.99,   3,  5],
    ["P012", "External Hard Drive 1TB","Electronics", 89.99,   7,  4],
]

total_units_sold = 0
total_sales_value = 0.0
sales_log = []

DISCOUNT_THRESHOLD = 100.00
DISCOUNT_RATE = 0.10


def find_product(code):
    for i, p in enumerate(products):
        if p[0].lower() == code.lower():
            return i
    return -1


def display_products():
    print("\n" + "=" * 78)
    print(f"{'CODE':<6}{'NAME':<28}{'CATEGORY':<14}{'PRICE':>9}{'STOCK':>8}{'REORDER':>9}")
    print("=" * 78)
    for p in products:
        print(f"{p[0]:<6}{p[1]:<28}{p[2]:<14}{p[3]:>9.2f}{p[4]:>8}{p[5]:>9}")
    print("=" * 78)


def search_product():
    code = input("Enter product code (or part of name): ").strip().lower()
    results = [p for p in products if code in p[0].lower() or code in p[1].lower()]
    if not results:
        print("No product found.")
    else:
        print("\n--- Search Results ---")
        for p in results:
            print(f"Code: {p[0]} | Name: {p[1]} | Category: {p[2]} | "
                  f"Price: {p[3]:.2f} | Stock: {p[4]} | Reorder: {p[5]}")

def process_sale():
    global total_units_sold, total_sales_value

    print("\n--- NEW SALE ---")
    code = input("Product code: ").strip()
    idx = find_product(code)

    if idx == -1:
        print("ERROR: Product not found.")
        return

    product = products[idx]
    name = product[1]
    price = product[3]
    stock = product[4]
    reorder = product[5]

    try:
        qty = int(input(f"Quantity of {name} to buy: "))
    except ValueError:
        print("ERROR: Invalid quantity.")
        return

    if qty <= 0:
        print("ERROR: Quantity must be positive.")
        return

    if qty > stock:
        print(f"ERROR: Insufficient stock. Available: {stock}, Requested: {qty}")
        return

    subtotal = price * qty
    print(f"\nUnit price:      ${price:.2f}")
    print(f"Quantity:        {qty}")
    print(f"Subtotal:        ${subtotal:.2f}")

    if subtotal >= DISCOUNT_THRESHOLD:
        discount = subtotal * DISCOUNT_RATE
        print(f"Discount (10%):  -${discount:.2f}")
    else:
        discount = 0.0

    total_due = subtotal - discount
    print(f"Total due:       ${total_due:.2f}")

    try:
        payment = float(input("Amount paid by customer: $"))
    except ValueError:
        print("ERROR: Invalid payment amount.")
        return

    if payment < total_due:
        print(f"ERROR: Insufficient payment. Need at least ${total_due:.2f}")
        return

    change = payment - total_due

    products[idx][4] = stock - qty
    new_stock = products[idx][4]

    total_units_sold += qty
    total_sales_value += total_due
    sales_log.append((name, qty, total_due))

    print("\n" + "-" * 40)
    print("           RECEIPT")
    print("-" * 40)
    print(f"Product:     {name}")
    print(f"Quantity:    {qty}")
    print(f"Subtotal:    ${subtotal:.2f}")
    print(f"Discount:    ${discount:.2f}")
    print(f"Total:       ${total_due:.2f}")
    print(f"Paid:        ${payment:.2f}")
    print(f"Change:      ${change:.2f}")
    print(f"New stock:   {new_stock}")
    print("-" * 40)

    if new_stock <= reorder:
        print(f"WARNING: '{name}' at/below reorder level ({reorder}). Reorder now!")

def check_reorder():
    return [p for p in products if p[4] <= p[5]]

def low_stock_report():
    print("\n===== LOW-STOCK REPORT =====")
    flagged = check_reorder()
    if not flagged:
        print("All products above reorder level.")
        return
    print(f"{'CODE':<6}{'NAME':<28}{'STOCK':>7}{'REORDER':>9}{'NEEDED':>8}")
    print("-" * 60)
    for p in flagged:
        needed = p[5] - p[4]
        print(f"{p[0]:<6}{p[1]:<28}{p[4]:>7}{p[5]:>9}{max(needed,0):>8}")
    print("-" * 60)

def sales_summary():
    print("\n===== SALES SUMMARY =====")
    print(f"Total units sold:     {total_units_sold}")
    print(f"Total sales value:    ${total_sales_value:.2f}")
    if sales_log:
        print("\nTransactions:")
        for item in sales_log:
            print(f"  {item[0]:<28} qty={item[1]:<4} total=${item[2]:.2f}")
    else:
        print("No sales yet.")

def main():
    while True:
        print("\n" + "#" * 45)
        print("#   INVENTORY & SALES MANAGEMENT SYSTEM   #")
        print("#" * 45)
        print("1. Display products")
        print("2. Search product")
        print("3. Process sale")
        print("4. Low-stock report")
        print("5. Sales summary")
        print("6. Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":
            display_products()
        elif choice == "2":
            search_product()
        elif choice == "3":
            process_sale()
        elif choice == "4":
            low_stock_report()
        elif choice == "5":
            sales_summary()
        elif choice == "6":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")