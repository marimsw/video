# видеокодек полный
import subprocess
import json

def get_video_codec(video_file):
    # Команда для получения методанных в видео
    command = [
        'ffprobe',
        '-v', 'error',
        '-select_streams', 'v:0',
        '-show_entries', 'stream= codec_long_name',
        '-of', 'json',
        video_file
    ]

    # Выполнение команды и получение результата
    result =  subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text= True)

    if result.returncode != 0:
      print(' Ошибка при получении метаданных', result.stderr)
      return None

    # Парсинг JSON-ответа
    metadata = json.loads(result.stdout)
    return metadata

video_file = input("Введите путь к видеофайлу: ")
metadata = get_video_codec(video_file)

if metadata:
    if 'streams' in metadata and len(metadata['streams'])> 0:
      stream = metadata['streams'][0]
      codec_name= stream.get('codec_long_name')
      print(f'Кодек видео: {codec_name}')
