"""
GET /pokemons
"""
def test_get_pokemons(db_connection, web_client):
    db_connection.seed("seeds/pokemon_store.sql")

    response = web_client.get("/pokemons")

    assert response.status_code == 200

    assert response.data.decode("utf-8") == "\n".join([
        "Pokemon(1, Bulbasaur, earth)",
        "Pokemon(2, Pikachu, electric)",
        "Pokemon(3, Mewtwo, psycho)",
        "Pokemon(4, Charizard, fire)",
        "Pokemon(5, Squirtle, water)"
    ])

"""
GET /pokemon/<id>
"""
def test_get_pokemon(db_connection, web_client):
    db_connection.seed("seeds/pokemon_store.sql")

    response = web_client.get("/pokemons/1")

    assert response.status_code == 200
    assert response.data.decode("utf-8") == "" \
        "Pokemon(1, Bulbasaur, earth)"