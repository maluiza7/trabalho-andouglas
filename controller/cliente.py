#carregando as funções em outros arquivos .py
import services.database as db

#função para inserir registro no banco de dados
def incluir(nome, email, especializacao):
    db.cur.execute("""
                   INSERT into public.tbprogramadores (nome, email, especializacao)
                   VALUES ('%s','%s','%s')
                   """ % (nome, email, especializacao))
    db.con.commit()
    
#função para inserir registro no banco de dados
def selecionar():
    db.cur.execute("""
                   SELECT * FROM tbprogramadores
                   """)
    data = db.cur.fetchall()
    rows = []
    for row in data:
        rows.append(row)
    return rows

def deletar(email):
    db.cur.execute("""
                   DELETE * FROM tbprogramadores WHERE matricula = '%s';
                   """ % (email))
    db.con.comit()

    #data = db.cur.fetchall()
    #rows = []
    #for row in data:
    #    rows.append(row)
    #return rows                   