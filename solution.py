
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

def naive2(l1):
    slides = []
    for element in l1:
        if(type(element.get('id'))==int):
            slides.append([element.get('id')])
        else:
            slides.append(element.get('id'))
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


def minimize(verticals):
    total_vers = []
    done = []
    for ver1 in range(len(verticals)):
        if ver1 not in done:
            init_list = [ver1, ver1]
        else:
            continue
        for ver2 in range(ver1+1, len(verticals)):
            if ((len(verticals[ver1].get('tags').intersection(verticals[ver2].get('tags')))) < (len(verticals[init_list[0]].get('tags').intersection(verticals[init_list[1]].get('tags'))))) and ver2 not in done:
                init_list.pop()
                init_list.append(ver2)
        done.append(init_list[1])
        print(len(done))
        total_vers.append(
            {"id":[verticals[init_list[0]].get('id'), verticals[init_list[
                1]].get('id')],
             "tags": verticals[init_list[0]].get(
                'tags').union(verticals[init_list[1]].get('tags'))})
    return total_vers

def naive3(l1):
    slides = []
    done = []
    for var1 in range(len(l1)):
        for var2 in range(var1+1, len(l1)):
                        
    for element in l1:
        if(type(element.get('id'))==int):
            slides.append([element.get('id')])
        else:
            slides.append(element.get('id'))
    return slides




if __name__ == '__main__':
    horizontal, vertical = read_file("documents/c_memorable_moments.txt")
    verticals_horizontal = minimize(vertical) + horizontal
    slides = naive2(verticals_horizontal)
    print (slides)
    # slides = naive(horizontal, vertical)
    output(slides, "output/naive_c.txt")