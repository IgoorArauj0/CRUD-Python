import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '12345',
    database = 'bdcrud',
)
cursor = conexao.cursor()


# =-=-=-=- CREATE -=-=-=-=
nome_produto = 'Teclado com Led Multilaser'
valor = 300
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
conexao.commit() # Editar BD

cursor.close()
conexao.close()


# =-=-=-=- READ -=-=-=-=
comando = f'SELECT * FROM vendas'
cursor.execute(comando)
resultado = cursor.fetchall() #Ler o BD
print(resultado)


# =-=-=-=- UPDATE -=-=-=-=
nome_produto = "Fone de Ouvido Bluetooth"
comando = f'UPDATE vendas SET nome_produto = "{nome_produto}" WHERE idvendas = 7'
cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close()


# =-=-=-=- DELETE -=-=-=-=
comando = f'DELETE FROM vendas WHERE idvendas = 1'
cursor.execute(comando)
conexao.commit()