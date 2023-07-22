employee_dictionary = {
    "Employee 1": { "name": "Joey", "title": "QA Engineer", "hireDate": "2020-09-01"},
    "Employee 2": { "name": "Scott", "title": "Software Engineer I", "hireDate": "2021-01-04"},
    "Employee 3": { "name": "Kara", "title": "CTO", "hireDate": "2019-11-01"},
    "Employee 4": { "name": "Sara", "title": "Sales Representative", "hireDate": "2017-03-14"}
}

# print the name & title of Employee 3
employee_3 = employee_dictionary["Employee 3"]
employee_name = employee_3["name"]
employee_title = employee_3["title"]

print(f"Name: {employee_name}")
print(f"Title: {employee_title}")