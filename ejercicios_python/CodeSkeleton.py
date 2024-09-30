import requests
from typing import List, Optional, Dict, Any

def fetch_data(url: str) -> Optional[Dict[str, Any]]:
    """
    Makes a GET request to the provided URL and returns the JSON data.

    Args:
        url (str): The URL to make the request to.

    Returns:
        Optional[Dict[str, Any]]: The JSON data from the response if successful, or None in case of an error.
    """

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an error for 4XX/5XX responses
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
   

def get_water_type_url() -> Optional[str]:
    """
    Retrieves the URL for the "Water" type Pokémon from the PokeAPI.

    Returns:
        Optional[str]: The URL to fetch Water-type Pokémon, or None if not found or error occurs.
    """
    url = "https://pokeapi.co/api/v2/type/"
    data = fetch_data(url)
    
    if data:
        for pokemon_type in data['results']:
            if pokemon_type['name'].lower() == 'water':
                return pokemon_type['url']
    return None

def fetch_water_pokemons() -> List[str]:
    """
    Fetches the list of all Water-type Pokémon by making an API request.

    Returns:
        List[str]: A list of names of Pokémon that are of Water type.
    """
    water_url = get_water_type_url()
    if not water_url:
        return []

    data = fetch_data(water_url)
    if not data:
        return []

    # names of all Water type Pokémon
    water_pokemons = [pokemon['pokemon']['name'] for pokemon in data['pokemon']]
    return water_pokemons

def display_pokemons(pokemons: List[str]) -> None:
    """
    Displays the names of all Water type Pokémon in a readable format.

    Args:
        pokemons (List[str]): A list of Pokémon names to be displayed.
    """
    if not pokemons:
        print("No Water type Pokémon found.")
    else:
        print("Water type Pokémon:")
        for index, pokemon in enumerate(pokemons, start=1):
            print(f"{index}. {pokemon}")


if __name__ == "__main__":
    """
    Main function to fetch and display Water type Pokémon.
    """
    water_pokemons = fetch_water_pokemons()
    display_pokemons(water_pokemons)

