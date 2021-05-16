import math


class NeuralNetwork:
    def __init__(self, matrix_size, original):
        self.__matrix_size = matrix_size
        self.__matrix = [[0] * (matrix_size) for _ in range(matrix_size)]
        self.__K = matrix_size
        self.__original = original
        self.count_matrix()

    def count_f_net(self, net, pred_f_net):
        if net > 0:
            return 1
        elif net < 0:
            return -1
        else:
            return pred_f_net

    def count_net(self, y, k):
        net = 0
        for j in range(self.__K):
            if j != k:
                net += self.__matrix[j][k] * y[j]
        return net

    def count_weight(self, j, k):
        sum = 0
        for i in range(len(self.__original)):
            sum += self.__original[i][j] * self.__original[i][k]
        return sum

    def count_matrix(self):
        for j in range(self.__matrix_size):
            for k in range(self.__matrix_size):
                if j == k:
                    self.__matrix[j][k] = 0
                else:
                    self.__matrix[j][k] = self.count_weight(j, k)

    def has_change(self, pred_result, result):
        for i in range(len(result)):
            if result[i] != pred_result[i]:
                return False
        return True

    def recognize(self, sample):
        size = len(sample)
        pred_result = [0] * size
        result = sample
        has_change = False

        while not has_change:
            for k in range(size):
                result[k] = self.count_f_net(self.count_net(result, k), pred_result[k])

            has_change = self.has_change(pred_result, result)
            pred_result = result

        return result

def print_pattern(sample, raw, col):
    result = ''
    for i in range(col):
        for j in range(raw):
            if sample[raw * i + j] == -1:
                result += "   "
            else:
                result += " * "
        result += "\n"
    print(result)


def start():

    sample_zero = [1,  1,  1, 1, -1,  1, 1, -1,  1, 1, -1,  1, 1,  1,  1]
    sample_one = [-1,  1, -1, 1,  1, -1, -1,  1, -1, -1,  1, -1, 1,  1,  1]
    sample_eight = [1,  1,  1, 1, -1,  1, 1,  1,  1, 1, -1,  1, 1,  1,  1]

    broken_sample_zero = [1,  -1,  1, 1, -1,  1, 1, -1,  1, 1, -1,  1, 1,  1,  1]
    broken_sample_one = [-1,  1, -1, 1,  1, -1, -1,  1, -1, -1,  -1, -1, 1, 1,  1]
    broken_sample_eight = [1,  1,  1, 1, 1,  1, 1,  1,  1, 1, 1,  1, 1,  1,  1]

    x = [sample_zero, sample_one, sample_eight]

    nw = NeuralNetwork(3 * 5, x)


    print("-" * 10, "Sample one", "-" * 10)
    print_pattern(sample_one, 3, 5)
    print_pattern(broken_sample_one, 3, 5)
    restored_one = nw.recognize(broken_sample_one)
    print_pattern(restored_one, 3, 5)

    print("-" * 10, "Sample zero", "-" * 10)
    print_pattern(sample_zero, 3, 5)
    print_pattern(broken_sample_zero, 3, 5)
    restored_one = nw.recognize(broken_sample_zero)
    print_pattern(restored_one, 3, 5)

    print("-" * 10, "Sample eight", "-" * 10)
    print_pattern(sample_eight, 3, 5)
    print_pattern(broken_sample_eight, 3, 5)
    restored_eight = nw.recognize(broken_sample_eight)
    print_pattern(restored_eight, 3, 5)


if __name__ == '__main__':
    start()