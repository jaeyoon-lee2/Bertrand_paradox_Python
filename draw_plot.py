import matplotlib.pyplot as plt


def all_probabilities_graph(all_probabilities):
    plt.figure(figsize=(6, 4))

    graph_info = [["Endpoint", "-b"], ["Radius", "-g"], ["Middlepoint", "-r"]]

    for idx, probabilities in enumerate(all_probabilities):
        plt.plot(list(range(1, len(probabilities)+1)),
                 probabilities, graph_info[idx][1], linewidth=0.5, label=graph_info[idx][0])

    plt.ylabel('Probabilities')
    plt.xlabel('number of trials')
    plt.title('Bertrand Paradox')
    plt.axis([0, len(all_probabilities[0]), 0, 1])
    plt.legend()
    plt.show()


def probabilities_graph(probabilities):
    plt.figure(figsize=(6, 4))

    plt.plot(list(range(1, len(probabilities)+1)),
             probabilities, '-r', linewidth=0.5)

    plt.ylabel('Probabilities')
    plt.xlabel('number of trials')
    plt.title('Bertrand Paradox')
    plt.axis([0, len(probabilities), 0, 1])
    # plt.legend()
    plt.show()


def draw_line(lines):
    for line in lines:
        x = [line[0][0], line[1][0]]
        y = [line[0][1], line[1][1]]
        plt.plot(x, y, '-b', linewidth=0.1)


def draw_circle(lines, r=1):
    plt.figure(figsize=(6, 6))

    draw_line(lines)
    plt.Circle((0, 0), r, color='black', fill=False)

    plt.ylabel('y')
    plt.xlabel('x')
    plt.title('Bertrand Paradox')
    plt.axis([-2*r, 2*r, -2*r, 2*r])
    # plt.legend()
    plt.show()
