import csv
import json
from collections import OrderedDict

f = open("movie_metadata.csv", encoding = "ISO-8859-1")
reader = csv.DictReader(f)
data = [row for row in reader]

#"num_critic_for_reviews", "duration", "director_facebook_likes",
#"actor_3_facebook_likes", "actor_1_facebook_likes", "gross", num_voted_users",
#"cast_total_facebook_likes", "num_user_for_reviews", "budget", "title_year",
#"actor_2_facebook_likes", "imdb_score", "aspect_ratio", "movie_facebook_likes"

def makeDict():
	movies = {}
	for row in data:
		if row["budget"] == '':
			continue
		if row["num_critic_for_reviews"] == '':
			continue
		if row["duration"] == '':
			continue
		if row["gross"] == '':
			continue
		if row["num_voted_users"] == '':
			continue
		if row["title_year"] == '':
			continue
		if row["imdb_score"] == '':
			continue

		movie_title = str(row["movie_title"].strip('åÊ'))
		title_year = int(row["title_year"].strip())
		movie_budget = int(row["budget"].strip())
		gross = int(row["gross"].strip())
		num_critic_for_reviews = int(row["num_critic_for_reviews"].strip())
		num_voted_users = int(row["num_voted_users"].strip())
		imdb_score = float(row["imdb_score"].strip())

		if movie_title not in movies:
			movies[movie_title] = {}
			movies[movie_title]["Year"] = title_year
			movies[movie_title]["Budget"] = movie_budget
			movies[movie_title]["Gross"] = gross
			movies[movie_title]["# Critics"] = num_critic_for_reviews
			movies[movie_title]["# Users"] = num_voted_users
			movies[movie_title]["IMDb Score"] = imdb_score

		else:
			continue

	return movies

formatted = makeDict()
outdata = json.dumps(formatted, indent=2)
outfile = open("formatted.json", "w")
outfile.write(outdata)
outfile.close()
