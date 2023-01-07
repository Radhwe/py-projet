departments = {
    'department_1': {
        'classes': ['class_1', 'class_2', 'class_3'],
        'students': {
            'class_1': ['student_1', 'student_2', 'student_3'],
            'class_2': ['student_4', 'student_5', 'student_6'],
            'class_3': ['student_7', 'student_8', 'student_9']
        }
    },
    'department_2': {
        'classes': ['class_4', 'class_5', 'class_6'],
        'students': {
            'class_4': ['student_10', 'student_11', 'student_12'],
            'class_5': ['student_13', 'student_14', 'student_15'],
            'class_6': ['student_16', 'student_17', 'student_18']
        }
    },
}

import json

# Encode les informations sur les départements en format JSON
department_data = json.dumps(departments)

# Écrivez les données dans un fichier JSON
with open('departments.json', 'w') as f:
    f.write(department_data)

import json

# Lit les données depuis le fichier JSON
with open('departments.json', 'r') as f:
    department_data = f.read()

# Décode les données JSON en un dictionnaire Python
departments = json.loads(department_data)



# Affiche la liste des départements
print(list(departments.keys()))


# Demande à l'utilisateur de choisir un département
department = input('Choisissez un département : ')

# Affiche la liste des classes pour le département choisi
if department in departments:
    print(f'Classes in {department}: {departments[department]["classes"]}')
else:
    print(f'Le département {department} n\'existe pas.')

    # Demande à l'utilisateur de choisir une classe
class_name = input('Choisissez une classe : ')
    # Vérifie si le département et la classe choisis existent
if department in departments and class_name in departments[department]['classes']:
    # Affiche la liste des étudiants pour la classe choisie
    print(f'Étudiants in {class_name}: {departments[department]["students"][class_name]}')
else:
    print(f'Le département {department} ou la classe {class_name} n\'existe pas.')