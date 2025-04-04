<!DOCTYPE html>
<html lang="pt-BR">
<body>

<h1>📊 Análise de Despesas Operacionais - ANS</h1>

<p>Este projeto realiza o processamento e análise de despesas trimestrais de operadoras de saúde com base em dados públicos da ANS (Agência Nacional de Saúde Suplementar).</p>

<h2>🚀 Tecnologias Utilizadas</h2>
<ul>
  <li><strong>Python 3.11</strong></li>
  <li><strong>Pandas</strong> – Análise e manipulação de dados</li>
  <li><strong>SQLAlchemy</strong> – ORM para conexão com banco de dados</li>
  <li><strong>PostgreSQL 15</strong></li>
  <li><strong>Docker</strong> e <strong>Docker Compose</strong></li>
  <li><strong>python-dotenv</strong> – Variáveis de ambiente</li>
</ul>
<h2>⚙️ Funcionalidades</h2>
<ul>
  <li>Importação do relatório <code>Relatorio_cadop.csv</code></li>
  <li>Importação dos arquivos trimestrais (ex: <code>1T2024.csv</code>)</li>
  <li>Exibição das 10 operadoras com maiores despesas:
    <ul>
      <li>No último trimestre</li>
      <li>No ano vigente</li>
    </ul>
  </li>
</ul>

<h2>📦 Como Rodar o Projeto com Docker</h2>

<h3>1. Pré-requisitos</h3>
<ul>
  <li>Docker</li>
  <li>Docker Compose</li>
</ul>

<h3>2. Clonar o Repositório</h3>
<pre><code>git clone https://github.com/seu-usuario/despesas-operacionais-ans.git
cd despesas-operacionais-ans</code></pre>

<h3>3. Estrutura Esperada</h3>
<ul>
  <li><code>Relatorio_cadop.csv</code> na raiz do projeto</li>
  <li>Arquivos <code>.csv</code> trimestrais em <code>trimestres/</code></li>
</ul>

<h3>4. Criar o Arquivo <code>.env.prod</code></h3>
<pre><code>BANCODEDADOS_URL=postgresql://user:password@db:5432/despesas_op</code></pre>

<h3>5. Rodar com Docker Compose</h3>
<pre><code>docker-compose up --build</code></pre>

<h2>📈 Saída Esperada</h2>
<pre><code>🏆 As 10 Operadoras com maiores despesas no último trimestre de 2024:
 operadora                   total_despesas
 UNIMED RIO                      R$ 55.000.000,00
 AMIL                           R$ 48.500.000,00
...

🏆 As 10 Operadoras com maiores despesas no ano de 2024:
 ...
</code></pre>
</body>
</html>
