import datetime
import requests
import time

start_date = datetime.date(year=2022, month=3, day=7)
end_date   = datetime.date(year=2022, month=3,  day=11)

current_date = start_date

headers = {
    'authority': 'www.covermanager.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
    'origin': 'https://www.covermanager.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.covermanager.com/reservation/module_restaurant/celler-de-can-roca/spanish?template=https://cellercanroca.com/wp-content/themes/celler/assets/css/custom_form.css',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,es;q=0.7',
    'dnt': '1',
    'sec-gpc': '1',
}

print("Celler de Can Roca waiting list:")
while current_date <= end_date:
    current_date_ccr_format=current_date.strftime("%d-%m-%Y")
    print("Signing up for the waiting list on " + current_date_ccr_format)
    file = open("already-in-the-waitlist.txt", "a")
    file.write(current_date_ccr_format+"\n")

    data = {
      'language': 'spanish',
      'restaurant': 'celler-de-can-roca',
      'people': '2',
      'dia': current_date_ccr_format,
      'hour': '3', # 1: Lunch | 2: Dinner | 3: Lunch or dinner
      'user_name': 'Benito',
      'user_last_name': 'Camelo',
      'user_email': 'benitocamelo@gmail.com',
      'user_phone': '666666666',
      'int_call_code': '34',
      'commentary_client': '',
      'food_restriction': ''
    }

    response = requests.post('https://www.covermanager.com/reservs/new_reserv_waiting', headers=headers, data=data)

    time.sleep(1)
    current_date += datetime.timedelta(days=1)

file.close()
