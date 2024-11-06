# Профиль уровня кодека

import subprocess
import json

def get_video_profile_level(video_file):
    command = [
        'ffprobe',
        '-v', 'error',
        '-select_streams', 'v:0',
        '-show_entries', 'stream=profile,level',
        '-of', 'json',
        video_file
    ]

    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if result.returncode != 0:
        print("Ошибка при получении метаданных:", result.stderr)
        return None

    metadata = json.loads(result.stdout)
    return metadata

def convert_level(level):
    if level is not None:
        return f"{level // 10}.{level % 10}"
    return None

# Пример использования
video_file = '/content/drive/MyDrive/Rabota/С андреем от 21_10_2024_макеты/video/Ютуб плати за субтитры миллионы также субтитры).mp4'  # Укажите путь к вашему видеофайлу
metadata = get_video_profile_level(video_file)

if metadata:
    if 'streams' in metadata and len(metadata['streams']) > 0:
        stream = metadata['streams'][0]
        profile = stream.get('profile')
        level = stream.get('level')
        converted_level = convert_level(level)
        print(f"Профиль кодека: {profile}, Уровень кодека: {converted_level}")
        if profile =='Main' and converted_level == '4.2':
          print('Профиль и уровень кодека соответствуют требованиям.')
        else:
          print('Профиль и уровень кодека не соответствуют требованиям.')
    else:
        print("Потоки не найдены.")
else:
    print("Не удалось получить метаданные.")
