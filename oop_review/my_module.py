from random import randint

def generate_secret_key():
    return randint(1, 10_000_000) * 100 + 2000 - randint(1,1400)

if __name__ == "__main__":
    print(generate_secret_key())
