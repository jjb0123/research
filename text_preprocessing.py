import pandas as pd
import csv 

df = pd.read_csv('mergeddataset.csv', on_bad_lines='skip')


# Check Datasets have merged 
# print(df.to_string())

with open('mergeddataset.csv', 'r') as file:
    review_array=[]
    csvreader=csv.reader(file)
    for row in csvreader:
        review_array.append(row[10])
    	#print(row[10])
	
while ('' in review_array):
    review_array.remove('')
    
# for item in review_array:
#     if item == '':
#         review_array.remove(item)
# writer=csv.writer()

# writer.writerow(review_array)

# print(writer)

pd.DataFrame(review_array).to_csv('preprocessed.csv')
    


        