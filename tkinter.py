# IMPORTING REQUIRED MODULES

import tkinter as tk
import csv
import matplotlib.pyplot as plt
import pandas as pd
import functools


# TKINTER GUI

root = tk.Tk()
root.title("Female Employment vs Socioeconimic Factors")
root.geometry('460x300')

# SETTING COLUMN USING PANDAS

pd.set_option('display.max_columns',14 )

col_list = ['Year','PerFemEmploy','FertilityRate','Ratio_MaletoFemale','PerFemEmployers','Agriculture','Industry','Services','Wage&Salaried','ContrFamWorkers','OwnAccount','Vulnerable']

# OPENING A DATA SET AND WRITING INTO CSV

with open('data.csv') as data_set:
# create the csv writer
    csv.writer(data_set)  
    data_set.close()
   
# OPENING CSV AND READIND    
   
with open('data.csv'):
    csv_reader = pd.read_csv('data.csv', delimiter=',',usecols = col_list)
    print(csv_reader)    

# FUNCTIONS TO PLOT THE DATA

def graphVulnerable():
    plt.hist(csv_reader['Vulnerable'],color='teal')
    plt.xlabel('Year')
    plt.ylabel('Vulnerable')
    plt.show()
   
    # CALCULATIONS ON DATA
   
    l = csv_reader['Vulnerable']
    MAX = max(l)
   
    print(f'MAXIMUM VULNERABLE {MAX} ')
   
    MIN = min(l)
   
    print(f'MINIMUM VULNERABLE {MIN} ')
   
    print("AVERAGE OF 25 YEARS ",(functools.reduce(lambda x , y : x + y,l ))/len(l))

def graphPie():
    OwnAccount = csv_reader['OwnAccount']
    plt.pie(OwnAccount,labels=csv_reader['Year'])
    plt.show()
   
    # CALCULATIONS ON DATA
   
    l = csv_reader['OwnAccount']
    MAX = max(l)
   
    print(f'MAXIMUM OwnAccount {MAX} ')
   
    MIN = min(l)
   
    print(f'MINIMUM OwnAccount {MIN} ')
   
    print("AVERAGE OF 25 YEARS ",(functools.reduce(lambda x , y : x + y,l ))/len(l))

def graphContrFamWorkers():
                 
        plt.hist(csv_reader['ContrFamWorkers'],color='tan')
        plt.xlabel('Year')
        plt.ylabel('ContrFamWorkers')
        plt.show()
       
        # CALCULATIONS ON DATA
       
        l = csv_reader['ContrFamWorkers']
        MAX = max(l)
       
        print(f'MAXIMUM ContrFamWorkers {MAX} ')
       
        MIN = min(l)
       
        print(f'MINIMUM ContrFamWorkers {MIN} ')
       
        print("AVERAGE OF 25 YEARS ",(functools.reduce(lambda x , y : x + y,l ))/len(l))
   
def graphWageSalaried():
                 
        plt.hist(csv_reader['Wage&Salaried'],color='yellow')
        plt.xlabel('Year')
        plt.ylabel('Wage&Salaried')
        plt.show()
       
        # CALCULATIONS ON DATA
       
        l = csv_reader['Wage&Salaried']
        MAX = max(l)
       
        print(f'MAXIMUM Wage&Salaried {MAX} ')
       
        MIN = min(l)
       
        print(f'MINIMUM Wage&Salaried {MIN} ')
       
        print("AVERAGE OF 25 YEARS ",(functools.reduce(lambda x , y : x + y,l ))/len(l))
   
def graphServices():
                 
        plt.plot(csv_reader['Year'],csv_reader['Services'],color = 'aqua')
        plt.xlabel('Year')
        plt.ylabel('Services')
        plt.show()  
       
        # CALCULATIONS ON DATA
       
        l = csv_reader['Services']
        MAX = max(l)
       
        print(f'MAXIMUM Services {MAX} ')
       
        MIN = min(l)
       
        print(f'MINIMUM Services {MIN} ')
       
        print("AVERAGE OF 25 YEARS ",(functools.reduce(lambda x , y : x + y,l ))/len(l))
   
def graphPerFemEmployers():
                 
        plt.bar(csv_reader['Year'],csv_reader['PerFemEmployers'],color = 'purple')
        plt.xlabel('Year')
        plt.ylabel('PerFemEmployers')
        plt.show()    
       
        # CALCULATIONS ON DATA
       
        l = csv_reader['PerFemEmployers']
        MAX = max(l)
       
        print(f'MAXIMUM PerFemEmployers {MAX} ')
       
        MIN = min(l)
       
        print(f'MINIMUM PerFemEmployers {MIN} ')
       
        print("AVERAGE OF 25 YEARS ",(functools.reduce(lambda x , y : x + y,l ))/len(l))
       
