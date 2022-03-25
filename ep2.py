"""
  AO PREENCHER ESSE CABECALHO COM O MEU NOME E O MEU NUMERO USP, 
  DECLARO QUE SOU O UNICO AUTOR E RESPONSAVEL POR ESSE PROGRAMA. 
  TODAS AS PARTES ORIGINAIS DESSE EXERCICIO PROGRAMA (EP) FORAM 
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUCÕES
  DESSE EP E QUE PORTANTO NAO CONSTITUEM DESONESTIDADE ACADEMICA
  OU PLAGIO.  
  DECLARO TAMBEM QUE SOU RESPONSAVEL POR TODAS AS COPIAS
  DESSE PROGRAMA E QUE EU NAO DISTRIBUI OU FACILITEI A
  SUA DISTRIBUICAO. ESTOU CIENTE QUE OS CASOS DE PLAGIO E
  DESONESTIDADE ACADEMICA SERAO TRATADOS SEGUNDO OS CRITERIOS
  DIVULGADOS NA PAGINA DA DISCIPLINA.
  ENTENDO QUE EP SEM ASSINATURA NAO SERAO CORRIGIDOS E,
  AINDA ASSIM, PODERAO SER PUNIDOS POR DESONESTIDADE ACADEMICA.

  Nome : Julia Inoscencia Oliveira dos Santos
  Prof.: Leo^nidas de Oliveira Branda~o

"""

# Para geracao de numeros pseudo-aleatorios: inicio
CPA_NUM1    =  16807;
CPA_NUM2    =   2836;
CPA_MOD     = 127773;

# Devolve o proximo 'pseudo-aleatorio' (seguinte ao 'anterior')
def _proximo_pseudo(anterior):
    return ((CPA_NUM1 * anterior + CPA_NUM2) % CPA_MOD); # proximo
# Para geracao de numeros pseudo-aleatorios: fim

def afinidade(a):
    resto = 0
    soma = 0
    result = 0
    while a > 0:
        resto = a%10
        a = (a-resto)//10
        soma += resto
    while soma > 0:
        resto = soma%10
        soma = (soma-resto)//10
        result += resto
    if result == 10:
        result = 1
    if result == 11:
        result = 2
    return result    

def modoi():
    print("modo", m, "eh invalido!")
    
def modo1():
    n = int(input("Digite a semente do sorteio:"))
    k = int(input("Digite o tamanho da sequencia:"))
    while k > 0:
        lista = [n]
        y = _proximo_pseudo (n)
        n = y
        k -= 1
        print (lista)
    
def modo2(c):
    y = soma(c)
    print("Soma dos digitos: ",y)
    
def modo3(s,p):
    y = afinidade(p)
    print("Numero de afinidade para",p , "eh:", y)
    
def modo4(x,y,a,b):
    if x == y:
        print(a, "compativel com", b, ": afinidade",y)
    else:
        print("NAO compativel! Afinidades:",x, y)

def modo5(n,k,c,h):
    print("\nSua caracteristica: %d"%(n))
    print("Sua afinidade: %d"%(h))
    while k > 0:
        lista = [n]
        pro = _proximo_pseudo (n)
        n = pro
        k -= 1
        b = afinidade(pro)
        a = afinidade(c)
        if a == b:
            print("(%d, %d) tem mesma afinidade! *** %d ***"%(c,pro,a))
        else:
            print("(%d, %d) com afinidades (%d, %d)"%(c,pro,a,b))
    
def soma(c):
    resto = 0
    soma = 0
    while c > 0:
        resto = c%10
        c = (c-resto)//10
        soma += resto    
    return soma
    
m = int(input("Digite o modo do jogo:"))
if m < 1 or m > 5:
    modoi()
if m == 1:
    modo1()
if m == 2:
    c = int(input("Digite o numero de caracteristica:"))
    modo2(c)
if m == 3:
    s = int(input("\nDigite uma semente para o sorteio:"))
    p = _proximo_pseudo(s)
    modo3(s,p)
if m == 4:
    a = int(input("\nDigite o numero de caracteristica:"))
    x = afinidade(a)
    b = int(input("\nDigite o numero de caracteristica:"))
    y = afinidade(b)
    modo4(x,y,a,b)
if m == 5:
    n = int(input("\nDigite a semente do sorteio:"))
    k = int(input("\nDigite o tamanho da sequencia:"))
    c = n
    h = afinidade(c)
    modo5(n,k,c,h)
