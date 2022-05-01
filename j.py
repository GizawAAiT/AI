# import matplotlib as plt
from matplotlib import pyplot as plt

data = {'depth fs': 10, 'breadth fs': 12, "Dijkstra": 9, 'A* search': 9}
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(1, 1, figsize=(9, 3), sharey=True)
# axs.bar(names, values)
# axs[1].scatter(names, values)
axs.plot(names, values)
fig.suptitle('Length benchmarks of algorithms')

plt.show()