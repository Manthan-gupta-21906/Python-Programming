def get_number(num):
    while True:
        try:
            return float(input(num))
        except ValueError:
            print(" Invalid input.\nenter a number.\n")

def calculate(a, b, op):
    match op:
        case "+": return a + b
        case "-": return a - b
        case "*": return a * b
        case "/":
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            return a / b
        case "%":
            if b == 0:
                raise ZeroDivisionError("Cannot modulo by zero.")
            return a % b
        case "pow": return a ** b
        case _:
            raise ValueError(f"Unknown operator: {op}")

def format_result(result):
    return int(result) if result.is_integer() else round(result, 10)

def show_menu():
    print("""
┌─────────────────────────────┐
│         OPERATIONS          │
├──────────┬──────────────────┤
│  +  - *  │  Basic Arithmetic│
│  /       │  Division        │
│  %       │  Modulo          │
│  pow     │  Power (a^b)     │
├──────────┼──────────────────┤
│  h       │  View history    │
│  c       │  Clear history   │
│  q       │  Quit            │
│  menu    │  menu            │
└──────────┴──────────────────┘
""")

def show_history(history):
    if not history:
        print("\n  No history yet.\n")
        return
    print("\nCalculation History")
    for i, entry in enumerate(history, 1):
        print(f"  {i:>2}. {entry}")
    print()

def format_expr(a, b, op):
    return f"{a} {op} {b}"

def main():
    history = []
    show_menu()

    valid_ops = {"+", "-", "*", "/", "%", "pow"}

    while True:
        try:
            print("─" * 32)
            op = input("  Operation : ").strip().lower()

            if op == "q":
                print("\nProgram closed\n")
                break
            elif op == "h":
                show_history(history)
                continue
            elif op == "c":
                history.clear()
                print("History cleared.\n")
                continue
            elif op == "menu":
                show_menu()
                continue
            elif op not in valid_ops:
                print(f"Unknown operation '{op}'. Type 'menu' to see options.\n")
                continue

            a = get_number("  Enter number 1 : ")
            b = get_number("  Enter number 2 : ")

            result = calculate(a, b, op)
            formatted = format_result(result)
            entry = f"{format_expr(a, b, op)} = {formatted}"
            history.append(entry)
            print(f"\n{entry}\n")

        except (ZeroDivisionError, ValueError) as e:
            print(f"\nError: {e}\n")
            break

if __name__ == "__main__":
    main()