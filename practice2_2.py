students = [
    {   
        "name": "Sally Jones",
        "homeroom_name": "HH-123",
        "grade": 2
    },
    {
        "name": "Chris Smith",
        "homeroom_name": "HH-124",
        "grade": 3
    },
    {
        "name": "Sarah Thompson",
        "homeroom_name": "HH-125",
        "grade": 6
    }
]
inputted_homeroom_name = input("Type in a student homeroom name: ")
for index in range(0, len(students)):
    if students[index]["homeroom_name"] == inputted_homeroom_name:
        print(f"{students[index]['name']} (index {index}) has homeroom name {inputted_homeroom_name}")
    else:
        print(f"{students[index]['name']} (index {index}) doesn't have the homeroom name {inputted_homeroom_name}")