import matplotlib.pyplot as plt
import random


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


def layoutConst(a, w, h):

    fs = list(range(1, len(a)+1))
    odr = list(range(1, len(a)))

    random.shuffle(fs)
    random.shuffle(odr)

    ori = [random.randrange(0, 2) for i in range(len(a)-1)]

    print("fs: ", fs)
    print("odr: ", odr)
    print("ori: ", ori)

    LC, RC, lr, ul, R = [], [], [], [], []

    n = len(fs)
    LC.insert(0, fs)

    for i in range(0, n):

        lr.append((w, 0))
        ul.append((0, h))

    j = 0

    while j != n-1:
        k = n-2
        while k >= 0:
            try:
                if (fs[odr[j]-1] in LC[k]):

                    R = LC[k]
                    break

                elif (fs[odr[j]-1] in RC[k]):

                    R = RC[k]
                    break

                k = k-1
            except IndexError:
                k = k-1

        temp = odr[j]

        if (j == 0):
            LC[j] = intersection(fs[0: temp], R)
        else:
            LC.insert(j, intersection(fs[0: temp], R))

        RC.insert(j, intersection(fs[temp:], R))

        sumA = 0
        for i in LC[j]:
            sumA = sumA + a[i-1]
        print(f"\nSum  for j = {j}: ", sumA)

        if ori[j] == 0:  # Vertical

            for i in LC[j]:

                lr[i-1] = ((ul[i-1])[0] + (sumA/(ul[i-1])[1]), (lr[i-1])[1])

            for i in RC[j]:

                ul[i-1] = ((ul[i-1])[0] + (sumA/(ul[i-1])[1]), (ul[i-1])[1])

        elif ori[j] == 1:  # Horizontal

            for i in LC[j]:

                lr[i-1] = ((lr[i-1])[0],  (ul[i-1])[1] -
                           (sumA/((lr[i-1])[0] - (ul[i-1])[0])))

            for i in RC[j]:

                ul[i-1] = ((ul[i-1])[0], (ul[i-1])[1] -
                           (sumA/((lr[i-1])[0] - (ul[i-1])[0])))

        j = j + 1

    for i in range(0, n):
        print(f"lr[{i+1}] : ", lr[i])
        print(f"ul[{i+1}] : ", ul[i])
        print("\n")

        b = (lr[i][0]-ul[i][0])
        h = (ul[i][1]-lr[i][1])
        
        print(f"Required Area for department {fs[i]}: ",b*h)


    # plt.figure(1)
    # plt.xlim([0, w])
    # plt.ylim([0, h])
    # for i in range(n):
    #     rectangle = plt.Rectangle(
    #         (ul[i][0], lr[i][1]), lr[i][0]-ul[i][0], ul[i][1]-lr[i][1], fc='green', ec="red")

    #     t1 = ul[i][0] + ((lr[i][0]-ul[i][0])/2)
    #     t2 = lr[i][1] + ((ul[i][1]-lr[i][1])/2)

    #     plt.text(t1, t2, 'D%s' % fs[i])

    #     plt.gca().add_patch(rectangle)
    # plt.show()
    return


if(__name__ == "__main__"):

    i = 1

    required_layouts = 1      # Set the layouts required

    while (i <= required_layouts):
        layoutConst([750, 600, 800, 450, 450, 500, 450], 80, 50)
        i += 1
