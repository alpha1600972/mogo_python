from pymongo import MongoClient
"""Information Presonnelle:
    Nom: Diallo
    Prénom: Mamadou Alpha
    Campus: Supinfo Campus Caen
    Sujet: TP3 - MongoDB"""
    
    
def get_database():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["tmdb"]
    return db