from .db import connect
from .consulta import Consulta

class ConsultaDAO():
    def add(c: Consulta):
        conn = connect()
        cursor = conn.cursor()
        SQL = "INSERT INTO consultoria(nome, email, telefone, data, estado, descricao) VALUES (?,?,?,?,?,?);"
        dados = [c.nome, c.email, c.telefone, c.data, c.estado, c.descricao]
        cursor.execute(SQL, dados)
        id_return = cursor.execute("SELECT last_insert_rowid();")
        id = id_return.fetchall()[0] [0]
        conn.commit()
        conn.close()
        
        return id
        
    def edit(c: Consulta,id: int):
        conn = connect()
        cursor = conn.cursor()
        SQL = "UPDATE consultoria SET nome=?,email=?,telefone=?,data=?,estado=?,descricao=? WHERE id=?"
        dados = [c.nome, c.email, c.telefone, c.data, c.estado, c.descricao,id]
        cursor.execute(SQL, dados)
        conn.commit()
        conn.close()
        
    def delete(id:int):
        conn = connect()
        cursor = conn.cursor()
        SQL = "DELETE FROM consultoria WHERE id=?;"
        cursor.execute(SQL,[id])
        conn.commit()
        conn.close()
    
    def selectALL():
        consults_list = []
        conn = connect()
        cursor = conn.cursor()
        SQL = "SELECT * FROM consultoria;"
        cursor.execute(SQL)
        return_list = cursor.fetchall()
        for c  in return_list:
            nova_consulta = Consulta(c[0],c[1],c[2],c[3],c[4],c[5],c[6])
            consults_list.append(nova_consulta)
            
        conn.close()
        
        return consults_list