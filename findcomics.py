import csv
import json
from collections import OrderedDict

f = open("movie_metadata.csv")
reader = csv.DictReader(f)
data = [row for row in reader]

keywords = ["superhero"]

def makeDict(keywords):
	comic_book_movies = {}
	for row in data:
#		if row["plot_keywords"] == NULL:
#			continue
		title = str(row["movie_title"].strip())
		yes = str(row["plot_keywords"].strip())
		for keyword in keywords:
			if yes == keywords:
				if courseName not in department:
					comic_book_movies[title] = {}
					comic_book_movies[title]["Title"] = title

	return comic_book_movies






SOCWarray = majorAverageSorted(SOCWjson, SOCWMajors)
SOCWarray= makeSimpleArray(SOCWarray)
outdata = json.dumps(SOCWarray, indent=2)
outfile = open("res/SOCWarray.json", "w")
outfile.write(outdata)
outfile.close()
