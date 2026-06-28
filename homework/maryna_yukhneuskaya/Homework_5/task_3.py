# Option 1 - not perfect 
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

last_name_1, last_name_2, last_name_3 = students
subject_1, subject_2, subject_3 = subjects

message = f'Students {last_name_1}, {last_name_2}, {last_name_3} stydy these subjects: {subject_1}, {subject_2}, {subject_3}'
print(message)

# Option 2

print(f'Students {", ".join(students)} study these subjects: {", ".join(subjects)}')