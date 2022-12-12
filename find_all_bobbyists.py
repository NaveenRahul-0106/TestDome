def find_all_hobbyists(hobby, hobbies):
    final_list = []
    for person in hobbies:
        if hobby in hobbies[person]:
            final_list.append(person)
    return final_list 

if __name__ == "__main__":
    hobbies = { 
        "Steve": ['Fashion', 'Piano', 'Reading'],
        "Patty": ['Drama', 'Magic', 'Pets'],
        "Chad": ['Puzzles', 'Pets', 'Yoga']
    }
    
    print(find_all_hobbyists('Yoga', hobbies))