coef_film = read.csv(file = "coef_film.csv", header = TRUE);
# Omit all N/A cells and create a subset called Film1
Film1 = na.omit(coef_film); # 3807 elements left
# Header of Film 1
head(Film1, 0);
# Get correlation coefficients for all 15 variables
CoefFilm = as.matrix.data.frame(cor(Film1)); 
CoefFilm;


