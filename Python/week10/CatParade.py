"""KodNandkwajafindindexKKK"""
def main():
    """Cat"""
    animal_lst = []
    unique_animals = []
    # input
    while (animal := input()) != "END":
        if animal == "IT'S A DOG":
            del animal_lst[-1]
        else:
            animal_lst.extend(animal.split(", "))
    # count
    for name in animal_lst:
        if name not in unique_animals:
            unique_animals.append(name)
    unique_animals.sort()
    for i in unique_animals:
        count = animal_lst.count(i)
        print(f"{i} {animal_lst.index(i) + 1} {count}")
main()
