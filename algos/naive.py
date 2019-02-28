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
