#O calendário escolar está passando bem rápido, devido a isso, as professoras de uma escola estão com
# dificuldade para calcular as notas dos alunos. Visando em resolver a situação, a diretora da escola contratou
# você para desenvolver um programa que leia as notas da primeira e da segunda avaliação de um aluno. Calcule e
# imprima a média semestral.O programa só aceitará notas válidas (uma nota válida deve pertencer ao intervalo
# [0,10]). Cada nota deve ser validada separadamente.No final deve ser impressa a mensagem “novo calculo
# (1-sim 2-nao)”, solicitando as professoras que informe um código (1 ou 2) indicando se ele deseja ou não
# executar o algoritmo novamente, (aceitar apenas os código 1 ou 2). Se for informado o código 1 deve ser
# repetida a execução de todo o programa para permitir um novo cálculo, caso contrário o programa deve ser
#  encerrado.
def notas_media(x, y):
    media=(x+y)/2
    print('media = %.2f' %media)

def notas_validas():
    x = float(input())
    if x >= 0 and x <=10:
        return x
    else:
        print('nota invalida')
        return notas_validas()

choice = 1
while choice == 1:
    j = -1
    k = -1
    while k==-1:
        k = notas_validas()
    while j==-1:
        j = notas_validas()
    notas_media(k,j)
    choice =3
    while choice<1 or choice>2:
        choice = eval(input('novo calculo (1-sim 2-nao)\n'))