# pip install ffmpeg-python

import ffmpeg
import json

def get_video_info(input_file):
    """
    Получает информацию о видеофайле.

    :param input_file: Путь к входному видеофайлу.
    :return: Словарь с информацией о видео.
    """
    try:
        # Получаем информацию о видео с помощью ffprobe
        probe = ffmpeg.probe(input_file)
        return probe
    except ffmpeg.Error as e:
        print(f"Ошибка при получении информации о видео: {e}")
        return None

def print_video_info(video_info):
    """
    Печатает информацию о видео.

    :param video_info: Словарь с информацией о видео.
    """
    if video_info:

        streams_info = video_info.get('streams', [])

        for stream in streams_info:
            if stream['codec_type'] == 'video':
                print("\nПараметры видео:")
                print(f"Кодек: {stream.get('codec_name')}")
                print(f"Разрешение: {stream.get('width')}x{stream.get('height')}")
                
                # Получаем битрейт и преобразуем его в мегабиты
                bit_rate = stream.get('bit_rate')
                if bit_rate:
                    bit_rate_mbps = int(bit_rate) / 1000000  # Преобразуем в Мбит
                    print(f"Битрейт: {bit_rate_mbps:.2f} Мбит/с")
                else:
                    print("Битрейт: Неизвестен")


# Пример использования
input_video = '/video/2024557.mp4'
video_info = get_video_info(input_video)
print_video_info(video_info)
