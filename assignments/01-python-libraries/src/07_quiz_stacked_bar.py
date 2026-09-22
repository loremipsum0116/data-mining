from pathlib import Path

import matplotlib.pyplot as plt

languages1 = ["Python", "Python", "Python", "Python"]
languages2 = ["C", "C", "C", "C++"]
languages3 = ["Java", "C++", "C++", "Java"]

# TIOBE Rating (%)
y1 = [13.58, 16.36, 13.97, 23.28]  # 1st
y2 = [12.44, 16.26, 11.44, 10.29]  # 2nd
y3 = [10.66, 12.91, 9.96, 10.15]  # 3rd

x = range(len(y1))

bottom1 = [a + b for a, b in zip(y3, y2)]

bar3 = plt.bar(x, y3, width=0.7, color="yellow", label="3rd")
bar2 = plt.bar(x, y2, width=0.7, color="orange", bottom=y3, label="2nd")
bar1 = plt.bar(x, y1, width=0.7, color="red", bottom=bottom1, label="1st")

plt.title("Top 3 Programming Languages by TIOBE Index, January 2022–2025")
plt.xlabel("Year")
plt.ylabel("Popularity (%)")

xLabel = ["2022", "2023", "2024", "2025"]
plt.xticks(x, xLabel, fontsize=10)

plt.legend([bar1, bar2, bar3], ["1st", "2nd", "3rd"])

for i in range(len(y1)):
    # 3위
    plt.text(i, y3[i] / 2, f"{languages3[i]} ({y3[i]}%)", ha="center", va="center")

    # 2위
    plt.text(
        i, y3[i] + y2[i] / 2, f"{languages2[i]} ({y2[i]}%)", ha="center", va="center"
    )

    # 1위
    plt.text(
        i,
        bottom1[i] + y1[i] / 2,
        f"{languages1[i]} ({y1[i]}%)",
        ha="center",
        va="center",
    )

output_dir = Path(__file__).resolve().parents[1] / "figures"
output_dir.mkdir(exist_ok=True)
plt.savefig(output_dir / "tiobe_stacked_bar.png", dpi=180, bbox_inches="tight")
if plt.get_backend().lower() != "agg":
    plt.show()
