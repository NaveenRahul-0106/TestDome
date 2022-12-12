def tuple_slice(startIndex, endIndex, tup):
    sl = ""
    for i in range(startIndex,endIndex):
        if i != endIndex-1:
            sl+=str(tup[i])+","
        else:
            sl+=str(tup[i])

    return sl

if __name__ == "__main__":
    print(tuple_slice(1, 4, (76, 34, 13, 64, 12)))