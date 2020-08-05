from models import Programadores, db_session

def insere_programadores():
    prog = Programadores(nome='Miguel',idade=4)
    print(prog)
    db_session.add(prog)
    db_session.commit()

def consulta_prog():
    prog = Programadores.query.all()
    print(prog)
if __name__=='__main__':
    insere_programadores()
    consulta_prog()