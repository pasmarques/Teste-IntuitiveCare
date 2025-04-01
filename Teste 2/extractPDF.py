import pandas as pd
import zipfile
import os
from pdfminer.high_level import extract_text
from pdfminer.high_level import extract_text
from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams
from io import StringIO

def extract_table_from_pdf(pdf_path):
    """Extrai o texto do PDF e estrutura os dados em uma tabela."""
    output_string = StringIO()
    with open(pdf_path, "rb") as file:
        extract_text_to_fp(file, output_string, laparams=LAParams(), output_type='text')
    
    text = output_string.getvalue()
    linhas = text.split("\n")
    
    # Processamento básico para capturar tabelas (deve ser refinado conforme o formato do PDF)
    tabela = []
    for linha in linhas:
        colunas = linha.split()  # Supondo que os dados estejam separados por espaço
        if len(colunas) > 2:  # Ajustar conforme o formato do PDF
            tabela.append(colunas)
    
    return tabela

def process_data(tabela):
    """Transforma os dados extraídos em um DataFrame estruturado."""
    df = pd.DataFrame(tabela)
    
    # Substituir colunas OD e AMB
    df.replace({"OD": "Seg. Odontológica", "AMB": "Seg. Ambulatorial"}, inplace=True)
    
    return df

def save_to_csv(df, output_csv):
    """Salva o DataFrame em um arquivo CSV."""
    df.to_csv(output_csv, index=False, encoding='utf-8')

def compress_csv(csv_path, zip_path):
    """Compacta o arquivo CSV em um ZIP."""
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(csv_path, os.path.basename(csv_path))

def main():
    pdf_path = 'C:/Users/pedro/OneDrive/Documentos/IntuitiveCare/Teste 1/pdfs/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf'

    """
    Preste atenção, se ao clonar o projeto você excluir os pdfs dentro de Teste 1 esse caminho não será achado
    portando baixe ele localmente em alguma outra pasta do seu pc e mude o caminho aqui 
     
    Tive problmeas com o OneDrive entãoo usei caminhos absolutos
    """
    output_csv = "C:/Users/pedro/OneDrive/Documentos/IntuitiveCare/Teste 2/Rol_Procedimentos.csv"
    zip_file = "C:/Users/pedro/OneDrive/Documentos/IntuitiveCare/Teste 2//Teste_Pedro_Affonso.zip"
    
    tabela = extract_table_from_pdf(pdf_path)
    df = process_data(tabela)
    save_to_csv(df, output_csv)
    compress_csv(output_csv, zip_file)
    
    print(f"Processo concluído! Arquivo salvo como {zip_file}")

if __name__ == "__main__":
    main()
