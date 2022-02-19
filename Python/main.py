from uber_lib.account import *
from uber_lib.car import *
from uber_lib.payment import *
from uber_lib.route import *

def main():
    user = User(1, 'Miguel', 1, 'miguel@mail.com', '1234')
    print(f'Usuario: {user.name} \nEmail: {user.email}')


if __name__ == '__main__':
    main()