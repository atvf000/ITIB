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
        self.__net = 0
        self.__weight = [0] * (p + 1)
        self.__x = []
        self.__y = []

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

    def countNet(self, y):
        self.__net = 0
        for i in range(self.__p + 1):
            self.__net += y[i] * self.__weight[i]

    def funcActivation(self):
        return self.__net

    def weightCorrect(self, sigma, y):
        for i in range(self.__p + 1):
            self.__weight[i] = self.__weight[i] + self.countDeltaweight(sigma, y[i])

    def countDeltaweight(self, sigma, x_i):
        return sigma * self.__eta * x_i

    def study(self):
        self.generateX()
        self.generateY()

        while self.__k < self.__M:

            for i in range(self.__p, self.__N):
                self.__y[i] = self.countNet()

            self.__k += 1


#def printGraph(errors):




def start():



    nw = NeuralNetwork(0.3)
    nw.study()


if __name__ == '__main__':
    start()
