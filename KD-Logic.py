import os
import subprocess
import sys

try:
    import yt_dlp
except ImportError:
    print("Instalando motor de descarga... espera.")
    subprocess.call([sys.executable, "-m", "pip", "install", "-U", "yt-dlp[requests]"])
    import yt_dlp

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def logo():
    print(r"""
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
    """)

def mostrar_resoluciones_y_descargar(url):
    folder = "Descargas_KDLogic"
    if not os.path.exists(folder): os.makedirs(folder)
    ruta_actual = os.path.dirname(os.path.abspath(__file__))

    print("\n[🛡️] Forzando extracción de Clip... (Bypass de modo En Vivo)")
    
    ydl_opts_info = {
        'quiet': True, 
        'no_warnings': True,
        'noplaylist': True,          
        'cookies_from_browser': 'chrome', 
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    }

    with yt_dlp.YoutubeDL(ydl_opts_info) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
            formats = info.get('formats', [])
            
            video_formats = [f for f in formats if f.get('vcodec') != 'none']
            
            if not video_formats:
                print("❌ No se detectaron formatos de video en este clip.")
                return

            print(f"\n🎥 Clip: {info.get('title')[:60]}...")
            print(f"{'N°':<4} | {'Resolución':<12} | {'Ext':<6} | {'FPS':<5}")
            print("-" * 55)

            mapa_opciones = {}
            for i, f in enumerate(video_formats, 1):
                res = f"{f.get('width', '??')}x{f.get('height', '??')}"
                if res == "??x??": res = "Resolución Nativa"
                
                print(f"{i:<4} | {res:<12} | {f.get('ext'):<6} | {f.get('fps', '??'):<5}")
                mapa_opciones[str(i)] = f['format_id']

            print("-" * 55)
            seleccion = input("\n👉 Elige el NÚMERO (o 'C' para cancelar): ").strip()

            if seleccion in mapa_opciones:
                id_video = mapa_opciones[seleccion]
                
                ydl_opts_final = {
                    'format': f'{id_video}+bestaudio/best',
                    'outtmpl': f'{folder}/%(uploader)s_CLIP_%(title)s.%(ext)s',
                    'merge_output_format': 'mp4',
                    'cookies_from_browser': 'chrome',
                    'ffmpeg_location': ruta_actual, 
                    'postprocessor_args': [
                        '-c:v', 'libx264', '-preset', 'ultrafast',
                        '-pix_fmt', 'yuv420p', '-bsf:v', 'h264_mp4toannexb'
                    ],
                }
                
                print(f"\n[🚀] Descargando y Limpiando Clip...")
                with yt_dlp.YoutubeDL(ydl_opts_final) as ydl_final:
                    ydl_final.download([url])
                print(f"\n✅ ¡Clip guardado con éxito en '{folder}'!")
            else:
                print("\n⚠️ Opción no válida.")

        except Exception as e:
            print(f"\n⚠️ Reintentando con extractor genérico...")
            try:
                subprocess.call([sys.executable, "-m", "yt_dlp", "--cookies-from-browser", "chrome", "-o", f"{folder}/%(title)s.%(ext)s", url])
            except:
                print(f"\n❌ Error final: {e}")

def main():
    while True:
        limpiar_pantalla()
        logo()
        link = input("[🔗] Link de Kick/TikTok o 'salir': ").strip()
        if link.lower() == 'salir': break
        if not link: continue
        
        mostrar_resoluciones_y_descargar(link)
        input("\nPresiona ENTER para volver...")

if __name__ == "__main__":
    main()