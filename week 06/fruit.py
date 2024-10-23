# Author:           Aaron Topping
# Class:            CSE 111
# Assignent:        Week06

def main():

    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print()
    print(f"original: {fruit_list}")

    # Reverse the list
    fruit_list.reverse()
    print(fruit_list)

    # Append
    fruit_list.append('orange')
    print(fruit_list)

    # Insert cherry before apple
    ind = fruit_list.index('apple')
    fruit_list.insert(ind,'cherry')
    print(fruit_list)

    # remove banana
    fruit_list.pop(fruit_list.index('banana'))
    print(fruit_list)

    # remove last item
    fruit_list.pop(len(fruit_list) - 1)
    print(fruit_list)

    # Sort
    fruit_list.sort()
    print(fruit_list)

    fruit_list.clear()
    print(fruit_list)



    print()


if __name__ == "__main__":
    main()