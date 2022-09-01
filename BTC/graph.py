import matplotlib.pyplot as plt
import numpy as np

def draw_graph(result, x, y):
    for i in result:
        x.append(i[0])
        y.append(i[1])
    fig, ax = plt.subplots()
    ax.set_title('Курс биткоина в зависимости от даты')
    plt.ylabel('Цена')
    ax.plot(x, y, color='g')
    plt.xticks(np.arange(0, len(x) + 1, int(len(x)/12)), rotation='vertical')
    plt.show()

