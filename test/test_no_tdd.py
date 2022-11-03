def sumar(n1, n2):
    if type(n1) not in [int, float] or type(n2) not in [int, float]:
        return 'Esto no es un número'

    return n1 + n2


#Happy Path
def test_sumar_dos_numeros():
    num1 = 3
    num2 = 5
    resultado = sumar(num1, num2)

    assert resultado == 8

#Edge Cases
def test_deberia_devolver_un_error_sino_se_mandan_numeros():
    num1 = 5
    num2 = 'esto no es un numero'

    resultado = sumar(num1, num2)

    assert resultado == 'Esto no es un número'

    num1 = True
    num2 = 5

    resultado = sumar(num1, num2)

    assert resultado == 'Esto no es un número'

def test_deberia_funcionar_correctamente_con_decimales():
    #Arrange
    num1 = 15.5
    num2 = 2.3

    #Act
    resultado = sumar(num1, num2)

    #Assert
    assert resultado == 17.8