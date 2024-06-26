from lib.pokemon import Pokemon

class PokemonRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from pokemons')
        pokemons = []
        for row in rows:
            item = Pokemon(row["id"], row["name"], row["type"])
            pokemons.append(item)
        return pokemons