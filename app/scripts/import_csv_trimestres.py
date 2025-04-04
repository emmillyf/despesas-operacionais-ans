import pandas as pd
from pathlib import Path
from database import get_engine, criar_tabelas

DIRETORIO_CSV = Path(r"C:\Users\emmyf\Documents\teste3\despesasop\app\trimestres")
NOME_TABELA = "despesas_trimestrais"

def importar_csvs_trimestrais():
    criar_tabelas()

    engine = get_engine()

    if not DIRETORIO_CSV.exists():
        print(f"{DIRETORIO_CSV} não encontrado.")
        return

    print("📁 Conteúdo da pasta:")
    for item in DIRETORIO_CSV.glob("*"):
        print("-", item.name)

    arquivos_encontrados = list(DIRETORIO_CSV.glob("*T2024.csv"))

    if not arquivos_encontrados:
        print("❌ Nenhum arquivo trimestral encontrado.")
        return

    for arquivo in arquivos_encontrados:
        print(f"📂 Lendo arquivo: {arquivo.name}")

        try:
            try:
                df = pd.read_csv(arquivo, delimiter=';', encoding='utf-8-sig')
            except UnicodeDecodeError:
                df = pd.read_csv(arquivo, delimiter=';', encoding='latin1')

            if df.empty:
                print(f"⚠️ O arquivo {arquivo.name} está vazio.")
                continue

            df['trimestre'] = arquivo.stem

            with engine.begin() as conn:
                df.to_sql(NOME_TABELA, conn, if_exists='append', index=False)

            print(f"✅ Dados de {arquivo.name} importados com sucesso!")

        except Exception as e:
            print(f"❌ Erro ao processar {arquivo.name}: {e}")

if __name__ == "__main__":
    importar_csvs_trimestrais()
