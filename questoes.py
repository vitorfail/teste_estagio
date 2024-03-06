

def atividade(respostas):
#########################################################################################################################################################
    #Questão Número 1
    def questao1():
        INDICE = 13 
        SOMA = 0 
        K = 0

        while K < INDICE:

            K = K + 1

            SOMA = SOMA + K

        print('''1) Observe o trecho de código abaixo:

        int INDICE = 13, SOMA = 0, K = 0;

        enquanto K < INDICE faça

        {

        K = K + 1;

        SOMA = SOMA + K;

        }

        imprimir(SOMA);



        Ao final do processamento, qual será o valor da variável SOMA?''')
        input("Digite qualquer coisa e dê enter para mostrar a resposta")

        print(SOMA)
###########################################################################################################################################################
    #Questão 2
    def questao2():
        print('''2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma 
                dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na 
                linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.''')
        numero = input("Digite o número: ")
        def fibonachi(numero):
            a, b = 0, 1
            while a <= numero:
                if a == numero:
                    return True
                a, b = b, a + b
            return False
        if fibonachi(int(numero)) == True:
            print(f"O número {numero} pertence a sequência de Fibonachi")
        else:
            print(f"O número {numero} não pertence a sequência de Fibonachi")

###########################################################################################################################################################
    #Questão 3
    def questao3():
        print('''3) Descubra a lógica e complete o próximo elemento:
            a) 1, 3, 5, 7, ___

            b) 2, 4, 8, 16, 32, 64, ____

            c) 0, 1, 4, 9, 16, 25, 36, ____

            d) 4, 16, 36, 64, ____

            e) 1, 1, 2, 3, 5, 8, ____

            f) 2,10, 12, 16, 17, 18, 19, ____''')
        input("Digite qualquer coisa e dê enter para mostrar a resposta")

        print('''3) [Resposta]Descubra a lógica e complete o próximo elemento:
            a) 1, 3, 5, 7, 9

            b) 2, 4, 8, 16, 32, 64, 128

            c) 0, 1, 4, 9, 16, 25, 36, 49

            d) 4, 16, 36, 64, 100

            e) 1, 1, 2, 3, 5, 8, 13

            f) 2,10, 12, 16, 17, 18, 19, 20''')
###########################################################################################################################################################
    #Questão 4:
    def questao4():
        print('''4) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada.

        Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?''')
        input("Digite qualquer coisa e dê enter para mostrar a resposta")
        print('''#Primeira ida: Ligue o primeiro interruptor e aguarde alguns minutos. Em seguida, desligue-o.
                   - Se a lâmpada acender, você sabe que o primeiro interruptor controla essa lâmpada.
                   - Se a lâmpada não acender, vá para o próximo passo.
                 #Segunda ida: Ligue o segundo interruptor e entre na sala das lâmpadas.
                   - Se você ver a lâmpada acesa, você sabe que o segundo interruptor controla essa lâmpada.
                   - Se a lâmpada estiver apagada e ainda estiver fria, você pode concluir que o terceiro interruptor controla essa lâmpada.
                   - Se a lâmpada estiver apagada, mas estiver quente, você pode concluir que o primeiro interruptor controla essa lâmpada.''')
###########################################################################################################################################################
    #Questão 5:
    def questao5():
        print('''5) Escreva um programa que inverta os caracteres de um string.
        
        IMPORTANTE:

        a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

        b) Evite usar funções prontas, como, por exemplo, reverse;''')
        respostas = input("Digite a string que você quer inverter:")
        respostas = ''
        for char in respostas:
            string_revertida = char + string_revertida
        print(f"Resposta: {respostas}")


    questoes =[questao1,questao2, questao3, questao4, questao5]
    if respostas> len(questoes):
        print("Esse questionãrio só possui 5 questões ;)")
    else:
        questoes[respostas]()

while True:
    respostas = input("Digite o número da questão para saber a resposta dela:")

    # Verifica se a entrada é composta apenas por dígitos
    if respostas.isdigit():
        numero_inteiro = int(respostas)
        break
    else:
        # Se a entrada não for um número, continua o loop
        print("Digite um numero iteiro entre de 1 a 5")
        pass


atividade(int(respostas)-1)