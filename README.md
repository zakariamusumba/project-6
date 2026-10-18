# project-6
README — Inventory & Sales Management System
A simple, menu-driven Python application for managing product inventory and processing customer sales. Built with plain Python (no classes, no external dependencies) using lists, functions, and global state — perfect for learning or small shop demos.

📋 Table of Contents
Overview

Features

Requirements

Project Structure

Installation

Usage

Running the Interactive Menu

Importing as a Module

Product Data Format

Menu Options

Discount Rules

Worked Example

Sample Test Cases

Known Limitations

Possible Extensions

License

🔍 Overview
This program simulates a point-of-sale (POS) and inventory system for a small retail shop. It lets you:

View all products and their current stock levels.

Search for a product by code or name.

Sell products to customers, applying discounts when applicable.

Automatically reduce stock after a successful sale.

Get warned when stock falls to or below the reorder level.

Track total units sold and total sales revenue.

The entire application lives in a single Python file and requires only the standard library.

✨ Features
#	Feature	Description
1	Display Products	Shows a formatted table of all products with code, name, category, price, stock, and reorder level.
2	Search Product	Finds products by exact code or partial name match.
3	Process Sale	Handles customer purchases end-to-end: quantity input, stock check, payment, and receipt.
4	Stock Validation	Rejects sales that exceed available stock before accepting payment.
5	Stock Reduction	Deducts quantity from inventory only after successful payment.
6	Subtotal & Discount	Calculates subtotal and applies a 10% discount on orders of $100 or more.
7	Payment & Change	Validates payment amount and calculates change.
8	Reorder Alerts	Warns the user immediately if a sale pushes stock to/below the reorder level.
9	Low-Stock Report	Lists all products that need restocking with the quantity needed.
10	Sales Summary	Displays total units sold, total sales value, and a transaction history.
💻 Requirements
Python 3.6+ (uses f-strings)

No external packages required

📁 Project Structure
text
inventory-system/
│
├── inventory.py        # Main program (single-file application)
└── README.md           # This file
Optionally, if you're using the module version (see Importing as a Module):

text
inventory-system/
│
├── inventory.py        # Refactored module (state dict + functions)
├── main_app.py         # Importer / driver script
└── README.md
⚙️ Installation
Clone or download the project:

bash
git clone https://github.com/your-username/inventory-system.git
cd inventory-system
(Optional) Create a virtual environment:

bash
python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows
No dependencies to install — you're ready to run.

🚀 Usage
Running the Interactive Menu
bash
python inventory.py
You'll see the main menu:

text
#############################################
#   INVENTORY & SALES MANAGEMENT SYSTEM   #
#############################################
1. Display products
2. Search product
3. Process sale
4. Low-stock report
5. Sales summary
6. Exit
Choose option:
Enter the number of the option you want and press Enter.

Importing as a Module
The program can be imported into other scripts. The if __name__ == "__main__": guard ensures the menu does not auto-run on import.

Example — accessing data from another file:

python
import inventory

# Display products from the imported module
inventory.display_products()

# Search programmatically
idx = inventory.find_product("P001")
if idx != -1:
    print("Found:", inventory.products[idx])

# Simulate a sale manually (bypassing input())
inventory.products[idx][4] -= 3
line_total = inventory.products[idx][3] * 3
inventory.total_units_sold += 3
inventory.total_sales_value += line_total

# Show summary
inventory.sales_summary()
⚠️ Note: The interactive functions (process_sale, search_product) call input() directly, so they only work in a terminal. For programmatic use, manipulate the products list and counters directly, or use the refactored module (state-dict version) described in the import guide.

🧾 Product Data Format
Each product is stored as a list inside the products list:

python
["P001", "Wireless Mouse", "Electronics", 25.50, 40, 10]
   │          │                │            │    │   │
   │          │                │            │    │   └── reorder_level (int)
   │          │                │            │    └────── stock quantity (int)
   │          │                │            └─────────── price (float, USD)
   │          │                └──────────────────────── category (str)
   │          └───────────────────────────────────────── name (str)
   └──────────────────────────────────────────────────── code (str, unique)
Field	Type	Example	Description
code	str	"P001"	Unique product identifier
name	str	"Wireless Mouse"	Display name
category	str	"Electronics"	Product grouping
price	float	25.50	Unit price in USD
stock	int	40	Current units in inventory
reorder_level	int	10	Minimum threshold before restocking
Default Product Catalog (12 items)
Code	Name	Category	Price	Stock	Reorder
P001	Wireless Mouse	Electronics	$25.50	40	10
P002	USB-C Cable 1m	Electronics	$8.99	15	5
P003	Bluetooth Headphones	Electronics	$59.99	12	8
P004	A4 Notebook	Stationery	$3.75	100	25
P005	Ballpoint Pen (Blue)	Stationery	$1.20	200	50
P006	Stapler	Stationery	$6.50	8	10
P007	Coffee Mug	Kitchen	$9.99	30	10
P008	Water Bottle 1L	Kitchen	$14.25	5	8
P009	Desk Lamp	Home	$32.00	18	6
P010	Phone Stand	Accessories	$7.49	22	10
P011	Laptop Sleeve 14"	Accessories	$18.99	3	5
P012	External Hard Drive 1TB	Electronics	$89.99	7	4
📖 Menu Options
1. Display Products
Prints a formatted table showing all products with their current stock and reorder levels.

