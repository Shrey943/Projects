import matplotlib.pyplot as plt
import random


class Layout:

    def __init__(self, fs=None, ord=None, ori=None, cost=None, aspectRatioDict=None, lr=None, ul=None, type=None):
        self.fs = fs
        self.ord = ord
        self.ori = ori
        self.cost = cost
        self.aspectRatioDict = aspectRatioDict
        self.lr = lr
        self.ul = ul
        self.type = type


class AdvanceLayoutConst():

    def __init__(self, mainDep, width, height, aspectRatio,  p, cr, ar, rar, stop, u):

        self.mainDep = mainDep
        self.width = width
        self.height = height
        self.aspectRatio = {}
        self.p = p
        self.cr = cr
        self.ar = ar
        self.rar = rar
        self.stop = stop
        self.u = u
        self.worst_fbs_layout = None
        self.worst_sts_layout = None
        self.best_fbs_layout = None
        self.best_sts_layout = None
        self.layoutList = []
        self.sts_list = []
        self.fbs_list = []

        for index, element in enumerate(aspectRatio):
            self.aspectRatio[index + 1] = element

    # Main Functions

    def driverFunc(self):

        for i in range(self.p):

            layout = self.randomizedLayout()
            if (layout.type == "FBS"):
                self.fbs_list.append(layout)
            else:
                self.sts_list.append(layout)

            self.layoutList.append(layout)

        self.worst_fbs_layout = self.getWorstLayout(self.fbs_list)
        self.worst_sts_layout = self.getWorstLayout(self.sts_list)

        for i in range(self.stop):

            # Let 1 represent random selection and 2 represent consideration selection.
            # Weights is for setting the probability
            selection = random.choices(
                [1, 2], weights=[1 - self.cr, self.cr], k=1)

            newLayout = Layout()
            if (selection == 1):
                newLayout = self.randomizedLayout()
            else:
                newLayout = self.considerationLayout()

            if (newLayout.type == "FBS" and newLayout.cost < self.worst_fbs_layout.cost):

                self.fbs_list[self.fbs_list.index(
                    self.worst_fbs_layout)] = newLayout

                self.worst_fbs_layout = self.getWorstLayout(self.fbs_list)
            elif (newLayout.type == "STS" and newLayout.cost < self.worst_sts_layout.cost):

                self.sts_list[self.sts_list.index(
                    self.worst_sts_layout)] = newLayout

                self.worst_sts_layout = self.getWorstLayout(self.sts_list)

        self.best_sts_layout = self.getBestLayout(self.sts_list)
        self.best_fbs_layout = self.getBestLayout(self.fbs_list)
       # Print and display best layout
        self.display()

    def getWorstLayout(self, layoutList):

        max = -1
        layout = Layout()
        for i in layoutList:

            if (i.cost > max):
                max = i.cost
                layout = i
        return layout

    def getBestLayout(self, layoutList):

        min = 9999
        layout = Layout()
        for i in layoutList:

            if (i.cost < min):
                min = i.cost
                layout = i
        return layout

    # Function to create new child

    def considerationLayout(self):

        # Randomly select 2 layouts
        temp = random.sample(self.layoutList, 2)
        l1, l2 = temp[0], temp[1]

        # print("l1:", l1.fs);
        # print("l2:", l2.fs);

        # Choice is used for selecting 1
        cut = random.choice(list(range(1, len(l1.fs))))

        child = Layout()

        child.fs = l1.fs[:cut] + l2.fs[cut:]
        child.ord = l1.ord[:cut] + l2.ord[cut:]
        child.ori = l1.ori[:cut] + l2.ori[cut:]

        self.replaceRecurring(child.fs, l1.fs, l2.fs, cut)
        self.replaceRecurring(child.ord, l1.ord, l2.ord, cut)

        # print("\n")
        # print("fs: ", child.fs)
        # print("odr: ", child.ord)
        # print("ori: ", child.ori)

        # Let 0 represent no adjustment and 1 represent adjustment to be done.
        # Weights is for setting the probability
        adjustment = random.choices([0, 1], weights=[1, self.ar], k=1)

        if (adjustment == 1):
            self.doAdjustment(child.fs, child.ord, child.ori)

        cost, aspectRatioDict, lr, ul, type = self.calculateCost(
            child.fs, child.ord, child.ori)

        child.aspectRatioDict = aspectRatioDict
        child.lr = lr
        child.ul = ul
        child.type = type

        # Penalty Check
        cost = cost * self.penaltyCheck(child)

        child.cost = cost

        return child

        # print("OFV = ", cost)

        # if ((not self.best_layout) or (cost < self.best_layout.cost)):
        #     self.best_layout = child

        # self.layoutList.append(child)

    # Function to replace recurring elements from child

    def replaceRecurring(self, l, l1, l2, cut):

        temp = []

        for index, element in enumerate(l):
            if (element in temp):
                n = self.nonCommon(l, l1, l2, cut)
                if (n):
                    l[index] = n

            else:
                temp.append(element)

    # Function to get value from parent layout which is not present in child layout
    def nonCommon(self, child, l1, l2, cut):

        for j in l1[cut:]:
            if j not in child:
                return j

        for k in l2[:cut]:
            if k not in child:
                return k

        return None

    # Function to do adjustments
    def doAdjustment(self, fs, ord, ori):

        # Well we can have all weights as 1 also but no problem in that one too
        adjustment = random.choices([1, 2, 3, 4], weights=[
                                    0.25, 0.25, 0.25, 0.25], k=1)

        if (adjustment == 1):

            # selecting any 2 index to swap department values
            index1, index2 = map(int, random.sample(
                list(range(0, len(fs))), 2))

            fs[index1], fs[index2] = fs[index2], fs[index1]

        elif(adjustment == 2):

            index1, index2 = map(int, random.sample(
                list(range(0, len(ord))), 2))

            ord[index1], ord[index2] = ord[index2], ord[index1]

        elif(adjustment == 3):

            # selecting any 2 indexs, 1st the value to be displaced and 2nd the position
            index1, index2 = map(int, random.sample(
                list(range(0, len(fs))), 2))

            val = fs.pop(index1)
            fs.insert(index2, val)

        else:

            # selecting any 2 indexs, 1st the value to be displaced and 2nd the position
            index1, index2 = map(int, random.sample(
                list(range(0, len(ord))), 2))

            val = ord.pop(index1)
            ord.insert(index2, val)

        # Re-Adjustment(1: Do readjustment, 0: Don't)
        readjustment = random.choices([0, 1], weights=[1, self.rar], k=1)

        if (readjustment == 1):

            for index, element in enumerate(ori):
                if (element == 0):
                    ori[index] = 1
                else:
                    ori[index] = 0

        return

    # function to check penalty
    def penaltyCheck(self, newLayout):

        v = 0
        for i in newLayout.fs:

            if (newLayout.aspectRatioDict[i] > self.aspectRatio[i]):
                v += 1

        return (self.u**v)

        # Function to create randomized layouts
    def randomizedLayout(self):
        fs = list(range(1, len(self.mainDep)+1))
        odr = list(range(1, len(self.mainDep)))

        random.shuffle(fs)
        random.shuffle(odr)

        ori = [random.randrange(0, 2) for i in range(len(self.mainDep)-1)]

        # print("fs: ", fs)
        # print("odr: ", odr)
        # print("ori: ", ori)
        cost, aspectRatioDict, lr, ul, type = self.calculateCost(fs, odr, ori)

        new = Layout(fs, odr, ori, cost, aspectRatioDict, lr, ul, type)

        # Penalty Check
        cost = cost * self.penaltyCheck(new)

        new.cost = cost

        return new

        # print("OFV = ", cost)

        # if ((not self.best_layout) or (cost < self.best_layout.cost)):
        #     self.best_layout = new

        # self.layoutList.append(new)

    def intersection(self, lst1, lst2):
        lst3 = [value for value in lst1 if value in lst2]
        return lst3

    # Function to calculate Cost
    def calculateCost(self, fs, odr, ori):
        LC, RC, lr, ul, R = [], [], [], [], []
        ff = [[0, 0, 0, 5, 5, 0, 0, 0, 1],
              [0, 0, 0, 3, 3, 0, 0, 0, 1],
              [0, 0, 0, 2, 2, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 4, 4, 0, 0],
              [0, 0, 0, 0, 0, 3, 0, 0, 4],
              [0, 0, 0, 0, 0, 0, 0, 0, 2],
              [0, 0, 0, 0, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0], ]

        n = len(fs)
        LC.insert(0, fs)

        for i in range(0, n):

            lr.append((self.width, 0))
            ul.append((0, self.height))

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
                LC[j] = self.intersection(fs[0: temp], R)
            else:
                LC.insert(j, self.intersection(fs[0: temp], R))

            RC.insert(j, self.intersection(fs[temp:], R))

            sumA = 0
            for i in LC[j]:
                sumA = sumA + self.mainDep[i-1]

            if ori[j] == 0:  # Vertical

                for i in LC[j]:

                    lr[i-1] = ((ul[i-1])[0] +
                               (sumA/((ul[i-1][1]-lr[i-1][1]))), (lr[i-1])[1])

                for i in RC[j]:

                    ul[i-1] = ((ul[i-1])[0] +
                               (sumA/((ul[i-1][1]-lr[i-1][1]))), (ul[i-1])[1])

            elif ori[j] == 1:  # Horizontal

                for i in LC[j]:

                    lr[i-1] = ((lr[i-1])[0],  (ul[i-1])[1] -
                               (sumA/((lr[i-1])[0] - (ul[i-1])[0])))

                for i in RC[j]:

                    ul[i-1] = ((ul[i-1])[0], (ul[i-1])[1] -
                               (sumA/((lr[i-1])[0] - (ul[i-1])[0])))

            j = j + 1

        # print("\n\nNew Layout: ")
        aspectRatioDict = {}
        cordinates = []
        for i in range(0, n):

            w = (lr[i][0]-ul[i][0])
            h = (ul[i][1]-lr[i][1])

            ar = max([w, h]) / min([w, h])

            # print("\n")
            # print(f"Aspect Ratio for department {fs[i]}: ",ar)
            # print(f"Area for department {fs[i]}: ", w*h)

            aspectRatioDict[fs[i]] = ar

            cordinates.append(
                [(ul[i][0], lr[i][1]), w, h])

        cost = 0
        for j in range(0, n):
            for i in range(0, n):

                dist = abs(lr[i][0]/2+ul[i][0]/2 - lr[j][0]/2-ul[j][0]/2) + \
                    abs(ul[i][1]/2+lr[i][1]/2 - ul[j][1]/2-lr[j][1]/2)
                cost = cost + dist * ff[i][j]

        type = self.getType(cordinates, ori)

        # print("\nOFV =", cost)
        return (cost, aspectRatioDict, lr, ul, type)

    # To display best layout
    def display(self):

        print("The best FBS layout is: ")
        print("\nDepartment Sequence: ", self.best_fbs_layout.fs)
        print("Cut Sequence: ", self.best_fbs_layout.ord)
        print("Cut Code: ", self.best_fbs_layout.ori)

        for i in range(0, len(self.best_fbs_layout.fs)):

            w = (self.best_fbs_layout.lr[i][0]-self.best_fbs_layout.ul[i][0])
            h = (self.best_fbs_layout.ul[i][1]-self.best_fbs_layout.lr[i][1])

            print("height,width: ", h, w)

            ar = max([w, h]) / min([w, h])

            print("\n")
            print(
                f"Aspect Ratio for department {self.best_fbs_layout.fs[i]}: ", ar)
            print(f"Area for department {self.best_fbs_layout.fs[i]}: ", w*h)

        print("\nWith the OFV of ", self.best_fbs_layout.cost)

        print("Here's the layout:")

        plt.figure(1)
        plt.xlim([0, self.width])
        plt.ylim([0, self.height])

        for i in range(len(self.best_fbs_layout.fs)):

            h = self.best_fbs_layout.ul[i][1]-self.best_fbs_layout.lr[i][1]
            w = self.best_fbs_layout.lr[i][0]-self.best_fbs_layout.ul[i][0]

            rectangle = plt.Rectangle(
                (self.best_fbs_layout.ul[i][0], self.best_fbs_layout.lr[i][1]), w, h, fc='green', ec="red")

            plt.text(self.best_fbs_layout.lr[i][0]/2+self.best_fbs_layout.ul[i][0]/2,
                     self.best_fbs_layout.ul[i][1]/2+self.best_fbs_layout.lr[i][1]/2, 'dpt%s' % (i+1))
            plt.gca().add_patch(rectangle)

        plt.title("FBS Layout")
        plt.show()

        # STS

        print("\n\nThe best STS layout is: ")
        print("\nDepartment Sequence: ", self.best_sts_layout.fs)
        print("Cut Sequence: ", self.best_sts_layout.ord)
        print("Cut Code: ", self.best_sts_layout.ori)

        for i in range(0, len(self.best_sts_layout.fs)):

            w = (self.best_sts_layout.lr[i][0]-self.best_sts_layout.ul[i][0])
            h = (self.best_sts_layout.ul[i][1]-self.best_sts_layout.lr[i][1])

            print("height,width: ", h, w)

            ar = max([w, h]) / min([w, h])

            print("\n")
            print(
                f"Aspect Ratio for department {self.best_sts_layout.fs[i]}: ", ar)
            print(f"Area for department {self.best_sts_layout.fs[i]}: ", w*h)

        print("\nWith the OFV of ", self.best_sts_layout.cost)

        print("Here's the layout:")

        plt.figure(1)
        plt.xlim([0, self.width])
        plt.ylim([0, self.height])

        for i in range(len(self.best_sts_layout.fs)):

            h = self.best_sts_layout.ul[i][1]-self.best_sts_layout.lr[i][1]
            w = self.best_sts_layout.lr[i][0]-self.best_sts_layout.ul[i][0]

            rectangle = plt.Rectangle(
                (self.best_sts_layout.ul[i][0], self.best_sts_layout.lr[i][1]), w, h, fc='green', ec="red")

            plt.text(self.best_sts_layout.lr[i][0]/2+self.best_sts_layout.ul[i][0]/2,
                     self.best_sts_layout.ul[i][1]/2+self.best_sts_layout.lr[i][1]/2, 'dpt%s' % (i+1))
            plt.gca().add_patch(rectangle)

        plt.title("STS Layout")
        plt.show()

    def getType(self, coordinates, oriL):

        vl = self.vertical_lines(coordinates)
        if (vl >= 1 and vl == oriL.count(0)):
            return "FBS"

        hl = self.horizontal_lines(coordinates)
        if (hl >= 1 and hl == oriL.count(1)):
            return "FBS"

        else:
            return "STS"

    def vertical_lines(self, coordinates):

        done = []
        num = 0
        for i in coordinates:

            height = 0

            if i[0][0] not in done:

                done.append(i[0][0])
                for j in coordinates:
                    if (j[0][0] == i[0][0]):
                        try:
                            height = height + j[2]
                        except IndexError:
                            print("overflow")

            if (height == self.height):
                num += 1

        return num - 1

    def horizontal_lines(self, coordinates):

        done = []
        num = 0
        for i in coordinates:

            width = 0

            if i[0][1] not in done:

                done.append(i[0][1])
                for j in coordinates:
                    if (j[0][1] == i[0][1]):
                        try:
                            width = width + j[1]
                        except IndexError:
                            print("overflow")

            if (width == self.width):
                num += 1

        return num - 1


if(__name__ == "__main__"):

    layout = AdvanceLayoutConst(
        mainDep=[16, 16, 16, 36, 36, 9, 9],
        width=13,
        height=12,
        aspectRatio=[4, 4, 4, 4, 4, 4, 4],
        p=1000,
        cr=0.78,
        ar=.21,
        rar=.1,
        stop=1000,
        u=4)

    layout.driverFunc()
