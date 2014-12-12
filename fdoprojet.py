from sys import argv

CACHE_LENGTH = 8
MEMORY_LENGTH = 32

GlobalCount = 1

def parse_file(file_name):
    try:
        file = open(file_name)
    except FileNotFoundError as error:
        raise error
    else:
        file_content = file.readlines()
        for line in file_content:
            action = line.strip().split(" ")
            #handle actions
        file.close()

def read(Address, L1Data, L1Addr, L1Dirt, M):
    index = -666
    for i in range(len(L1Addr)):
        if L1Addr[i] == Address:
            index = i
            ret = L1Data[i]
            LastUse[Address] = GlobalCount
            if L1Dirt[i] == True:
                M[L1Addr[i]] = L1Data[i]
            GlobalCount += 1
    if index == -666:
        ret = M[Adress]
        last = min(LastUse, key = LastUse.index)
        L1Addr[Last] = Address
        L1Data[Last] = ret
        L1Dirt[Last] = False
    return ret

def write(val, Address, L1Data, L1Addr, L1Dirt, M):
    for i in range(len(L1Addr)):
        index = i
        if L1Addr[i] == Address:
            L1Data[i] = v
            L1Dirt[i] = True
    if index == -666:
        pass

def main(argv):
    M = [0] * MEMORY_LENGTH
    L1Data = [0] * CACHE_LENGTH
    #The address -1 can not exist
    L1Addr = [-1] * CACHE_LENGTH
    L1Dirt = [False] * CACHE_LENGTH
    #step -1 can not exist
    LastUse = [-1] * CACHE_LENGTH
    parse_file(argv[1])

if __name__ == "__main__":
    main(argv)
