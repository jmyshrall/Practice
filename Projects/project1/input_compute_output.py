"""
File: project1/input_compute_output.py
Contributor: Justin Myshrall
Created: 2/2/2023

"""
years = input("Enter a number of years and I'll tell you how many minutes that is ")
years = int(years)
days = years * 365      # converts years to days
hours = days * 24       # converts to hours
minutes = hours * 60    # converts to minutes
seconds = minutes * 60  # converts to seconds
print(years, "years is ", seconds, "seconds")


seconds = input("Enter a number  of seconds and I'll tell you how many years that is")
seconds = int(seconds)
minutes = seconds / 60      # takes seconds and makes minutes
hours = minutes / 60        # converts to hours
days = hours / 24           # converts to days
years = days / 365          # converts to years, excluding leap years
print(seconds, "seconds is", years, "years")      # solution is written in terms of years

second = input("Enter number of seconds I'll tell you Y:M:D:M")
minutes = seconds // 60  # calculates minutes // gives an integer with no remainder
hours = minutes // 60    # converts to hours
days = hours // 24       # converts to days
months = days // 30      # converts to months, 30 days average
years = months // 12     # converts to years, leap year excluded
months = months % 12    # months account for years by returning the remainder of the division
days = days % 30        # days account for years by returning the remainder of the division
print("Years:", years)
print("Months:", months)    # results are presented in order of Y:M:D:M
print("Days:", days)
print("Minutes:", minutes)
