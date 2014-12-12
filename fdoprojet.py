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
        

def main():
    M = [-1] * 32
    L1Data = [0] * 8
    L1Addr = [0] * 8
    L1Dirt = [False] * 8
    LastUse = [0] * 8
    GlobalCount = 0

if __name__ == '__main__':
    main()
