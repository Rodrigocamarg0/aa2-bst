from BSTree import BSTree

tree = BSTree()
print(tree)
tree.insert(10)
tree.insert(20)
tree.insert(5)
tree.insert(6)
tree.insert(4)
tree.insert(15)
tree.insert(25)


num = 0
while num != 8:

     print("\n========================================")
     print("Insira um número de acordo com a Função:")
     print(" #1: Inserir")
     print(" #2: Remover")
     print(" #3: Pesquisar")
     print(" #4: Em Ordem")
     print(" #5: Pre Ordem")
     print(" #6: Pos Ordem")
     print(" #7: Exibir")
     print(" #8: Sair do programa")
     tree.visualization()
     print("\n========================================")

     num = int(input("-> "))
     if num == 1:
          x = int(input(" Informe o valor -> "))
          tree.insert(x)
     elif num == 2:
          x = int(input(" Informe o valor -> "))
          if tree.remove(x) == False:
               print(" Valor nao encontrado!")
     elif num == 3:
          x = int(input(" Informe o valor -> "))
          if tree.search(x) != None:
               print(" Valor Encontrado")
          else:
               print(" Valor nao encontrado!")	
     elif num == 4:
          tree.printOrder("emOrdem") 
     elif num == 5:
          tree.printOrder("preOrdem")
     elif num == 6:
          tree.printOrder("posOrdem")
     elif num == 7:
          tree.treeInfo()
     elif num == 9:
          tree.treeVizualizer()
     elif num == 8:
          break
 