#!/usr/bin/python3.10
if __name__ == "__main__":
    import hidden_4

    name = dir(hidden_4)
    for name in sorted(name):
        if not name.startswith("__"):
            print(name)
