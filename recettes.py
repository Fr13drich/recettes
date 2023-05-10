from dataclasses import dataclass
import pandas as pd

"""
menu
    recettes[]




ingredient

nom	
kcal	
unité	
proteines	
lipides	
glucides	
sel	
fibres
prix

    nom
    tuple (proteine, glucide, lipide,fibre,kcal)
    prix
    unite:poids(ou piece)
    produit ou acheté
"""


class Ingredient:
    count = 0
    def __init__(self, nom, kcal, unit, protein, lipid, glucid, salt, fibre, price ) -> None:
        self.nom        = nom	
        self.kcal	    = kcal 
        self.unit	    = unit 
        self.protein	=  protein
        self.lipid	    =  lipid
        self.glucid 	=  glucid
        self.salt	    =  salt
        self.fibre      =  fibre
        self.price      =  price

        Ingredient.count += 1

        print("Ingredient créé")
"""
recette
    nom
    nombreDeRepas
    ingredients et/ou recette []
    modeOperatoire []
    saison
    temps
"""
class Recette:
    count = 0
    def __init__(self) -> None:
        

  
#    def addToShoppingList(self):


i1 = Ingredient("café",	20,	"L", 2,	0, 3, 0, 0, 0.7)
i2 = Ingredient("café",	20,	"L", 2,	0, 3, 0, 0, 0.7)
print (Ingredient.count)

df = pd.read_csv("dataScience/data.csv")
print(df.columns.tolist())
print(df.email.tolist())
df["country"].isin(["France", "Canada"])
df.fillna(0, inplace=True)
