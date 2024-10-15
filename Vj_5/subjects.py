#!python.exe

import db

res = db.getSubjects()

subjects = {}
for row in res:
    subjects[str(row["kod"])] = {"name": str(row["ime"]),
                                 "year": row["godina"], "ects": row["bodovi"]}

# subjects = {
#     'ip': {'name': 'Introduction to programming', 'year': 1, 'ects': 6},
#     'c1': {'name': 'Calculus 1', 'year': 1, 'ects': 7},
#     'cu': {'name': 'Computer usage', 'year': 1, 'ects': 5},
#     'dmt': {'name': 'Digital and microprocessor technology', 'year': 1, 'ects': 6},
#     'db': {'name': 'Databases', 'year': 2, 'ects': 6},
#     'c2': {'name': 'Calculus 2', 'year': 2, 'ects': 7},
#     'dsa': {'name': 'Data structures and alghoritms', 'year': 2, 'ects': 5},
#     'ca': {'name': 'Computer architecture', 'year': 2, 'ects': 6},
#     'isd': {'name': 'Information systems design', 'year': 3, 'ects': 5},
#     'c3': {'name': 'Calculus 3', 'year': 3, 'ects': 7},
#     'sa': {'name': 'Server Architecture', 'year': 3, 'ects': 6},
#     'cds': {'name': 'Computer and data security', 'year': 3, 'ects': 6}
# }

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


def read_session_data(session_data):
    dictionary = dict.fromkeys(subjects)
    for subject_id in dictionary:
        if subject_id not in session_data:
            dictionary[subject_id] = 'not'
        else:
            dictionary[subject_id] = session_data[subject_id]
    return dictionary


def display_buttons():
    print('<div>')
    for key in year_ids:
        print('<input type="submit" name="button" value="' + key + '"/>')
    print('<input type="submit" name="button" value="Enrollment List"/>')
    print('</div>')


def check_status_radio(subject_id, dictionary, status_key):
    if dictionary[subject_id] == status_key:
        return ' checked/>'
    return '/>'

# print subject with info and radio buttons


def print_subject(subject_id, dictionary):
    print('''
    <tr>
        <td>''' + subjects[subject_id]['name'] + '''</td>
        <td>''' + str(subjects[subject_id]['ects']) + '''</td>
        <td>
    ''')
    for status_key, status_value in status_names.items():
        print(status_value + '<input type="radio" name="' + subject_id + '" value="' +
              status_key + '"' + check_status_radio(subject_id, dictionary, status_key))
    print('''
        </td>
    </tr>
    ''')


# print all subjects of the chosen year of study


def print_subjects_year(currYear, dictionary):
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
                print_subject(subject_id, dictionary)
    print('</table>')


# print enrollment list - all subjects from all years, their statuses and calculate ects


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
