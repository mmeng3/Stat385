import csv
import json
from collections import OrderedDict

f = open("movie_metadata.csv", encoding = "ISO-8859-1")
reader = csv.DictReader(f)
data = [row for row in reader]

budgets = [200000000, 100000000, 50000000, 25000000, 10000000, 5000000, 1000000]

def makeDict(budgets):
	big_budget = {}
	for row in data:
		if row["budget"] == '':
			continue
		movie_title = str(row["movie_title"].strip())
		movie_budget = int(row["budget"].strip())
		for budget in budgets:
			big_budget[str(budget)] = {}
			if movie_budget > budget:
				big_budget[str(budget)]["Title"] = movie_title

				else:
					 continue

	return big_budget

big_budget_movies = makeDict(budgets)
outdata = json.dumps(big_budget_movies, indent=2)
outfile = open("big_budget_movies.json", "w")
outfile.write(outdata)
outfile.close()
