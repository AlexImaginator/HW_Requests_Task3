import requests
import datetime as dt
import time


class QuestionFinder:

    def get_unix_time(self, date_str):
        year, month, day = date_str.split('-')[:]
        date = dt.date(int(year), int(month), int(day))
        unix_time = time.mktime(date.timetuple())
        return unix_time

    def get_questions(self, *tags, fromdate=str(dt.date.today()-dt.timedelta(days=2)), todate=str(dt.date.today())):
        url = 'https://api.stackexchange.com/2.3/search/advanced'
        params = {
            'fromdate': int(self.get_unix_time(fromdate)),
            'todate': int(self.get_unix_time(todate)),
            'order': 'desc',
            'sort': 'creation',
            'site': 'stackoverflow'
        }
        if len(tags) > 0:
            params['tagged'] = ';'.join(tags)
        resp = requests.get(url, params=params)
        for number, item in enumerate(resp.json()['items'], start=1):
            print(f'''{number}. {item['title']}''')


q_finder = QuestionFinder()
fromdate = '2022-03-28'
todate = '2022-03-30'
q_finder.get_questions('Python')
