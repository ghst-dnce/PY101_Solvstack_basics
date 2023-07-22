from pprint import pprint
employee_dictionary = {
    "Employee 1": { "name": "Joey", "title": "QA Engineer", "hireDate": "2020-09-01"},
    "Employee 2": { "name": "Scott", "title": "Software Engineer I", "hireDate": "2021-01-04"},
    "Employee 3": { "name": "Kara", "title": "CTO", "hireDate": "2019-11-01"},
    "Employee 4": { "name": "Sara", "title": "Sales Representative", "hireDate": "2017-03-14"}
}

# add a new employee to the above dictionary named Bob, with the title of UI 
# designer and a hire date of 2011-04-10
employee_dictionary["Employee 5"] = {"name": "Bob", "title": "UI designer", "hire date": "2011-04-10"}
pprint(employee_dictionary)