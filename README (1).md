**Pruebas Automatizadas Urban Routes**
Descripción del proyecto:

Este proyecto implementa una serie de pruebas automatizadas para Urban Routes, una aplicación web de solicitud de taxis. 
El objetivo es validar el flujo completo de pedido de un viaje, desde la configuración de la ruta hasta la aparición del
modal de búsqueda de conductor, cubriendo todas las funcionalidades intermedias que un usuario real completaría durante 
ese proceso.

Las pruebas cubren los siguientes escenarios del flujo de pedido:

1.Configuración de la dirección de origen y destino.
2.Selección de la tarifa Comfort entre las opciones disponibles.
3.Registro del número de teléfono del pasajero.
4.Agregado de una tarjeta de crédito, incluyendo la verificación mediante código de confirmación por SMS.
5.Escritura de un mensaje para el conductor.
6.Solicitud de manta y pañuelos (verificación del estado del switch/slider).
7.Solicitud de helados (incremento del contador a 2 unidades).
8.Verificación de la aparición del modal de búsqueda de taxi al finalizar el pedido.

Cada prueba valida de forma independiente que la interacción del usuario con la interfaz produce el resultado esperado 
en el DOM (estado de elementos, valores de campos, visibilidad de modales, etc.).

Tecnologías y técnicas utilizadas:
1.Python como lenguaje de programación principal.
2.Selenium WebDriver para la automatización e interacción con el navegador.
3.Pytest como framework de ejecución y organización de pruebas.
4.Patrón Page Object Model (POM): toda la lógica de localización de elementos e interacción con la página se encapsula 
en la clase UrbanRoutesPage. Las pruebas en TestUrbanRoutes solo orquestan llamadas a estos métodos y realizan las 
aserciones.