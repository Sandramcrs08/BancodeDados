#Exercício 2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.

import conexpy as con

# Conectar ao banco de dados
conexao = con.conectar_bd()

# Criar um cursor a partir da conexão
cursor = conexao.cursor()

# Comando SQL para inserir registros na tabela alunos
comando_inserir = """
    INSERT INTO alunos
                (nome,
                 idade,
                 curso)
    VALUES      (?, ?, ?) 
"""

# Lista de alunos a serem inseridos
alunos = [
    ('Lucas Silva', 22, 'Administração'),
    ('Isabela Oliveira', 20, 'Engenharia'),
    ('Rafael Santos', 26, 'Direito'),
    ('Mariana Costa', 28, 'Engenharia'),
    ('Matheus Pereira', 25, 'Ciências da Computação')
]

# Iterar sobre a lista de alunos e inserir cada um
for aluno in alunos:
    cursor.execute(comando_inserir, aluno)

# Commit para efetivar as mudanças
conexao.commit()

# Fechar conexão com o banco
conexao.close()

