# Lógica Matemática - Proyecto 1
En este proyecto se pretende desarrollar un reconocedor léxico-sintáctico para el sistema proposicional L, un fragmento reducido del cálculo proposicional que emplea los conectivos ~, ^ ,o, => Y <=>, así como variables p-z y constantes de verdad 0/1. Utilizando el paquete de Python PLY se construirá un analizador capaz de validar fórmulas bien formadas, generar su AST y visualizar la estructura lógica resultante. Se integra la teoría de autómatas DFC que reconocen el alfabeto, técnicas de compilación como gramáticas LARL (1) y tablas shift-reduce y herramientas de software adicionales para poder proporcionar una buena compresión de los procesos de análisis léxico y sintáctico en la construcción de lenguajes formales. 

### Integrantes del Grupo 4 
+ Ana Laura Tschen 221645
+ Mario Fernando Rocha 23501

### Tecnologías
- Python 3.x
- PLY (Python Lex-Yacc)
- NetworkX (para grafos)
- Matplotlib (para visualización)
- Graphviz (para layout de grafos)

## Instalación

### Prerrequisitos
1. Instalar Python 3.x
2. Instalar Graphviz:
   ```bash
   # En macOS con Homebrew
   brew install graphviz
   
   # En Ubuntu/Debian
   sudo apt-get install graphviz
   
   # En Windows
   # Descargar desde https://graphviz.org/download/
   ```



## Uso

```bash
# Ejecutar el reconocedor
python recognizer.py "<formula>"
```

### Ejemplos
```bash
# Fórmula simple
python recognizer.py "p^q"

# Fórmula con implicación
python recognizer.py "p=>q"

# Fórmula compleja (modus ponens)
python recognizer.py "((p=>q)^p)=>q"

# Fórmula con negación
python recognizer.py "~p"

# Fórmula con bicondicional
python recognizer.py "p<=>q"
```

## Conectivos Soportados
- `~` : Negación (NOT)
- `^` : Conjunción (AND)
- `o` : Disyunción (OR)
- `=>` : Implicación (IMPLIES)
- `<=>` : Bicondicional (IFF)

## Variables y Constantes
- Variables: `p`, `q`, `r`, `s`, `t`, `u`, `v`, `w`, `x`, `y`, `z`
- Constantes: `0` (falso), `1` (verdadero)
- Paréntesis: `(` y `)` para agrupación

## Salida
El programa genera:
1. La representación textual del AST en la consola
2. Un archivo `formula_graph.png` con la visualización gráfica del árbol de sintaxis

