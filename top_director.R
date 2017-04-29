director = sort(film_complete$director_name)
years = film_complete$title_year
gross = film_complete$gross
rating = film_complete$imdb_score
df1 = data.frame(director, movies, years, gross, rating)
df1
df1[df1$director %in% names(table(df1$director))[table(df1$director) >= 5],]

write.csv(top_director, file = "Director.csv")
