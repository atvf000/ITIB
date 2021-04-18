import math
import matplotlib.pyplot as plot
import numpy


class NeuralNetwork:
    def __init__(self, eta, bf, x, c):
        self.__eta = eta
        self.__net = 0
        self.__bf = bf
        self.__errors = []
        self.__x = x
        self.__c = c
        self.__n = len(x[0])
        self.__J = 3
        self.__weight = [0] * (self.__J + 1)

    def countPhi(self, j, x):
        result = 0
        for i in range(0, self.__n):
            result += (x[i] - self.__c[j][i]) ** 2
        return math.exp(-1 * result)

    def countNet(self, x):
        self.__net = 0
        for j in range(self.__J):
            self.__net += self.countPhi(j, x) * self.__weight[j]
        self.__net += self.__weight[-1]

    def weightCorrect(self, sigma, x):
        for j in range(self.__J + 1):
            self.__weight[j] = self.__weight[j] + self.countDeltaWeight(sigma, j, x)

    def countDeltaWeight(self, sigma, j, x):
        if j == self.__J:
            return sigma * self.__eta
        return sigma * self.__eta * self.countPhi(j, x)


    def getErrors(self):
        return self.__errors

    def study(self):
        print("|", "k".ljust(3), "|", "W".ljust(39), "|", "y".ljust(18), "|", "E".ljust(3), "|")
        print("+", "-" * 3, "+", "-" * 39, "+", "-" * 18, "+", "-" * 3, "+")
        done = False
        epoch = 0
        while not done:
            error = 0
            y = ""
            for i in range(len(self.__x)):

                self.countNet(self.__x[i])
                result = self.__net >= 0.0

                if result is not self.__bf[i]:
                    error += 1
                    self.weightCorrect(int(self.__bf[i]) - int(result), self.__x[i])

                y += str(int(result))

            w_string = ', '.join([str("%.3f" % it) if it < 0 else str("%.4f" % it) for it in self.__weight])
            self.__errors.append([epoch, error])
            print("|", str(epoch).ljust(3), "|", str(w_string).ljust(39), "|", str(y).ljust(18), "|",
                  str(error).ljust(3), "|")
            if error == 0:
                done = True
            epoch += 1


def printGraph(errors):
    err = numpy.array(errors)
    x, y = err.T
    plot.ylabel('E')
    plot.xlabel('k')
    plot.scatter(x, y)
    plot.plot(x, y)
    plot.show()


def start():
    bFunc = [False, False, False, False, True, True, False, True, False,
             False, False, False, False, False, False, False]

    bFuncSelected = [False, False, False, False, True, True, False, True]

    xSelected = [
        [0, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 0, 1, 1],
        [0, 1, 0, 0],
        [0, 1, 0, 1],
        [0, 1, 1, 0],
        [0, 1, 1, 1],
    ]

    x = [
        [0, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 0, 1, 1],
        [0, 1, 0, 0],
        [0, 1, 0, 1],
        [0, 1, 1, 0],
        [0, 1, 1, 1],
        [1, 0, 0, 0],
        [1, 0, 0, 1],
        [1, 0, 1, 0],
        [1, 0, 1, 1],
        [1, 1, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 1, 0],
        [1, 1, 1, 1],
    ]

    c = [
        [0, 1, 0, 0],
        [0, 1, 0, 1],
        [0, 1, 1, 1],
    ]

    print("Task Full", '\n')
    print("+", "-" * 3, "+", "-" * 39, "+", "-" * 18, "+", "-" * 3, "+")
    nw1 = NeuralNetwork(0.3, bFunc, x, c)
    nw1.study()
    printGraph(nw1.getErrors())
    print("+", "-" * 3, "+", "-" * 39, "+", "-" * 18, "+", "-" * 3, "+")

    print("Task Selected", '\n')
    print("+", "-" * 3, "+", "-" * 39, "+", "-" * 18, "+", "-" * 3, "+")
    nw2 = NeuralNetwork(0.3, bFuncSelected, xSelected, c)
    nw2.study()
    printGraph(nw2.getErrors())
    print("+", "-" * 3, "+", "-" * 39, "+", "-" * 18, "+", "-" * 3, "+")


if __name__ == '__main__':
    start()
