import pandas as pd
from pathlib import Path
from database import get_engine
from sqlalchemy import inspect

BASE_DIR = Path(__file__).resolve().parent.parent  
CAMINHO_CSV = BASE_DIR / "Relatorio_cadop.csv"
NOME_TABELA = "relatorio_cadop"

def importar_relatorio_cadop():
    engine = get_engine()

    try:
        try:
            df = pd.read_csv(CAMINHO_CSV, delimiter=';', encoding='utf-8-sig')
        except UnicodeDecodeError:
            df = pd.read_csv(CAMINHO_CSV, delimiter=';', encoding='latin1')
                
        df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

        if df.empty:
            print("❌ O arquivo Relatorio_cadop.csv está vazio.")
            return

        with engine.begin() as conn:
            df.to_sql(NOME_TABELA, conn, if_exists='replace', index=False)

        print("✅ Dados do Relatorio_cadop importados com sucesso!")

    except Exception as e:
        print(f"❌ Erro ao importar o Relatorio_cadop: {e}")

def listar_tabelas():
    engine = get_engine()
    inspetor = inspect(engine)
    tabelas = inspetor.get_table_names()
    
    print("📋 Tabelas encontradas no banco de dados:")
    for tabela in tabelas:
        print("-", tabela)

if __name__ == "__main__":
    importar_relatorio_cadop()
    listar_tabelas()
