import ply.lex as lex
import ply.yacc as yacc
import networkx as nx
import matplotlib.pyplot as plt

# Token names
tokens = (
    "VAR", "CONST",
    "NOT", "AND", "OR",
    "IMPLIES", "IFF",
    "LPAREN", "RPAREN",
)

#single char tokens
t_NOT    = r"~"      
t_AND    = r"\^"    
t_OR     = r"o"       
t_LPAREN = r"\("  
t_RPAREN = r"\)"

#multi char tokens
def t_IFF(t):
    r"<=>"           
    return t

def t_IMPLIES(t):
    r"=>"            
    return t

def t_VAR(t):
    r"[p-z]"
    return t

def t_CONST(t):
    r"[01]"
    return t

t_ignore = " \t\n"


def t_error(t):
    raise SyntaxError(f"Illegal character {t.value[0]!r} at position {t.lexpos}")
lexer = lex.lex()

#class node
class Node:
    def __init__(self, typ, *children):
        self.typ = typ
        self.children = list(children)

    def __repr__(self):
        if not self.children:
            return self.typ
        return f"{self.typ}({', '.join(map(str, self.children))})"
    
#lowest to highest precedence
precedence = (
    ("left", "IFF"),
    ("left", "IMPLIES"),
    ("left", "OR"),
    ("left", "AND"),
    ("right", "NOT"),
)

start = "formula"

def p_formula_var(p):
    """formula : VAR"""
    p[0] = Node(p[1])

def p_formula_const(p):
    """formula : CONST"""
    p[0] = Node(p[1])

def p_formula_paren(p):
    """formula : LPAREN formula RPAREN"""
    p[0] = p[2]

def p_formula_not(p):
    """formula : NOT formula"""
    p[0] = Node("NOT", p[2])

def p_formula_and(p):
    """formula : formula AND formula"""
    p[0] = Node("AND", p[1], p[3])

def p_formula_or(p):
    """formula : formula OR formula"""
    p[0] = Node("OR", p[1], p[3])

def p_formula_implies(p):
    """formula : formula IMPLIES formula"""
    p[0] = Node("IMPLIES", p[1], p[3])

def p_formula_iff(p):
    """formula : formula IFF formula"""
    p[0] = Node("IFF", p[1], p[3])

def p_error(p):
    if p:
        raise SyntaxError(f"Syntax error near {p.value!r} (index {p.lexpos})")
    raise SyntaxError("Unexpected end of input")
parser = yacc.yacc()

#add to graph
def _add_to_graph(G, node):
    idx = id(node)
    if idx not in G:
        G.add_node(idx, label=node.typ)
        for child in node.children:
            G.add_edge(idx, _add_to_graph(G, child))
    return idx

#graph construccion
def build_graph(ast):
    G = nx.DiGraph()
    _add_to_graph(G, ast)
    return G


def draw_graph(G, outfile="formula_graph.png"):
    pos = nx.nx_pydot.graphviz_layout(G, prog="dot")
    labels = nx.get_node_attributes(G, "label")
    nx.draw(G, pos, labels=labels, with_labels=True, node_size=1500)
    plt.savefig(outfile, bbox_inches="tight")
    plt.close()
    return outfile


def parse_and_show(expr: str):
    ast = parser.parse(expr)
    print(ast)
    png = draw_graph(build_graph(ast))
    print(f"Graph exported to {png}") #export graph to png
    return png

if __name__ == "__main__":
    import sys, textwrap
    if len(sys.argv) != 2:
        print(textwrap.dedent(
            """
            Usage:
               python logic_recognizer.py "<formula>"

            Example:
               python logic_recognizer.py "((p=>q)^p)"
            """))
        sys.exit(1)
    parse_and_show(sys.argv[1])