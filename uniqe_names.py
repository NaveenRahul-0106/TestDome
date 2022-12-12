from itertools import chain

def unique_names(names1, names2):
    print(chain(names1,names2))
    return list(set(chain(names1, names2)))

if __name__ == "__main__":
    names1 = ["Ava", "Ava", "Olivia"]
    names2 = ["Olivia", "Ava", "Emma"]
    print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia
