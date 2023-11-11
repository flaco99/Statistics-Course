with open('sales.txt', 'r') as file:
    big_list = file.readlines()

sales = [0]*12
top_sales = 0
top_loc = ''
lowest_sales = -1
lowest_loc = ''

for line in big_list:
    list_line = line.split(' ')
    name = list_line[0]
    loc_sales = 0

    for i in range(11):
        sales_in_month = int(list_line[i+1])
        sales[i] += sales_in_month
        loc_sales += sales_in_month
    dec_sales = int(list_line[12].strip('\n'))
    sales[11] += dec_sales
    loc_sales += dec_sales

    if loc_sales > top_sales:
        top_sales = loc_sales
        top_loc = name
    if lowest_sales == -1:
        lowest_sales = loc_sales
        lowest_loc = name
    if loc_sales < lowest_sales:
        lowest_sales = loc_sales
        lowest_loc = name

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']

with open('summary.txt', 'w') as file:
    for m in range(12):
        file.write(months[m] + ' ' + str(sales[m]) + '\n')
    file.write('Highest sales: ' + top_loc + ' ' + str(top_sales) + '\n')
    file.write('Lowest sales: ' + lowest_loc + ' ' + str(lowest_sales))