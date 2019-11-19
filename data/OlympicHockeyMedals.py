import csv
import matplotlib.pyplot as plt

golds = []
silvers = []
bronzes = []

categories = [] # first row -> not data

with open('data/MensMedal.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			print("this is the first row  in the spreadsheet")
			categories.append(row)
			line_count += 1

		else:
			if row[7] == "Gold":
				print("won a gold medal")
				golds.append(row[7])
			elif row[7] == "Silver":
				print("won a silver medal")
				silvers.append(row[7])
			else:
				print("won a bronze medal")
				bronzes.append(row[7])

			print(line_count)
			line_count += 1

# now we can see our medal counts
print(len(golds))
print(len(silvers))
print(len(bronzes))

labels = ["Golds", "Silver", "Bronze"]
sizes = [len(golds), len(silvers), len(bronzes)]
color = ['gold', 'silver', 'darkgoldenrod']
explode = (0.1, 0.1, 0.1)

plt.pie(sizes, explode=explode, colors=color, autopct='%1.f%%', shadow=True, startangle=140)

plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("hockey Medal Wins - Historic Medal Counts")
plt.xlabel("medal Counts Since 1924")
plt.show()