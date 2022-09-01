from graph import draw_graph
from API import make_request
import argparse
from datetime import timedelta
from datetime import datetime
from Data_Base import Base

parser = argparse.ArgumentParser()
parser.add_argument('--start', type=str, help='Введите начальную дату поиска в формате: гггг-мм-дд')
parser.add_argument('--end', type=str, help='Введите конечную дату поиска в формате: гггг-мм-дд')
parser.add_argument('--n', type=int, help='Введите количество дней в запросе - n, где n <=100')
arg = parser.parse_args()
start, end, n = arg.start, arg.end, arg.n

x = []
y = []
BTC= Base()
date_end = datetime.strptime(end, "%Y-%m-%d").date()
date = datetime.strptime(start, "%Y-%m-%d").date()

list_of_rest_to_base = []
list_of_rest_to_API = []

while date != date_end + timedelta(days=1):
    if Base.check_base_rest(BTC, date) ==[]:
        list_interval = []
        while Base.check_base_rest(BTC, date) == [] \
                and date != date_end + timedelta(days=1) \
                and len(list_interval) <=n:
            list_interval.append(date)
            date = date + timedelta(days=1)

        list_of_rest_to_API.append(list_interval)

    else:
        list_of_rest_to_base.append(' ')
        date = date + timedelta(days=1)

for i in range(len(list_of_rest_to_API)):
    Base.insert_to_base(BTC, make_request(list_of_rest_to_API[i][0], list_of_rest_to_API[i][-1]))

draw_graph(Base.execute_rest_to_base(BTC, start, end), x, y)




