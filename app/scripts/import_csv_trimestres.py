import pandas as pd
from pathlib import Path
from sqlalchemy import inspect
from database import get_engine

BASE_DIR = Path(__file__).resolve().parent.parent
DIRETORIO_CSV = BASE_DIR / "trimestres"
NOME_TABELA = "despesas_trimestrais"

def importar_csvs_trimestrais():
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
                
            df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

            if df.empty:
                print(f"⚠️ O arquivo {arquivo.name} está vazio.")
                continue

            df['trimestre'] = arquivo.stem

            with engine.begin() as conn:
                df.to_sql(NOME_TABELA, conn, if_exists='append', index=False)

            print(f"✅ Dados de {arquivo.name} importados com sucesso!")

        except Exception as e:
            print(f"❌ Erro ao processar {arquivo.name}: {e}")

def listar_tabelas():
    engine = get_engine()
    inspetor = inspect(engine)
    tabelas = inspetor.get_table_names()

    print("\n📋 Tabelas encontradas no banco de dados:")
    for tabela in tabelas:
        print("-", tabela)

if __name__ == "__main__":
    importar_csvs_trimestrais()
