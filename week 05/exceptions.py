# Week 05 practice

def run_file():
    with open("get_line.py" , "rt" ) as get_line_file:


def main():

    x = 42
    y = 0
    num = 0

    try:
        num = x / y
    except ZeroDivisionError:
        print("ERROR")
    finally:
        print(num)

if __name__ == "__main__":
    main()