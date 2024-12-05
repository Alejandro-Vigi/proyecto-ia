document.addEventListener("DOMContentLoaded", function () {
    // Código para manejar la selección de si trabaja o no
    document.getElementById('works').addEventListener('change', function() {
        var workPressureDiv = document.getElementById('work_pressure_div'); // Div del campo de "Presión Laboral"
        var workPressureInput = document.getElementsByName('work_pressure')[0]; // Input del campo de "Presión Laboral"
        
        if (this.value === 'No') {
            // Si selecciona "No", ocultamos el campo de "Presión Laboral" y ponemos el valor a 0
            workPressureDiv.style.display = 'none'; // Ocultamos el campo
            workPressureInput.value = 0; // Ponemos el valor del input en 0
            workPressureInput.setAttribute('placeholder', 'Presión Laboral: 0'); // Mostramos el placeholder con valor 0
        } else if (this.value === 'Yes') {
            // Si selecciona "Sí", mostramos el campo de "Presión Laboral" y le damos el placeholder adecuado
            workPressureDiv.style.display = 'block'; // Mostramos el campo
            workPressureInput.setAttribute('placeholder', '1-10 (1: poca, 10: demasiada)'); // Placeholder para el rango de presión laboral
            workPressureInput.value = ''; // Dejamos el campo vacío para que el usuario lo complete
        }
    });
    
    // Código para manejar el flashMessage con SweetAlert
    if (flashMessage.length > 0) {
        var mensaje = flashMessage[0];  // Mensaje de la alerta
        var tipo = flashMessage[1];     // Tipo de alerta ('warning' o 'info')
    
        // Mostrar el SweetAlert con el loading (sin botón de confirmación por ahora)
        Swal.fire({
            title: 'Procesando...', // Título de la alerta
            text: 'Estamos calculando los resultados...', // Texto de la alerta
            allowOutsideClick: false,  // Bloquea la interacción con la página
            didOpen: () => {
                // Mostrar el spinner (SweetAlert tiene soporte integrado)
                Swal.showLoading();
            }
        });
    
        // Simular un tiempo de procesamiento (puedes cambiar este tiempo)
        setTimeout(function() {
            // Mostrar el mensaje final con el icono y color adecuado
            Swal.fire({
                title: 'Resultado de la prueba',  // Título de la alerta
                text: mensaje,  // Mensaje de la alerta
                icon: tipo,  // Determina el tipo de icono ('warning' o 'info')
                confirmButtonText: 'Aceptar',  // Texto del botón de confirmación
                confirmButtonColor: '#4a9dec', // Color del botón
                width: 800,  // Ancho de la ventana
                heightAuto: true,  // La ventana se ajusta automáticamente a su contenido
                padding: '3em',  // Aumenta el padding dentro del popup
                backdrop: true,  // Agrega un fondo detrás del popup
                showCloseButton: true,  // Muestra un botón de cierre
                iconColor: tipo === 'warning' ? 'red' : '#3085d6',  // El color del icono depende del tipo de alerta
                customClass: {
                    popup: 'custom-popup',  // Aplica una clase personalizada al popup
                    title: 'custom-title',  // Clase para el título
                    content: 'custom-content',  // Clase para el contenido del mensaje
                    icon: 'custom-icon',  // Clase para el ícono
                    confirmButton: 'custom-confirm-button',  // Clase para el botón de confirmar
                    cancelButton: 'custom-confirm-button cancelButton' // Clase personalizada para el botón de "Obtener ayuda"
                },
                timer: 0,  // Nunca se cierra automáticamente
                showCancelButton: tipo === 'warning',  // Si es 'warning', muestra el botón de "Obtener Ayuda"
                cancelButtonText: 'Obtener ayuda',  // Texto del botón de ayuda
                cancelButtonColor: '#FF7F00',  // Color naranja para el botón de ayuda
            }).then((result) => {
                if (result.isDismissed) {
                    // Si el usuario hace clic en "Obtener ayuda"
                    Swal.fire({
                        title: 'Recibe ayuda en la Facultad de Psicología', // Título del mensaje de ayuda
                        text: 'Si estás pasando por una situación difícil, puedes recibir ayuda en la Facultad de Psicología en CU. Más información en: https://misalud.unam.mx/',
                        icon: 'success', // Icono de éxito
                        confirmButtonText: 'Cerrar', // Texto del botón
                        confirmButtonColor: '#4a9dec', // Color del botón
                        width: 800,  // Ancho de la ventana
                        heightAuto: true,  // Ajuste automático del alto
                        padding: '3em',  // Padding aumentado
                        backdrop: true,  // Fondo detrás del popup
                        showCloseButton: true,  // Botón de cierre visible
                        customClass: {
                            popup: 'custom-popup', // Clase personalizada para el popup
                            title: 'custom-title', // Clase para el título
                            content: 'custom-content', // Clase para el contenido
                            icon: 'custom-icon', // Clase para el ícono
                            confirmButton: 'custom-confirm-button', // Usamos la misma clase aquí para el botón
                        },
                    });
                }
            });
        }, 2000);  // Este es el tiempo que se muestra el loading (en milisegundos)
    }
});