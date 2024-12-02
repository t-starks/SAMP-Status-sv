# SAMP Status sv

Este script es una herramienta para consultar información de un servidor **SAMP (San Andreas Multiplayer)**. Permite obtener el nombre del servidor, número de jugadores conectados, lista de jugadores, y reglas configuradas en el servidor.

## Requisitos

Para usar este script, necesitas:

1. **Python 3** instalado en tu sistema o en Termux. Puedes instalarlo en Termux con:
   ```bash
   pkg install python
   ```

2. **Módulos necesarios**: Instala las dependencias ejecutando:
   ```bash
   pip install trio samp-query
   ```

3. **IP y Puerto del Servidor**: Asegúrate de tener la dirección IP y el puerto del servidor SAMP que deseas consultar.

## Instalación

1. **Clona este repositorio** en tu dispositivo:
   ```bash
   git clone https://github.com/t-starks/SAMP-Status-sv.git
   ```

2. **Navega al directorio** donde se encuentra el script:
   ```bash
   cd SAMP-Status-sv
   ```

3. **Ejecuta el script**:
   ```bash
   python main.py
   ```

## Uso

1. Al ejecutar el script, se te pedirá ingresar la dirección IP y el puerto del servidor SAMP en este formato:
   ```
   123.456.789:7777
   ```

2. El script mostrará información sobre:
   - Nombre del servidor
   - Número de jugadores conectados
   - Lista de jugadores conectados y sus puntajes
   - Reglas configuradas en el servidor

## Ejemplo de Salida
```
Servidor: My SAMP Server
Jugadores: 10/100

Lista de jugadores conectados:
- Player1 (Score: 200)
- Player2 (Score: 150)

Reglas del servidor:
- version: 0.3.7-R2
- lagcomp: On
- mapname: Los Santos Roleplay
```

## Notas

- **Errores comunes**: 
  - Asegúrate de ingresar la IP y puerto en el formato correcto (`IP:PUERTO`).
  - Verifica que el servidor SAMP esté activo y accesible.

- Si no se muestran jugadores, puede que no haya jugadores conectados en ese momento.

## Contribuciones

Si tienes ideas para mejorar este script, por favor crea un _pull request_ o abre un _issue_ en este repositorio.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

¿Te gustaría agregar algún detalle más, como enlaces o ejemplos adicionales? 🚀
