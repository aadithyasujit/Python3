Myarr = (1, 2, 3, 4, 5, 6, 7, 8, 9)
sumto = int(12)

def Sumcheck(Myarr, sumto):
    count = int(0)
    First = []
    Second = []
    for i in range(len(Myarr)):

        # print(Myarr[i])

        for j in range(len(Myarr)):

            if (i == j):

                j = j + 1

            else:

                if (Myarr[i] + Myarr[j] == sumto):
                    First.append(Myarr[i])
                    Second.append(Myarr[j])
                    count = count + 1

        continue

    print(count, "pairs sum up to", sumto)

    for i in range(len(First)):

        print("Pair",i+1,":[", First[i], ",", Second[i],"]")

        continue

Sumcheck(Myarr, sumto)
