import cx_Oracle

# Parâmetros de conexão
host = '10.85.0.73'
servico = 'XE'
usuario = 'SYSTEM'
senha = 'CAIXA'

# Tente estabelecer a conexão
cx_Oracle.init_oracle_client(lib_dir="C:/oraclexe/app/oracle/product/10.2.0/server/NETWORK/ADMIN/instantclient_19_19")

try:
    conn = cx_Oracle.connect(usuario, senha, f'{host}/{servico}')
    print("Conexão bem-sucedida!")

    # Executa a consulta SELECT
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM TEST_TABLE")
    result = cursor.fetchall()

    # Imprime os resultados
    for row in result:
        print(row)

    # Fecha o cursor
    cursor.close()
except cx_Oracle.DatabaseError as e:
    print("Erro ao conectar ao banco de dados:", e)

# Aguardar entrada do usuário para encerrar o programa
input("Pressione qualquer tecla para sair...")
