# Audio Transcription with Vosk

Este projeto realiza a transcrição de arquivos de áudio utilizando a biblioteca [Vosk](https://alphacephei.com/vosk/). Ele suporta conversão automática de formatos populares de áudio para WAV, com taxa de amostragem de 16kHz, para garantir compatibilidade com o modelo de reconhecimento.

## Funcionalidades

- **Conversão de áudio**: Converte arquivos de áudio em diferentes formatos (MP3, OGG, FLAC, etc.) para WAV com taxa de amostragem de 16kHz e áudio mono.
- **Transcrição de áudio**: Utiliza o modelo Vosk para transcrever o áudio processado.
- **Processamento automático**: Detecta o formato do arquivo de entrada e executa as etapas necessárias para transcrição.

## Pré-requisitos

Certifique-se de ter as seguintes dependências instaladas:

- **Python 3.8 ou superior**
- **FFmpeg**: Para conversão de formatos de áudio.
- **Bibliotecas Python**:
  - `vosk`
  - `wave`
  - `os`
  - `json`
  - `subprocess`

Para instalar as bibliotecas necessárias, execute:

```bash
pip install vosk pydub
```

## Como usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/audio-transcription.git
   cd audio-transcription
   ```

2. Baixe o modelo Vosk para português do Brasil:
   - [vosk-model-small-pt-0.3](https://alphacephei.com/vosk/models)
   - Extraia o conteúdo na pasta do projeto.

3. Execute o script:

   ```bash
   python transcribe.py
   ```

4. Insira o caminho para o arquivo de áudio quando solicitado. O script fará a conversão (se necessário) e exibirá a transcrição na tela.

## Exemplo

```bash
Digite o caminho para o arquivo de áudio: exemplo.mp3
Processando o áudio: exemplo.mp3
Áudio convertido para: exemplo_convertido.wav
Transcrevendo o áudio com Vosk...

Transcrição:
"Esta é uma transcrição de teste feita usando o Vosk."
```

## Limitações

- O modelo padrão suporta apenas português do Brasil. Certifique-se de usar um modelo apropriado para o idioma do áudio.
- Apenas arquivos de áudio são suportados.

## Contribuição

Sinta-se à vontade para enviar pull requests ou abrir issues para melhorias.


## Referências

- [Vosk Speech Recognition](https://alphacephei.com/vosk/)
- [FFmpeg Documentation](https://ffmpeg.org/documentation.html)
``` 

Você pode ajustar conforme o necessário para refletir detalhes específicos do seu projeto.