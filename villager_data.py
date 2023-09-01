"""Functions to parse a file containing villager data."""
filename = open("villagers.csv", "r")
villager_list = list(filename)
villager_split = []

for villager in (villager_list):
    villager_split.append(villager.split('|'))

#print(villager_split)

def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """
    species = set()
    for villager in (villager_split):
        
        species.add(villager[1])
    
    # file1 = open("MyFile.txt", "r")
    # TODO: replace this with your code
    ## print(species)
    return species
print(all_species(filename))
        


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []
    print(search_string)

    for villager in villager_split:
        if search_string in ("All", villager[1]):
            villagers.append(villager[0])

    # if search_string != "All":
    #     for villager in villager_split:
    #         if villager[1] == search_string:
    #             villagers.append(villager[0])
    # else:
    #     for villager in villager_split:
    #         villagers.append(villager[0])


    # TODO: replace this with your code

    return sorted(villagers)

print(get_villagers_by_species(filename))

def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    hobbies = ['Fitness', 'Nature', 'Education', 'Music', 'Fashion', 'Play']
    

    fitness = []
    nature = []
    education = []
    music = []
    fashion = []
    play = []
    
    for villager in villager_split:
        if villager[3] == "Fitness":
            fitness.append(villager[0])
        
        elif villager[3] == "Nature":
            nature.append(villager[0])
        
        elif villager[3] == "Education":
            education.append(villager[0])

        elif villager[3] == "Music":
            music.append(villager[0])
    
        elif villager[3] == "Fashion":
            fashion.append(villager[0])
    
        elif villager[3] == "Play":
            play.append(villager[0])

    grouped_villagers = [sorted(fitness), sorted(nature), sorted(education),
                         sorted(music), sorted(fashion), sorted(play)]
    


    # TODO: replace this with your code

    return grouped_villagers

print(all_names_by_hobby(filename))


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = tuple(villager_split)

    # TODO: replace this with your code

    return all_data

print(all_data(filename))

def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code

print

def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code
