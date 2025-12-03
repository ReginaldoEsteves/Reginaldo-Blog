import requests
import random
import folium

TOKEN = "146b60256cd0c250ba42479f2744ced2811333a4cb9c5a73dae6664fcbdc675b"
BASE_URL = "http://api.olhovivo.sptrans.com.br/v2.1"


session = requests.Session()

def autenticacao():
    url = f"{BASE_URL}/Login/Autenticar?token={TOKEN}"
    r = session.post(url)

    if r.status_code == 200:
        return r.json()
    return False

def buscar_linhas_ativas():
    url = f"{BASE_URL}/Posicao"
    r = session.get(url)

    if r.status_code != 200:
        print("Erro ao obter veículos:", r.text)
        return []

    dados = r.json()

    if "l" not in dados:
        print("Resposta inesperada:", dados)
        return []

    linhas = dados["l"]

    return [linha for linha in linhas if len(linha.get("vs", [])) > 0]

def gerar_mapa(linha):
    nome = linha["c"]
    veiculos = linha["vs"]

    lat = veiculos[0]["py"]
    lon = veiculos[0]["px"]

    mapa = folium.Map(location=[lat, lon], zoom_start=13)

    for v in veiculos:
        folium.Marker([v["py"], v["px"]], popup=str(v["p"])).add_to(mapa)

    output = f"mapa_linha_{nome}.html"
    mapa.save(output)
    print("Mapa gerado:", output)

if autenticacao():
    print("Autenticado com sucesso.")
else:
    print("Falha na autenticação.")
    exit()

print("Buscando linhas ativas...")
linhas_ativas = buscar_linhas_ativas()

print("Total de linhas com ônibus:", len(linhas_ativas))

if not linhas_ativas:
    print("Nenhuma linha ativa encontrada. A API deve ter retornado vazio.")
    exit()

linha_escolhida = random.choice(linhas_ativas)
print("Linha escolhida:", linha_escolhida["c"])

gerar_mapa(linha_escolhida)
