from lark import Lark,Token,Discard
from lark import Transformer

grammar= '''
start : expression*
expression : contrl | atrib | defs
defs: deff | defplus
deff : type varinit ";"
defplus : type varinit "=" value ";"
type : ATOM | struct
ATOM : "bool" | "int"
struct : array | lista | set
array: type "[" NUMBER "]"
set: "SET<" type ">"
lista: "LIST<" type ">"
contrl: cif | cwhile
cif : "if(" conds "){" expression* "}"
cwhile : "while (" conds "){" expression* "}"
conds : cond (CONDOP cond)*
cond : BOOL | arit COMPOP arit | var
BOOL : "true" | "false"
CONDOP : "&&" | "||" | "!"
COMPOP : "<" | ">" | "<=" | ">=" | "==" | "!="
arit : term | arit ARITOP arit
term : NUMBER | var
ARITOP: "-" | "+" | "*" | "/" | "%"
atrib : var "=" value ";"
value : arit | listaextenso
listaextenso : PE elemento PD
elemento: NUMBER (VIR NUMBER)*
PE : "["
PD : "]"
VIR : ","
var : WORD
varinit : WORD
%import common.WS
%import common.NUMBER
%import common.WORD
%ignore WS
'''
class Transf(Transformer):
    count = 0
    #declared variables
    vars = {}
    def start(self,item):
        return item

    def defs(self,item):
        return item

    def cif(self,item):
        self.count+=1
        return item

    def atrib(self,item):
        return item

    def deff(self,item):
        self.vars.update({item[1] : False})
        return item

    def defplus(self,item):
        self.vars.update({item[1] : True})
        return item

    def var(self,item):
        print("nome da var:")
        print(item[0])
        print("init?")
        if(self.vars.get(item[0])):
            print("yes")
        else:
            print("no!")
            self.vars.update({item[0] : False})
        return item[0]

    def varinit(self,item):
        #print("var:")
        #print(str(item[0]))
        return item[0]

l = Lark(grammar)
inp = open("test")
f= inp.read()
tree = l.parse(f)
t = Transf()
data = t.transform(tree)
for a in t.vars:
    if(not t.vars.get(a)):
        print(str(a) + " nao inicializado")
print("count " + str(t.count))
