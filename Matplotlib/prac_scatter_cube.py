import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x ** 3 for x in x_values]

plt.scatter(x_values, y_values, s=1, c=y_values,
            cmap=plt.cm.Blues, edgecolors="none")

plt.title("Cube", fontsize=14)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)

plt.axis([0, 5100, 0, 5100 ** 3])
plt.tick_params(axis="both", labelsize=14)

plt.show()