import random

class RPS:
    data_list = []
    res_dct = {}
    options = ['rock', 'paper', 'scissors']

    greet_user = input("Enter your name:")
    print("Hello, "+greet_user)

    read_file = open("rating.txt", 'r')
    data = read_file.readlines()

    for line in data:
        (key, val) = line.split(" ")
        res_dct[key] = int(val)
        line.strip()


    if greet_user not in res_dct:
        res_dct[greet_user] = 0

    score = 0
    user_input = ''

    def looping_options(greet_user):
        while True:

            user_in = input()

            score = 0
            name = greet_user

            if user_in == '!exit':
                print("Bye!")
                exit()
                break

            elif user_in == '!rating':
                if greet_user in res_dct:
                    score = int(res_dct[greet_user])
                    print("Your rating:" + str(score))

            elif user_in is None:

                print("Okay, let's start")
                user_input = input()
                comp_input = random.choice(options)

                if user_input in options:
                    if user_input == comp_input:
                        print("There is a draw ({})".format(user_input))
                        if greet_user == name:
                            res_dct[greet_user] = (int(res_dct[greet_user]) + 50)

                elif user_input == 'rock' and comp_input == 'paper':
                    print("Sorry, but computer chose {}".format(comp_input))
                elif user_input == 'scissors' and comp_input == 'rock':
                    print("Sorry, but computer chose {}".format(comp_input))
                elif user_input == 'paper' and comp_input == 'scissors':
                    print("Sorry, but computer chose {}".format(comp_input))
                else:
                    if greet_user == name:
                        res_dct[greet_user] = (int(res_dct[greet_user]) + 100)
                    else:
                        score1 = globals().score1 + 100
                        print("Well done. Computer chose {} and failed".format(comp_input))

            elif user_in == user_str:
                print("Okay, let's start")
                user_input = input()
                comp_input = random.choice(user_input_list)
                if user_input in user_input_list:


                    if user_input == comp_input:
                        print("There is a draw ({})".format(user_input))
                    if greet_user == name:
                        res_dct[greet_user] = (int(res_dct[greet_user]) + 50)

                elif user_input == 'rock' or user_input == 'spock' and comp_input == 'paper':
                    print("Sorry, but computer chose {}".format(comp_input))
                elif user_input == 'scissors' or user_input == 'lizard'and comp_input == 'rock':
                    print("Sorry, but computer chose {}".format(comp_input))
                elif user_input == 'paper' or user_input == 'lizard'and comp_input == 'scissors':
                    print("Sorry, but computer chose {}".format(comp_input))
                elif user_input == 'paper' or user_input == 'spock' and comp_input == 'lizard':
                    print("Sorry, but computer chose {}".format(comp_input))
                elif user_input == 'rock' or user_input == 'scissors' and comp_input == 'spock':
                    print("Sorry, but computer chose {}".format(comp_input))
                else:
                    if greet_user == name:
                        res_dct[greet_user] = (int(res_dct[greet_user]) + 100)
                    else:
                        score1 = globals().score1 + 100
                        print("Well done. Computer chose {} and failed".format(comp_input))
            else:
                print("Invalid input")


rps = RPS()
rps.looping_options(greet_user)
read_file.close()
