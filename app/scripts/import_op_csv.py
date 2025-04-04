import pandas as pd
from database import get_engine, criar_tabelas

# Caminho relativo "C:\Users\{seuUser}\..."
CAMINHO_CSV = r"C:\Users\emmyf\Documents\teste3\despesasop\app\Relatorio_cadop.csv"
NOME_TABELA = "relatorio_cadop"

def importar_relatorio_cadop():
    criar_tabelas()
    
    try:
        df = pd.read_csv(CAMINHO_CSV, delimiter=';', encoding='utf-8-sig')

        if df.empty:
            print("❌ O arquivo Relatorio_cadop.csv está vazio.")
            return

        engine = get_engine()
        with engine.begin() as conn:
            df.to_sql(NOME_TABELA, conn, if_exists='replace', index=False)

        print("✅ Dados do Relatorio_cadop importados com sucesso!")

    except Exception as e:
        print(f"❌ Erro ao importar o Relatorio_cadop: {e}")

if __name__ == "__main__":
    importar_relatorio_cadop()
