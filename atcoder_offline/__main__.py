import json


def main():
    env = {}
    with open("config/env.json", mode="r") as f:
        env = json.load(f)


if __name__ == "__main__":
    main()
