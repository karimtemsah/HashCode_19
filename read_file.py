
def read_file(filename):
    # Horizontal/Vretical is a list of pictures in the format (id, set(tags))
    horizontal = []
    vertical = []
    with open(filename, 'r') as file:
        i = 0
        n = int(file.readline().strip())

        for i in range(n):
            l = file.readline().rstrip('\n').split(" ")
            if l[0] == 'H':
                horizontal.append({"id": i, "tags": set(l[2:])})
            else:
                vertical.append({"id": i, "tags": set(l[2:])})
    return horizontal, vertical


def output(slides, filename):
    f = open(filename, 'w')
    f.writeline("%d\n".format(len(slides)))
    for s in slides:
        if len(s) == 2:
            f.writeline("%d %d\n".format(s[0], s[1]))
        elif len(s) == 1:
            f.writeline("%d %d\n".format(s[0]))
    f.close()


if __name__ == '__main__':
    