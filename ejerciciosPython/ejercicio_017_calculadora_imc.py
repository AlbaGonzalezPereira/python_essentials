import ejercicio_016_calculadora_imc as calculadora # renombramos para utilizar nombre más pequeño

if __name__=='__main__': # main es el valor del script a ejecutar, en este caso ejercicio_016_calculadora_imc
    peso_persona = float(input('Introduce tu peso en kg: '))
    altura_persona = float(input('Introduce tu altura en m: '))
    imc_persona = calculadora.calcular_imc(peso=peso_persona, altura=altura_persona)
    print(f'Tu índice de masa corporal es {imc_persona}')
    estado = calculadora.calcular_estado(imc_persona)
    print(f'El estado del paciente es {estado}')