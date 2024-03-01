def main(lines):
    for i in range(lines):
        for j in range(i + 1):
            print('*', end='')
        print('')


if __name__ == '__main__':
    # Test case 1
    main(6)