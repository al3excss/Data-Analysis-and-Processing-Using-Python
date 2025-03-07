
#Definti o functie python care primeste un string ca argument si returneaza un nou string in care toate vocalele au fost eliminate
#vocale = "aeiouAEIOU"
#input_string = "Salutare,ce mai faci"

vocale = "aeiouAEIOU"
input_string = "Salutare,ce mai faci"

#Varianta 1
def elimina_vocala(ch):
    return ch not in vocale

print(list(filter(elimina_vocala,input_string)))

#Varianta 2

print(filter(lambda x: x not in vocale, input_string))

#Varianta 3 list-comprehention

print(([ch for ch in input_string if ch not in vocale]))