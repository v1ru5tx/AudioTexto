from TTS.api import TTS

def main():

    texto = """
    Hola !!! se podra clonar esta voz!?
    """


    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")
    tts.tts_to_file(
        text=texto,
        speaker_wav="resources/voz.wav",
        language="es",
        file_path="audio_clonado.wav",
        # --- Parámetros de mejora ---
        temperature=0.65,      # Valores bajos (0.6 - 0.7) hacen la voz más estable y monótona; valores altos la hacen errática.
        speed=1.0,             # Mantén la velocidad natural para evitar distorsiones.
        repetition_penalty=2.0 # Evita que la IA tartamudee o repita sílabas.
    )

    print("[i] Audio generado con éxito")

if __name__ == "__main__":
    main()