movie.data = read.csv("coef_film.csv", header = TRUE)
new.data = movie.data[complete.cases(movie.data),]

str(new.data)
limfit = lm(aspect_ratio ~ num_critic_for_reviews 
            + duration 
            + director_facebook_likes 
            + actor_3_facebook_likes
            + actor_1_facebook_likes
            + num_voted_users
            + cast_total_facebook_likes
            + num_user_for_reviews
            + budget
            + title_year
            + actor_2_facebook_likes
            + imdb_score
            + movie_facebook_likes,
            data = movie.data)
summary(limfit)


