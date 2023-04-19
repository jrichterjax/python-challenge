import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# Read in Budget csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read Budget csv header
    csv_header = next(csvreader)
         
    # Set variables, lists
    total_months = 0
    loop_count = 0
    total_profit_loss = 0
    total_profit_loss_change = 0
    profit_loss = []
    profit_loss_change = []
    profit_loss_date = []

    for row in csvreader:
    
        # Calculate the total number of months included in the dataset
        total_months += 1

        # Calculate the net total amount of "Profit/Losses" over the entire period
        profit_loss.append(int(row[1]))
        total_profit_loss += profit_loss[loop_count]

        # Create a list containing all values in the date column
        profit_loss_date.append(row[0])    

        # Calculate the changes in "Profit/Losses" over the entire period
        if loop_count >= 1:
            profit_loss_change.append(int(profit_loss[loop_count]) - int(profit_loss[loop_count-1]))
   
        # Next loop
        loop_count += 1   

    # Average the changes in "Profit/Losses" over the entire period
    for number in profit_loss_change:
        total_profit_loss_change += number
    
    avg_profit_loss = round(total_profit_loss_change / len(profit_loss_change), 2)   

    # Calculate the greatest increase in profits (date and amount) over the entire period (https://www.pythonforbeginners.com/basics/find-the-index-of-max-value-in-a-list-in-python)
    inc_profits_amount = max(profit_loss_change)
    inc_profits_index = profit_loss_change.index(inc_profits_amount)
    inc_profits_date = profit_loss_date[inc_profits_index + 1]

    # Calculate the greatest decrease in profits (date and amount) over the entire period (https://www.pythonforbeginners.com/basics/find-the-index-of-max-value-in-a-list-in-python)
    dec_profits_amount = min(profit_loss_change)
    dec_profits_index = profit_loss_change.index(dec_profits_amount)
    dec_profits_date = profit_loss_date[dec_profits_index + 1]  

    # Display analysis
    print('Finanacial Analysis')
    print('--------------------------------')
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit_loss}")
    print(f"Average Change: ${avg_profit_loss}")
    print(f"Greatest Increase in Profits: {inc_profits_date} (${inc_profits_amount})")
    print(f"Greatest Decrease in Profits: {dec_profits_date} (${dec_profits_amount})")

    # Export results to text file (https://www.pythontutorial.net/python-basics/python-write-text-file/)   
    with open('../Analysis/financial_analysis.txt', 'w') as txt_file:
        txt_file.write('Finanacial Analysis\n')
        txt_file.write('--------------------------------\n')
        txt_file.write(f"Total Months: {total_months}\n")
        txt_file.write(f"Total: ${total_profit_loss}\n")
        txt_file.write(f"Average Change: ${avg_profit_loss}\n")
        txt_file.write(f"Greatest Increase in Profits: {inc_profits_date} (${inc_profits_amount})\n")
        txt_file.write(f"Greatest Decrease in Profits: {dec_profits_date} (${dec_profits_amount})")

