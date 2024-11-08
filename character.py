###Inputs do jogador para nome do personagem, ataque e defesa
name1 = input()
atk1 = input()
def1 = input()
name2 = input()
atk2 = input()
def2 = input()
name3 = input()
atk3 = input()
def3 = input()

###Array Bidimensional com os inputs do jogadore
array = [
    [(name1), (atk1, def1)],
    [(name2), (atk2, def2)],
    [(name3), (atk3, def3)]
]

###Imprimir os inputs do jogador guardados no Array
print("[['",
    array[0][0],
    "', (",
    array[0][1][0],
    ",",
    array[0][1][1],
    ")], ['",
    array[1][0],
    "', (",
    array[1][1][0],
    ",",
    array[1][1][1],
    ")], ['",
    array[2][0],
    "', (",
    array[2][1][0],
    ",",
    array[2][1][1],
    ")]]"
    )

###Verificação de qual o ataque mais alto + impressão da menssagem correta

if (array[0][1][0] > array [1][1][0] and array[0][1][0] > array[2][1][0]):
    print ("Ataque" , array[0][0], array[0][1][0])
else:
    pass

if (array[1][1][0] > array [0][1][0] and array[1][1][0] > array[2][1][0]):
    print ("Ataque" , array[1][0], array[1][1][0])
else:
    pass

if (array[2][1][0] > array [0][1][0] and array[2][1][0] > array[1][1][0]):
    print ("Ataque" , array[2][0], array[2][1][0])
else:
    pass

###Verificação de qual a defesa mais alta + impressão da mensagem correta

if (array[0][1][1] > array [1][1][1] and array[0][1][1] > array[2][1][1]):
    print ("Defesa" , array[0][0], array[0][1][1])
else:
    pass

if (array[1][1][1] > array [0][1][1] and array[1][1][1] > array[2][1][1]):
    print ("Defesa" , array[1][0], array[1][1][1])
else:
    pass

if (array[2][1][1] > array [0][1][1] and array[2][1][1] > array[1][1][1]):
    print ("Defesa" , array[2][0], array[2][1][1])
else:
    pass