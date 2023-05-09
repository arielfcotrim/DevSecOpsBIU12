#!/bin/bash

echo "What's your name?"
read name

echo "What year were you born?"
read birth_year

current_year=$(date +%Y)
age=$((current_year - birth_year))

if (( $age < 0 )); then
  echo "You haven't been born yet!"
elif (( $age < 18 )); then
  echo "Hello $name, you are $age years old. You are still a minor."
else
  echo "Hello $name, you are $age years old. You are an adult."
fi
When you run this script, it will prompt the user for their name and birth year, calculate their age, and then output a greeting based on their age, for example:

rust
Copy code
What's your name?
Alice
What year were you born?
1990
Hello Alice, you are 31 years old. You are an adult.
Note that this script uses the date command to get the current year and the read command to prompt the user for input. The if statement is used to check the user's age and output a greeting based on their age.






