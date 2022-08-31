import pandas as pd
import numpy as np
import re

def check_country(country):
    VALID_COUNTRIES = ['France','India','China','Benin','Madagascar','USA']
    if country not in VALID_COUNTRIES:
        print('- "{}" is not valid contry, we deleted it'.format(country))
        return np.NaN
    return country

def first(string):
    parts = string.split(',')
    first_part = parts[0]
    if len(parts) > 1:
        print(' - There are multiples parts of "{}", use only "{}"'.format(parts,first_part))
        return first_part
    else:
        return string

def convet_hight(height):
    found = re.search('\d\.\d{2}m',height)
    if found is None:
        print('- "{}" is the wrong format. It will be ingnored.'.format(height))
        return np.NaN
    else:
        value = height[:-1] # we remove the 'm'
        return float(value)

def fill_height(height, replacement):
    if pd.isnull(height):
        print('Imputation by the mean: {}'.format(replacement))
        return round(replacement,3)
    return height

def lower_case(value): #Never used
    print ('Here is the first value', value)
    return value.lower()

def main():
    VALID_COUNTRIES = ['France','India','Berin','Madagascar','USA']

    
    data = pd.read_csv('persons.csv')
    print(data)
    print('\ncleaning data\n')

    #3 ways to do the same job

    #Way 1
    #new_column = []
    #for t in data['email']:
    #    new_column.append(first(t))
    #data['email'] = new_column

    #Way 2
    #data['email'] = data['email'].apply(first)

    #Way 3.  Picked because It looks sexy
    data['email'] = [first(t) for t in data['email']]
    
    data['country'] = data['country'].apply(check_country)
    
    data['date_of_birth'] = pd.to_datetime(data['date_of_birth'],format='%d/%m/%Y',errors='coerce')

    data['height'] = [convet_hight(t) for t in data['height']]
    data['height'] = [t if t<3 else np.NaN for t in data['height']]

    mean_height = data['height'].mean()
    data['height'] =[fill_height(t, mean_height) for t in data['height']]

    print('\nCleaned data\n')
    
    print(data)


if __name__=='__main__':
    main()
