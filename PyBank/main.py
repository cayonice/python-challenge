import csv

budget_csv= 'budget_data_1.csv'

totalMonths=0
totalRevenue=0
prev_month=0
monthChange=0
topIncRev=0
topDecRev=0
totalChange=0
max_inc=['',0]
max_dec=['',0]



with open(budget_csv,"r") as budget:
    csvreader=csv.DictReader(budget)
    count=1
    for row in csvreader:
        totalMonths += 1
        totalRevenue+= int(row['Revenue'])
        monthChange = (int(row['Revenue'])- prev_month)
        totalChange= totalChange+monthChange
        
        if prev_month !=0:
            if monthChange> max_inc[1]:
                max_inc[0]=row['Date']
                max_inc[1]=int(monthChange)
            elif monthChange < max_dec[1]:
                max_dec[0]=row['Date']
                max_dec[1]=int(monthChange)
                
        prev_month= int(row['Revenue'])  
       
        
print("Finanial Analysis:")
print("Total Months: "+ str(totalMonths)
print("Total Revenue: $" + str(totalRevenue))
print("Average Revenue Change: "+ str(totalChange)
print("Greatest Increase in Revenue: "+ str(max_inc[0])+" "+ str(max_inc[1])
print("Greatest Decrease in Revenue: "+ str(max_dec[0])+" "+ str(max_dec[1])