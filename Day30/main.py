import pandas as pd

data=pd.read_csv('nato_phonetic_alphabet.csv')
print(data)

dictionaire_fonetique={row.letter:row.code for (index,row) in data.iterrows()}
print(dictionaire_fonetique)
mot=input("Enter a word: ").upper()
try:
    code_fonetique=[dictionaire_fonetique[lettre] for lettre in mot]
except KeyError:
    print("Sorry, only letters in the alphabet please.")
else:
    print(code_fonetique)
