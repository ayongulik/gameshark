# Prequisites:
# 1. Install Anaconda
# 2. Launch Spyder IDE from Anaconda Navigator
# 3. Create new project on Spyder IDE
# 4. Create new python file on the project
import pandas as pd

def main():
    # 1. Variable & data type
    # grades = df['G3'] # list of numbers
    grades = [12, 10, 5, 6, 8, 11, 15, 17, 19, 4, 
              5, 20, 10, 11, 13, 3, 0, 8, 10, 12] # list of numbers
    
    # 2. Data structure (list & dictionary)
    bucket_grades = {
        '0-5': {
            'count': 0,
            'grades': []
        },
        '6-10': {
            'count': 0,
            'grades': []
        },
        '11-15': {
            'count': 0,
            'grades': []
        },
        '16-20': {
            'count': 0,
            'grades': []
        }
    }
    
    # 4. Looping
    for grade in grades:
        bucket = '0-5'
        
        # 3. Conditionals
        if 0 <= grade <= 5:
            bucket = '0-5'
        elif 6 <= grade <= 10:
            bucket = '6-10'
        elif 11 <= grade <= 15:
            bucket = '11-15'
        else:
            bucket = '16-20'
        
        bucket_grades[bucket]['count'] = bucket_grades[bucket]['count'] + 1
        bucket_grades[bucket]['grades'].append(grade)
    
    for key, value in bucket_grades.items():
        print(f"The number of final grades in range {key} is {value['count']}.")

if __name__ == '__main__':
    df = pd.read_csv('data/student-mat.csv', delimiter=';')
    main()