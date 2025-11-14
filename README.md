# Revision Priority Algorithm

This algorithm prioritises subject revision based on the subjects current grade and predicted grade.

## How it works

The algorithm works by calculating a priority score considering both predicted and current grade value, with a customisable weight for how much a predicted grade will impact this. This is then compared inside of the sorting algorithm against other subjects that you have provided.

## Example usage

```py
maths = Subject("Maths", "A", "C")
english = Subject("English", "B", "D")
business = Subject("Business", "C", "F")

subjects = [maths, english, business]

sorted_subjects = sortSubjectPriority(subjects)

for subject in sorted_subjects:
    print(f"{subject.name} ~ Current: {subject.getCurrentGrade()} --> Predicted: {subject.getPredictedGrade()}")
```
