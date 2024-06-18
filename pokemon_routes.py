from lib.database_connection import get_flask_database_connection
from lib.pokemon_repository import PokemonRepository
from lib.pokemon import Pokemon
from flask import request

def apply_pokemon_routes(app):
    @app.route('/pokemons', methods=['GET'])
    def get_pokemons():
        connection = get_flask_database_connection(app)
        pokemon_repository = PokemonRepository(connection)
        return "\n".join([
            str(pokemon) for pokemon in pokemon_repository.all()
        ])