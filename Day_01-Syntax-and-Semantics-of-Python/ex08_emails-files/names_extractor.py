import sys


def names_extractor():
    if len(sys.argv) != 2:
        exit()
    try:
        with open(sys.argv[1]) as file:
            new_f = open("employees.tsv", 'w')
            new_f.write("Name\tSurname\tE-mail\n")
            for i in file:
                mail = i.replace("\n", "")
                name, surname = i.split("@")[0].split(".")
                new_f.write(f"{name.capitalize()}\t{surname.capitalize()}\t{mail}\n")
            new_f.close()
    except FileNotFoundError:
        print("File is not found!")
    except Exception:
        print("Something gone wrong")


def main():
    names_extractor()


if __name__ == '__main__':
    main()
