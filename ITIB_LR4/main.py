import math
import matplotlib.pyplot as plot


class NeuralNetwork:
    def __init__(self, eta, x, t, N, J, M, target_epsilon):
        self.__eta = eta
        self.__x = x
        self.__t = t
        self.__N = N
        self.__J = J
        self.__M = M
        self.__epoch = 0
        self.__target_epsilon = target_epsilon
        self.__epsilon = 1

        self.__first_w = [[0] * (N + 1) for _ in range(J)]
        self.__first_net = [0] * J
        self.__first_out = [0] * J
        self.__first_error = [0] * J

        self.__second_w = [[0] * (J + 1) for _ in range(M)]
        self.__second_net = [0] * M
        self.__second_out = [0] * M
        self.__second_error = [0] * M

        self.__all_epsilon = []

    def count_first_net(self, i):
        self.__first_net[i] = self.__first_w[i][0]
        for j in range(1, self.__N + 1):
            self.__first_net[i] += self.__first_w[i][j] * self.__x[j - 1]

    def count_second_net(self, i):
        self.__second_net[i] = self.__second_w[i][0]
        for j in range(1, self.__J + 1):
            self.__second_net[i] += self.__second_w[i][j] * self.__first_out[j - 1]

    def count_f(self, net):
        return (1 - math.exp((-1) * net)) / (1 + math.exp((-1) * net))

    def count_df(self, net):
        return 0.5 * (1 - (self.count_f(net) ** 2))

    def count_epsilon(self):
        self.__epsilon = 0
        for i in range(len(self.__t)):
            self.__epsilon += (self.__t[i] - self.__second_out[i]) ** 2
        self.__epsilon = math.sqrt(self.__epsilon)

    def count_sum(self, j):
        result = 0
        for i in range(self.__M):
            result += self.__second_w[i][j] * self.__second_out[i]
        return result

    def get_epsilon(self):
        return self.__all_epsilon

    def get_epoch(self):
        return self.__epoch

    def study(self):
        done = False

        while not done:
            for i in range(self.__J):
                self.count_first_net(i)
                self.__first_out[i] = self.count_f(self.__first_net[i])

            for i in range(self.__M):
                self.count_second_net(i)
                self.__second_out[i] = self.count_f(self.__second_net[i])

            for i in range(self.__M):
                df = self.count_df(self.__second_net[i])
                self.__second_error[i] = df * (self.__t[i] - self.__second_out[i])

            for i in range(self.__J):
                df = self.count_df(self.__first_net[i])
                self.__first_error[i] = df * self.count_sum(i)

            for i in range(self.__J):
                self.__first_w[i][0] += self.__eta * self.__first_error[i]
                for j in range(self.__N):
                    self.__first_w[i][j + 1] += self.__eta * self.__x[j] * self.__first_error[i]

            for i in range(self.__M):
                self.__second_w[i][0] += self.__eta * self.__second_error[i]
                for j in range(self.__J):
                    self.__second_w[i][j + 1] += self.__eta * self.__first_out[j] * self.__second_error[i]

            self.__epoch += 1
            self.count_epsilon()
            self.__all_epsilon.append(self.__epsilon)

            print("|", str(self.__epoch).ljust(3),
                  "|", str(', '.join(str("%.3f" % it) for it in self.__second_out)).ljust(5),
                  "|", str("%.3f" % self.__epsilon).ljust(5), "|")
            done = self.__epsilon <= self.__target_epsilon

        print("+", "-" * 3, "+", "-" * 5, "+", "-" * 5, "+")


def print_graph(errors, epoch):
    ep = [[i] for i in range(epoch)]
    plot.ylabel('Epsilon')
    plot.xlabel('epoch')
    plot.plot(ep, errors, "ro-")
    plot.show()


def start():
    print("Task Full", '\n')
    print("+", "-" * 3, "+", "-" * 5, "+", "-" * 5, "+")
    print("|", "k".ljust(3), "|", "y".ljust(5), "|", "E".ljust(5), "|")
    print("+", "-" * 3, "+", "-" * 5, "+", "-" * 5, "+")

    nw = NeuralNetwork(0.5, [1, 2], [0.4], 1, 2, 1, 0.001)
    nw.study()
    print_graph(nw.get_epsilon(), nw.get_epoch())


if __name__ == '__main__':
    start()
