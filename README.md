﻿# MovieHub-recommendations

This project is created using Tmdb 5000 dataset (https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) and Word2Vec text representation to convert the text data we have about the movies and turn them into vectors on which we can do computation on. I used cosine similarity between the vectors to find similar movie recommendations. The python code for the model is the notebok folder and the dataset can be downloaded form kaggle. This website uses flask for the backend.

To run the website:
1) import the code into you machine.
2) first run the jupyter notebook code to get the model ready and wrap it in a pickle.
3) use the pickle of our model in the flask app to get the model in the backend.
4) run python app.py in your terminal, make sure you are in the right directory.

#Images
 The home page:
 ![image](https://github.com/GeethKrishna/MovieHub-recommendations/assets/96900928/451f9131-88e4-4cda-8610-f7ea6cb278f1)

 The search page:
 ![image](https://github.com/GeethKrishna/MovieHub-recommendations/assets/96900928/0bacbdf8-7e18-4a42-9630-a5b23e5b5258)

The recommendations:
![image](https://github.com/GeethKrishna/MovieHub-recommendations/assets/96900928/e8256bca-8234-478b-995a-57a05153ad2d)

Details of the movie and futher recommendations:
![image](https://github.com/GeethKrishna/MovieHub-recommendations/assets/96900928/38a34687-15b5-45c5-9777-80a96d03d231)

![image](https://github.com/GeethKrishna/MovieHub-recommendations/assets/96900928/1e159182-9610-49be-a382-38d041ac67b3)
