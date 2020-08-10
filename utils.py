from models import Programadores, db_session

# Insere dados na tabela programadores
def insere_programadores():
    prog = Programadores(nome='Miguel',idade=4)
    print(prog)
    prog.save()

# consulta registro na tabela programadores
def consulta_programadores():
    programadores = Programadores.query.all()
    programador = Programadores.query.filter_by(nome='Miguel').first()
    print(programadores)
    print(programador.idade)

# altera dados na tabela programadores
def altera_progamador():
    programador = Programadores.query.filter_by(nome='Miguel').first()
    programador.idade = 5
    programador.save()

# exclui dados na tabela programadores
def exclui_programador():
    programador = Programadores.query.filter_by(nome='Jailton').first()
    programador.delete()


if __name__=='__main__':
    #insere_programadores()
    #altera_progamador()
    exclui_programador()
    consulta_programadores()
