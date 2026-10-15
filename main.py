import sys
from global_variables import Global_variables
from predict import predict
from training import training


def main():
    while True:
        try:
            print()
            user_choice = int(input("1 - Program: Prediction\n2 - "
                                    "Program: Training\n3 - Exit\n\nYour "
                                    "choice (1, 2 or 3): "))

            if user_choice == 1:
                predict()
            elif user_choice == 2:
                training()
            elif user_choice == 3:
                print("\n   Bye !\n")
                sys.exit()
            else:
                print("\n" + Global_variables.ERROR + " Enter 1, 2 or 3")

        except ValueError:
            print("\n" + Global_variables.ERROR + " Enter 1, 2 or 3")
        except KeyboardInterrupt:
            print("\n\nOK :/\n")
            sys.exit()

if __name__ == "__main__":
    main()
