from random import randint

def create_repository():
    right_action = randint(0, 100)
    again_try = randint(0, 100)
    blyat_count = 0
    while again_try != right_action:
        print('blyat'); blyat_count += 1
        again_try = randint(0, 100)
    print(f'And after {blyat_count} blyat - congratulations!')


if __name__ == '__main__':
    create_repository()
