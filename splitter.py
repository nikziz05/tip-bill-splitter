# Tip and Bill Splitter

def split_bill(bill, people):
    """Return the amount each person has to pay."""
    total = bill + (bill * 0.10)  # add 10% tip
    return total / people


def main():
    bill = float(input("Enter the bill amount: "))
    people = int(input("Enter the number of people: "))

    if bill < 0 or people < 1:
        print("Bill cannot be negative and there must be at least 1 person.")
        return

    share = split_bill(bill, people)
    print(f"Each person pays: Rs. {share:.2f}")


if __name__ == "__main__":
    main()
