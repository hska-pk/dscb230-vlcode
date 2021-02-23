# everything is an object
x = 2
print(type(x))

l = list()  # create an empty list

d = dict()  # create an empty dictionary

t = tuple()  # create an empty tuple


# Exemplary list operations
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
print(fruits.count('tangerine'))
print(fruits.index('banana'))
print(fruits.index('banana', 4))  # find next banana starting a position 4
fruits.reverse()
print(fruits)

fruits.append('grape')
print(fruits)

fruits.sort()
print(fruits)

print(fruits.pop())
print(fruits)



# dictionary iteration
capitols = {'Germany': 'Berlin', 'France': 'Paris'}
for k, v in capitols.items():
    print(k, v)

# access only the keys or values
print(capitols.keys())
print(capitols.values())

# update / add new dictionary to existing one
capitols.update({'Germany':'Berlin', 'Ireland':'Dublin'})
print(capitols)

# "in"-notation to check existence of keys
print("Ireland" in capitols.keys())

# pop-method in analogy to its usage with lists
print(capitols.pop('France'))
print(capitols)



# create example tabular data structure (pandas DataFrame)
import pandas as pd 
df_sales = pd.DataFrame([['A', 10], ['B', 20], ['B', 15], ['A', 5]], columns=['product', 'sales'])
print(df_sales)

# # use exemplary analysis-method on the DataFrame object
# print(df_sales.groupby('product').agg({'sales' : ['mean', 'min', 'max']}))

# # load dataset 'mpg' into dataframe
# import seaborn as sns
# df_mpg = sns.load_dataset('mpg')
# print(df_mpg.groupby(['origin']).agg({'mpg':'mean', 'horsepower':'mean'}))


# Iteratoren
fruits = ['orange', 'apple']
for fruit in fruits:
    print(fruit)

# explizite Erstellung und Verwendung eines Iterator-Objekts
x = iter(fruits)
print(x)
print(next(x))
print(next(x))
#print(next(x))  # kein nächstes Objekt mehr vorhanden! --> Exception

# so könnte die vollständige 
# Iteration umgesetzt werden,
# aber for-loops sind "eleganter" 
x = iter(fruits)
try:
    while True:
        print(next(x))
except StopIteration:
    pass

# NICHT EMPFOHLEN! Nutzen Sie die pandas-API!
for row in df_sales.values:
    print(row)