import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(10,5))

# -------------------
# Example 6
# -------------------
points6 = [(0,1),(0,2),(0,3),(1,1),(2,2)]
x6 = [p[0] for p in points6]
y6 = [p[1] for p in points6]

axes[0].scatter(x6, y6, color="black")

for x,y in points6:
    axes[0].text(x+0.05, y+0.05, f"({x},{y})")

axes[0].axvline(x=0, linestyle="--", color="black")

axes[0].set_xlim(-1,3)
axes[0].set_ylim(0,4)
axes[0].set_title("Example 6 – Vertical line covers 3 points")
axes[0].set_xlabel("x")
axes[0].set_ylabel("y")
axes[0].grid(True)

# -------------------
# Example 7
# -------------------
points7 = [(1,3),(2,3),(3,3),(4,3),(2,2)]
x7 = [p[0] for p in points7]
y7 = [p[1] for p in points7]

axes[1].scatter(x7, y7, color="black")

for x,y in points7:
    axes[1].text(x+0.05, y+0.05, f"({x},{y})")

axes[1].axhline(y=3, linestyle="--", color="black")

axes[1].set_xlim(0,5)
axes[1].set_ylim(1,4)
axes[1].set_title("Example 7 – Horizontal line covers 4 points")
axes[1].set_xlabel("x")
axes[1].set_ylabel("y")
axes[1].grid(True)

plt.tight_layout()
plt.show()