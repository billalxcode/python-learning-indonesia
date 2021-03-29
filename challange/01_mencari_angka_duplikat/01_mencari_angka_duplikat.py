inpt = [[1, 2, 3, 3, 4, 5, 6], [1, 3, 4, 2, 2, 6, 6, 1]]

def cari(data):
    result = []
    temp = []
    for x in data:
        for tmp in temp:
            if tmp == x:
                result.append(x)
        temp.append(x)
    return result

def main():
    for data in inpt:
        hasil = cari(data)
        for strx in hasil:
            print ("Angka duplikat: " + str(strx))
        print ("Dengan jumlah: " + str(len(hasil)))
        print ("-" * 10)

if __name__ == "__main__":
    main()