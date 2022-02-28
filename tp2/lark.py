#straight up maiso u menos ripado do st
from lark import Lark,Token,Discard
from lark import Transformer
some = 0
cump = 0

class TransformaLista(Transformer):
    def start(self,item):
        # [1] para trabalhar so com a lista de elementos sem os brakets redundantes
        soma = sum(item[1])
        comp = len(item[1])
        return item 

    def elemento(self, elemento):
        # remove as virgulas dalista ja que quando se da print ja fica com virgulas no meio e assim nao se mostra a virgula que seria so apra deliniar elementos
        r : list(filter(lambda x : x!=",",elemento))
        return r 

    def PE(self,pe):
        return str(pe)

    def PD(self,pd):
        return str(pd)

    def VIR(self,vir):
        return ""

    def NUM(self,num):
        elem = int(num)
        soma += elem
        cump+=1
        return elem


grammar = '''
start : PE elemento PD
elemento: NUMERO (VIR NUMERO)*
PE : "["
PD : "]"
VIR : ","
NUMERO : /("0"..."9")+/
import common.WS
%ignore WS
'''

l = Lark(grammar)
frase = "[1,2,3]"
tree = l.parse(frase)

# 
data = TransformaLista().transform(tree)
print(data)