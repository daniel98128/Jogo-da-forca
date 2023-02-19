from random import randint

pokemons = ['bulbasaur','charmander','squirtle',"charizard","wartortle","metapod","pidgeotto","rattata","raticate","spearow","fearow","ekans","arbok","pikachu","raichu","sandshrew","sandslash","nidoqueen","nidora","nidorina","nidoking","clefairy","clefabe","ninetales","jiggkypuff","wigglytuff","zubat","golbat","paras","dugtrio"] # lista de possiveis palavras participantes da forca

def pokemon (pokemons):

    # funçao que define um pokemon(palavra) entre uma lista de pokemons(lista de palavras)
    # lista -> string

    n = len(pokemons)
    localizaçao = randint(0,n-1)

    pokemon = pokemons[localizaçao]

    return pokemon

def forca (palavra,caractere):

    # função que define a forca para cada caractere definido
    # exemplo: se a palavra for banana e defininimos o caractere "a"
    # iremos percorrer a palavra e se não encontramos o caractere "a", iremos substituir por um espaço vazio
    # resultado: _ a _ a _ a
    
    forca = ""

    for letra in palavra:

        if letra == caractere:
            forca = forca + caractere

        else:
            forca = forca + "-"

    return forca

def corpo_da_forca (palavra):

    # funçao que define a forca para uma certa palavra
    # exemplo: banana
    # sua forca seria: _ _ _ _ _ _

    # string -> string

    corpo_da_forca = ""

    for letra in palavra:

        letra = "-"
        corpo_da_forca = corpo_da_forca + letra

    return corpo_da_forca

def display(palavra,recipiente_caracteres):

    # função que define o que irá aparecer na tela do usuario em relação a forca
    # esta função irá funcionar dentro de uma função while
    # os caracteres informados pelo usuario serão acumulados no recipiente_caracteres
    # A função utiliza este parametro e identifica se o caractere se encontra na palavra ou não
    # Se o caractere estiver na palavra, indica o mesmo na posição
    # Se o caractere não se encontra, irá representar a mesma por "-"

    # string -> string

    display = ""
    
    for letra in palavra:

        for caractere in recipiente_caracteres:

            if letra == caractere:
                display = display + letra


        if letra not in recipiente_caracteres:
            display = display + "-"

    return display

def checando_caracteres (caractere, recipiente_caracteres):

    # função que checa se o usuario esta tentando informar um caractere que antes já foi informado
    # se o mesmo informar um caractere que já foi informado
    # ira receber um aviso e poderá informar outro caractere
    # enquanto o usuario não informar um caractere que já não foi informado, a mesma ficará presa dentro de um loop

    # caractere -> caractere

    if caractere in recipiente_caracteres:

        recipiente = []
        contador = 0

        tentativas = list(range(0,100))
        contador_tentativas = 0
    
        while (contador_tentativas < len(tentativas)):

            print("Este caractere já foi informado!!")
            novo_caractere = input("Informe um novo caractere: ")

            list.append(recipiente,novo_caractere)

            if recipiente[contador] not in recipiente_caracteres:

                letra = recipiente[contador]
                return letra
                

            contador = contador + 1

    else:

        return caractere

def main ():

    # lista de palavras possiveis
    
    pokemons = ['bulbasaur','charmander','squirtle',"charizard","wartortle","metapod","pidgeotto","rattata","raticate","spearow","fearow","ekans","arbok","pikachu","raichu","sandshrew","sandslash","nidoqueen","nidora","nidorina","nidoking","clefairy","clefabe","ninetales","jiggkypuff","wigglytuff","zubat","golbat","paras","dugtrio"] # lista de possiveis palavras participantes da forca    
    
    # f que sorteia a palavra

    palavra = pokemon(pokemons)

    # f que define o formato da forca

    variavel_corpo_da_forca = corpo_da_forca(palavra) # variavel que define o formato da forca

    print("Vamos ao jogo da forca !!")
    print("Você tem 8 tentativas para acertar")
    print("Esta é sua palavra:", variavel_corpo_da_forca)

    oportunidades = ['7','6','5','4','3','2','1','0'] # o usuario tem 8 tentativas
    contador_oportunidades = 0

    tentativas_possiveis = list(range(0,100)) # variavel aleatorio com um valor muito alto apenas para delimitar a função
    contador_tentativas = 0
        
    recipiente_caracteres = [] # local que iremos armazenar os caracteres que o usuario informar
    
    while (contador_tentativas < len(tentativas_possiveis)) or (contador_oportunidades < len(oportunidades)):  # variavel que permite definir quando o jogo pode terminar e permiti acumular de maneira + simples o resultado da forca

        caractere = input ("Informe a sua escolha: ")  # o usuario ira informar sua escolha

        variavel_caractere = checando_caracteres(caractere, recipiente_caracteres) # variavel que fez check dos caracteres e informa o resultado já definido
                                                                                   # como dito antes, se o usuario anteriormente ja informou um caractere e o mesmo se encontra no recipiente
                                                                                   # enquanto o mesmo não informar fica preso em um loop
             
        list.append(recipiente_caracteres,variavel_caractere) # vamos acumular a variavel_caractere no recipiente

        # f que define a forca da jogada

        variavel_forca = forca(palavra,variavel_caractere)

        # f que define o que irá aparecer na tela do usuario (forca)

        variavel_display = display(palavra,recipiente_caracteres)

        if variavel_forca == variavel_corpo_da_forca: # condicional que nos diz se o caractere que o usuario informou fez alguma mudança na forca ou não
                                                      
                                                      # se nos encaixarmos nesse condicional
                                                            # o mesma informa que o caractere não se encontra na palavra 
                                                            # o usuario tbm perde uma das suas oportunidades e informado em qual oportunidade se encontra
                                                            # se o contador de oportunidades chegar no limite. A função fecha e o usuario será informado que o jogo acabou e foi perdido. E qual palavra era a que devia ser encontrada
                                                      
                                                      # se não nos encaixarmos nesse condicional
                                                            # o mesmo informa que o caractere se encontra na palavra
                                                            # o mesmo tbm informa o acumulado de caracteres na forca e a posição do caractere na forca
                                                            # se o display chegar ao ponto de ser igual a palavra. A função fecha e o usuario será informado que o jogo acabou e foi ganho. E qual a palavra que foi encontrada
                                                            
            
            print(variavel_caractere, "não se encontra na palavra: ", variavel_display) 
           
            # parametro que irá informar as tentativas restantes do usuario

            vida = oportunidades[contador_oportunidades]
            print("Você possui mais: " + vida + " oportunidades")
          
            contador_oportunidades = contador_oportunidades + 1

            if contador_oportunidades == 8:
                return print("Infelizmente suas chances acabaram !! Você foi enforcado !! \n" + "A palavra a ser encontrada deveria ser: " + palavra)
                
        else:

            print(variavel_caractere, "se encontra na palavra: ", variavel_display)

            if variavel_display == palavra:
                return print ("Parabéns você venceu o jogo !! \n" + "A palavra encontrada foi: " + palavra)

        contador_tentativas = contador_tentativas + 1

if __name__ == "__main__":
    main()
        

            

            
