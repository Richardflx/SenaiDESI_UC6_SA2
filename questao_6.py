horas = int(input('Digite a quantidade de horas: '))

def Horas_para_seg(var):
    return var*60

print(f'{horas} {"hora" if horas == 1 else "horas"} é igual a {Horas_para_seg(horas)} segundos')