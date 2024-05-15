from z6sum_less_than_k import sum_less_than_k

def main():
    my_list = [10, 5, 3, 8, 12, 4]
    k = 7

    result = sum_less_than_k(my_list, k)
    print(f"Сумма элементов списка, меньших {k}, равна {result}")

if __name__ == "__main__":
    main()
