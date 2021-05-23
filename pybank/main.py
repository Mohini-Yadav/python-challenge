import os
import csv


months = []
p_l = []
average_net_change = 0
total_months = 0
net_change = []


csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)
   
    for row in csv_reader:
        month = row[0]
        months.append(month)
        values = int(row[1])
        p_l.append(values)

total_months = len(months)
net_total = sum(p_l)
net_total_months = len(months) - 1
difference_budget_data = []

for i in range(len(p_l) - 1):
    difference_budget_data.append(float(p_l[i + 1]) - float(p_l[i]))
new_net_total = sum(difference_budget_data)


average_net_change = new_net_total / net_total_months


min_p = p_l[p_l.index(min(p_l))] - p_l[p_l.index(min(p_l)) - 1]
max_p = p_l[p_l.index(max(p_l))] - p_l[p_l.index(max(p_l)) - 1]


print("Financial Analysis")
print("--------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${round(average_net_change, 2)}")
print(f'Greatest Increase in Profits: {months[p_l.index(max(p_l))]} (${max_p})')
print(f"Greatest Descrease in Profits: {months[p_l.index(min(p_l))]} (${min_p})")


output_file = 'Analysis/financial_analysis.txt'
with open(output_file, "w", newline="") as datafile:
     csvwriter = csv.writer(datafile)
     csvwriter.writerow(["Financial Analysis"])
     csvwriter.writerow(["--------------------"])
     csvwriter.writerow([f"Total Months: {total_months}"])
     csvwriter.writerow([f"Total: ${net_total}"])
     csvwriter.writerow([f"Average Change: ${round(average_net_change, 2)}"])
     csvwriter.writerow([f'Greatest Increase in Profits: {months[p_l.index(max(p_l))]} (${max_p})'])
     csvwriter.writerow([f"Greatest Decrease in Profits: {months[p_l.index(min(p_l))]} (${min_p})"])
