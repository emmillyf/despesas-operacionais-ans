import pandas as pd
from pathlib import Path
from sqlalchemy import text, inspect
from database import get_engine

BASE_DIR = Path(__file__).resolve().parent.parent
CAMINHO_CADOP = BASE_DIR / "Relatorio_cadop.csv"
DIRETORIO_CSV = BASE_DIR / "trimestres"

TABELA_DESPESAS = "despesas_trimestrais"
TABELA_CADOP = "relatorio_cadop"

def formatar_moeda(valor):
    return f'R$ {valor:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')

def consultar_despesas():
    pd.set_option('display.float_format', '{:,.2f}'.format)
    engine = get_engine()

    with engine.connect() as conn:
        descricao = "EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA À SAÚDE"

        existe = conn.execute(text("""
            SELECT 1 FROM despesas_trimestrais
            WHERE TRIM(descricao) = :descricao LIMIT 1
        """), {"descricao": descricao}).scalar()

        if not existe:
            print(f"⚠️ Descrição não encontrada: '{descricao}'")
            return

        ultimo_trimestre = conn.execute(text("""
            SELECT MAX(trimestre) FROM despesas_trimestrais
            WHERE TRIM(descricao) = :descricao
        """), {"descricao": descricao}).scalar()

        ano = ultimo_trimestre[-4:]

        query_base = """
            SELECT rc.razao_social AS operadora,
                   SUM(CAST(NULLIF(REPLACE(TRIM(dt.vl_saldo_final), ',', '.'), '') AS REAL)) AS total_despesas
            FROM despesas_trimestrais dt
            JOIN relatorio_cadop rc ON dt.reg_ans = rc.registro_ans
            WHERE {filtro}
              AND TRIM(dt.descricao) = :descricao
            GROUP BY operadora
            ORDER BY total_despesas DESC
            LIMIT 10
        """

        df_tri = pd.read_sql(
            text(query_base.format(filtro="dt.trimestre = :trimestre")),
            conn, params={"trimestre": ultimo_trimestre, "descricao": descricao}
        )

        df_ano = pd.read_sql(
            text(query_base.format(filtro="dt.trimestre LIKE '%' || :ano")),
            conn, params={"ano": ano, "descricao": descricao}
        )

        print(f"\n🏆 Top 10 Operadoras no último trimestre de {ano}:")
        df_tri['total_despesas'] = df_tri['total_despesas'].apply(formatar_moeda)
        print(df_tri.to_string(index=False))

        print(f"\n🏆 Top 10 Operadoras no ano de {ano}:")
        df_ano['total_despesas'] = df_ano['total_despesas'].apply(formatar_moeda)
        print(df_ano.to_string(index=False))


def consultar_despesas():
    pd.set_option('display.float_format', '{:,.2f}'.format)
    engine = get_engine()

    with engine.connect() as conn:
        descricao_alvo = "EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA À SAÚDE"

        query_verifica_descricao = text("""
            SELECT 1 FROM despesas_trimestrais
            WHERE TRIM(DESCRICAO) = :descricao LIMIT 1;
        """)
        existe = conn.execute(query_verifica_descricao, {"descricao": descricao_alvo}).scalar()

        if not existe:
            print(f"⚠️ Descrição não encontrada: '{descricao_alvo}'")
            return

        query_ultimo_trimestre = text("""
            SELECT MAX(trimestre) FROM despesas_trimestrais
            WHERE TRIM(DESCRICAO) = :descricao;
        """)
        ultimo_trimestre = conn.execute(query_ultimo_trimestre, {"descricao": descricao_alvo}).scalar()
        ultimo_ano = ultimo_trimestre[-4:]

        query_trimestre = text("""
            SELECT rc.Razao_Social AS operadora,
                   SUM(CAST(NULLIF(REPLACE(TRIM(dt.VL_SALDO_FINAL), ',', '.'), '') AS REAL)) AS total_despesas
            FROM despesas_trimestrais dt
            JOIN relatorio_cadop rc ON dt.REG_ANS = rc.Registro_ANS
            WHERE dt.trimestre = :trimestre
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
            SELECT rc.Razao_Social AS operadora,
                   SUM(CAST(NULLIF(REPLACE(TRIM(dt.VL_SALDO_FINAL), ',', '.'), '') AS REAL)) AS total_despesas
            FROM despesas_trimestrais dt
            JOIN relatorio_cadop rc ON dt.REG_ANS = rc.Registro_ANS
            WHERE dt.trimestre LIKE '%' || :ano
              AND TRIM(dt.DESCRICAO) = :descricao
            GROUP BY operadora
            ORDER BY total_despesas DESC
            LIMIT 10;
        """)
        df_ano = pd.read_sql(query_ano, conn, params={
            "ano": ultimo_ano,
            "descricao": descricao_alvo
        })

        print(f"\n🏆 As 10 Operadoras com maiores despesas no último trimestre de {ultimo_ano}: ")
        df_trimestre['total_despesas'] = df_trimestre['total_despesas'].apply(formatar_moeda)
        print(df_trimestre.to_string(index=False))

        print(f"\n🏆 As 10 Operadoras com maiores despesas no ano de {ultimo_ano}:  ")
        df_ano['total_despesas'] = df_ano['total_despesas'].apply(formatar_moeda)
        print(df_ano.to_string(index=False))


if __name__ == "__main__":
    consultar_despesas()