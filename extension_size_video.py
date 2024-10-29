# Выводит расширение видео

import cv2
import os

video_path = '/video/1995584.mp4'

max_size = 10 # MБ

file_size_mb = os.path.getsize(video_path)
file_size_mb = file_size_bytes / (1024*1024) # Перевод МБ

if file_size_mb > max_size:
  print('Ошибка: Размер видео привышает 10 МБ')
else:
  cap =cv2.VideoCapture(video_path)

  if not cap.isOpened():
      print('Ошибка: Не удалось открыть выдео.')
  else:
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Проверка и вывод расширения
    if (width, height) == (1920, 1080):
      print('Расширение видео 1920х1080 px')
    elif (width, height) == (1080, 1920):
      print('Расширение видео 1080х1920 px')
    else:
      print(f'Разрешение видео : {width}x{height} px')

    # Вывод размера в МБ
    print(f'Размер видео: {file_size_mb:.2f} МБ')

  cap.release()
