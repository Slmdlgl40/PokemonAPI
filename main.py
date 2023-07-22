import requests

while True:

    try:
        pokemon_name = input("Bir pokemon ismi girin(Çıkmak için 'q' ya basın): ")
        if pokemon_name == "q":
            break
        else:
            link = "https://pokeapi.co/api/v2/pokemon/" + pokemon_name
            response = requests.get(link)
            pokemon_data = response.json()
            print("İsim: ", pokemon_data["name"])
            print("Tür: ", [t["type"]["name"] for t in pokemon_data["types"]])
            print("Resim", pokemon_data["sprites"]["front_default"])
    except:
        print("Lütfen geçerli bir pokemon adı giriniz ve küçük harf kullanınız")
