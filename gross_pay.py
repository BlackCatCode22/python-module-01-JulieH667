def calculate_gross_pay(hours, rate):
    overtime_hours = max(0, hours - 40)
    regular_hours = hours - overtime_hours
    overtime_rate = rate * 1.5
    return (regular_hours * rate) + (overtime_hours * overtime_rate)


def main():
    try:
        hours = float(input("Enter the number of hours worked: "))
        rate = float(input("Enter the hourly rate: "))

        if hours < 0 or rate < 0:
            raise ValueError("Hours and rate must be non-negative numbers.")

        gross_pay = calculate_gross_pay(hours, rate)
        print(f"Gross pay: ${gross_pay:.2f}")

    except ValueError as e:
        print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()
