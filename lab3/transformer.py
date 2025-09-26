import json

def run_task():
    while True:
        names_input = input("Enter product names (comma-separated): ").strip()
        if names_input:
            product_names = [n.strip() for n in names_input.split(",") if n.strip()]
            if product_names:
                break
        print("Invalid input. Please enter product names.")

    while True:
        prices_input = input("Enter product prices (comma-separated): ").strip()
        try:
            product_prices = [float(p.strip()) for p in prices_input.split(",") if p.strip()]
            if len(product_prices) == len(product_names):
                break
            else:
                print("Number of prices must match number of products.")
        except Exception:
            print("Invalid input. Please enter numeric prices.")

    paired = zip(product_names, product_prices)

    products = list(map(
        lambda item: {"product": item[0], "price": item[1], "discounted": round(item[1] * 0.9, 2)},
        filter(lambda item: item[1] > 0, paired)
    ))

    with open("products.json", "w") as f:
        json.dump(products, f, indent=4)

    print("Products saved to products.json")
    print("Preview (first 5):")
    for p in products[:5]:
        print(p)
