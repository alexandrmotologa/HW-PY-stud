# Definirea dictionarului student cu valorile corespunzatoare
student = {
    'firstname': 'John',
    'lastname': 'Doe',
    'age': 20,
    'grade_1': 8.75,
    'grade_2': 9.25,
    'grade_3': 9.11
}

# Calcularea mediei notelor
grades = [value for key, value in student.items() if key.startswith("grade")]
grades_avg = sum(grades) / len(grades)

# Afisarea detaliilor studentului
for key, value in student.items():
    if key.startswith("grade"):
        key = key.replace("_", " ").capitalize()
        print(f"{key}: {value:.2f}")
    else:
        key = key.capitalize()
        print(f"{key}: {value}")

# Afisarea mediei notelor cu doua zecimale
print(f"Media notelor este: {grades_avg:.2f}")

# Verificarea daca studentul a trecut examenul si afisarea unui mesaj corespunzator
if grades_avg >= 5.00:
    status = "a trecut"
else:
    status = "nu a trecut"
print(f"Studentul \"{student['firstname']} {student['lastname']}\" {status} examenul.")
