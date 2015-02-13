# Lab 0
# Using Python write a program that will calculate your final
# grade in this course
#
# By - Dallas Hays - dallas.hays@colorado.edu
# Date - 1/14/15
# Homework 30% (7 total)
# Labs 30% (9 total)
# Project 20% (1 total)
# Quizzes 10% (3 total)
# Peer Reviews 10% (7 total)

def final_grade():
    # Change grades in here
    # Find the percent for each of the requirements and add them together

    fg = hw_grade(100,100,100,100,100,100,100)
    fg += lab_grade(100,100,100,100,100,100,100,100,100)
    fg += proj_grade(100)
    fg += quiz_grade(100,100,100)
    fg += peer_grade(100,100,100,100,100,100,100,100,100)
    print fg*100, '%'

# Each function below will divide your total by the total amount of
# points that were available. Then multiplys by the total percent that
# part of your grade is worth
def hw_grade(hw1, hw2, hw3, hw4, hw5, hw6, hw7):
    final_grade = (hw1+hw2+hw3+hw4+hw5+hw6+hw7)/700.0*0.3
    return round(final_grade, 2)

def lab_grade(lab1,lab2,lab3,lab4,lab5,lab6,lab7,lab8,lab9):
    final_grade = (lab1+lab2+lab3+lab4+lab5+lab6+lab7+lab8+lab9)/900.0*0.3
    return round(final_grade, 2)

def proj_grade(proj):
    final_grade = proj/100*0.2
    return round(final_grade, 2)

def quiz_grade(quiz1,quiz2,quiz3):
    final_grade = (quiz1+quiz2+quiz3)/300.0*0.1
    return round(final_grade, 2)

def peer_grade(peer1,peer2,peer3,peer4,peer5,peer6,peer7,peer8,peer9):
    final_grade = (peer1+peer2+peer3+peer4+peer5+peer6+peer7+peer8+peer9)/900.0*0.1
    return round(final_grade, 2)

final_grade()
