# Spare Parts Inventory CLI
# Simple inventory management system for technical spare parts.

inventory = [
    {"id": 101, "name": "Hydraulikventil A1", "category": "Mechanik", "stock": 12, "price": 45.50},
    {"id": 102, "name": "Sensor Typ-C", "category": "Elektronik", "stock": 5, "price": 129.00},
    {"id": 103, "name": "Dichtungssatz K8", "category": "Wartung", "stock": 28, "price": 8.75}
]

def list_items():
    """Displays all items in the inventory."""
    print("\n--- Aktueller Lagerbestand ---")
    for item in inventory:
        print(f"ID: {item['id']} | Name: {item['name']} | Kategorie: {item['category']} | Bestand: {item['stock']} Stk. | Preis: {item['price']:.2f} €")

def add_item(name: str, category: str, stock: int, price: float):
    """Adds a new item to the inventory list."""
    new_id = max([item["id"] for item in inventory], default=100) + 1
    new_item = {
        "id": new_id,
        "name": name,
        "category": category,
        "stock": stock,
        "price": price
    }
    inventory.append(new_item)
    print(f"\n[ERFOLG] Artikel '{name}' wurde mit ID {new_id} hinzugefügt.")

def main():
    """Main application loop."""
    print("=== Lagerverwaltungssystem gestartet ===")
    list_items()
    print("\n--- Neuer Artikel wird angelegt ---")
    add_item(name="Kabelbaum Heavy Duty", category="Elektronik", stock=15, price=89.90)
    list_items()

if __name__ == "__main__":
    main()
