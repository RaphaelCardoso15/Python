#Precisamos saber quanto uma determinada empresa deve pagar para seus colaboradores, porém temos apenas
#a quantidade de horas trabalhadas e o valor hora. Escreva um programa que leia o número de um colaborador,
#seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse colaborador. Em
#seguida, apresente o número e o salário do colaborador, com duas casas decimais.

emp_no = int(input())

worked_hours = int(input())

receives_per_worked_hour = float(input())

salario = worked_hours * receives_per_worked_hour

print("NUMBER =",emp_no,end="\n")
print("SALARY = U$ %0.2f"%salario,end="\n")
