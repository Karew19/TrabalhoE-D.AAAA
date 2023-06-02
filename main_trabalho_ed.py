import os
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity

# Carregar os dados de avaliações de filmes
ratings_data = pd.read_csv("ratings.csv")

# Carregar os dados dos filmes
movies_data = pd.read_csv('movies.csv')

# Criar a matriz esparsa das avaliações
ratings_matrix = csr_matrix((ratings_data['rating'], (ratings_data['userId'], ratings_data['movieId'])))

# Calcular a similaridade entre os filmes usando a similaridade de cosseno
movie_similarity = cosine_similarity(ratings_matrix.T, dense_output=False)

# Função para recomendar filmes com base em um ID de usuário
def recommend_movies(user_id, top_n=5):
    # Obter a linha de similaridades para o usuário de referência
    user_ratings = ratings_matrix[user_id]
    sim_scores = cosine_similarity(user_ratings, ratings_matrix)[0]
    # Obter os índices dos filmes com maior similaridade
    top_indices = sim_scores.argsort()[::-1][:top_n]

    return top_indices

# Função para obter o nome do filme a partir do ID
def get_movie_name(movie_id):
    
    if movie_id in movies_data['movieId'].values:
        title = movies_data[movies_data['movieId'] == movie_id]['title'].values[0]
        return title
    else:  
        return 0

while(1):
# Obter o ID do usuário para obter as recomendações
    user_id = int(input("Digite o ID do usuário para obter as recomendações de filmes: "))

    # Verificar se o ID do usuário existe nos dados
    if user_id not in ratings_data['userId'].unique():
        print("ID de usuário inválido.")
    else:
        # Obter as recomendações de filmes para o usuário
        recommended_movies = recommend_movies(user_id)

        # Imprimir os nomes dos filmes recomendados
        print("Filmes recomendados para o usuário de referência (ID: {}):".format(user_id))
        for movie in recommended_movies:
            movie_name = get_movie_name(movie)
            if movie_name != 0:
                print("{} - {}".format(movie, movie_name))

    os.system('PAUSE')
    os.system('cls')