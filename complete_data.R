film = read.csv("film.csv", na.strings = T, header = T)
str(film)

film_complete = film[complete.cases(film),]
str(film_complete)


combine = c(as.character(film_complete$actor_2_name),
            as.character(film_complete$actor_1_name),
            as.character(film_complete$actor_3_name))
actors = unique(combine)
actors


movies = film_complete$movie_title
a1 = film_complete$actor_1_name
a2 = film_complete$actor_2_name
a3 = film_complete$actor_3_name
df = data.frame(a1, a2, a3, movies)
df

actor1_movie = split(as.character(movies), as.character(a1))
actor2_movie = split(as.character(movies), as.character(a2))
actor3_movie = split(as.character(movies), as.character(a3))