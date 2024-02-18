from flask import Flask, request, render_template
import pickle
import numpy as np
from numpy.linalg import norm
import requests


# Load DataFrame from the saved file
with open('Notebooks/pickles/web_200.pkl', 'rb') as file:
    df = pickle.load(file)

movies_list = df['title'].values.tolist()

""" async def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=ebed6aa40471ee69f35b136d4d71f3c3&language=en-US".format(movie_id)
    res = requests.get(url)
    data = await res.json()
    
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
  
    print("hi")
    return full_path
"""
def recommed(movie):
    Top_movies = []
    Top_movies_posters = []
    
    cosine_array = []
    index = df.loc[df['title'] == movie].index[0]
    B = df['genre_vector'][index]
    B = np.array(B)
    print(B)
    for i in df.index:
        A = df['genre_vector'][i]

        # Check for missing or invalid data (NoneType or empty vectors)
        if A is not None and len(A) > 0:
            A = np.array(A)
            cos = np.dot(A, B) / (norm(A) * norm(B))
            cosine_array.append(cos)
        else:
            cosine_array.append(0.0)  # Handle missing or invalid data with a default value

    # Now cosine_array contains the cosine similarities
    #print(cosine_array)
    sorted_with_indices = sorted(enumerate(cosine_array), key=lambda x: x[1], reverse=True)
    for i in range(1,5):
        Top_movies.append(df['title'][sorted_with_indices[i][0]])
        print("bii")
        movie_id = df['movie_id'][sorted_with_indices[i][0]]

    return Top_movies

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/moviedetails', methods=["GET","POST"])
def moviedetails():
    movie_name = request.form['hidden-input-1']
    index = df.loc[df['title'] == movie_name].index[0]
    movie_id = df['movie_id'][index]
    url = "https://api.themoviedb.org/3/movie/{}?api_key=ebed6aa40471ee69f35b136d4d71f3c3&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    genre = ', '.join([g['name'] for g in data['genres']])
    ph = ', '.join([p['name'] for p in data['production_companies']])
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    rating = ""
    if (data['adult']==True):
        rating = "adult"
    else:
        rating = "U/A"
    Top_movies = recommed(movie_name)
    
    return render_template('moviedetails.html', details=data, full_path = full_path,genres=genre,ph=ph,rating=rating,movie_names=Top_movies)

@app.route('/search')
def search():
    query = request.args.get('movie-search')
    if query:
        # Perform a case-insensitive search
        search_results = [movie for movie in movies_list if query.lower() in movie.lower()]
    else:
        # If no query provided, return all movies
        search_results = movies_list
    return render_template('recommendation.html', search_results=search_results)

@app.route("/recommendation", methods = ['GET','POST'])
def recommendation():
    
    status = False

    if request.method == "POST":
        try:
            movies_name = request.form['hidden-input']
            print(movies_name)
            Top_movies = recommed(movies_name)
            status = True
            print(Top_movies)
            return render_template("recommendation.html", movie_names = Top_movies, status = status)
        except Exception as e:
            error = {'error': e}
            return render_template("recommendation.html",error = error,status = status)
    return render_template("recommendation.html", status = status)
    

if __name__ == '__main__':
    app.degug = True
    app.run()
    