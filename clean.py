import csv
import json
from collections import OrderedDict

f = open("coef_film.csv")
reader = csv.DictReader(f)
data = [row for row in reader]

#Columns = ["num_critic_for_reviews", "duration", "director_facebook_likes",
#"actor_3_facebook_likes", "actor_1_facebook_likes", "gross, num_voted_users",
#"cast_total_facebook_likes", "num_user_for_reviews", "budget", "title_year",
#"actor_2_facebook_likes", "imdb_score", "aspect_ratio", "movie_facebook_likes"]

def cleanData(notClean):
    for row in data:
        for column in notClean:
            if notClean[row[notClean]] == NULL:
                notClean[row[notClean]] = 0;

    return cleanData


#clean = cleanData(data)
#outfile.write("clean.csv")
