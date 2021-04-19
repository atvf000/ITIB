import math
import matplotlib.pyplot as plot


class NeuralNetwork:
    def __init__(self, eta, N, a, b, p, M):
        self.__eta = eta
        self.__N = N
        self.__a = a
        self.__b = b
        self.__p = p
        self.__M = M
        self.__epoch = 0
        self.__weight = [0] * (p + 1)
        self.__x = []
        self.__y = []
        self.__realY = []
        self.__error = 0

    def generateX(self):
        deltaX = (abs(self.__b) + abs(self.__a)) / self.__N
        for i in range(self.__p):
            self.__x.append(self.__a + i * deltaX)

    def generateY(self):
        for i in self.__x:
            self.__y.append(self.func(i))
        self.__realY = self.__y.copy()

    def func(self, x):
        return 0.5 * math.cos(0.5 * x) - 0.5

    def countNet(self, i):
        net = 0
        for j in range(0, self.__p):
            net += self.__y[i + j] * self.__weight[j]
        net += self.__weight[self.__p]
        return net

    def weightCorrect(self, sigma, i):
        for j in range(0, self.__p):
            self.__weight[j] = self.__weight[j] + self.countDeltaWeight(sigma, self.__y[i + j])

    def countDeltaWeight(self, sigma, y_j):
        return sigma * self.__eta * y_j

    def countError(self):
        for j in range(self.__N, 2 * self.__N):
            self.__error += (self.__realY[j] - self.__y[j]) ** 2
        self.__error = math.sqrt(self.__error)

    def study(self):
        while self.__epoch < self.__M:
            self.__x.clear()
            self.__y.clear()
            self.__realY.clear()

            self.generateX()
            self.generateY()

            for i in range(self.__p, self.__N):
                y = self.countNet(i - self.__p)
                self.__x.append(self.__x[-1] + (abs(self.__b) + abs(self.__a)) / self.__N)
                self.__realY.append(self.func(self.__x[i]))

                self.weightCorrect(self.__realY[i] - y, i - self.__p)
                self.__y.append(self.__realY[i])

            self.__epoch += 1

    def forecast(self):
        for i in range(self.__N, 2 * self.__N):
            self.__y.append(self.countNet(i - self.__p))
            self.__x.append(self.__x[-1] + (abs(self.__b) + abs(self.__a)) / self.__N)
            self.__realY.append(self.func(self.__x[i]))

        self.countError()

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getRealY(self):
        return self.__realY

    def getError(self):
        return self.__error

    def getWeight(self):
        return self.__weight


def printGraph(x, y, realY):
    plot.plot(x, y, 'go-')
    plot.plot(x, realY, 'b-')
    plot.grid(True)
    plot.show()

def printErrors(m, errors):
    plot.plot(m, errors, 'ro-')
    plot.grid(True)
    plot.show()


def start():
    nw1 = NeuralNetwork(1, 20, -5, 5, 4, 500)
    nw1.study()
    nw1.forecast()
    printGraph(nw1.getX(), nw1.getY(), nw1.getRealY())

    print("\nAmount of epochs 500")
    print('+', '-' * 50, '+', sep='')
    print("|", "error".ljust(6), "|", "W".ljust(39), "|")
    print('+', '-' * 50, '+', sep='')
    w_string = ', '.join([str("%.3f" % it) if it < 0 else str("%.4f" % it) for it in nw1.getWeight()])
    print("|", str("%.4f" % nw1.getError()).ljust(5), "|", w_string.ljust(39), "|")
    print('+', '-' * 50, '+', sep='')

    nw2 = NeuralNetwork(1, 20, -5, 5, 4, 2000)
    nw2.study()
    nw2.forecast()
    printGraph(nw2.getX(), nw2.getY(), nw2.getRealY())

    print("\n\nAmount of epochs 1500")
    print('+', '-' * 50, '+', sep='')
    print("|", "error".ljust(6), "|", "W".ljust(39), "|")
    print('+', '-' * 50, '+', sep='')
    w_string = ', '.join([str("%.3f" % it) if it < 0 else str("%.4f" % it) for it in nw2.getWeight()])
    print("|", str("%.4f" % nw2.getError()).ljust(5), "|", w_string.ljust(39), "|")
    print('+', '-' * 50, '+', sep='')

    errors = []
    m = [i for i in range(500, 1500, 100)]

    for i in range(len(m)):
        nwE = NeuralNetwork(1, 20, -5, 5, 4, m[i])
        nwE.study()
        nwE.forecast()
        errors.append(nwE.getError())

    printErrors(m, errors)


if __name__ == '__main__':
    start()
