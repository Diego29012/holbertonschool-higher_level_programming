#!/usr/bin/python3

if __name__ == '__main__':
    import hidden_4
    for d in dir(hidden_4):
        if not d.startswith("__"):
            print(d)
