# Identificar malas prácticas en un proyecto antiguo
Kevin Jhoan Carreño Patiño 20242020308 - Daniel Felipe Santamaria Duran 20242020023

# Problemas de diseño

## Clase `Parqueadero` con demasiadas responsabilidades

* La clase maneja lógica del programa, validaciones, interfaz de consola y archivos.
* Todo queda muy acoplado y difícil de mantener.
* Si se cambia algo del menú o del sistema de guardado, probablemente afecta varias partes.

## Mezcla entre lógica e interfaz

* Métodos como `registrar_entrada()` o `registrar_salida()` usan `input()` y `print()`.
* Eso hace difícil reutilizar la lógica en otro entorno como una app web o gráfica.
* La lógica debería estar separada de la interacción con el usuario.

## Falta de separación por capas

* Todo está junto en un solo flujo.
* No hay separación clara entre:

  * datos,
  * lógica,
  * interfaz,
  * persistencia.

---

# Problemas de reutilización

## Código repetido en validaciones

* Muchas validaciones siguen el mismo patrón:

  * pedir dato,
  * validar,
  * mostrar error,
  * volver a pedir.
* Eso podría centralizarse en funciones reutilizables.

## Repetición en carga y guardado de datos

* El parseo del archivo y la creación de objetos se hace manualmente varias veces.
* Si cambia el formato del archivo, habría que modificar muchas partes.

## Poca reutilización de funciones auxiliares

* Hay varias operaciones similares que podrían reutilizar funciones comunes.
* Por ejemplo:

  * validaciones,
  * búsquedas,
  * manejo de matrículas,
  * formateo de datos.

---

# Problemas de estructura

## Uso excesivo de listas mutables

* `vehiculos` e `historial_vehiculos` se modifican directamente desde muchos lugares.
* No hay mucho control sobre esos cambios.

## Búsquedas poco eficientes

* Cada búsqueda recorre listas completas.
* Si el sistema creciera, eso sería lento.

## Historial mal modelado

* El historial guarda copias simples de objetos.
* No guarda información más completa como:

  * salidas,
  * pagos,
  * tiempos históricos,
  * facturas.

## Manejo simple de archivos

* El `.txt` funciona como base de datos improvisada.
* Si el archivo se daña o cambia el formato, el programa podría fallar.

---

# Problemas de programación orientada a objetos

## Objetos usados más como estructuras de datos

* Algunas clases solo almacenan información.
* No tienen responsabilidades muy claras ni mucho encapsulamiento.

## Dependencia fuerte del estado interno

* Muchas funciones dependen directamente de variables globales de la clase.
* Eso hace el sistema más difícil de probar o modificar.

---

# Posibles patrones de diseño que podrían aplicarse

## MVC o separación por capas

Se podría separar el proyecto en:

* Modelo:

  * `Vehiculo`
  * `Usuario`

* Vista:

  * menú,
  * mensajes por consola.

* Controlador o lógica:

  * operaciones del parqueadero.

## Repository o DAO

* Serviría para separar el manejo de archivos de la lógica principal.
* Así `Parqueadero` no tendría que guardar ni cargar archivos directamente.

## Strategy

* El cálculo de tarifas cambia dependiendo del tipo de vehículo.
* Se podría usar una estrategia distinta para carros y motos.

## Factory

* La creación de vehículos podría centralizarse.
* Ayudaría a manejar validaciones y construcción de objetos en un solo lugar.

## Command

* El menú podría manejar cada opción como una acción separada.
* Evitaría tener muchos `if/elif` seguidos.

---

# Otros problemas encontrados

## Falta manejo de errores

* Hay varios `int(input())` sin validación.
* Si el usuario escribe letras, el programa puede romperse.

## Código muy acoplado

* Muchas partes dependen entre sí.
* Eso dificulta hacer cambios sin afectar otras funciones.

## Escalabilidad limitada

* El programa funciona para consola y proyectos pequeños.
* Pero si creciera, sería difícil mantenerlo y agregar nuevas funciones.
