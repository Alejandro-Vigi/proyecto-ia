from flask import Flask, request, render_template, flash, redirect  # Asegúrate de incluir render_template
import joblib  # Se utiliza para cargar el modelo preentrenado.
import os  # Proporciona funciones para interactuar con el sistema de archivos.
import pandas as pd  # Biblioteca para manejar y manipular datos tabulares como DataFrames.
import subprocess  # Nos permite ejecutar scripts o comandos externos desde Python.

# Crear la aplicación Flask
app = Flask(__name__)   # Inicializa la aplicación Flask.

# Se Establece una clave secreta
app.secret_key = 'prueba'

# Función para verificar y cargar el modelo
def cargar_modelo():
    modelo_path = 'proyecto_curso.pkl'  # Ruta donde se almacena el modelo serializado.
    if not os.path.exists(modelo_path):  # Verifica si el archivo del modelo existe.
        print("Modelo no encontrado. Entrenando modelo...")  # Mensaje en caso de que no encuentra el modelo (Manejo de excepciones).
        subprocess.run(["python", "proyecto_curso.py"], check=True)  # Ejecuta el script externo para entrenar el modelo.
    return joblib.load(modelo_path)  # Carga el modelo.

# Cargar el modelo
model = cargar_modelo()  # Se llama a la función para cargar el modelo al iniciar la aplicación.

# Ruta para mostrar el formulario
@app.route('/')
# Se define el formulario HTML para la entrada de datos.
def formulario():
    return render_template('index.html')  # Usa el archivo index.html de la carpeta templates

# Ruta para manejar la predicción
@app.route('/predecir', methods=['POST'])
def predecir():
    # Obtener datos del formulario
    age = int(request.form['age'])    # Obtiene la edad ingresada en el formulario.
    gender = request.form['gender']  # Obtiene el género seleccionado (internamente solo Gender_Male = 1 si es hombre, en caso de ser mujer es = 0)
    academic_pressure = float(request.form['academic_pressure']) # Obtiene la presión académica (valor numérico).
    cgpa = float(request.form['cgpa'])     # Obtiene el promedio acumulado de calificaciones.
    study_hours = float(request.form['study_hours'])    # Obtiene las horas de estudio/trabajo.
    study_satisfaction = float(request.form['study_satisfaction'])  # Obtiene la satisfacción en los estudios.
    financial_stress = float(request.form['financial_stress'])      # Obtiene el nivel de estrés financiero.
    family_history = request.form['family_history']  # Obtiene la selección de antecedentes familiares.
    suicidal_thoughts = request.form['suicidal_thoughts']  # Obtiene la selección sobre pensamientos suicidas.
    sleep_duration = request.form['sleep_duration']  # Obtiene la selección de duración del sueño.
    dietary_habits = request.form['dietary_habits']  # Obtiene la selección de hábitos alimenticios.
    works = request.form['works']   # Obtiene la selección sobre si trabaja.
    work_pressure = float(request.form['work_pressure']) if works == "Yes" else 0   # Obtiene la presión laboral en caso de que haya seleccionado que trabaja.

    # Crear un DataFrame vacío con las columnas del modelo
    columnas_modelo = model.feature_names_in_   # Obtiene las columnas que espera el modelo.
    nuevo_estudiante = pd.DataFrame(columns=columnas_modelo)    # Crea un DataFrame con esas columnas.
    nuevo_estudiante.loc[0] = 0  # Inicializamos todas las columnas con el valor de 0.

    # Llenar las columnas correspondientes
    nuevo_estudiante.loc[0, 'Age'] = age    # Asigna la edad al DataFrame.
    nuevo_estudiante.loc[0, 'Gender_Male'] = 1 if gender == "Male" else 0   # Asigna 1 si es hombre, 0 si es mujer.
    nuevo_estudiante.loc[0, 'Academic Pressure'] = academic_pressure    # Asigna la presión académica.
    nuevo_estudiante.loc[0, 'CGPA'] = cgpa    # Asigna el promedio acumulado.
    nuevo_estudiante.loc[0, 'Work/Study Hours'] = study_hours   # Asigna las horas de trabajo/estudio.
    nuevo_estudiante.loc[0, 'Study Satisfaction'] = study_satisfaction  # Asigna la satisfacción de estudios.
    nuevo_estudiante.loc[0, 'Financial Stress'] = financial_stress      # Asigna el estrés financiero.
    nuevo_estudiante.loc[0, 'Family History of Mental Illness_Yes'] = 1 if family_history == "Yes" else 0   # Asigna 1 si hay antecedentes familiares.
    nuevo_estudiante.loc[0, 'Have you ever had suicidal thoughts ?_Yes'] = 1 if suicidal_thoughts == "Yes" else 0   # Asigna 1 si hay pensamientos suicidas.

    # Manejo de las opciones de sueño
    sleep_duration_columns = ['Sleep Duration_7-8 hours', 'Sleep Duration_Less than 5 hours', 'Sleep Duration_More than 8 hours']
    for col in sleep_duration_columns:
        if col.endswith(sleep_duration):    # Marca la columna correspondiente a la duración del sueño.
            nuevo_estudiante.loc[0, col] = 1

    # Manejo de hábitos alimenticios
    dietary_habits_columns = ['Dietary Habits_Others', 'Dietary Habits_Moderate', 'Dietary Habits_Unhealthy']
    for col in dietary_habits_columns:
        if col.endswith(dietary_habits):    # Marca la columna correspondiente a los hábitos alimenticios.
            nuevo_estudiante.loc[0, col] = 1

    # Manejo de la presión laboral
    nuevo_estudiante.loc[0, 'Work Pressure'] = work_pressure    # Asigna la presión laboral en caso que se haya seleccionado que trabaja.

    # Profesión (suponemos estudiantes)
    nuevo_estudiante.loc[0, 'Profession_Student'] = 1   # Marca que el estudiante pertenece a la profesión "Student".

    # Verificar que no haya columnas adicionales
    extra_cols = [col for col in nuevo_estudiante.columns if col not in columnas_modelo]    # Identifica columnas extra.
    if extra_cols:      # Si hay columnas adicionales se eliminan como en el modelo.
        nuevo_estudiante.drop(columns=extra_cols, inplace=True)

    # Verificar que todas las columnas necesarias están presentes
    for col in columnas_modelo:     # Asegura que todas las columnas requeridas estén presentes.
        if col not in nuevo_estudiante.columns:
            nuevo_estudiante[col] = 0

    # Realizar predicción
    prediccion = model.predict(nuevo_estudiante)    # Realiza la predicción.
    probabilidad = model.predict_proba(nuevo_estudiante)[0][1]      # Calcula la probabilidad de riesgo.

    # Determinar el mensaje basado en la predicción
    if prediccion[0] == 1:
        mensaje = f'Alto riesgo de depresión (Probabilidad: {probabilidad:.2f})'
        tipo = 'warning'  # Cambié de 'error' a 'warning' para un color más adecuado
    else:
        mensaje = f'Bajo riesgo de depresión (Probabilidad: {probabilidad:.2f})'
        tipo = 'info'  # Para bajo riesgo, usamos 'info'
    
    # Usamos flash para enviar solo los mensajes como cadenas
    flash(mensaje)
    flash(tipo)
    
    # Redirigir de nuevo a la página de inicio
    return redirect('/')

# Ejecutar la aplicación
if __name__ == '__main__':  # Verifica si el script se está ejecutando directamente.
    app.run(debug=True)     # Ejecuta la app Flask en modo debug para desarrollo.