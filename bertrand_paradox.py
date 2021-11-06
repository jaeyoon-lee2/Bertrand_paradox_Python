import random
import math
import draw_plot


r = 1
side_of_triangle = r * math.sqrt(3)


def get_length_of_line(line):
    return math.sqrt((line[1][0] - line[0][0])**2 + (line[1][1] - line[0][1])**2)


def check_length_of_line(length: float) -> bool:
    return side_of_triangle < length


def random_endpoint_1():  # -> 1/3
    line = []
    for _ in range(2):
        theta = random.uniform(0, 2*math.pi)
        x = math.cos(theta)
        y = math.sin(theta)
        line.append([x, y])

    return line


def random_endpoint_2():  # -> 1/3
    line = []
    for _ in range(2):
        theta = random.uniform(0, 2*math.pi)
        x = math.cos(theta)
        y = math.sin(theta)
        line.append([x, y])

    return line


def random_radius():  # -> 1/2
    line = []

    theta = random.uniform(0, 2*math.pi)
    distance = random.random() * r
    # print(theta, distance)

    def linear_function(x): return (distance - math.cos(theta) * x) / \
        math.sin(theta) if theta % math.pi != 0 else (
            x/distance * math.cos(theta))*math.sqrt(1-x**2)
    xs = []
    for n in [-1, 1]:
        if theta % math.pi == 0:
            x = n * distance * math.cos(theta)
            print("wow")
        else:
            x = distance * math.cos(theta) + n * \
                math.sin(theta) * math.sqrt(1 - distance**2)
        xs.append(x)
    for x in xs:
        line.append([x, linear_function(x)])

    return line


def random_middlepoint():  # -> 1/4
    line = []

    while True:
        x1 = random.uniform(-1, 1)
        y1 = random.uniform(-1, 1)
        d = math.sqrt((x1**2) + (y1**2))

        if d < r:
            # print(x1, y1, d)
            break

    def linear_function(x):
        return (-1*x1*x + d**2) / y1 if y1 != 0 else (x/x1)*math.sqrt(1-x**2)

    xs = []
    for n in [-1, 1]:
        if y1 == 0:
            x = n * x1
            print("wow")
        else:
            x = x1 + n * math.sqrt(-1*(y1**2)*(d+1)*(d-1)) / d
        xs.append(x)
    for x in xs:
        line.append([x, linear_function(x)])

    return line


def main():
    all_probabilities = []
    N_trials = 1000

    for i in range(3):
        # lines = []  # [[[x1, y1], [x2, y2]],...]
        probabilities = []
        count = 0

        for j in range(N_trials):
            if i == 0:
                line = random_endpoint_2()
            elif i == 1:
                line = random_radius()
            else:
                line = random_middlepoint()
            length = get_length_of_line(line)
            if check_length_of_line(length):
                count += 1
            # lines.append(line)
            # print(line)
            probabilities.append(count / (j + 1))
        all_probabilities.append(probabilities)

        print("시행횟수:", j+1)
        print(str(100*count / (j + 1)) + "%")

    # draw_plot.draw_circle(lines)
    # draw_plot.probabilities_graph(probabilities)
    draw_plot.all_probabilities_graph(all_probabilities)


if __name__ == "__main__":
    main()