def graphFertilityRate():
                 
        plt.plot(csv_reader['Year'],csv_reader['FertilityRate'],color = 'gold')
        plt.xlabel('Year')
        plt.ylabel('FertilityRate')
        plt.show()  
       
        # CALCULATIONS ON DATA
       
        l = csv_reader['FertilityRate']
        MAX = max(l)
       
        print(f'MAXIMUM FertilityRate {MAX} ')
       
        MIN = min(l)
       
        print(f'MINIMUM FertilityRate {MIN} ')
       
        print("AVERAGE OF 25 YEARS ",(functools.reduce(lambda x , y : x + y,l ))/len(l))
       
def graphPerFemEmploy():
                 
        plt.bar(csv_reader['Year'],csv_reader['PerFemEmploy'],color = 'pink')
        plt.xlabel('Year')
        plt.ylabel('PerFemEmploy')
        plt.show()
       
        # CALCULATIONS ON DATA
       
        l = csv_reader['PerFemEmploy']
        MAX = max(l)
       
        print(f'MAXIMUM PerFemEmploy {MAX} ')
       
        MIN = min(l)
       
        print(f'MINIMUM PerFemEmploy {MIN} ')
       
        print("AVERAGE OF 25 YEARS ",(functools.reduce(lambda x , y : x + y,l ))/len(l))
       
   
def graphRatio_MaletoFemale():
                 
        plt.plot(csv_reader['Year'],csv_reader['Ratio_MaletoFemale'],color = 'indigo')
        plt.xlabel('Year')
        plt.ylabel('Ratio_MaletoFemale')
        plt.show()
       
        # CALCULATIONS ON DATA
       
        l = csv_reader['Ratio_MaletoFemale']
        MAX = max(l)
       
        print(f'MAXIMUM Ratio_MaletoFemale {MAX} ')
       
        MIN = min(l)
       
        print(f'MINIMUM Ratio_MaletoFemale {MIN} ')
       
        print("AVERAGE OF 25 YEARS ",(functools.reduce(lambda x , y : x + y,l ))/len(l))
       
       
def graphAgriculture():
                 
        plt.plot(csv_reader['Year'],csv_reader['Agriculture'],color = 'green')
        plt.xlabel('Year')
        plt.ylabel('Agriculture')
        plt.show()
       
        # CALCULATIONS ON DATA
       
        l = csv_reader['Agriculture']
        MAX = max(l)
       
        print(f'MAXIMUM Agriculture {MAX} ')
       
        MIN = min(l)
       
        print(f'MINIMUM Agriculture {MIN} ')
       
        print("AVERAGE OF 25 YEARS ",(functools.reduce(lambda x , y : x + y,l ))/len(l))

def graphIndustry():
                 
        plt.plot(csv_reader['Year'],csv_reader['Industry'])
        plt.xlabel('Year')
        plt.ylabel('Industry')
        plt.show()  
       
        # CALCULATIONS ON DATA
       
        l = csv_reader['Industry']
        MAX = max(l)
       
        print(f'MAXIMUM Industry {MAX} ')
       
        MIN = min(l)
       
        print(f'MINIMUM Industry {MIN} ')
       
        print("AVERAGE OF 25 YEARS ",(functools.reduce(lambda x , y : x + y,l ))/len(l))
       

def graphIndustryAgriculture():
                 
        plt.stackplot(csv_reader['Agriculture'],csv_reader['Industry'],color='blue' )
        plt.xlabel('Agriculture')
        plt.ylabel('Industry')
        plt.show()
       
 
       
# TKINTER BUTTONS TO CALL GRAPHING FUNCTIONS
   
button = tk.Button(root, text="GET GRAPH Industry Agriculture",bg='black',fg = "white",command = graphIndustryAgriculture)
button.pack()

button = tk.Button(root, text="GET GRAPH PerFemEmploy",bg='black',fg = "white",command = graphPerFemEmploy)
button.pack()

button = tk.Button(root, text="GET GRAPH FertilityRate",bg='black',fg = "white",command = graphFertilityRate)
button.pack()

button = tk.Button(root, text="GET GRAPH Ratio_MaletoFemale",bg='black',fg = "white",command = graphRatio_MaletoFemale)
button.pack()

button = tk.Button(root, text="GET GRAPH PerFemEmployers",bg='black',fg = "white",command = graphPerFemEmployers)
button.pack()

button = tk.Button(root, text="GET GRAPH Agriculture",bg='black',fg = "white",command = graphAgriculture)
button.pack()

button = tk.Button(root, text="GET GRAPH Industry",bg='black',fg = "white",command = graphIndustry)
button.pack()

button = tk.Button(root, text="GET GRAPH Services",bg='black',fg = "white",command = graphServices)
button.pack()

button = tk.Button(root, text="GET GRAPH Wage&Salaried",bg='black',fg = "white",command = graphWageSalaried)
button.pack()

button = tk.Button(root, text="GET GRAPH ContrFamWorkers",bg='black',fg = "white",command = graphContrFamWorkers)
button.pack()

button_pie = tk.Button(root, text="GET PIE CHART 'OwnAccount'",bg='black',fg = "white",command = graphPie)
button_pie.pack()

button = tk.Button(root, text="GET GRAPH Vulnerable",bg='black',fg = "white",command = graphVulnerable)
button.pack()

root.mainloop()
