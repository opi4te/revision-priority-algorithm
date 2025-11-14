grades = {
    "A+": 7,
    "A": 6,
    "B": 5,
    "C": 4,
    "D": 3,
    "E": 2,
    "F": 1
}

# Contains the basic details about a subject; name, current grade and predicted grade.
class Subject:
    def __init__(self, name, predicted, current) -> None:
        self.name = name
        self._predicted = predicted
        self._current = current

    def getCurrentGrade(self):
        return self._current
    
    def getPredictedGrade(self):
        return self._predicted

# Calculates the priority score on a subject based on how well you are doing in the subject
# and also the subjects predicted grade.
def calculatePriorityScore(subject):
    # weight controls how much the predicted grade influences the score. 
    # A higher weight means the predicted grade has more impact on the final score.
    weight = 0.5

    current_grade_value = grades[subject.getCurrentGrade()]
    improvement = grades[subject.getPredictedGrade()] - current_grade_value
    
    return current_grade_value - weight * improvement

# We use a selection sort to go through each subject and prioritise each one based on the priority score.
def sortSubjectPriority(subjects):
    x = len(subjects)
    
    for i in range(x):
        idx = i

        for j in range(i + 1, x):
            if calculatePriorityScore(subjects[j]) < calculatePriorityScore(subjects[idx]):
                idx = j

        subjects[i] = subjects[idx]
        subjects[idx] = subjects[i]
    
    return subjects
