def match_key_combo(sequence):
    q_count = 0
    z_count = 0
    sequence_upper = sequence.upper()

    for i in range(0,len(sequence_upper)-2):
            if(sequence_upper[i]+sequence_upper[i+1]+sequence_upper[i+2]=="QEE"):
                q_count+=1
            if(sequence_upper[i]+sequence_upper[i+1]+sequence_upper[i+2]=="ZCC"):
                z_count+=1
    print(q_count)
    print(z_count)
    
    if(q_count == z_count):
        return True
    elif (q_count==0 and z_count==0):
        return True
    elif(q_count != z_count):
        return False

print(match_key_combo('QEEAZCC'))