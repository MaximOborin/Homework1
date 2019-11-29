wow = [1, 21, 19, 6, 5, 4, 6, 3, 7, 1]

for kaktak in wow:
    print(kaktak +1)

wow1 = 'Ужасные оценки'
for word in wow1:
    print(word)

students_score = [
    {'school_class': '4a', 'scores': [3,4,4,5,2]}, 
    {'school_class': '4b', 'scores': [3,5,5,5,3]},
    {'school_class': '1a', 'scores': [5,5,5,5,5]},
    {'school_class': '1b', 'scores': [2,1,3,5,2]},
    {'school_class': '2a', 'scores': [3,4,3,5,3]},
    {'school_class': '3a', 'scores': [5,4,2,5,3]},
    {'school_class': '2b', 'scores': [3,1,3,2,3]},
    {'school_class': '3b', 'scores': [5,4,3,5,5]},  
]

sum_school_score = 0
caunt_score = 0

for score in students_score:
    sum_school_score += sum(score["scores"]) 
    caunt_score += len(score["scores"]) 
    first_school = sum_school_score / caunt_score
print(f'Среднее бал по школе: {first_school}')

for what in students_score:
    all_score_per_class = sum(what['scores']) / len(what['scores'])
    number_class = what['school_class']
    print(f'Средний бал в каждом классе {number_class} : {all_score_per_class}')
    print("---")

    
    