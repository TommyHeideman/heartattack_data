# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 16:05:04 2023

@author: Tommy
"""


# Tommy Heideman and Joey Matusik

import utilities

def main():
    print("\033[1mHeart Attack Analysis\033[0m\n")
    print("These are the factors related to heart attacks that are considered in this data:\n")
    print("1. Heart Attack Percentage is calculated based on all data to see if the data is skewed.")
    utilities.getHeartAttack()
    print("\n2. Gender Percent is used to distinguish between the heart attack rates in men and women.")
    utilities.getGender()
    print("\n3. Four types of Chest Pain are considered, along with the associated heart attack percentages.")
    utilities.getChestPain()
    print("\n4. Fasting Blood Sugar levels are considered to determine possible coronary heart disease.")
    utilities.getBloodSugar()
    print("\n5. EKG is considered, as it detects heart problems that can forecast chance of future heart attacks.")
    utilities.getEKG()
    print("\n6. Exercise is considered to see if likelihood of heart attack increases when physically active.")
    utilities.getExercise()

if __name__ == "__main__":
    main()



