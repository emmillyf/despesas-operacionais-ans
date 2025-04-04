from import_op_csv import importar_relatorio_cadop
from import_csv_trimestres import importar_csvs_trimestrais
from analisar import consultar_despesas

def main():
    print("🚀 Iniciando importação dos dados...")
    
    print("\n📂 Importando Relatório Cadop...")
    importar_relatorio_cadop()
    
    print("\n📂 Importando Despesas Trimestrais...")
    importar_csvs_trimestrais()
    
    print("\n🔍 Consultando Top Operadoras...")
    consultar_despesas()
    
    print("\n✅ Processo concluído!")

if __name__ == "__main__":
    main()