from sqlalchemy import create_engine, text

CAMINHO_BANCO = "sqlite:///despesatotal.db"

def get_engine():
    return create_engine(CAMINHO_BANCO)

def criar_tabelas():
    """Cria as tabelas necessárias no banco de dados"""
    queries = [
        text("""
            CREATE TABLE IF NOT EXISTS relatorio_cadop (
                Registro_ANS TEXT,
                CNPJ TEXT,
                Razao_Social TEXT,
                Nome_Fantasia TEXT,
                Modalidade TEXT,
                Logradouro TEXT,
                Numero TEXT,
                Complemento TEXT,
                Bairro TEXT,
                Cidade TEXT,
                UF TEXT,
                CEP TEXT,
                DDD TEXT,
                Telefone TEXT,
                Fax TEXT,
                Endereco_eletronico TEXT,
                Representante TEXT,
                Cargo_Representante TEXT,
                Regiao_de_Comercializacao TEXT,
                Data_Registro_ANS TEXT
            )
        """),
        text("""
            CREATE TABLE IF NOT EXISTS despesas_trimestrais (
                DATA TEXT,
                REG_ANS INTEGER,
                CD_CONTA_CONTABIL INTEGER,
                DESCRICAO TEXT,
                VL_SALDO_INICIAL TEXT,
                VL_SALDO_FINAL TEXT,
                trimestre TEXT
            )
        """)
    ]
    
    engine = get_engine()
    with engine.begin() as conn:
        for query in queries:
            conn.execute(query)

    print("✅ Tabelas `relatorio_cadop` e `despesas_trimestrais` criadas/verificadas.")

if __name__ == "__main__":
    criar_tabelas()
