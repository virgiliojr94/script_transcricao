from vosk import Model, KaldiRecognizer
import wave
import os
import json
from pydub import AudioSegment
import subprocess

def converter_para_wav(input_audio):
    output_audio = f"{input_audio}_convertido.wav"
    
    comando_ffmpeg = [
        "ffmpeg", "-i", input_audio, "-ar", "16000", "-ac", "1", "-f", "wav", output_audio
    ]
    
    try:
        subprocess.run(comando_ffmpeg, check=True)
        print(f"Áudio convertido para: {output_audio}")
        return output_audio
    except subprocess.CalledProcessError as e:
        print(f"Erro ao converter o áudio: {e}")
        return None

def transcribe_audio_with_vosk(file_path):
    """
    Transcreve um arquivo de áudio usando a biblioteca Vosk.
    """
    # Carregando o modelo
    print("Carregando o modelo Vosk...")
    model_path = "vosk-model-small-pt-0.3"  # Certifique-se de baixar o modelo para PT-BR: https://alphacephei.com/vosk/models
    if not os.path.exists(model_path):
        raise FileNotFoundError("Modelo Vosk não encontrado. Faça o download em https://alphacephei.com/vosk/models")

    model = Model(model_path)

    # Abrindo o arquivo WAV
    print(f"Abrindo o arquivo de áudio: {file_path}")
    wf = wave.open(file_path, "rb")

    # Garantir que o arquivo é mono
    if wf.getnchannels() != 1:
        raise ValueError("O áudio precisa ser mono. Verifique o processo de conversão.")
    
    recognizer = KaldiRecognizer(model, wf.getframerate())
    recognizer.SetWords(True)

    print("Transcrevendo o áudio com Vosk...")
    transcription = ""
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            transcription += result.get("text", "") + " "

    return transcription.strip()


if __name__ == "__main__":
    audio_file = input("Digite o caminho para o arquivo de áudio: ")
    
    try:
        # Verificar se o arquivo já é WAV, caso contrário, converter
        if not audio_file.lower().endswith(".wav"):
            audio_file = converter_para_wav(audio_file)
        
        # Transcrever o áudio
        transcription = transcribe_audio_with_vosk(audio_file)
        print("\nTranscrição:")
        print(transcription)
    except Exception as e:
        print(f"Erro ao processar o áudio: {e}")
