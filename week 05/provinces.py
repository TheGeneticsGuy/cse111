# If file is imported, it will skip this main call


def read_file():

    provinces_list = []
    with open ("provinces.txt" , "rt" ) as text_file:
        for line in text_file:
            if line.strip() == "AB":
                line = "Alberta"
            provinces_list.append(line.strip())

    print(provinces_list)

    # Remove first and last
    provinces_list.pop(0)
    provinces_list.pop(len (provinces_list) - 1 )

    num = provinces_list.count('Alberta')
    print(f'Alberta appears {num} times in the list.')
    print()

def main():
    print()
    read_file()

if __name__ == "__main__":
    main()