orig_sent = "List Comprehensions are the Greatest!"
vowels = ["a", "e", "i", "o", "u"]
new_sent = "".join([letter for letter in orig_sent if not letter in vowels])
print (new_sent)

###########################

with open("text_for_hw") as my_file:
    contents = my_file.readlines()


def water_and_date(item):
    return [line.split(",")[4:] for line in item]

last_two = water_and_date(contents)

def water_list(data):
    return [float(flt[0]) for flt in data[1:]]

celsius_temps = water_list(last_two)

def fahrenheit_temps(data):
    return [int((celsius_temps * 1.8) + 32) for celsius_temps in data]
print (fahrenheit_temps(celsius_temps))

def waves_and_dates(item):
    return [line.split(",")[-1::-4] for line in item]
date_waves = waves_and_dates(contents)
dw_dict = dict(date_waves)
print (dw_dict)

def wave_ht_func(item):
    return [(line.split(",")[1]) for line in item]
wave_ht = wave_ht_func(contents)
wave_ht_num = wave_ht[1:]
print (wave_ht_num)

def date_func(item):
    return [(line.split(",")[-1]) for line in item]
just_date = date_func(contents)

new_list = []
for item in wave_ht_num:
    new_list.append(float(item))

def avg_waves(item):
    return [(sum(new_list)) / len(new_list)]
avg_wave_var = avg_waves(contents)
print (avg_wave_var)

#####################################################

d = {
'Gale': {'Homework 1': 88, 'Homework 2': 76},
'Jordan': {'Homework 1': 92, 'Homework 2': 87},
'Peyton': {'Homework 1': 84, 'Homework 2': 77},
'River': {'Homework 1': 85, 'Homework 2': 91}
 }
