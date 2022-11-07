def valida_string (s, minimo, maximo):
    tamanho = len(s)
    while True:
        if tamanho >= minimo and tamanho <= maximo:
            return True
            break
        if tamanho > maximo:
            return False
            break
            
print(valida_string("ABCOKMNASDAAA", 3, 20))

        
