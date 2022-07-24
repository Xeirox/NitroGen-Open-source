import random
import requests


CHARACTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def gen_code():
    return ''.join(random.choice(CHARACTERS) for _ in range(16))


def save_code(code):
    with open("nitros.txt", "a") as f:
        f.write(f"https://discord.gift/{code}\n")


def main():
    while True:
        try:
            checks = int(input("How many nitros do you want to generate? "))
        except ValueError:
            print("Invalid input.")
            continue
        if checks < 1:
            print("Invalid input.")
            continue
        break

    valid = 0

    for checked in range(checks):
        nitrocode = gen_code()

        print(
            f"Checking code: {nitrocode}")
        try:
            r = requests.get(
                f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitrocode}?with_application=false&with_subscription_plan=true")
        except:
            print("Error while checking code.")
            continue

        if r.status_code == 200:
            save_code(nitrocode)
            print(f"Found code: {nitrocode}\nSaved to nitros.txt")
            valid += 1
        checked += 1
        print(f"Checked: {checked} - Valid: {valid}\n")


if "__main__" == __name__:
    main()
    print("Done!")
    input("Press enter to exit.")
    exit(0)
