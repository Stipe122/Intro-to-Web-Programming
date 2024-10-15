#!python.exe

import db

res = db.getSubjects()

subjects = {}
for row in res:
    subjects[str(row["kod"])] = {"name": str(row["ime"]),
                                 "year": row["godina"], "ects": row["bodovi"]}

year_names = {
    1: '1st Year',
    2: '2nd Year',
    3: '3rd Year'
}

year_ids = {
    '1st Year': 1,
    '2nd Year': 2,
    '3rd Year': 3
}

status_names = {
    'not': 'Not selected',
    'enr': 'Enrolled',
    'pass': 'Passed',
}

# create helper dictionary from session data:
# read radio input statuses chosen by user so far from session data,
# remaining radio inputs (not chosen so far) have the status: 'not' - Not selected


# def read_session_data(session_data):
#     dictionary = dict.fromkeys(subjects)
#     for subject_id in dictionary:
#         if subject_id not in session_data:
#             dictionary[subject_id] = 'not'
#         else:
#             dictionary[subject_id] = session_data[subject_id]
#     return dictionary

def addToUpisniList():
    for subject in subjects:
        print(subject)


def display_buttons():
    print('<div>')
    for key in year_ids:
        print('<input type="submit" name="button" value="' + key + '"/>')
    print('<input type="submit" name="button" value="Enrollment List"/>')
    print('</div>')


def fillList(userId):
    for row in res:
        db.fillUpisniList(userId, row["id"], "not")


# print subject with info and radio buttons


def print_subject(subject_id, id):
    # Get data from db using id of user

    print('''
    <tr>
        <td>''' + subjects[subject_id]['name'] + '''</td>
        <td>''' + str(subjects[subject_id]['ects']) + '''</td>
        <td>
    ''')
    # Check status of radio button from db for all with userId
    for status_key, status_value in status_names.items():
        print(status_value + '<input type="radio" name="' + subjects[subject_id]['name'] + '" value="' +
              status_key + '"' + check_status_radio(id, status_key, subject_id))
    print('''
        </td>
    </tr>
    ''')


# print all subjects of the chosen year of study

def print_subjects_year(currYear, id):
    print('''
    <table border="1">
        <tr>
            <td colspan="3">''' + currYear + '''</td>
        </tr>
        <tr>
            <td>Subject</td>
            <td>Ects</td>
            <td>Status</td>
        </tr>
    ''')
    for year_key, year_value in year_names.items():
        for subject_id, subject_value in subjects.items():
            if subject_value['year'] == year_key and year_value == currYear:
                print_subject(subject_id, id)
    print('</table>')


def check_status_radio(id, status_key, subject_id):
    # id - userId
    # status_key - not,enr,pass
    # subject_id - ip, ca itd
    # Return data from db if its else than not set that to checked
    # Based on userId
    userList = db.upisniListFromUserId(id)
    # print(userList)

    # Get subject id for given subject_id (ip - ip npr id je 1)
    idPredmeta = db.getSubjectIdFromListByName(subject_id)

    # AKo je subjectId koji je u subject id npr on je not i ako je u bazi not pod tim imenom predmeta stavi ga na checked
    # Get vrijednost predmeta iz upisnog lista za usera za id predmeta
    # SELECT * FROM upisni_list WHERE id_studenta = userList AND id_predmeta = idPredmeta
    res = db.getStatusByUserIdAndPredmetId(idPredmeta, id)
    if res == status_key:
        return ' checked/>'
    return '/>'

# print enrollment list - all subjects from all years, their statuses and calculate ects


def print_user_enrollment_list(userId):
    total_ects = 0

    print('''
    <table border="1">
        <tr>
            <td>Subject</td>
            <td>Status</td>
            <td>Ects</td>
        </tr>
    ''')

    # Get user list
    res = db.upisniListFromUserId(userId)
    # print(res)

    for row in res:
        # Ime predmeta - subjectNames[2]
        # Status - row[3]
        # Ects - subjectNames[3]

        # Get subjects
        subjectNames = db.getSubjectNameForListById(row[2])

        print('''
        <tr>
            <td>''' + str(subjectNames[2]) + '''</td>
            <td>''' + str(row[3]) + '''</td>
            <td>''' + str(subjectNames[3]) + '''</td>
        </tr>''')

        # Calculate total ects for all subjects from list
        if (row[3] == "pass"):
            ects = subjectNames[3]
            total_ects += ects

    print('''
    <tr>
        <td></td>
        <td>Total:</td>
        <td>''' + str(total_ects) + '''</td>
    </tr>''')
    print('</table>')


def print_enrollment_list(dictionary):
    total_ects = 0

    print('''
    <table border="1">
        <tr>
            <td>Subject</td>
            <td>Status</td>
            <td>Ects</td>
        </tr>
    ''')

    for subject_id in subjects:
        if dictionary[subject_id] == 'pass':
            total_ects += subjects[subject_id]['ects']

        print('''
        <tr>
            <td>''' + subjects[subject_id]['name'] + '''</td>
            <td>''' + status_names[dictionary[subject_id]] + '''</td>
            <td>''' + str(subjects[subject_id]['ects']) + '''</td>
        </tr>''')

    print('''
    <tr>
        <td></td>
        <td>Total:</td>
        <td>''' + str(total_ects) + '''</td>
    </tr>''')
    print('</table>')
