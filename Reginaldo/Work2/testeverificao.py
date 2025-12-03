import requests

TOKEN = "146b60256cd0c250ba42479f2744ced2811333a4cb9c5a73dae6664fcbdc675b"
API = "http://api.olhovivo.sptrans.com.br/v2.1"

session = requests.Session()

def autenticar():
    url = f"{API}/Login/Autenticar?token={TOKEN}"
    r = session.post(url)

    print("Status autenticação:", r.status_code)
    print("Resposta autenticação:", r.text)

    if r.status_code == 200 and r.json() is True:
        print("Autenticado com sucesso!")
    else:
        print("Erro ao autenticar")
        exit()


def buscar_linha_teste():
    url = f"{API}/Linha/Buscar?termosBusca=8000"
    r = session.get(url)

    print("\nStatus da busca:", r.status_code)
    print("Resposta da API (texto):")
    print(r.text)

    try:
        dados = r.json()
        print("\nJSON convertido:")
        print(dados)
    except:
        print("\nNão foi possível decodificar JSON")


if __name__ == "__main__":
    autenticar()
    buscar_linha_teste()
