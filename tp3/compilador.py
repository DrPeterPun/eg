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
contrl: (nestedcif | cif | cwhile) ";"
cif : "if(" conds "){" expression* "}"
nestedcif.1 : "if(" conds "){" "if(" conds "){" expression* "}" "}"
cwhile : "while(" conds "){" expression* "}"
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

    def expression(self,item):
        #print(str(item)+"\n")
        return item

    def contrl(self,item):
        print("///////////////////////////////////////////////////////////////////////////////////////////")
        print(str(item)+"\n")
        print(str(item[0])+"\n")
        return item

    def nestedcif(self,item):
        print("lsadkjfa;sldfja;sldfjkasdlkfjas;fja;1n1n1n1n\n\nn\n\n\nasdasdf")

    def cif(self,item):
        #self.count+=1
        #print("///////////////////////////////////////////////////////////////////////////////////////////")
        #print(str(item)+"\n")
        #print(str(item[0])+"\n")
        #print(str(item[1])+"\n")
        #print(item[1].children[0])
        return item

    def atrib(self,item):
        return item

    def deff(self,item):
        self.vars.update({item[1] : False})
        return item
    pass

    def defplus(self,item):
        self.vars.update({item[1][0] : True})
        return item

    def var(self,item):
        #print("nome da var:")
        #print(item[0])
        #print("init?")
        if(self.vars.get(item[0][0])):
            pass
            #print("yes")
        else:
            #print("no!")
            self.vars.update({item[0] : False})
        return item

    def varinit(self,item):
        #print("var:")
        #print(str(item[0]))
        return item

l = Lark(grammar,keep_all_tokens=False)
inp = open("test")
f = inp.read()
tree = l.parse(f)
tree.pretty()
t = Transf()
tree.pretty(indent_str=" ")
data = t.transform(tree)
print(tree)

for a in t.vars:
    #if(not t.vars.get(a)):
        #print(str(a) + " nao inicializado")
    pass
#print("count " + str(t.count))
