from lark import Lark,Token
from lark import Transformer

class TransformaLista(Transformer):
    def __init(self):
        some = 0
        comp = 0
        dict = {}
    
    def start(self,item):
        # [1] para trabalhar so com a lista de elementos sem os brakets redundantes
        soma = sum(item[1])
        comp = len(item[1])
        return item 

    def elemento(self, elemento):
        r : list(filter(lambda x : x!=",",elemento))
        return r 

    def DOT(self,dot):
        return str(dot)

    def COM(self,com):
        return str(com)

    def PAL(self,pal):
        return str(pal)

grammar = '''
start : "LISTA" elemento DOT
elemento: PAL (COM PAL)*
PAL : ("a"..."Z")+|("0"..."9")+
DOT : "."
COM : ","
import common.WS
ignore WS
'''

l = Lark(grammar)
frase = "[1,2,3]"
tree = l.parse(frase)

data = TransformaLista().transform(tree)
print(data)