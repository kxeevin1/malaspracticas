# Identificar malas prácticas en un proyecto antiguo
Kevin Jhoan Carreño Patiño 20242020308 - Daniel Felipe Santamaria Duran 20242020023

Errores de diseño

* La clase Parqueadero tiene demasiadas responsabilidades.
* Hay mucho acoplamiento entre lógica, interfaz y archivos.
* Falta separación por capas.
* Hay `int(input())` sin manejo de errores.
* El sistema sería difícil de escalar o mantener si creciera.

Reutilización

* Hay código repetido en validaciones.
* El patrón pedir-validar-repetir aparece muchas veces.
* La carga y guardado de datos repite lógica.
* Varias funciones podrían reutilizar auxiliares comunes.

Patrones que podrían aplicarse

* MVC para separar lógica, interfaz y datos.
* Repository o DAO para separar persistencia.
* Strategy para manejar tarifas según el tipo de vehículo.
* Factory para centralizar creación de vehículos.
* Command para organizar mejor el menú.

