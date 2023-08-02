import pandas as pd
from docx import Document

ENG520=[]

import sys

user_name=str(input("Enter the name of subject  "))
sys.stdout.flush()
print(user_name)

def extract_table(table_index,user_name):

    document=Document(r"C:\Users\HP\Downloads\CO.docx")
    print(document)
    
    table_data=[]
    table=document.tables[table_index]
    for row in table.rows:
        row_data=[]
        for cell in row.cells:
            row_data.append(cell.text.strip())

        table_data.append(row_data)
    df=pd.DataFrame(table_data[1:],columns=table_data[0])

    for index,row in df.iterrows():
        value=row["Subjects2"]
        if user_name in value:
            value=df.loc[index,"ClassRollNo"]
            ENG520.append(value)
        
    
for i in range(0):
    extract_table(i,user_name)

print(ENG520)
print(f"total no of students are {len(ENG520)}")

with open("newfile.txt",'w') as file:
    for data in ENG520:
        file.write(data+ " ")



    
    
