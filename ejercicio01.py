# Aquí tenemos un diccionario de una persona.
persona = {
 'first_name': 'Roy',
 'last_name': 'Torre',
 'age': 19,
 'country': 'Peru',
 'is_married': True, #
 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
 'address': {
 'street': 'Space street',
 'zipcode': '02210'
 }
}

# a 

if 'skills' in persona:
    skills_list = persona['skills']
    if len(skills_list) > 1:
        middle_skill_index = len(skills_list) // 2
        middle_skill = skills_list[middle_skill_index]
        print(f"Habilidad del medio: {middle_skill}")
    else:
        print("La persona tiene solo una habilidad en la lista.")
else:
    print("La clave 'skills' no está presente en el diccionario de la persona.")

# b 

if 'skills' in persona:
    if 'Python' in persona['skills']:
        print("La persona tiene la habilidad 'Python'.")
    else:
        print("La persona no tiene la habilidad 'Python'.")
else:
    print("La clave 'skills' no está presente en el diccionario de la persona.")

# c

if 'skills' in persona:
    skills_list = persona['skills']
    if skills_list == ['JavaScript', 'React']:
        print("Él es un desarrollador frontend.")
    elif all(skill in skills_list for skill in ['Node', 'Python', 'MongoDB']):
        print("Él es un desarrollador backend.")
    elif all(skill in skills_list for skill in ['React', 'Node', 'MongoDB']):
        print("Él es un desarrollador fullstack.")
    else:
        print("Título desconocido.")
else:
    print("La clave 'skills' no está presente en el diccionario de la persona.")