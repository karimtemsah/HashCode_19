
def read_file(filename):
    # Horizontal/Vretical is a list of pictures in the format (id, [tags])
    horizontal = []
    vertical = []
    with open(filename, 'r') as file:
        i = 0
        n = int(file.readline().strip())

        for i in range(n):
            l = file.readline().rstrip('\n').split(" ")
            if l[0] == 'H':
                horizontal.append((i, l[2:]))
            else:
                vertical.append((i, l[2:]))
    return horizontal, vertical

