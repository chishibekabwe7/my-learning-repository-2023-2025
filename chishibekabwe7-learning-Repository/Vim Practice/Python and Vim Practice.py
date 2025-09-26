#!/bin/python3
correct_username = '24148580'
correct_password = 'test1234'
attempts = 3
while attempts > 0:
    username = input("Enter Username:")
    password = input("Enter your password:")
    if (correct_username == username) and (correct_password == password):
        print("Access Granted!")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Please Try again {attempts} attempts remaining.")
        else:
            print("Locked!")

   






# for col in range(6):
#     for rol in range(6):
#         if (col + rol)  % 2 == 0:
#             print('*',end="")
#         else:
#             print('*',end='')
#     print()

# counter = 10
# while counter > 0:
#     print(counter)
#     counter -= 1

# counter = 1
# while counter <= 10:
#     print(counter)
#     counter += 1


