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
    fg = hw_grade()
    fg += lab_grade()
    fg += proj_grade(100)
    fg += quiz_grade(100,100,100)
    fg += peer_grade(100,100,100,100,100,100,100,100,100)
    print fg*100, '%'

# Each function below will divide your total by the total amount of
# points that were available. Then multiplys by the total percent that
# part of your grade is worth
def hw_grade():
    hw1 = int(raw_input("Homework 1 grade: "))
    hw2 = int(raw_input("Homework 2 grade: "))
    hw3 = int(raw_input("Homework 3 grade: "))
    hw4 = int(raw_input("Homework 4 grade: "))
    hw5 = int(raw_input("Homework 5 grade: "))
    hw6 = int(raw_input("Homework 6 grade: "))
    hw7 = int(raw_input("Homework 7 grade: "))
    final_grade = (hw1+hw2+hw3+hw4+hw5+hw6+hw7)/700.0*0.3
    return round(final_grade, 2)

def lab_grade():
    lab1 = int(raw_input("Lab 1 grade: "))
    lab2 = int(raw_input("Lab 2 grade: "))
    lab3 = int(raw_input("Lab 3 grade: "))
    lab4 = int(raw_input("Lab 4 grade: "))
    lab5 = int(raw_input("Lab 5 grade: "))
    lab6 = int(raw_input("Lab 6 grade: "))
    lab7 = int(raw_input("Lab 7 grade: "))
    lab8 = int(raw_input("Lab 8 grade: "))
    lab9 = int(raw_input("Lab 9 grade: "))
    final_grade = (lab1+lab2+lab3+lab4+lab5+lab6+lab7+lab8+lab9)/900.0*0.3
    return round(final_grade, 2)

def proj_grade(proj):
    proj = int(raw_input("Project grade: "))
    final_grade = proj/100*0.2
    return round(final_grade, 2)

def quiz_grade(quiz1,quiz2,quiz3):
    quiz1 = int(raw_input("Quiz 1 grade: "))
    quiz2 = int(raw_input("Quiz 2 grade: "))
    quiz3 = int(raw_input("Quiz 3 grade: "))
    final_grade = (quiz1+quiz2+quiz3)/300.0*0.1
    return round(final_grade, 2)

def peer_grade(peer1,peer2,peer3,peer4,peer5,peer6,peer7,peer8,peer9):
    peer1 = int(raw_input("Peer 1 grade: "))
    peer2 = int(raw_input("Peer 2 grade: "))
    peer3 = int(raw_input("Peer 3 grade: "))
    peer4 = int(raw_input("Peer 4 grade: "))
    peer5 = int(raw_input("Peer 5 grade: "))
    peer6 = int(raw_input("Peer 6 grade: "))
    peer7 = int(raw_input("Peer 7 grade: "))
    peer8 = int(raw_input("Peer 8 grade: "))
    peer9 = int(raw_input("Peer 9 grade: "))
    final_grade = (peer1+peer2+peer3+peer4+peer5+peer6+peer7+peer8+peer9)/900.0*0.1
    return round(final_grade, 2)

final_grade()
