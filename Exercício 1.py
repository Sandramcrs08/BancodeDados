import conexpy as con

# Conectar ao banco de dados
conexao = con.conectar_bd()

# Comando SQL para criar a tabela alunos
comando_model = '''CREATE TABLE alunos (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    idade INTEGER,
    curso TEXT
);'''

# Executar o comando SQL
con.executar_comando(conexao, comando_model)

# Salvar alterações no banco de dados
con.salvar_alteracoes_bd(conexao)

# Fechar conexão com o banco de dados
con.fechar_conexao_bd(conexao)
