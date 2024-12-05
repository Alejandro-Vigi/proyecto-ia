# Diagnóstico de Depresión en Estudiantes

Bienvenido al proyecto **Diagnóstico de Depresión en Estudiantes**. Este proyecto tiene como objetivo proporcionar una prueba rápida para predecir la probabilidad de depresión en estudiantes, basada en diferentes factores como la presión académica, el estrés financiero, la calidad del sueño, entre otros.

El sistema utiliza un modelo de machine learning para realizar la predicción y mostrar los resultados al usuario a través de una interfaz amigable.

## 🚀 **Cómo Funciona**

1. **Formulario de Entrada:** El usuario debe llenar un formulario con información relevante sobre su situación académica, laboral y personal. Los campos incluyen:
    - Edad
    - Sexo
    - Presión académica
    - Promedio de calificaciones
    - Horas de estudio/trabajo al día
    - Satisfacción de estudios
    - Estrés financiero
    - Duración del sueño
    - Antecedentes familiares de enfermedades mentales
    - Pensamientos suicidas
    - Hábitos alimenticios
    - Si actualmente trabaja, se agrega un campo adicional de "Presión laboral"

2. **Procesamiento:** Una vez que el formulario es enviado, los datos se procesan y el modelo de machine learning realiza una predicción sobre la probabilidad de que el usuario esté pasando por una situación de depresión.

3. **Resultados:** Los resultados se presentan al usuario en una alerta tipo **SweetAlert2**, donde se informa si los síntomas pueden sugerir una posible depresión y se ofrecen recomendaciones para recibir ayuda si es necesario.

4. **Prueba en Línea:** Puedes probar el diagnóstico directamente en el siguiente enlace:
    - [Realiza tu prueba aquí](https://studentdepressionml.pythonanywhere.com/)

---

## 💻 **Dependencias**

Para ejecutar este proyecto localmente, necesitarás tener instaladas las siguientes dependencias:

### Requisitos

Este proyecto tiene las siguientes dependencias para que puedas ejecutarlo localmente:

- **Python** 3.x
- **Flask** (Para el servidor web)
- **Scikit-learn** (Para el modelo de machine learning)
- **Pandas** (Para manejar los datos)
- **NumPy** (Para procesamiento de datos)
- **Matplotlib** (Para visualización de la curva ROC)
- **Seaborn** (Para visualización de datos avanzados y gráficos personalizados)
- **Joblib** (Para cargar y guardar modelos entrenados)
- **SweetAlert2** (Para alertas emergentes personalizadas en el frontend)
- **Subprocess** (Para ejecutar scripts o comandos externos desde Python)

### Instalación

1. Clona este repositorio a tu máquina local:

    ```bash
    git clone https://github.com/tuusuario/diagnostico-depresion-estudiantes.git
    ```

2. Instala las dependencias necesarias con `pip`:

    ```bash
    pip install flask joblib pandas numpy matplotlib seaborn scikit-learn
    ```

5. Una vez instaladas las dependencias, puedes ejecutar la aplicación localmente:

    ```bash
    python app.py
    ```

6. Accede a la aplicación abriendo tu navegador y visitando:

    ```
    http://127.0.0.1:5000/
    ```

---

## 🌍 **Estructura del Proyecto**

Este proyecto está dividido en las siguientes carpetas y archivos:
```bash
/diagnostico-depresion-estudiantes
├── /static
│   ├── /css
│   │   ├── normalize.css      # Estilos base para normalizar el diseño entre navegadores
│   │   └── styles.css         # Estilos personalizados de la página
│   ├── /js
│   │   └── main.js            # Lógica JavaScript para el frontend (manejo de formularios y alertas)
├── /templates
│   └── index.html             # Página principal con el formulario
├── app.py                     # Código backend en Flask
├── requirements.txt           # Archivo de dependencias
└── README.md                  # Este archivo README
```

---

## 🧑‍💻 **Desarrollo**

1. **Frontend:** El frontend está construido con HTML, CSS y JavaScript.
   - El formulario está diseñado con HTML5 y estilizado con **CSS**.
   - Se utiliza **SweetAlert2** para mostrar mensajes emergentes personalizados con los resultados del diagnóstico.
   
2. **Backend:** El backend está basado en **Flask** (Python) para gestionar las solicitudes HTTP.
   - El formulario es procesado y los resultados son enviados a través de Flask a una página de resultados.
   - Se usa un modelo de **machine learning** entrenado previamente para predecir la probabilidad de depresión en función de los datos ingresados.

---

## 📈 **Prueba el Diagnóstico**

Si prefieres no configurar el proyecto localmente, puedes probar la aplicación directamente en línea utilizando el siguiente enlace:

- [Realiza tu prueba aquí](https://studentdepressionml.pythonanywhere.com/)

---

## 📝 **Contribuciones**

¡Las contribuciones son bienvenidas! Si tienes alguna idea para mejorar el proyecto, puedes hacer un **fork**, realizar tus cambios y abrir un **pull request**.

¡Gracias por usar este proyecto! Espero que sea útil para quienes necesiten realizar un diagnóstico sobre su salud mental. Si tienes alguna pregunta o sugerencia, no dudes en abrir un **issue** en el repositorio.


