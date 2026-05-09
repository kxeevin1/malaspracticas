# Identificar malas prácticas en un proyecto antiguo
Kevin Jhoan Carreño Patiño 20242020308 - Daniel Felipe Santamaria Duran 20242020023

Errores de diseño

* La clase `Parqueadero` tiene demasiadas responsabilidades.
* Hay mucho acoplamiento entre lógica, interfaz y archivos.
* `registrar_entrada()` y `registrar_salida()` mezclan lógica con consola usando `input()` y `print()`.
* `main()` tiene demasiada lógica centralizada.
* Falta separación por capas.
* El sistema depende mucho del estado interno de la clase.
* El historial de vehículos está muy simple y poco modelado.
* Las búsquedas recorren listas completas todo el tiempo.
* El manejo de archivos está demasiado unido a la lógica principal.
* El `.txt` funciona como una base de datos improvisada.
* La persistencia es frágil porque depende totalmente del formato manual del archivo.
* La programación orientada a objetos está usada más como contenedor de datos.
* Hay poco encapsulamiento.

Reutilización

* Hay código repetido en las validaciones.
* El patrón de pedir-validar-repetir aparece muchas veces.
* Hay repetición en carga y guardado de datos.
* El parseo del archivo se hace manualmente varias veces.
* La comparación de matrículas usando `upper()` se repite demasiado.
* Varias validaciones podrían reutilizar funciones auxiliares.
* Hay lógica repetitiva en el manejo de fechas.
* Hay poca modularidad en general.

Errores o malas prácticas

* Hay `int(input())` sin manejo de errores.
* El programa puede romperse si el usuario escribe letras.
* Las listas internas se modifican directamente.
* Hay dependencia excesiva de consola.
* El código sería difícil de escalar.
* Muchas partes dependen entre sí.
* Los vehículos estacionados no se restauran correctamente al reiniciar.
* El código sería difícil de mantener si el proyecto creciera.

Patrones que podrían aplicarse

* MVC para separar modelo, vista y lógica.
* Repository o DAO para separar persistencia.
* Strategy para el cálculo de tarifas.
* Factory para centralizar la creación de vehículos.
* Command para organizar el menú y evitar tantos `if/elif`.
