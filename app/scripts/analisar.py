import pandas as pd
from sqlalchemy import text
from database import get_engine

def formatar_moeda(valor):
    return f'R$ {valor:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')

def consultar_despesas():
    """
    Consulta as 10 operadoras com maiores despesas em:
    - "EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA À SAÚDE"
    (último trimestre e último ano)
    """
    pd.set_option('display.float_format', '{:,.2f}'.format)
    
    engine = get_engine()
    with engine.connect() as conn:
        descricao_alvo = "EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA À SAÚDE"

        query_verifica_descricao = text("""
            SELECT 1 
            FROM despesas_trimestrais 
            WHERE TRIM(DESCRICAO) = :descricao 
            LIMIT 1;
        """)
        existe = conn.execute(query_verifica_descricao, {"descricao": descricao_alvo}).scalar()

        if not existe:
            print(f"⚠️ Descrição não encontrada: '{descricao_alvo}'")
            return
        
        query_ultimo_trimestre = text("""
            SELECT MAX(trimestre)
            FROM despesas_trimestrais
            WHERE TRIM(DESCRICAO) = :descricao;
        """)
        ultimo_trimestre = conn.execute(query_ultimo_trimestre, {"descricao": descricao_alvo}).scalar()
        ultimo_ano = ultimo_trimestre[-4:] 

        query_trimestre = text("""
            SELECT 
                rc.Razao_Social AS operadora,
                SUM(CAST(NULLIF(REPLACE(TRIM(dt.VL_SALDO_FINAL), ',', '.'), '') AS REAL)) AS total_despesas
            FROM despesas_trimestrais dt
            JOIN relatorio_cadop rc ON dt.REG_ANS = rc.Registro_ANS
            WHERE 
                dt.trimestre = :trimestre
                AND TRIM(dt.DESCRICAO) = :descricao
            GROUP BY operadora
            ORDER BY total_despesas DESC
            LIMIT 10;
        """)
        df_trimestre = pd.read_sql(query_trimestre, conn, params={
            "trimestre": ultimo_trimestre,
            "descricao": descricao_alvo
        })

        query_ano = text("""
            SELECT 
                rc.Razao_Social AS operadora,
                SUM(CAST(NULLIF(REPLACE(TRIM(dt.VL_SALDO_FINAL), ',', '.'), '') AS REAL)) AS total_despesas
            FROM despesas_trimestrais dt
            JOIN relatorio_cadop rc ON dt.REG_ANS = rc.Registro_ANS
            WHERE 
                dt.trimestre LIKE '%' || :ano
                AND TRIM(dt.DESCRICAO) = :descricao
            GROUP BY operadora
            ORDER BY total_despesas DESC
            LIMIT 10;
        """)
        df_ano = pd.read_sql(query_ano, conn, params={
            "ano": ultimo_ano,
            "descricao": descricao_alvo
        })
        
        print(f"\n🏆 As 10 Operadoras com maiores despesas no último trimestre de 2024: ")
        df_trimestre['total_despesas'] = df_trimestre['total_despesas'].apply(formatar_moeda)
        print(df_trimestre.to_string(index=False))
        
        print(f"\n🏆 As 10 Operadoras com maiores despesas no ano de 2024:  ")
        df_ano['total_despesas'] = df_ano['total_despesas'].apply(formatar_moeda)
        print(df_ano.to_string(index=False))

if __name__ == "__main__":
    consultar_despesas()