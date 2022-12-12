def group_by_owners(files):
    final_dict = {}
    for key,value in files.items():
        if value not in list(final_dict.keys()):
            final_dict[value] = []
            final_dict[value].append(key)
        else:
            final_dict[value].append(key)
    return final_dict
        
if __name__ == "__main__":    
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }   
    print(group_by_owners(files))
