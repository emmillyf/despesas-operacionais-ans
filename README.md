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

<h2>📦 Como Rodar o Projeto Localmente</h2>

<h3>1. Pré-requisitos</h3>
<p>Antes de rodar o projeto, você precisará ter os seguintes componentes instalados:</p>
<ul>
  <li><strong>Python 3.11</strong> ou superior</li>
  <li><strong>PostgreSQL 15</strong> (ou outra versão compatível)</li>
  <li><strong>pip</strong> (gerenciador de pacotes do Python)</li>
</ul>

<h3>2. Clonar o Repositório</h3>
<p>Clone o repositório do projeto para o seu ambiente local:</p>
<pre><code>git clone https://github.com/seu-usuario/despesas-operacionais-ans.git
cd despesas-operacionais-ans</code></pre>

<h3>3. Criar e Ativar um Ambiente Virtual (opcional, mas recomendado)</h3>
<p>É uma boa prática usar um ambiente virtual para isolar as dependências do projeto. Para criar e ativar o ambiente virtual, execute:</p>
<pre><code>python3 -m venv venv
# Para ativar o ambiente virtual:
# No Linux/macOS:
source venv/bin/activate
# No Windows:
venv\Scripts\activate</code></pre>

<h3>4. Instalar as Dependências</h3>
<p>Instale as dependências do projeto utilizando o <strong>pip</strong>:</p>
<pre><code>pip install -r requirements.txt</code></pre>
<p>Se o arquivo <code>requirements.txt</code> não estiver presente, você pode instalar manualmente as dependências:</p>
<pre><code>pip install pandas sqlalchemy psycopg2 python-dotenv</code></pre>

<h3>5. Configuração do Banco de Dados</h3>
<p>1. <strong>Instale o PostgreSQL</strong> (se ainda não tiver instalado) e crie um banco de dados para o projeto. Você pode fazer isso com os seguintes comandos no terminal do PostgreSQL:</p>
<pre><code>CREATE DATABASE despesas_op;
CREATE USER user WITH ENCRYPTED PASSWORD 'password';
ALTER ROLE user SET client_encoding TO 'utf8';
ALTER ROLE user SET default_transaction_isolation TO 'read committed';
ALTER ROLE user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE despesas_op TO user;</code></pre>
<p>2. <strong>Configuração das Variáveis de Ambiente</strong></p>
<p>Crie um arquivo <code>.env</code> na raiz do projeto e adicione as variáveis de ambiente necessárias para a conexão com o banco de dados. O conteúdo do arquivo deve ser algo como:</p>
<pre><code>BANCODEDADOS_URL=postgresql://user:password@localhost:5432/despesas_op</code></pre>

<h3>6. Executando o Script</h3>
<p>Agora, você pode rodar o script diretamente no terminal. Dependendo de como o projeto está estruturado, pode ser necessário executar um arquivo Python específico. Supondo que o script principal seja <code>main.py</code>, execute:</p>
<pre><code>python main.py</code></pre>

<h3>7. Arquivos Esperados</h3>
<p>Certifique-se de que a estrutura do projeto esteja conforme abaixo:</p>
<ul>
  <li><code>Relatorio_cadop.csv</code> na raiz do projeto</li>
  <li>Arquivos <code>.csv</code> trimestrais na pasta <code>trimestres/</code></li>
</ul>

<h3>8. Saída Esperada</h3>
<p>A execução do script irá gerar a saída esperada com as 10 operadoras com maiores despesas nos períodos solicitados. O resultado será algo como:</p>
<pre><code>🏆 As 10 Operadoras com maiores despesas no último trimestre de 2024:
 operadora                   total_despesas
 UNIMED RIO                  R$ 55.000.000,00
 AMIL                        R$ 48.500.000,00
 ...

🏆 As 10 Operadoras com maiores despesas no ano de 2024:
 ...
</code></pre>

</body>
</html>
