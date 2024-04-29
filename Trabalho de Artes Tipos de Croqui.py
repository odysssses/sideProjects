#Code for some school assignment :)
from os import system, name
from time import sleep

msg1 = '''-----Croqui Arquitetônico-----
    É o esboço inicial de uma construção, é usado para representar de forma básica uma construção. É uma forma básica e rápida de representar como “ficará” a construção após ser construída, porém ela não tem cem por cento de certeza que ficará igual ao croqui, pois como o croqui é a representação INICIAL da construção ela sempre é muito diferente da representação. No croqui há muitos elementos abstratos, já que não é extremamente necessário utilizar uma régua para fazer os croquis isso permite que os arquitetos possam “criar” seus próprios detalhes, sem se limitar a utilizar apenas linhas retas.'''
msg2 = '''-----Croqui Cenográfico-----
    O Croqui Cenográfico é um esboço de como um teatro, cinema, ou outros estabelecimentos relacionados a cenografia. Nele, há de pensar sobre 3 elementos: A arquibancada onde a plateia ficará, o proscênio onde os artistas irão se apresentar e a orquestra onde a música será tocada. A arquibancada fica na parte de trás do teatro, a orquestra na frente da arquibancada e o proscênio atrás da orquestra.
    Os teatros de hoje em dia possuem muitas características da Grécia antiga, incluindo os próprios temas, a arquitetura do lugar, entre outros fatores. '''
msg3 = '''-----Croqui de Moda/Figurino-----
    Croqui de Moda, também chamado de senho artístico ou croqui de estilos. É um tipo de desenho da moda capaz de ‘’dizer’’ (expressar) as ideias principais do estilista para a peça ou coleção. A partir de um pequeno ‘’rascunho’’ (esboço), o designer da moda desenvolve o seu próprio croqui. Só que depois ele passa a adicionar os detalhas para que comecem a dar a forma da ideia principal, e mais tarde, será a obra finalizada. 
    Ainda que o croqui haja detalhes como cores, acabamento, caimento, acabamento e texturas, o objetivo não é atingir o realismo. Os detalhes do corpo humano, as proporções do corpo humano, aqui, apresentam espaço para a representação conceitos e emoções, passadas pelo criador. 
    Em suma, desenhar moda é expressar emoções, conceitos, referências e experiências através de roupas ou coleções. '''
msg4 = '''-----Croqui de Design-----
    '''
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

print('''Trabalho de Artes feito por:
[REDACTED]
Professora = [REDACTED]
Título = Tipos de Croqui.''')
resp = str(input('quer continuar? [S]: ')).upper().strip()[0]
if resp == 'S':
    clear()
else:
    while resp != 'S':
        resp = str(input('Tente de novo [S]: ')).upper().strip()[0]

while True:
    resp = int(input('''[1] Croqui Arquitetônico
[2] Croqui Cenográfico
[3] Croqui de Moda/Figurino
[4] Croqui de Design
insira que slide quer ir: '''))
    clear()
    if resp == 1:
        print(msg1)
        resp = str(input('Quer continuar? [S]: ')).upper().strip()[0]
        clear()
    elif resp == 2:
        print(msg2)
        resp = str(input('Quer continuar? [S]: ')).upper().strip()[0]
        clear()
    elif resp == 3:
        print(msg3)
        resp = str(input('Quer continuar? [S]: ')).upper().strip()[0]
        clear()
    elif resp == 4:
        print(msg4)
        resp = str(input('Quer continuar? [S]: ')).upper().strip()[0]
        clear()