# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 16:05:05 2023

@author: Tommy
"""



import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('heart.csv')

total_ppl = len(df['attack'])
attack_df = df[df.attack == 1]
no_attack_df =df[df.attack == 0]


def getHeartAttack():
    attack = df['attack'].value_counts()[1]

    no_attack = df['attack'].value_counts()[0]

    percent_attack = attack/total_ppl * 100
    percent_no_attack = no_attack/total_ppl * 100

    percent_attack_round = np.round(percent_attack,2)
    percent_no_attack_round = np.round(percent_no_attack,2)


    print('The percent of no heart attacks in the data: ', percent_no_attack_round, '%')
    print('The percent of heart attacks in the data: ', percent_attack_round, '%')

    plt.pie([percent_no_attack_round, percent_attack_round], startangle=90, labels=["No Heart Attack", "Heart Attack"], autopct=lambda p: '{:.2f}%'.format(p))
    plt.title('Heart Attack Ratio in Data')
    plt.savefig('heart_attack.png')
    plt.show()
    
    return 0

getHeartAttack()
    
def getGender():
    
    total_attack = len(attack_df['attack'])
    female_attack = attack_df['sex'].value_counts()[1]
    male_attack = attack_df['sex'].value_counts()[0]
    
    
    percent_female = female_attack/total_attack * 100 
    percent_male = male_attack/total_attack * 100
    
    percent_female_round = np.round(percent_female,2)
    percent_male_round = np.round(percent_male,2)
    
    
    print('Male heart attacks: ', percent_male_round, "%")
    print('Female heart attacks: ', percent_female_round, "%")
    
    plt.pie([percent_male_round, percent_female_round], startangle=90, labels=["Male", "Female"], autopct=lambda p: '{:.2f}%'.format(p))
    plt.title('Heart Attack Ratio between Male & Female')
    plt.savefig('Gender.png')
    plt.show()
    
    
    
    return 0

getGender()

def getChestPain():
   
    typical_total = df['cp'].value_counts()[0]
   
    atypical_total = df['cp'].value_counts()[1]
   
    notchest_total = df['cp'].value_counts()[2]
                       
    asymptomatic_total = df['cp'].value_counts()[3]
   
    typical_attack = attack_df['cp'].value_counts()[0]
       
    atypical_attack = attack_df['cp'].value_counts()[1]
       
    notchest_attack = attack_df['cp'].value_counts()[2]
       
    asymptomatic_attack = attack_df['cp'].value_counts()[3]
       
    percent_typical = typical_attack/typical_total * 100
    percent_atypical = atypical_attack/atypical_total * 100
    percent_notchest = notchest_attack/notchest_total * 100
    percent_asymptomatic = asymptomatic_attack/asymptomatic_total * 100
   
    percent_typical_round = np.round(percent_typical,2)
    percent_atypical_round = np.round(percent_atypical,2)
    percent_notchest_round = np.round(percent_notchest,2)
    percent_asymptomatic_round = np.round(percent_asymptomatic,2)
   
   
    print('Chest Pain Type: ')
   
    print('  0- Typical Chest Pain')
    print('  1- Atypical Chest Pain')
    print('  2- Any pain that is not chest pain')
    print('  3- Asymptomatic')
   
   
   
    print('The percent of heart attacks in the data with chest pain type 0: ', percent_typical_round, '%')
    print('The percent of heart attacks in the data with chest pain type 1: ', percent_atypical_round, '%')
    print('The percent of heart attacks in the data with chest pain type 2: ', percent_notchest_round, '%')
    print('The percent of heart attacks in the data with chest pain type 3: ', percent_asymptomatic_round, '%')
   
    #Bar Graph
   
    names = ['Typical Chest Pain', 'Atypical Chest Pain', 'Any pain that is not chest pain', 'Asymptomatic']
    values = [percent_typical_round, percent_atypical_round, percent_notchest_round, percent_asymptomatic_round]
   
    plt.bar(names, values, color = ['red'])
    plt.title('Percent Heart Attack')
    plt.savefig('Chest_pain_heart_attack.png')
    plt.show()
   
getChestPain()  


def getBloodSugar():
   
    high_total = df['fbs'].value_counts()[1]
   
    regular_total = df['fbs'].value_counts()[0]
   
    high_attack = attack_df['fbs'].value_counts()[1]
   
    regular_attack = attack_df['fbs'].value_counts()[0]
   
    percent_high = high_attack/high_total * 100
    percent_regular = regular_attack/regular_total * 100
   
    percent_high_round = np.round(percent_high,2)
    percent_regular_round = np.round(percent_regular,2)
   
    print('The percent of heart attacks in the data with high blood sugar: ', percent_high_round, '%')
    print('The percent of heart attacks in the data with regular blood sugar: ', percent_regular_round, '%')
   
    labels = ['High', 'Regular']
    values = [percent_high_round, percent_regular_round]
    plt.bar(labels, values, color = 'green')
    plt.ylabel('Percent Heart Attack')
    plt.title('Blood Sugar')
    plt.savefig('Blood_sugar_heart_attack.png')
    plt.show()
   
   
   
getBloodSugar()

def getEKG():

    normal_total = df['restecg'].value_counts()[0]
    ST_wave_total = df['restecg'].value_counts()[1]
    LV_total = df['restecg'].value_counts()[2]

    normal_attack = attack_df['restecg'].value_counts()[0]
    ST_wave_attack = attack_df['restecg'].value_counts()[1]
    LV_attack = attack_df['restecg'].value_counts()[2]

    percent_normal = normal_attack/normal_total * 100
    percent_ST_wave = ST_wave_attack/ST_wave_total * 100
    percent_LV = LV_attack/LV_total * 100

    percent_normal_round = np.round(percent_normal,2)
    percent_ST_wave_round = np.round(percent_ST_wave,2)
    percent_LV_round = np.round(percent_LV,2)
   
    print('EKG Type:')
    print('     0 - EKG was normal')
    print('     1 - EKG had an abnormality with ST-T Wave')
    print('     2 - EKG had an abnormality in the Left ventricular')

    print('Resting EKG Type 0 had this percent of heart attack:', percent_normal_round, '%')
    print('Resting EKG Type 1 had this percent of heart attack:', percent_ST_wave_round, '%')
    print('Resting EKG Type 2 had this percent of heart attack:', percent_LV_round, '%')
   
    #Bar Graph
    names = ['Normal', 'Abnormal ST-T Wave', 'Abnormal Left Ventrical']
    values = [percent_normal_round, percent_ST_wave_round, percent_LV_round]

    plt.bar(names, values, color = ['red'])
    plt.title('Percent Heart Attack By Resting EKG')
    plt.xlabel('EKG Type')
    plt.ylabel('Percent')
    plt.savefig('EKG_heart_attack.png')
    plt.show()

    return 0

getEKG()

def getExercise():
  people_exng = df['exng'].value_counts()[1]
  people_noexng = df['exng'].value_counts()[0]
  
    
  exng_attack = attack_df['exng'].value_counts()[1]
  noexng_attack = attack_df['exng'].value_counts()[0]

  percent_exe_ht = exng_attack/people_exng  * 100
  percent_no_exe_ht = noexng_attack/people_noexng * 100 
    
  percent_exe_ht_round = round(percent_exe_ht, 2)
  percent_no_exe_ht_round = round(percent_no_exe_ht, 2)
  
  
  print("Percent who Exercised and had heart attack: ", percent_exe_ht_round, "%" )
  print("Percent with No Exercise and had heart attack: ", percent_no_exe_ht_round, "%")
    
  # plot bar graph
  labels = ['Yes', 'No']
  values = [percent_exe_ht_round, percent_no_exe_ht_round]
  plt.bar(labels, values, color = 'purple')
  plt.ylabel('Percentage')
  plt.title('Exercise and Heart Attack')
  plt.savefig('Exercise_afa.png')
  plt.show()


  return 0 

getExercise()



    


    
     

   


