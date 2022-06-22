def añoBisiesto(año):
    if año%4 == 0:
        return 'el año es bisiesto'
    else:
        return 'el año NO es bisiesto'

resultado = añoBisiesto(2022)
print(resultado)

