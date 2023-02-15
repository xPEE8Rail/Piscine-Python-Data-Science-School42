def read_and_write():
    f = open("ds.csv", "r")
    new_f = open('ds.tsv', 'w')
    check = 1
    for row in f:
        for i in row:
            if i == '"':
                check = check * (-1)
            elif i == ',':
                if check == 1:
                    new_f.write('\t')
                    continue
            new_f.write(i)
    new_f.close()
    f.close()


if __name__ == '__main__':
    read_and_write()