2. Search Product
Prompts for a code or partial name (case-insensitive). Returns all matching products.

text
Enter product code (or part of name): mouse
--- Search Results ---
Code: P001 | Name: Wireless Mouse | Category: Electronics | Price: 25.50 | Stock: 40 | Reorder: 10
3. Process Sale
Full sales workflow:

Enter product code (e.g., P001).

Enter quantity.

System checks if stock is sufficient.

Displays subtotal, discount (if any), and total due.

Enter payment amount.

System validates payment and shows change.

Stock is reduced; a receipt is printed.

If new stock ≤ reorder level, a warning is shown.

4. Low-Stock Report
Lists all products at or below their reorder level with the quantity needed to restock.

text
===== LOW-STOCK REPORT =====
CODE  NAME                         STOCK  REORDER  NEEDED
------------------------------------------------------------
P006  Stapler                          8       10       2
P008  Water Bottle 1L                  5        8       3
P011  Laptop Sleeve 14"                3        5       2
------------------------------------------------------------
5. Sales Summary
Shows the running totals for the session:

text
===== SALES SUMMARY =====
Total units sold:     5
Total sales value:    $161.98

Transactions:
  External Hard Drive 1TB      qty=2    total=$161.98
  Wireless Mouse               qty=3    total=$76.50
6. Exit
Ends the program cleanly.

💰 Discount Rules
Discount logic is defined by two constants at the top of the file:

python
DISCOUNT_THRESHOLD = 100.00   # spend >= $100 gets a discount
DISCOUNT_RATE = 0.10          # 10% off
If the subtotal is ≥ $100.00, a 10% discount is applied.

Otherwise, no discount.

Discount is applied before payment is requested.

Example:

Qty	Unit Price	Subtotal	Discount	Total Due
3	$25.50	$76.50	$0.00	$76.50
2	$89.99	$179.98	−$18.00	$161.98
🧪 Worked Example
Scenario: Customer buys 2 × External Hard Drive (P012).

text
--- NEW SALE ---
Product code: P012
Quantity of External Hard Drive 1TB to buy: 2

Unit price:      $89.99
Quantity:        2
Subtotal:        $179.98
Discount (10%):  -$18.00
Total due:       $161.98
Amount paid by customer: $200

----------------------------------------
           RECEIPT
----------------------------------------
Product:     External Hard Drive 1TB
Quantity:    2
Subtotal:    $179.98
Discount:    $18.00
Total:       $161.98
Paid:        $200.00
Change:      $38.02
New stock:   5
----------------------------------------
✅ Sample Test Cases
#	Action	Expected Outcome
1	Sell P005 × 5	Subtotal $6.00, no discount, change calculated.
2	Sell P012 × 2, pay $200	Subtotal $179.98, 10% discount, change $38.02.
3	Sell P011 × 5 (only 3 in stock)	❌ Rejected: "Insufficient stock".
4	Sell P001, pay less than total	❌ Rejected: "Insufficient payment".
5	Sell P006 × 1	Stock → 7, warning: "Stapler at/below reorder level".
6	Search "pen"	Matches "Ballpoint Pen (Blue)" (P005).
7	Run low-stock report on start	Lists P006, P008, P011 (already at/below reorder).
8	Buy 0 or negative qty	❌ Rejected: "Quantity must be positive".
⚠️ Known Limitations
In-memory only — all data resets when the program exits. No file or database persistence.

Single-user, single-sale — one transaction is processed at a time; no shopping cart.

Global state — total_units_sold, total_sales_value, and sales_log are module-level globals, which is fine for a demo but not for concurrency.

No authentication — intended for demo purposes.

Interactive only — the sale workflow depends on input(), so it can't be automated without refactoring (see Importing as a Module).

No currency formatting — prices are shown with $ prefix but no thousands separator (e.g., $1,234.56).

🔮 Possible Extensions
Persistence — save/load products and sales to products.json or CSV.

Multiple-item sales — build a cart, calculate grand total across many products.

User roles — admin (restock, add products) vs. cashier (sell only).

Tax support — add configurable tax rate to totals.

Receipt export — write receipts to .txt or print directly.

GUI / Web UI — Tkinter desktop app or Flask/FastAPI backend.

Barcode scanning — hook up a USB barcode scanner as keyboard input.

Refactor to classes — replace the list-of-lists with a Product class and an Inventory class for cleaner testing.

📄 License
This project is released for educational purposes. You may freely use, modify, and distribute it. No warranty is provided.

Last updated: 2026
