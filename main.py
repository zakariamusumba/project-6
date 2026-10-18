import importlib.util
from pathlib import Path

inventory_path = Path(__file__).with_name("inventory.py")
spec = importlib.util.spec_from_file_location("inventory", inventory_path)
if spec is None or spec.loader is None:
	raise ModuleNotFoundError(f"Could not load inventory module from {inventory_path}")

inventory = importlib.util.module_from_spec(spec)
spec.loader.exec_module(inventory)
print("=== Displaying products from imported module ===")
inventory.display_products()

print("\n=== Low-stock report ===")
inventory.low_stock_report()
print("\n=== Sales summary (before any sale) ===")
inventory.sales_summary()

print("\n=== Product list length ===")
print(len(inventory.products), "products loaded")

print("\n=== First product ===")
print(inventory.products[0])
idx = inventory.find_product("P001")
if idx != -1:
    qty = 3
    if inventory.products[idx][4] >= qty:
        inventory.products[idx][4] -= qty          # reduce stock
        line_total = inventory.products[idx][3] * qty
        inventory.total_units_sold += qty
        inventory.total_sales_value += line_total
        inventory.sales_log.append((inventory.products[idx][1], qty, line_total))
        print(f"\nSimulated sale: {qty} x {inventory.products[idx][1]} = ${line_total:.2f}")

print("\n=== Sales summary (after simulated sale) ===")
inventory.sales_summary()