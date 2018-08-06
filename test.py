# -*- coding: euc-kr -*-
# -*- coding: utf-8 -*-

# 세계날씨 출력 프로그램
# 제작자 : 10808 이재우
# 참고자료 : http://junolefou.tistory.com/1
# 'pyowm'은 OpenWeatherMap의 API 파싱을 가능하게 하는 래퍼(wrapper) 라이브러리 입니다.
# 'pyowm'이 설치되어 있지 않을 경우를 대비하여 url과 .json 파일을 이용하여 API를 가져오는 방식도 구현하였습니다.

import datetime
now = datetime.datetime.now()
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')

print "Welcome to WorldTemperatureProgram [Version 0.99 beta]"
print "(c) 2018 LJW Corporation. All rights reserved.\n"
print "현재 시각은 ",nowDatetime

question = str(raw_input("OpenWeatherMap의 API 파싱 래퍼(wrapper)라이브러리 'pyowm'이 당신의 컴퓨터에 설치되어 있습니까? Yes 또는 No로 입력해주세요. : "))

while True:
    if question == 'No' or 'no' or 'n':
        import urllib
        import json

        apiurl = 'http://api.openweathermap.org/data/2.5/weather?q='
        city = raw_input('도시를 영문으로 입력하세요(Ex. 서울 = Seoul, 뉴욕 : New York) : ')
        apikey = '&APPID=e4d344e63d9674bcc68a782409c3d5e8'


        def weather(inputcity):
            url = urllib.urlopen(apiurl + city + apikey)
            apid = url.read()
            data = json.loads(apid)
            cityname = data['name']
            weather = data['weather'][0]['main']
            temp = int(data['main']['temp'] - 273.15)
            print cityname + ':', weather + ',', str(temp) + '˚C'


        weather(city)
        
    elif question == 'Yes' or 'yes' or 'y':
        from pyowm import OWM

        API_key = 'e4d344e63d9674bcc68a782409c3d5e8'
        owm = OWM(API_key)

        city = raw_input('도시를 영문으로 입력하세요(Ex. 서울 = Seoul, 뉴욕 : New York) : ')


        def weather(city):
            obs = owm.weather_at_place(city)
            w = obs.get_weather()
            l = obs.get_location()
            print l.get_name() + ':', w.get_status() + ',', w.get_temperature(unit='celsius')['temp'], '˚C'


        weather(city)

    else:
        print "프로그램을 이용해주셔서 감사합니다."
        break
