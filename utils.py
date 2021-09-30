from models import Pessoas

#Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='DiogoLima', idade=22)
    print(pessoa)
    pessoa.save()

#Realiza consulta na tabela pessoa
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='DiogoLima').first()
    print(pessoa.idade)

#altera dados na tabela pessoa
def altera_pessoas():
    pessoa = Pessoas.query.filter_by(nome='DiogoLima').first()
    pessoa.nome = 'Mudei_o_Nome'
    pessoa.save()

#excli dados na tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='DiogoLima').first()
    pessoa.delete()



if __name__ == '__main__':

    # insere_pessoas()
    #consulta_pessoas()
    #altera_pessoas()
    exclui_pessoa()
