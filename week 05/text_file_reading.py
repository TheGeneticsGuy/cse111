# If file is imported, it will skip this main call


def read_file():
    with open('provinces.txt','rt') as text_file:

        for line in text_file:
            print(line)



def main():
    print()
    read_file()

if __name__ == "__main__":
    main()