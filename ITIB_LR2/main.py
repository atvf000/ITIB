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
        self.__error = 0

    def generateX(self):
        x = []
        for i in range(self.__a, self.__b, (abs(self.__b) + abs(self.__a)) / self.__N):
            x.append(i)
        return x

    def generateY(self):
        y = []
        for i in self.__x:
            y.append(self.func(i))

    def func(self, x):
        return 0.5 * math.cos(0.5 * x) - 0.5

    def countNet(self, i):
        net = 0
        for j in range(1, self.__p + 1):
            net += self.__y[i + j] * self.__weight[j]
        return net

    def weightCorrect(self, sigma, i):
        for j in range(1, self.__p + 1):
            self.__weight[j] = self.__weight[j] + self.countDeltaWeight(sigma, self.__y[i + j])

    def countDeltaWeight(self, sigma, y_j):
        return sigma * self.__eta * y_j

    def countError(self, i):
        for j in (1,self.__p):
            self.__error += (self.__x[i] - self.__x[i + j]) ** 2
        self.__error = math.sqrt(self.__error)

    def study(self):
        self.generateX()
        self.generateY()

        while self.__k < self.__M:

            for i in range(self.__p, self.__N):
                self.__y[i] = self.countNet(i)

                self.__x[i] = self.__x[-1] + (abs(self.__b) + abs(self.__a)) / self.__N
                self.weightCorrect(self.func(self.__x[i]) - self.__y[i], i)
                self.countError(i)

            self.__k += 1

def start():

    nw = NeuralNetwork(1, 20, -5, 5, 4, 100)
    nw.study()


if __name__ == '__main__':
    start()
