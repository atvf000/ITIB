import math
import matplotlib.pyplot as plot
import numpy


class NeuralNetwork:
    def __init__(self, isThres, eta, bf, x):
        self.__isThres = isThres
        self.__eta = eta
        self.__net = 0
        self.__bf = bf
        self.__weight = [0, 0, 0, 0, 0]
        self.__errors = []
        self.__x = x

    def countNet(self, x):
        self.__net = 0
        for i in range(5):
            self.__net += x[i] * self.__weight[i]

    def funcThres(self):
        return self.__net

    def funcLogistic(self):
        return 0.5 * (self.__net / (1 + abs(self.__net)) + 1)

    def weightCorrect(self, sigma, x):
        for i in range(5):
            self.__weight[i] = self.__weight[i] + self.countDeltaweight(sigma, x[i])

    def countDeltaweight(self, sigma, x_i):
        result = sigma * self.__eta * x_i
        if not self.__isThres:
            result *= self.countDerivative()
        return result

    def countDerivative(self):
        result = 0.5 * (1 - abs(self.funcLogistic())) ** 2
        return result

    def getErrors(self):
        return self.__errors

    def study(self):
        print("|", "k".ljust(3), "|", "W".ljust(36), "|", "y".ljust(18), "|", "E".ljust(3), "|")
        print("+", "-" * 3, "+", "-" * 36, "+", "_" * 18, "+", "-" * 3)
        done = False
        epoch = 0
        while not done:
            error = 0
            y = ""
            for i in range(len(self.__x)):
                x = [1, math.floor(i // 8) % 2, math.floor(i // 4) % 2, math.floor(i // 2) % 2, math.floor(i // 1) % 2]
                if self.__isThres:
                    self.countNet(x)
                    result = self.funcThres() >= 0.0
                else:
                    self.countNet(x)

                    result = 0.5 <= self.funcLogistic()

                if result is not self.__bf[i]:
                    error += 1
                    self.weightCorrect(int(self.__bf[i]) - int(result), x)

                y += str(int(result))

            w_string = ', '.join([str("%.3f" % it) if it < 0 else str("%.4f" % it) for it in self.__weight])
            self.__errors.append([epoch, error])
            print("|", str(epoch).ljust(3), "|",  str(w_string).ljust(36), "|", str(y).ljust(18), "|",
                  str(error).ljust(3))
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

def generateX():
    x = []
    for i in range(16):
        x.append([1, math.floor(i // 8) % 2, math.floor(i // 4) % 2, math.floor(i // 2) % 2, math.floor(i // 1) % 2])
    return x

def start():
    bFunc = [False, False, False, False, True, True, False, True, False,
             False, False, False, False, False, False, False]

    bFuncSelected = [False, False, False, False, True, True, False, True]

    xSelected = [
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 1, 0],
        [1, 0, 0, 1, 1],
        [1, 0, 1, 0, 0],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 0],
        [1, 0, 1, 1, 1],
        #[1, 1, 0, 0, 0],
        #[1, 1, 0, 0, 1],
        #[1, 1, 0, 1, 0],
        #[1, 1, 0, 1, 1],
        #[1, 1, 1, 0, 0],
        #[1, 1, 1, 0, 1],
        #[1, 1, 1, 1, 0],
        #[1, 1, 1, 1, 1],
    ]

    print("Task 1", '\n')
    print("+", "-" * 3, "+", "-" * 36, "+", "_" * 18, "+", "-" * 3)
    nw1 = NeuralNetwork(True, 0.3, bFunc, generateX())
    nw1.study()
    printGraph(nw1.getErrors())
    print("+", "-" * 3, "+", "-" * 36, "+", "_" * 18, "+", "-" * 3)

    print("Task 2", '\n')
    print("+", "-" * 3, "+", "-" * 36, "+", "_" * 18, "+", "-" * 3)
    nw2 = NeuralNetwork(False, 0.3, bFunc, generateX())
    nw2.study()
    printGraph(nw2.getErrors())
    print("+", "-" * 3, "+", "-" * 36, "+", "_" * 18, "+", "-" * 3)

    print("Task 3", '\n')
    print("+", "-" * 3, "+", "-" * 36, "+", "_" * 18, "+", "-" * 3)
    nw3 = NeuralNetwork(False, 0.3, bFuncSelected, xSelected)
    nw3.study()
    printGraph(nw3.getErrors())
    print("+", "-" * 3, "+", "-" * 36, "+", "_" * 18, "+", "-" * 3)

if __name__ == '__main__':
    start()
