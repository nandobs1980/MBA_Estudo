import requests


def main():
    print("Hello, World!!!")
    nome_pokemon = "pikachu"
    url = f"https://pokeapi.co/api/v2/pokemon/{nome_pokemon}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            dados = response.json()
            print(f"Nome: {dados['name']}")
            print(f"ID: {dados['id']}")
            print(f"Altura: {dados['height']}")
            print(f"Peso: {dados['weight']}")
            print("Habilidades:")
            for habilidade in dados["abilities"]:
                print(" -", habilidade["ability"]["name"])
        else:
            print("Pokémon não encontrado!")
    except requests.exceptions.RequestException:
        print("Falha ao conectar-se à PokeAPI.")


if __name__ == "__main__":
    main()


