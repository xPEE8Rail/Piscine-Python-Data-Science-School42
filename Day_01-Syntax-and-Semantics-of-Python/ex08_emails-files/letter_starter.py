import sys


def letter_starter():
    if len(sys.argv) != 2:
        exit()
    try:
        check = False

        with open("employees.tsv") as file:
            for i in file:
                inf = i.replace("\n", "").split("\t")
                if inf[2] == sys.argv[1]:
                    check = True
                    break
        if not check:
            raise RuntimeError("Such email was not found")
        return f'Dear {inf[0]}, welcome to our team. ' + \
               'We are sure that it will be a pleasure to work with you. ' + \
               'That’s a precondition for the professionals that our company hires.'

    except FileNotFoundError:
        print("File is not found!")
    except Exception:
        print("Something gone wrong")


def main():
    print(letter_starter())


if __name__ == '__main__':
    main()
