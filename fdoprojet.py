from sys import argv

CACHE_LENGTH = 8
MEMORY_LENGTH = 32

GlobalCount = 1

def parse_file(file_name, L1Data, L1Addr, L1Dirt, LastUse, M):
    global GlobalCount
    try:
        file = open(file_name)
    except FileNotFoundError as error:
        raise error
    else:
        file_content = file.readlines()
        for line in file_content:
            action = line.strip().split(" ")
            if action[0] == 'R':
                read_value = read(
                            int(action[1]),
                            L1Data,
                            L1Addr,
                            L1Dirt,
                            LastUse,
                            M
                        )
            elif action[0] == 'W':
                write(
                    int(action[1]),
                    int(action[2]),
                    L1Data,
                    L1Addr,
                    L1Dirt,
                    LastUse,
                    M
                )
            else:
                raise ValueError("Wrong file format")
            GlobalCount += 1
        file.close()

def read(address, L1Data, L1Addr, L1Dirt, LastUse, M):
    index = -1
    for i in range(len(L1Addr)):
        if L1Addr[i] == address:
            index = i
            ret = L1Data[i]
            LastUse[i] = GlobalCount
            print("RD " + str(ret) + " from " + str(address) + "\thit: " + \
                  "case " + str(index) + " (LU " + str(LastUse[i]) + ")")
    if index == -1:
        ret = M[address]
        last = LastUse.index(min(LastUse))
        save_data = L1Data[last]
        if L1Dirt[last]:
            M[L1Addr[last]] = L1Data[last]
        save = L1Dirt[last]
        L1Dirt[last] = False
        L1Addr[last] = address
        L1Data[last] = ret
        LastUse[last] = GlobalCount
        print("RD " + str(ret) + " from " + str(address) + "\tmiss: " + \
              "case " + str(last) + " (LU " + str(LastUse[last]) + \
              ")", end='\t' if save else '\n')
        if save:
            print("dirty WR " + str(save_data) + " to " + str(ret))
    return ret

def write(val, address, L1Data, L1Addr, L1Dirt, LastUse, M):
    index = -1
    for i in range(len(L1Addr)):
        if L1Addr[i] == address:
            index = i
            LastUse[index] = GlobalCount
            L1Data[i] = val
            save = L1Dirt[i]
            L1Dirt[i] = True
            print("WR " + str(val) + " to " + str(address) + "\thit: case " + \
                  str(index) + " (LU " + str(LastUse[index]) + ")",
                  end='\n' if save else '\t')
            if not save:
                print("dirty!")
    if index == -1:
        M[address] = val
        last = LastUse.index(min(LastUse))
        if L1Dirt[last]:
            M[L1Addr[last]] = L1Data[last]
        save_addr = L1Addr[last]
        L1Addr[last] = address
        save_data = L1Data[last]
        L1Data[last] = val
        save = L1Dirt[last]
        L1Dirt[last] = False
        LastUse[last] = GlobalCount
        print("WR " + str(val) + " to " + str(address) + "\tmiss: victime " + \
              str(last) + " (LU " + str(LastUse[last]) + ")",
              end='\t' if save else '\n')
        if save:
            print("dirty WR " + str(save_data) + " to " + str(save_addr))
              

def main(argv):
    M = [0] * MEMORY_LENGTH
    L1Data = [0] * CACHE_LENGTH
    #The address -1 can not exist
    L1Addr = [-1] * CACHE_LENGTH
    L1Dirt = [False] * CACHE_LENGTH
    #step -1 can not exist
    LastUse = [-1] * CACHE_LENGTH
    parse_file(argv[1], L1Data, L1Addr, L1Dirt, LastUse, M)

if __name__ == "__main__":
    main(argv)
