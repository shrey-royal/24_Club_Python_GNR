def calculateTotal(*prices: int):
    print(prices, type(prices))
    for price in prices:
        if price < 1:
            raise ValueError("Price can't be negative!")
        
    return sum(prices)


def main():
    total_price = 0
    try:
        total_price = calculateTotal(1, 2, 3, 23, 123, 34, 123, 234, 345, 12)
    except ValueError as e:
        print(e)

    print(f"Calculate Total: {total_price if total_price != 0 else "Error"}")

if __name__ == "__main__":
    main()