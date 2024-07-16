import csv
import ast

def update(row):
    f = open('MiniProject\\orders.csv', 'a', newline='')
    
    # Use ast.literal_eval to convert the string to a list
    data = ast.literal_eval(row)
    
    csvw = csv.writer(f)
    csvw.writerow(data)  # Use writerow for a single row
    f.flush()
    f.close()
    return 0

