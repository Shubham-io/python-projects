
import os
import glob
import time


def init_lib():
    books = ['hindi', 'english', 'math', 'history', 'java',
             'python', 'swift', 'c programming', 'accounts', 'marketing']
    with open('library.txt', 'w') as file:
        file.write('*** All Books ***' + '\n\n')
        for book in books:
            file.write(book+'\n')


def verification(user_name):
    # user_name = input("Enter your name: ")
    fetch_users = glob.glob('*.txt')  # getting only txt files
    if user_name + '.txt' in fetch_users:
        print("\nVerification is under process")
        print("Please wait.......")
        time.sleep(1.5)
        print("User detected :)\n")
        return True
    else:
        print("Invalid username!\n")
        return False


def check_account(user_name):
    fetch_users = glob.glob('*.txt')  # getting only txt files
    if user_name + '.txt' in fetch_users:
        return 0
    else:
        return 1


def display():

    with open('library.txt', 'r') as file:
        all_books = file.readlines()
        for book in all_books:
            print(book.strip())


def create_account():
    name = input("Enter a username: ")
    if check_account(name):
        id = input("Enter your 4 digit id: ")
        with open(name + '.txt', 'w') as file:
            file.write("Name: " + name)
            file.write("\nId: " + id)
            file.write("\n*** Your books are here ***")
    else:
        print("This username is not available\n")



lib = []
file = open("library.txt", 'a')


def library():
    pass


with open('library.txt') as file:
    books = file.read()
    lib.append(books)


def take_book(user_name):
    requested_book = input("which book you want: ")
    with open('library.txt', 'r+') as file:
        lib = file.readlines()
        new_lib = []
        for book in lib:
            new_lib.append(book.strip())
        # print(new_lib)
        if requested_book in new_lib:
            new_lib.remove(requested_book)

            with open('library.txt', 'w') as file:
                for book in new_lib:
                    file.write('%s\n' % book)
            # print(new_lib)

            with open(user_name+'.txt', 'a') as file:
                file.write("\n" + requested_book)
                print("book has been added to your account\n")
        else:
            print("Book is out of stock!")


def return_book(user_name):
    user_books = []
    ret_book = input("Which book you want to return: ")
    with open(user_name + '.txt', 'r') as file:
        fetch_user_books = file.readlines()
        for book in fetch_user_books:
            user_books.append(book.strip())

    if ret_book in user_books:
        with open('library.txt', 'a') as file:
            file.write('\n'+ret_book)
            user_books.remove(ret_book)
        with open(user_name + '.txt', 'w') as file:
            for book in user_books:
                file.write('%s\n' % book)
            print("Book has been submitted")

    else:
        print(f"You don't have {ret_book} book!!")


print("******* WELCOME TO LIBRARY MANAGEMENT SYSTEM *******\n\tCreated by Shubham Vishwakarma\n\n")
print("Note: You must create a account first !\n")
init_lib()
while 1:
    c = int(input("\n1. Verify yourself\n2. Create new account\n3. Exit\n"))
    if c == 1:
        user_name = input("Enter your name: ")
        if verification(user_name):
            while True:
                choice = int(
                    input("\n1. Take book\n2. Return book\n3. Display\n4. Exit\n\n"))
                if choice == 1:
                    take_book(user_name)
                elif choice == 2:
                    return_book(user_name)
                elif choice == 3:
                    display()
                elif choice == 4:
                    break
                else:
                    print("Invalid input given\n")

    elif c == 2:
        create_account()
    elif c == 3:
        exit()
    else:
        print("User does not exist!\n")
