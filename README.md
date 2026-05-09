# Identificar malas prácticas en un proyecto antiguo
Kevin Jhoan Carreño Patiño 20242020308 - Daniel Felipe Santamaria Duran 20242020023

# Problemas de diseño

## Clase `Parqueadero`

* Tiene demasiadas responsabilidades.
* Hay alto acoplamiento.
* Falta separación de responsabilidades.

## Métodos `registrar_entrada()` y `registrar_salida()`

* Mezclan lógica con interfaz.
* Dependencia directa de consola (`input` y `print`).

## `main()`

* Mucha lógica centralizada.
* Menú muy acoplado al sistema.

---

# Problemas de reutilización

## Validaciones

* Código repetido.
* Baja reutilización.

## Manejo de fechas

* Lógica repetitiva.
* Validaciones reutilizables no abstraídas.

## Guardado y carga de datos

* Repetición de parseo.
* Repetición de construcción de objetos.

## Comparaciones de matrículas

* Normalización repetida (`upper()` varias veces).

---

# Problemas de estructura

## Listas `vehiculos` e `historial_vehiculos`

* Uso excesivo de estado mutable.
* Modificación directa de estructuras internas.

## Búsquedas

* Complejidad lineal innecesaria.
* Poco escalable.

## Historial

* Modelo de historial limitado.
* Persistencia poco robusta.

## Archivo `.txt`

* Persistencia frágil.
* Dependencia de formato manual.

---

# Problemas de programación orientada a objetos

## Clase `Vehiculo`

* Se usa más como contenedor de datos.

## Clase `Usuario`

* Poco comportamiento encapsulado.

## Encapsulamiento

* Bajo encapsulamiento general.
* Acceso directo a atributos.

---

# Patrones que podrían aplicarse

## MVC

* Falta separación entre:

  * modelo,
  * vista,
  * controlador.

## Repository / DAO

* Persistencia mezclada con lógica.

## Strategy

* Tarifas dependientes del tipo de vehículo.

## Factory

* Creación de objetos centralizable.

## Command

* Menú dependiente de muchos `if/elif`.

---

# Otros errores o malas prácticas

## Manejo de errores

* `int(input())` sin validaciones completas.

## Acoplamiento

* Muchas funciones dependen entre sí.

## Escalabilidad

* Diseño poco mantenible a largo plazo.

## Persistencia

* Vehículos actuales no se restauran correctamente.

## Dependencia de consola

* Sistema difícil de reutilizar fuera de terminal.
