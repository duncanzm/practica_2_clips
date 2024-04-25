# Define un diccionario para almacenar atributos del usuario, similar a los hechos en CLIPS
attributes = {}

def get_input(prompt):
    return input(prompt)

# Solicita el nombre
def get_name():
    attributes['name'] = get_input("What is your name? ")

# Solicita el género y valida que sea masculino o femenino
def get_gender():
    attributes['gender'] = get_input(f"{attributes['name']}, what is your gender? ").lower()
    while attributes['gender'] not in ['male', 'female']:
        print("Invalid gender. Please enter 'male' or 'female'.")
        attributes['gender'] = get_input(f"{attributes['name']}, what is your gender? ").lower()

# Solicita el colesterol total y valida que sea un número positivo
def get_total_cholesterol():
    attributes['total_cholesterol'] = float(get_input(f"{attributes['name']}, what is your total cholesterol? "))
    while attributes['total_cholesterol'] <= 0:
        print("Invalid value. Please enter a positive number.")
        attributes['total_cholesterol'] = float(get_input(f"{attributes['name']}, what is your total cholesterol? "))
        
# Solicita el HDL y valida que sea un número positivo
def get_hdl():
    attributes['HDL'] = float(get_input(f"{attributes['name']}, what is your HDL? "))
    while attributes['HDL'] <= 0:
        print("Invalid value. Please enter a positive number.")
        attributes['HDL'] = float(get_input(f"{attributes['name']}, what is your HDL? "))

# Calcula la relación entre el colesterol total y el HDL
def compute_ratio():
    attributes['ratio'] = attributes['total_cholesterol'] / attributes['HDL']

# Evalúa el riesgo de enfermedad cardíaca basado en el género y la relación calculada
def assess_risk():
    ratio = attributes['ratio']
    gender = attributes['gender']
    name = attributes['name']
    if (gender == 'male' and ratio < 3.5) or (gender == 'female' and ratio < 3.0):
        print(f"{name}, you have a low risk of heart disease.")
    elif (gender == 'male' and 3.5 <= ratio <= 5.0) or (gender == 'female' and 3.0 <= ratio <= 4.4):
        print(f"{name}, you have a moderate risk of heart disease.")
    elif (gender == 'male' and ratio > 5.0) or (gender == 'female' and ratio > 4.4):
        print(f"{name}, you have a high risk of heart disease.")

def main():
    get_name()
    get_gender()
    get_total_cholesterol()
    get_hdl()
    compute_ratio()
    assess_risk()

if __name__ == "__main__":
    main()
