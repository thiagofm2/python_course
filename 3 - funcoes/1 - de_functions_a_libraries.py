"""
Começaremos a estudar o conceito de funções em Python agora.
Imagine que temos um código para resolver determinado problema, e precisamos replicá-lo em outros locais de nosso
código.

Não é muito inteligente ter que reescrever ou copiar e colar o código várias vezes, por uma questão de manutenção e
poupar tempo/trabalho. Para resolver isso, existem as funções.
Hoje veremos sobre alguns conceitos no Python relacionados a:

- Funções (function)
- Módulos (module)
- Pacotes (package)
- Biblioteca (library)

Vamos imaginar um exemplo básico: Supermercado.
Imagine que temos uma função que faça referência as características das maçãs, e que nós precisamos usar essa
função em vários locais diferentes do código. Neste caso é inteligente criarmos uma função, para poupar nosso tempo
de escrita.

Agora vamos pensar que temos uma função que faça referência a peras, ou seja, outra fruta e com características
semelhantes, poderíamos então criar um Módulo que agrupe essas funções de frutas, e dar um nome como "fruit_module".

Imagine que depois de um tempo, nós temos outros módulos referentes a outros setores do supermercado, como por exemplo
setor de moda, setor de laticíneos, setor de carnes, e por assim em diante. Podemos então agrupar todos esses módulos
dentro de um Pacote.

Vamos pensar no seguinte agora, este Pacote contendo todos os módulos referentes aos setores do supermercado, vende
produtos do oriente, e agora o supermercado abriu franquias que vendem produtos de outras regiões do mundo, ou seja
criamos uma biblioteca chamada Hipermercado contendo pacotes referente a diversos supermercados que vendem produtos de
várias regiões, e dentro destes pacotes terão os módulos referente aos setores de produtos do supermercado, estes
contendo as funções referentes aos produtos que são vendidos.
"""
