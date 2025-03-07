
#Creati o funcite python care primeste o lista de intregi ca argument si returneaza o noua lista care contine doar valori mai mari de 5.
#lista = [10,2,30,50,300,10]


lista = [10,2,30,50,300,10]

def elimina_elem(element):
    return element > 5

filter(elimina_elem, lista)

#lista filter
print(list(filter(elimina_elem,lista)))

#filter + lambda
print(list(filter(lambda x:x > 5,lista)))

# list comprehention
print([element for element in lista if element > 5])