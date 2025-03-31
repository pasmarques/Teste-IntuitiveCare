import requests as req
from bs4 import BeautifulSoup
import os
import zipfile

# URL da página onde os PDFs estão localizados.
URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

# Cabeçalho da requisição HTTP para simular um navegador e evitar bloqueios do servidor.
HEADER = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
}

# Diretório base dentro da pasta do projeto onde os arquivos serão armazenados.
BASE_FOLDER = "Teste 1"
PDF_FOLDER = os.path.join(BASE_FOLDER, "pdfs")
ZIP_FILENAME = os.path.join(BASE_FOLDER, "anexos.zip")

def search_pdfs(URL, HEADER):
    """
    Faz uma requisição HTTP para a página fornecida e busca links internos.
    Ao inspecionar com o f12 verifiquei que os links estavam dentro da classe internal-link
    Filtra apenas os links que terminam com '.pdf' e cujo texto seja 'ANEXO I' ou 'ANEXO II'.
    Retorna uma lista com os links dos arquivos PDF que atendem aos critérios.
    """
    response = req.get(URL, headers=HEADER)
    if response.status_code != 200:
        print(f'Erro {response.status_code} ao acessar a página')
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    pdf_links = [a["href"] for a in soup.find_all("a", class_="internal-link") 
                 if a["href"].endswith(".pdf") and ("ANEXO I" in a.text.upper() or "ANEXO II" in a.text.upper())]
    
    return pdf_links

def download_pdfs(pdf_links, folder):
    """
    Baixa os arquivos PDF encontrados na etapa anterior.
    Cria a pasta de destino caso ainda não exista e armazena os arquivos localmente.
    Exibe mensagens informando quais arquivos foram baixados ou se ocorreu erro na requisição.
    """
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    for link in pdf_links:
        filename = os.path.join(folder, link.split("/")[-1])
        response = req.get(link, headers=HEADER, stream=True)
        if response.status_code == 200:
            with open(filename, "wb") as f:
                for chunk in response.iter_content(1024):  # Baixa o arquivo em partes para evitar sobrecarga
                    f.write(chunk)
            print(f"Baixado: {filename}")
        else:
            print(f"Erro ao baixar {link}")

def zip_pdfs(folder, zip_filename):
    """
    Compacta todos os arquivos PDF baixados em um único arquivo ZIP.
    Percorre a pasta de PDFs, adiciona cada arquivo ao ZIP e exibe uma mensagem ao final.
    Isso facilita o armazenamento e o compartilhamento dos arquivos baixados.
    """
    with zipfile.ZipFile(zip_filename, "w") as zipf:
        for root, _, files in os.walk(folder):
            for file in files:
                zipf.write(os.path.join(root, file), file)  # Adiciona cada PDF ao arquivo ZIP
    print(f"Compactação concluída: {zip_filename}")

def main():
    """
    Função principal que executa todo o fluxo do programa.
    Primeiro, busca os links dos PDFs; depois, baixa os arquivos encontrados.
    Por fim, compacta todos os arquivos em um ZIP, caso tenha encontrado PDFs.
    """
    pdf_links = search_pdfs(URL, HEADER)
    if pdf_links:
        download_pdfs(pdf_links, PDF_FOLDER)
        zip_pdfs(PDF_FOLDER, ZIP_FILENAME)
    else:
        print("Nenhum PDF encontrado.")

# Garante que o código será executado apenas quando o script for chamado diretamente.
if __name__ == "__main__":
    main()
