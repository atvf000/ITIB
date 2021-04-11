import math
import matplotlib.pyplot as plot
import numpy


class NeuralNetwork:
    def __init__(self, eta, N, a, b, p, M):
        self.__eta = eta
        self.__N = N
        self.__a = a
        self.__b = b
        self.__p = p
        self.__M = M
        self.__k = 0
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
            self.__weight[j + 1] = self.__weight[j + 1] + self.countDeltaWeight(sigma, self.__y[i + j])

    def countDeltaWeight(self, sigma, y_j):
        return sigma * self.__eta * y_j

    def countError(self, i):
        for j in range(i, i + self.__p):
            self.__error += (self.__realY[j] - self.__y[j]) ** 2
        self.__error = math.sqrt(self.__error)

    def study(self):
        while self.__k < self.__M:
            self.__x.clear()
            self.__y.clear()
            self.__realY.clear()

            self.generateX()
            self.generateY()

            for i in range(self.__p, self.__N):
                self.__y.append(self.countNet(i - self.__p))
                self.__x.append(self.__x[-1] + (abs(self.__b) + abs(self.__a)) / self.__N)
                self.__realY.append(self.func(self.__x[i]))

                self.weightCorrect(self.__realY[i] - self.__y[i], i - self.__p)
                self.countError(i - self.__p)

            self.__k += 1

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getRealY(self):
        return self.__realY


def printGraph(x, y, realY):
    plot.plot(x, y, 'go-')
    plot.plot(x, realY, 'b-')
    plot.grid(True)
    plot.show()


def start():
    nw = NeuralNetwork(1, 20, -5, 5, 4, 4000)
    nw.study()
    printGraph(nw.getX(), nw.getY(), nw.getRealY())


if __name__ == '__main__':
    start()
