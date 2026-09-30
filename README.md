# PLP Python Week 3 Assignment

This repository contains my Python Week 3 assignment.

* `name_greeter.py` — asks for a full name, splits it into parts, and greets the user by their first name.
* `bug_hunt.py` — fixes three bugs in the provided Python program and includes three `# BUG:` comments explaining the fixes.
* `ticket_checker.py` — checks whether a person is an adult and displays the appropriate ticket price.
* `screenshots/` — contains screenshots showing each Python program running successfully.
* `README.md` — provides an overview of the assignment files and the Part B debugging experience.

### Part B Debugging

The bug that took me longest to find was the age calculation because `input()` returns the age as a string, so Python could not add `1` directly to it. The error message helped me understand that I needed to convert the input into an integer using `int()`.
# PLP Python Week 4 Assignment

This repository contains my Python Week 4 assignment covering conditional statements, validation, logical operators, and nested decisions.

### Files

* `grade_classifier.py` — Classifies a score from 0 to 100 into grades A, B, C, D, or F and validates the input.
* `eligibility_checker.py` — Checks whether a person is eligible to join a local coding club based on age and parental consent.
* `atm_menu.py` — Simulates a simple ATM withdrawal using a PIN, balance checking, and nested decisions.
* `screenshots/` — Contains screenshots showing the programs running with the required test cases.

### When is `elif` better than several separate `if` statements?

`elif` is better when you are checking several mutually exclusive conditions and only one result should be selected. It makes the code clearer and ensures that once one condition is true, the remaining conditions are not checked.
# PLP Python Week 5 Assignment

This repository contains my PLP Python Week 5 assignment covering while loops, for loops, counters, and repetition.

### Files

* `countdown.py` — Counts down from a number entered by the user and prints "Blast off!" when the countdown ends.
* `guess_game.py` — Runs a number guessing game with hints and an attempt counter.
* `spell_it_out.py` — Prints each letter of a word separately and then displays the letters with numbers.
* `screenshots/` — Contains screenshots showing each program running successfully.

### When would you reach for a `while` loop instead of a `for` loop?

I would use a `while` loop when I want a program to keep repeating until a particular condition becomes false or an event occurs. A `for` loop is usually better when I know what items or range I want to iterate through.

# PLP Python Week 6 Assignment

`safe_tools.py` — Contains three safe functions for division, number conversion, and dictionary field lookup.

`unbreakable.py` — Demonstrates handling errors so the program can continue running safely.

The `if` check cannot catch `abc` on its own because `abc` causes a `ValueError` when Python tries to convert it to an integer. The `if` statement can check a value after conversion, but `try/except` is needed to handle the conversion error itself.

# PLP Python Week 7 Assignment

This repository contains my Python Week 7 assignment.

* `shopping_list.py` — manages a shopping list by allowing the user to add, remove, show, and finish the list.
* `list_report.py` — prints a numbered list, counts item names with more than four letters, and finds the longest item name.
* `screenshots/` — contains screenshots showing the programs running successfully.
* `README.md` — explains the assignment files and why checking `in` before `.remove()` is important.

### Why check `in` before `.remove()`?

It is safer to check whether an item is in the list before calling `.remove()` because `.remove()` causes a `ValueError` if the item does not exist. Using `if item in shopping_list` prevents the program from crashing and allows us to display a helpful message such as, "That item is not on your list."

