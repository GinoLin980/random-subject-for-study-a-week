import random

# define hyperparameters (which are defined by us)
DAILY_COURSES = 2
MAXIMUM_OCCURRENCES = DAILY_COURSES * 1.5
MINIMUM_OCCURRENCES = 0
DUPLICATES_ALLOWED = False

subjects = ["國文", "數學", "英文", "地理", "歷史", "公民"] # add subjects if needed
week =["週日", "週一", "週二", "週三", "週四", "週五", "週六"]

# make a list of the curriculum of one day.
def make_daily_curriculum() -> list:
    # pick random subject from subjects
    curriculum = random.choices(subjects, k=DAILY_COURSES) if DUPLICATES_ALLOWED else random.sample(subjects, DAILY_COURSES)
    # run the function again if we don't allow duplicates
    # and there are duplicates in the list
    if DUPLICATES_ALLOWED == False and len(set(curriculum)) != len(curriculum):
        return make_daily_curriculum()

    return curriculum

# make a curriculum of a whole week
def make_weekly_curriculum() -> list:
    count = {}
    weekly_curriculum = []
    # make a curriculum of a whole week
    for day in range(len(week)):
        weekly_curriculum.append(make_daily_curriculum())
        
    # count occurrences of every subject
    for subject in subjects:
        count[subject] = sum(item.count(subject) for item in weekly_curriculum)
        
    # run the function again if any subject reach max/min number of occurrence
    for subject in count:
        if count[subject] > MAXIMUM_OCCURRENCES or count[subject] == MINIMUM_OCCURRENCES:
            return make_weekly_curriculum()
        
    return weekly_curriculum, count

def make_table() -> None:
    weekly_curriculum, count = make_weekly_curriculum()
    print(" ".join(week), '\n')
    for index in range(DAILY_COURSES):
        print(" ".join([sublist[index] for sublist in weekly_curriculum]))
        
    print("\n各科數量與佔比")
    for item in count:
        print(f"{item}： {count[item]} | 百分比：{(count[item]/(DAILY_COURSES*7)*100):.2f}%")



make_table()