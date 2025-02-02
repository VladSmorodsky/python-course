from csv_manager import CsvManager
from exceptions.student_score_exception import StudentScoreException

# Error
# CsvManager.read_file('rrrr.jpg')

# Read CSV file
for row in CsvManager.read_file('students.csv'):
    print(row)

# Get average score
try:
    print('Average value:', CsvManager.get_avg_students_value('students.csv'))
except StudentScoreException as exception:
    print(exception)
except Exception as exception:
    print(exception)

# Add student
try:
    CsvManager.write_csv('students.csv', ['Vasil', 22, 90, 'rrr'])
except Exception as exception:
    print(exception)
