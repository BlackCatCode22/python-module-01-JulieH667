import datetime


def get_greeting():
    now = datetime.datetime.now()
    hour = now.hour

    if 5 <= hour < 12:
        return "Good morning"
    elif 12 <= hour < 17:
        return "Good afternoon"
    else:
        return "Good evening"


def main():
    name = input("Enter your name: ")
    greeting = get_greeting()
    print(f"{greeting}, {name}!")


if __name__ == "__main__":
    main()
