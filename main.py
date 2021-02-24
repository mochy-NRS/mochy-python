# coding: utf-8

#時間の入力
hours = []
#分の入力
minutes = []



def calc():
  i = 0
  day = 0
  total_minute = 0
  total_hour = 0
  calc_minute = 0
  a = int(len(minutes))
  for i in range(a):
    total_minute += minutes[i]
    total_hour += hours[i]
    day += 1
  calc_minute = total_minute / 60 
  total_hour += calc_minute
  print(str(total_hour) + "時間")
  print(str(day) +  "日")

calc()