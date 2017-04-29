library(dplyr)
library(tidyr)
library(plyr)
library(RSentiment)

movie <- read.csv(file = "movie_metadata.csv", header = TRUE);

# Subset which include actor_1_name, movie_title, imdb_score and plot_keywords
Sentiment <- movie[c(11:12, 17, 26, 9, 24)];


# Based on these two models, num_voted_users is the most significant variable in explaining imdb_score
t1 <- count(movie$actor_1_name)[count(movie$actor_1_name)[2]>=20,];
i1 <- movie$actor_1_name %in% t1[,1];
Actor1 <- na.omit(Sentiment[i1,]);


getKeywordsList = function(df) {
  for (i in 1: nrow(df)) {
    keywordsRow = as.character(df[i,'Keywords'][[1]])
    keywords = strsplit(keywordsRow,"\\|")[[1]]
    df[i, 'Keyword1'] = keywords[1]
    df[i, 'Keyword2'] = keywords[2]
    df[i, 'Keyword3'] = keywords[3]
    df[i, 'Keyword4'] = keywords[4]
    df[i, 'Keyword5'] = keywords[5]
  }
  df[,'Keywords'] = NULL
  return(df)
}

cleanString = function(badString) {
  return(strsplit(as.character(badString),'\214\346'))
}


clean.df = Actor1 %>%
  select(Actor = actor_1_name, Score = imdb_score, Title = movie_title, Keywords = plot_keywords, Year = title_year, Gross = gross) %>%
  group_by(Actor) %>%
  filter(Score == max(Score)) %>%
  mutate(Title = as.character(cleanString(Title))) %>%
  separate(Keywords, into = paste("Keyword", 1:5, sep = ""), sep = "\\|")

write.csv(clean.df, file = "best_movie.csv")
# Calculate sentiment score
Test.Keyword <- clean.df[c(4:8)];
SScore = integer();

for (i in 1:dim(Test.Keyword)[1]){
  SScore[i] = sum(calculate_score(Test.Keyword[i,]))
}




# Movies with rating >= 7.0
test_df = Actor1 %>%
  select(Actor = actor_1_name, Rating = imdb_score, Title = movie_title, Keywords = plot_keywords, Year = title_year, Gross = gross) %>%
  group_by(Actor) %>%
  filter(Score >= 7) %>%
  mutate(Title = as.character(cleanString(Title))) %>%
  separate(Keywords, into = paste("Keyword", 1:5, sep = ""), sep = "\\|")

write.csv(test_df, file = "Good_Movies.csv")




TopDir <- read.csv(file = "top_director.csv", header = TRUE);
TopDirector.df = TopDir %>%
    select(Director = director, Title = movies, Year = years, Gross = gross, Score = rating) %>%
    group_by(Director) %>%
    filter(Score == max(Score)) %>%
    mutate(Title = as.character(cleanString(Title)))

write.csv(TopDirector.df, file = "Top_Director.csv");

  
