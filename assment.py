# Simple Fruit Market CLI using basic if/elif and loops
# - Heading: "Enter the Fruit Market"
# - Main menu: 1) Manager 2) Customer 3) Exit
# - Manager: Add, View, Update fruits
# - Customer: View fruits
# - Uses simple lists, loops, and if/elif/else (no classes)

def get_int(prompt, min_val=None, max_val=None):
    while True:
        s = input(prompt).strip()
        if not s.isdigit() and not (s.startswith("-") and s[1:].isdigit()):
            print("Please enter an integer.")
            continue
        val = int(s)
        if min_val is not None and val < min_val:
            print(f"Enter a number >= {min_val}.")
            continue
        if max_val is not None and val > max_val:
            print(f"Enter a number <= {max_val}.")
            continue
        return val

def get_float(prompt, min_val=None, max_val=None):
    while True:
        s = input(prompt).strip()
        try:
            val = float(s)
        except ValueError:
            print("Please enter a valid number (e.g., 12.5).")
            continue
        if min_val is not None and val < min_val:
            print(f"Enter a value >= {min_val}.")
            continue
        if max_val is not None and val > max_val:
            print(f"Enter a value <= {max_val}.")
            continue
        return val

def get_nonempty(prompt):
    while True:
        s = input(prompt).strip()
        if s:
            return s
        print("This field cannot be empty.")

def print_heading():
    print("\n" + "=" * 50)
    print("Enter the Fruit Market".center(50))
    print("=" * 50)

def show_table(fruits):
    if not fruits:
        print("No fruits available.")
        return
    print("\n{:<5} {:<20} {:>10} {:>10}".format("ID", "Name", "Price", "Quantity"))
    print("-" * 50)
    for f in fruits:
        print("{:<5} {:<20} {:>10.2f} {:>10}".format(f["id"], f["name"], f["price"], f["quantity"]))

def main():
    fruits = []  # each item: {"id": int, "name": str, "price": float, "quantity": int}
    next_id = 1

    while True:
        print_heading()
        print("1) Manager")
        print("2) Customer")
        print("3) Exit")
        choice = get_int("Choose an option (1-3): ", 1, 3)

        if choice == 1:
            # Manager Menu
            while True:
                print("\nManager Menu")
                print("1) Add Fruit")
                print("2) View Fruits")
                print("3) Update Fruit")
                print("4) Back")
                m_choice = get_int("Choose an option (1-4): ", 1, 4)

                if m_choice == 1:
                    # Add Fruit
                    name = get_nonempty("Enter fruit name: ")
                    price = get_float("Enter price: ", min_val=0.0)
                    qty = get_int("Enter quantity: ", min_val=0)

                    fruits.append({
                        "id": next_id,
                        "name": name,
                        "price": round(price, 2),
                        "quantity": qty
                    })
                    print(f"Added fruit: ID={next_id}, Name={name}, Price={price:.2f}, Qty={qty}")
                    next_id += 1

                elif m_choice == 2:
                    # View Fruits
                    show_table(fruits)

                elif m_choice == 3:
                    # Update Fruit
                    if not fruits:
                        print("No fruits to update.")
                    else:
                        show_table(fruits)
                        fid = get_int("Enter Fruit ID to update: ", min_val=1)
                        # Find fruit by id using a simple loop
                        idx = -1
                        for i in range(len(fruits)):
                            if fruits[i]["id"] == fid:
                                idx = i
                                break

                        if idx == -1:
                            print("Fruit not found.")
                        else:
                            current = fruits[idx]
                            print("Press Enter to keep current value.")
                            new_name = input(f"New name (current: {current['name']}): ").strip()
                            new_price_str = input(f"New price (current: {current['price']:.2f}): ").strip()
                            new_qty_str = input(f"New quantity (current: {current['quantity']}): ").strip()

                            # Update using if/else checks
                            if new_name:
                                current["name"] = new_name

                            if new_price_str:
                                try:
                                    np = float(new_price_str)
                                    if np >= 0:
                                        current["price"] = round(np, 2)
                                    else:
                                        print("Price cannot be negative; keeping old value.")
                                except ValueError:
                                    print("Invalid price; keeping old value.")

                            if new_qty_str:
                                if new_qty_str.isdigit() or (new_qty_str.startswith("-") and new_qty_str[1:].isdigit()):
                                    nq = int(new_qty_str)
                                    if nq >= 0:
                                        current["quantity"] = nq
                                    else:
                                        print("Quantity cannot be negative; keeping old value.")
                                else:
                                    print("Invalid quantity; keeping old value.")

                            print("Fruit updated successfully.")

                else:
                    # Back to main
                    break

        elif choice == 2:
            # Customer Menu
            while True:
                print("\nCustomer Menu")
                print("1) View Fruits")
                print("2) Back")
                c_choice = get_int("Choose an option (1-2): ", 1, 2)

                if c_choice == 1:
                    show_table(fruits)
                else:
                    break

        else:
            print("Thank you for visiting the Fruit Market!")
            break

if __name__ == "__main__":
    main()