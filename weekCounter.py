common = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
special = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]

def special_or_not(year):
    if year % 100 == 0:
        return special if year%400 == 0 else common
    return special if year%4==0 else common

def weekCounter(init_position, year):
    month_list = special_or_not(year)
    print(str(year)+':special') if sum(month_list)==335 else print(str(year))
    week_list = [init_position + 1]
    for index in range(len(common)):
        day = (week_list[-1] + month_list[index]-1)%7 + 1
        week_list.append(day)
    return week_list

def yearSpan(start_year, end_year, init_day):
    i = init_day -1
    for y in range(start_year,end_year+1):
       list = weekCounter(i,y)
       i = (list[-1] -1 + 31)%7
       print(list)
       print('-------------------------------')
#yearSpan(1900,1930,1)

#根据已知日期推算某年的元旦是星期几
#2020-02-20 星期四   2022-01-01,
def dayCounterWithSource(source_date, source_week, dest_date):
    source_date_list = list(map(int,source_date.split('-')))
    dest_date_list = list(map(int,dest_date.split('-')))

    year_list = list(range(source_date_list[0]+1,dest_date_list[0]))

    days = 0
    for year in year_list:
        how_many_days = sum(special_or_not(year)) + 31
        days += how_many_days

    full_month_list = special_or_not(source_date_list[0]) + [31]
    days_left_from_next_month = sum(full_month_list[source_date_list[1]:])
    days_left_curr_month = full_month_list[source_date_list[1]-1]-source_date_list[2]+1
    days_left_curr_year = days_left_curr_month+days_left_from_next_month

    total_days = days_left_curr_year + days
    dest_week = (source_week-1 + total_days)%7 + 1
    return dest_week

def autoYearSpan(source_date, source_week, dest_date, year_span):
    dest_date_list = list(map(int, dest_date.split('-')))
    init_day = dayCounterWithSource(source_date, source_week, dest_date)
    yearSpan(dest_date_list[0], dest_date_list[0]+year_span, init_day)


autoYearSpan('2020-10-8',4,'2050-1-1',100)
