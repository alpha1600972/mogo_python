from pymongo import errors

from connection import get_database

# Connexion à la base de données
try:
    db = get_database()
    print("Connexion réussie à MongoDB !")
    movies_collection = db["movies"]
except errors.ConnectionFailure as e:
    print(f"Erreur de connexion à MongoDB : {e}")
    exit(1)

# Affichage de 5 films
def print_5_movies():
    movies = movies_collection.find().limit(5)
    for movie in movies:
        print(movie)

# Affichage de tous les films sortis en 2016
def all_movies_in_2016():
    movies_2016 = movies_collection.find({"release_date": {"$regex": "^2016"}})
    for movie in movies_2016:
        print(movie)

# Affichage de tous les films avec une note supérieure à 9
def average_vote_greater_than_9():
    movies_with_high_vote = movies_collection.find({"vote_average": {"$gt": 9}})
    for movie in movies_with_high_vote:
        print(movie)

# Affichage de tous les Films avec le genre "Action"
def movies_with_genre_action():
    action_movies = movies_collection.find({"genres": "Action"})
    for movie in action_movies:
        print(movie)

# Affichage des Films avec une popularité decroissante
def short_movies_by_popularity_descending():
    short_popular_movies = movies_collection.find({}).sort("popularity", -1)
    for movie in short_popular_movies:
        print(movie)

#Mettre à jour la note moyenne (vote_average) d'un film 
def update_average_vote_for_movie(movie_title, new_vote):
    result = movies_collection.update_one(
        {"title": movie_title},
        {"$set": {"vote_average": new_vote}}
    )
    if result.modified_count > 0:
        print(f"Movie with title '{movie_title}' updated successfully.")
    else:
        print(f"No movie found with title '{movie_title}'.")

#supprimer un film avec la note moyenne la plus basse
def delete_movies_with_minimum_vote():
    doc = movies_collection.find({"vote_average":{"$gt":0}}).sort("vote_average", 1).limit(1).toArray()[0]
    result = movies_collection.delete_one({"title": doc["title"]})
    print(f"Movie with title '{doc['title']}' deleted successfully.")

#supprimer les films sans date de sortie  
def delete_movies_whithout_release_date():
    result = movies_collection.delete_many({"release_date": ""})
    print(f"{result.deleted_count} movies without release date deleted successfully.")
 
#compter le nombre total de films   
def count_movies():
    count = movies_collection.count_documents({})
    print(f"Total number of movies: {count}")

# Affichage de tous les films avec une revenue supérieure à 500 millions et une note moyenne inférieure à 6.5
def movies_revenu_then_500_million():
    movies_with_high_revenue = movies_collection.find({"revenue": {"$gt": 500000000},"vote_average":{"$lt": 6.5}})
    for movie in movies_with_high_revenue:
        print(movie)

if __name__ == "__main__":
    print_5_movies()
    # all_movies_in_2016()
    # average_vote_greater_than_9()
    # movies_with_genre_action()
    # short_movies_by_popularity_descending()
    # update_average_vote_for_movie("Interstellar", 9.0)
    # delete_movies_with_minimum_vote()
    # delete_movies_whithout_release_date()
    # count_movies()
    # movies_revenu_then_500_million()
    print("Done!")