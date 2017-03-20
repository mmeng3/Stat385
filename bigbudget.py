import csv
import json
from collections import OrderedDict

f = open("movie_metadata.csv", encoding = "ISO-8859-1")
reader = csv.DictReader(f)
data = [row for row in reader]

budgets = [100000, 1000000, 10000000, 100000000]

def makeDict(keywords):
	big_budget = {}
	for row in data:
		if row["budget"] == '':
			continue
		title = str(row["movie_title"].strip())
		yes = int(row["budget"].strip())
		for budget in budgets:
			if yes > budget:
				if title not in big_budget:
					big_budget[title] = {}
					big_budget[title]["Title"] = title

	return big_budget

big_budget_movies = makeDict(budgets)
outdata = json.dumps(big_budget_movies, indent=2)
outfile = open("big_budget_movies.json", "w")
outfile.write(outdata)
outfile.close()
