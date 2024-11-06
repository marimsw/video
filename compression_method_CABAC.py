# Метод сжатия CABAC или CAVLC
import subprocess
import json

def get_video_codec_info(video_file):
    # Команда для получения метаданных видео
    command = [
        'ffprobe',
        '-v', 'error',
        '-select_streams', 'v:0',
        '-show_entries', 'stream=codec_name,profile',
        '-of', 'json',
        video_file
    ]

    # Выполнение команды и получение результата
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if result.returncode != 0:
        print("Ошибка при получении метаданных:", result.stderr)
        return None

    if not result.stdout:
        print("Пустой ответ от ffprobe")
        return None

    # Парсинг JSON-ответа
    try:
        metadata = json.loads(result.stdout)
    except json.JSONDecodeError:
        print("Ошибка при парсинге JSON")
        return None

    return metadata

def determine_compression_method(metadata):
    if 'streams' in metadata and len(metadata['streams']) > 0:
        stream = metadata['streams'][0]
        codec_name = stream.get('codec_name')
        profile = stream.get('profile')

        if codec_name and profile:
            if codec_name == 'h264':
                if 'Main' in profile or 'High' in profile or 'High 10' in profile:
                    return "Используется CABAC"
                elif 'Baseline' in profile:
                    return "Используется CAVLC"
            else:
                return f"Неизвестный кодек: {codec_name}"
        else:
            return "Неизвестный стандарт: не найдены codec_name или profile"

    return "Неизвестный стандарт"

# Пример использования
video_file = input('введите путь к video файлу: ')  # Укажите путь к вашему видеофайлу
metadata = get_video_codec_info(video_file)

if metadata:
    method = determine_compression_method(metadata)
    print("Метод сжатия:", method)
