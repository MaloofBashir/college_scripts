import pandas as pd
from docx import Document

ENG520=[]

import sys

user_name=str(input("Enter the name of subject  "))
sys.stdout.flush()
print(user_name)

def extract_table(table_index,user_name):

    document=Document(r"C:\Users\HP\Downloads\college.docx")
   
     
    table_data=[]
    table=document.tables[table_index]
    for row in table.rows:
        row_data=[]
        for cell in row.cells:
            row_data.append(cell.text.strip())

        table_data.append(row_data)
    df=pd.DataFrame(table_data[1:],columns=table_data[0])
 
    new_count=0

    for index,row in df.iterrows():
        value=row["Subjects1"]
        if user_name in value:
            value=df.loc[index,"Regd. No"]
            if value.isdigit()!=True:
                print(df.iloc[index])
                new_count+=1
            #value not in ["417","343"]:
            ENG520.append(value)

    #print(f"no of missing values are {new_count}")
for i in range(12):
    extract_table(i,user_name)

print(ENG520)
print(f"total no of students are {len(ENG520)}")
count=0

    
with open("roolno.txt",'w') as file:
    for data in ENG520:
        file.write(data+ ",")


for i in ENG520:
    if i.isdigit():
        count=count+1
        
print(f"new counter value is {count}")
    
    
