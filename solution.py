import os


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


def naive(horizontal, vertical):
    # naive solution just outputs the input as is
    slides = []
    for h in horizontal:
        slides.append([h["id"]])

    # select verticals without any sorting
    i = 0
    while i + 1 < len(vertical):
        slides.append([vertical[i]['id'], vertical[i + 1]['id']])
        i += 2

    return slides


def output(slides, filename):
    f = open(filename, 'w')
    f.write("%d\n" % (len(slides)))
    for s in slides:
        if len(s) == 2:
            f.write("%d %d\n" % (s[0], s[1]))
        elif len(s) == 1:
            f.write("%d\n" % (s[0]))
    f.close()


if __name__ == '__main__':
    for algo in [naive]:
        if not os.path.exists("output/" + algo.__name__):
            os.makedirs("output/" + algo.__name__)
        for input_file in os.listdir('documents'):
            if input_file.endswith('txt'):
                horizontal, vertical = read_file("documents/" + input_file)
                slides = algo(horizontal, vertical)
                output(slides, "output/" + algo.__name__ + "/" + input_file[:-4] + ".out")
