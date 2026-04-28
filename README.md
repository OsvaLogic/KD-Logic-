# KD-Logic Video Downloader (V8.6)

```text
========================================================================================
 :::    ::: :::::::::          :::        ::::::::   ::::::::   :::::::::::  :::::::: 
 :+:   :+:  :+:    :+:         :+:       :+:    :+: :+:    :+:      :+:     :+:    :+: 
 +:+  +:+   +:+    +:+         +:+       +:+    +:+ +:+            +:+     +:+        
 +#++:++    +#+    +:+         +#+       +#+    +#+ :#:            +#+     +#+        
 +#+  +#+   +#+    +:+         +#+       +#+    +#+ +#+    +#+      +#+     +#+        
 #+#   #+#  #+#    #+#         #+#       #+#    #+# #+#    #+#      #+#     #+#    #+# 
 ###    ### #########          ##########  ########   ########   ###########  ######## 
========================================================================================
                      KD-LOGIC V8.6 | KICK CLIP FIX | OSVA.LOGIC
```

KD-Logic es una herramienta por consola desarrollada en Python diseñada para forzar la extracción y descarga de clips de plataformas como Kick y TikTok, haciendo bypass al modo "En Vivo" y permitiendo elegir la resolución deseada.

## 📋 Requisitos Previos

Para que el script funcione correctamente, necesitas tener instalado lo siguiente:

1. **Python 3.7 o superior**: Asegúrate de marcar la opción "Add Python to PATH" durante la instalación.
2. **Google Chrome**: El script extrae las cookies de tu navegador Chrome local para evitar bloqueos y restricciones de edad o región.
3. **FFmpeg y FFprobe**: Necesarios para procesar, unir el video y el audio de alta calidad, y para la conversión de formatos. 
   - Debes descargar **`ffmpeg.exe`** y **`ffprobe.exe`** y colocarlos **exactamente en la misma carpeta** que el archivo `KD-Logic.py` (la carpeta principal de tu descargador).

## 🚀 Instalación

1. Abre una terminal (Símbolo del sistema o PowerShell).
2. Navega hasta la carpeta del proyecto:
   ```bash
   cd ruta\a\tu\carpeta\Video
   ```
3. Instala las dependencias necesarias ejecutando:
   ```bash
   pip install -r requirements.txt
   ```
   *(Nota: El script cuenta con un auto-instalador que intentará instalar `yt-dlp` automáticamente si lo ejecutas y no lo tienes instalado).*

## ⚙️ Uso

1. Ejecuta el script desde la consola o haciendo doble clic sobre el archivo si tienes configurado Python:
   ```bash
   python KD-Logic.py
   ```
2. Pega el enlace del clip de Kick o TikTok cuando el programa te lo solicite.
3. El programa detectará las resoluciones disponibles. Escribe el número correspondiente a la resolución que deseas y presiona Enter.
4. El clip se procesará y se guardará automáticamente en una subcarpeta llamada `Descargas_KDLogic` dentro de este mismo directorio.

## ⚠️ Notas de Solución de Problemas

- **Error de FFmpeg no encontrado**: Asegúrate de que `ffmpeg.exe` esté en la misma carpeta que `KD-Logic.py`.
- **Descarga rechazada o "Not Live"**: El script tiene un método alternativo por si el clip está rebelde, pero asegúrate de que el enlace sea válido y que tu navegador Chrome tenga la sesión iniciada en la plataforma si el clip es privado.
- Para salir de la aplicación, simplemente escribe `salir` cuando te pida el enlace.