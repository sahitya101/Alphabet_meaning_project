import pandas
data = pandas.read_csv('format.csv')
dict_data = {row.letter:row.code for (index, row) in data.iterrows()}
user_input = input("enter a word: ").upper()
output = [dict_data[letter] for letter in user_input]
print(output)