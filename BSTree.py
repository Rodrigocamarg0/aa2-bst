# Binary Serach Tree

# Código usado como referencia https://gist.github.com/divanibarbosa/a8662693e44ab9ee0d0e8c2d74808929


from Node import Node

from binarytree import build



tree_list = []

class BSTree:

     def __init__(self):
          self.root = None

     # PRIMEIRA OPERACAO = INSERCAO
     # 1 - criar um nodo
     # 2 - verificar se a arvore esta vazia
          # 4 -- se estiver vazia nodo a ser inserido eh a raiz (nodo solitario)
          # 3 - se nao estiver vazia - ocorre a insercao recursiva

     def insert(self, label):
          # CRIANDO O NODO QUE SERAH INSERIDO (objeto da classe -node-)
          node = Node(label)
          # current_node = None
          # node_d = None

          # verificando se a arvore esta vazia , ou nao
          if self.empty():  # raiz eh o nodo que esta sendo inserido
               self.root = node
          else:
               # arvore nao esta vazia - insercao sera realizada de forma recursiva
               node_d = None
               current_node = self.root

               while True:  # se repete ate o meu caso base (node == null)

                    # 1 - etapa do fluxo do percurso
                    if current_node != None:  # cheguei no caso base, aqui vou inserir

                         node_d = current_node

                         # verifica se eh maior ou menor - se vai para direita ou para esquerda
                         if node.getLabel() < current_node.getLabel():  # esquerda
                              current_node = current_node.getLeft()
                         else:  # vai para direita
                              current_node = current_node.getRight()

                         # 2 - para encontrar onde deve ser inserido, ate que o nodo current_node seja none
                    else:  # current_node eh NONE --> eh para realizar a insercao
                              # insere ou na direita, ou na esquerda
                              if node.getLabel() < node_d.getLabel():
                                   # insercao na esquerda do dad
                                   node_d.setLeft(node)
                              else:
                                   # insercao na direita do dad
                                   node_d.setRight(node)
                              break  # sai do grupo

     def empty(self):
          if self.root == None:  # se a raiz nao existe
               return True  # sim, a arvore esta vazia
          return False

     # metodo pre-ordem para percorrer : raiz, esquerda, direita
     def showTree(self, current_node):
          if current_node != None:
               print('%d' % current_node.getLabel(), end=' ')
               self.showTree(current_node.getLeft())
               self.showTree(current_node.getRight())

     def getRoot(self):
          return self.root


     def search(self, label):
         if self.root == None:
              return None # se arvore vazia
         current_node = self.root # começa a procurar desde raiz
         while current_node.label != label: # enquanto nao encontrou
               if label < current_node.label:
                    current_node = current_node.getLeft() # caminha para esquerda
               else:
                    current_node = current_node.getRight() # caminha para direita
               if current_node == None:
                    return None # encontrou uma folha -> sai
         return current_node  # terminou o laço while e chegou aqui é pq encontrou item    

     def next_node(self, delete):  # O parametro é a referencia para o No que deseja-se deleter
          dad_next_node = delete
          next_node = delete
          current_node = delete.getRight()  # vai para a subarvore a direita

          while current_node != None:  # enquanto nao chegar no Nó mais a esquerda
               dad_next_node = next_node
               next_node = current_node
               current_node = current_node.getLeft()  # caminha para a esquerda

          if next_node != delete.getRight():  # se next_node nao é o filho a direita do Nó que deverá ser eliminado
               dad_next_node.setLeft(next_node.getRight())
               next_node.setRight(delete.getRight()) 
                                        # quando ele assumir a posição correta na arvore
          return next_node



     def remove(self, label):
          if self.root == None:
               return False # se arvore vazia
          current_node = self.root
          dad = self.root
          filho_esq = True
          # ****** Buscando o valor **********
          while current_node.label != label: # enquanto nao encontrou
               dad = current_node
               if label < current_node.label: # caminha para esquerda
                    current_node = current_node.getLeft()
                    filho_esq = True # é filho a esquerda? sim
               else: # caminha para direita
                    current_node = current_node.getRight() 
                    filho_esq = False # é filho a esquerda? NAO
               if current_node == None:
                    return False # encontrou uma folha -> sai

          # Se nao possui nenhum filho (é uma folha), elimine-o
          if current_node.getLeft() == None and current_node.getRight() == None:
               if current_node == self.root:
                    self.root = None # se raiz
               else:
                    if filho_esq:
                         dad.setLeft(None) # se for filho a esquerda do dad
                    else:
                         dad.setRight(None) # se for filho a esquerda do dad

          # Se é dad e nao possui um filho a direita, substitui pela subarvore a direita
          elif current_node.getRight() == None:
               if current_node == self.root:
                    self.root = current_node.getLeft() # se raiz
               else:
                    if filho_esq:
                         dad.setLeft(current_node.getLeft()) # se for filho a esquerda do dad
                    else:
                         dad.setRight(current_node.getRight()) # se for filho a direita do dad
          
          # Se é dad e nao possui um filho a esquerda, substitui pela subarvore a esquerda
          elif current_node.getLeft() == None:
               if current_node == self.root:
                    self.root = current_node.getRight() # se raiz
               else:
                    if filho_esq:
                         dad.setLeft(current_node.getRight()) # se for filho a esquerda do dad
                    else:
                         dad.setRight(current_node.getLeft()) # se for  filho a direita do dad

          # Se possui mais de um filho, se for um avô ou outro grau maior de parentesco
          else:
               sucessor = self.next_node(current_node)
               # Usando sucessor que seria o Nó mais a esquerda da subarvore a direita do No que deseja-se remover
               if current_node == self.root:
                    self.root = sucessor # se raiz
               else:
                    if filho_esq:
                         dad.setLeft(sucessor) # se for filho a esquerda do dad
                    else:
                         dad.setRight(sucessor) # se for filho a direita do dad
               sucessor.setLeft(current_node.getLeft()) # acertando o ponteiro a esquerda do sucessor agora que ele assumiu 
                                        # a posição correta na arvore   

          return True
     # metodo pre-ordem para percorrer : esquerda, raiz, direita
     def inOrder(self, current_node):
         if current_node != None:
              self.inOrder(current_node.getLeft())
              print(current_node.label,end=" ")
              self.inOrder(current_node.getRight())
  
     # metodo pre-ordem para percorrer : raiz, esquerda, direita
     def preOrder(self, current_node):
         if current_node != None:
              print(current_node.label,end=" ")
              self.preOrder(current_node.getLeft())
              self.preOrder(current_node.getRight())

     # metodo pre-ordem para percorrer : esquerda, direita, raiz
     def posOrder(self, current_node):
         if current_node != None:
              self.posOrder(current_node.getLeft())
              self.posOrder(current_node.getRight())
              print(current_node.label,end=" ")


  
     def altura(self, current_node):
          if current_node == None or current_node.getLeft() == None and current_node.getRight() == None:
               return 0
          else:
             if self.altura(current_node.getLeft()) > self.altura(current_node.getRight()):
                return  1 + self.altura(current_node.getLeft()) 
             else:
                return  1 + self.altura(current_node.getRight()) 
  
     def folhas(self, current_node):
         if current_node == None:
              return 0
         if current_node.getLeft() == None and current_node.getRight() == None:
              return 1
         return self.folhas(current_node.getLeft()) + self.folhas(current_node.getRight())

  
     def contarNos(self, current_node):
        if current_node == None:
             return 0
        else:
             return  1 + self.contarNos(current_node.getLeft()) + self.contarNos(current_node.getRight())

     def minn(self):
         current_node = self.root
         anterior = None
         while current_node != None:
              anterior = current_node
              current_node = current_node.getLeft()
         return anterior

     def maxx(self):
         current_node = self.root
         anterior = None
         while current_node != None:
              anterior = current_node
              current_node = current_node.getRight()
         return anterior

     def printOrder(self, ordem):
          if ordem == 'emOrdem':
               print(" Exibindo em ordem: ",end="")
               self.inOrder(self.root)
          
          if ordem == 'posOrdem':
               print("\n Exibindo em pos-ordem: ",end="")
               self.posOrder(self.root)

          if ordem == 'preOrdem':
               print("\n Exibindo em pre-ordem: ",end="")
               self.preOrder(self.root)


     def treeInfo(self):
          print("\n Altura da arvore: %d" %(self.altura(self.root)))
          print(" Quantidade de folhas: %d"  %(self.folhas(self.root)))
          print(" Quantidade de Nós: %d" %(self.contarNos(self.root)))
          if self.root != None: # se arvore nao esta vazia
             print(" Valor minimo: %d" %(self.minn().label))
             print(" Valor maximo: %d" %(self.maxx().label))

     def visualization(self):
          values = [10,5,20,4,6,15,25]
          root = build(values)
          print(root)


            
    






