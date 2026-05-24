# SonarQube
<img width="1562" height="884" alt="image" src="https://github.com/user-attachments/assets/74c8e957-1c40-4e91-bedc-cd3e97dd660c" />
SonarQube no identificó ningun problema en nuestro proyecto de parqueadero, salió con:
 
 
 0.0% Duplicación de código
 0 errores encontrados
 100% hospots revisados y aprobados

 
Lo único es que nos dió una advertencia sobre que teniamos las 3 versiones de python y sería más preciso cambiándolo.
<img width="1673" height="863" alt="image" src="https://github.com/user-attachments/assets/6eff2e7a-23fd-40e2-9777-18e26c9d5716" />



# Identificar malas prácticas en un proyecto antiguo
Kevin Jhoan Carreño Patiño 20242020308 - Daniel Felipe Santamaria Duran 20242020023

El proyecto era un parqueadero que se realizó para la materia de programación básica, es de daniel con otro compañero.

Errores de diseño

* La clase Parqueadero tiene demasiadas responsabilidades, puede ser el antipatron godclass o blob
* Hay mucho acoplamiento entre lógica, interfaz y archivos
* Falta separación por capas
* Hay mucho int(input()) sin manejo de errores
* El sistema sería difícil de escalar o mantener si creciera

Reutilización

* Hay código repetido en validaciones, puede ser el antipatron de copy-paste programming
* El patrón pedir-validar-repetir aparece muchas veces
* La carga y guardado de datos repite lógica
* Varias funciones podrían reutilizar auxiliares comunes

Patrones que podrían aplicarse

* MVC para separar lógica, interfaz y datos
* Repository o DAO para separar persistencia
* Strategy para manejar tarifas según el tipo de vehículo
* Factory para centralizar creación de vehículos
* Command para organizar mejor el menú

15 Antipatrones conocidos
1) God Class: Una clase hace demasiadas cosas y concentra gran parte del sistema.
2) Spaghetti Code: Código desordenado y difícil de seguir por tantas dependencias y conexiones.
3) Copy-Paste Programming: Repetir bloques de código en vez de reutilizar funciones o módulos.
4) Magic Numbers: Usar números “quemados” en el código sin explicación ni constantes.
5) Hardcoding: Valores escritos directamente en el código en vez de configurarse dinámicamente.
6) Tight Coupling: Componentes demasiado dependientes entre sí.
7) Lava Flow: Código viejo o innecesario que nadie elimina por miedo a romper algo.
8) Golden Hammer: Usar siempre la misma solución o tecnología aunque no sea la mejor opción.
9) Shotgun Surgery: Un cambio pequeño obliga a modificar muchas partes del sistema.
10) Boat Anchor: Código o funcionalidades innecesarias que solo hacen más pesado el proyecto.
11) Reinventing the Wheel: Crear algo desde cero cuando ya existe una solución mejor o estándar.
12) Blob: Una clase crece demasiado y absorbe responsabilidades de otras.
13) Poltergeist: Clases muy pequeñas o inútiles que casi no aportan comportamiento.
14) Premature Optimization: Optimizar cosas demasiado temprano sin necesidad real.
15) Vendor Lock-In: Diseñar el sistema dependiendo demasiado de una tecnología o plataforma específica.
