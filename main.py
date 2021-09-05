import  time, datetime, asyncio
import os.path 
import os
from pyowm import OWM
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'

owm = OWM('449eaf77b3da91774fae55929496bad0', config_dict)
mgr = owm.weather_manager()

async def weatherstate(b, a, c):
    
    failname = 'temp.txt'
    cur_dir = os.getcwd()
    file_list = os.listdir(cur_dir)
    p = os.path.dirname(cur_dir)

    observation = mgr.weather_at_place(b)
    w = observation.weather
    tempr = w.temperature('celsius').get('temp')
    h = w.humidity
    wind = w.wind().get('speed')
    gr = w.wind().get('deg')
    could = w.clouds

    if  failname in file_list:
        
        f = open('temp.txt', 'a')
        for i in range(a):
            f.write(f"\n{b}\n----------------------------------------\n")
            f.write(f"{datetime.datetime.now()}\n")
            f.write(f"Temperature:{tempr}\nHumidity:{h}%\nWind:{wind} m/s, Deg:{gr}\nClouds:{could}%\n----------------------------------------\n")
            
            time.sleep(c)
        f.close()

    else:
        f = open('temp.txt', 'w')
        for i in range(a):
            f.write(f"\n{b}\n----------------------------------------\n")
            f.write(f"{datetime.datetime.now()}\n")
            f.write(f"Temperature:{tempr}\nHumidity:{h}%\nWind:{wind} m/s, Deg:{gr}\nClouds:{could}%\n----------------------------------------\n")
            
            time.sleep(c)
        f.close()


print("One hour: 3600; 30 minute: 1800; Ten hour: 36000; twelve hour: 43200\n----------------------------------------")
b = str(input("Place: "))
a = int(input("COl=Vo: "))
c = int(input("Time Step (on second's): "))


asyncio.run(weatherstate(b , a, c))
