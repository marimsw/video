# FPS
import cv2

video_path= '2024557.mp4'

# Открываем файл
cap =cv2.VideoCapture(video_path)

# Проверяем удалось открыть файл

if not cap.isOpened():
  print('Ошибка: Не удалось открыть видео')
else:
  # Получаем частоту кадров
  fpd= int(cap.get(cv2.CAP_PROP_FPS))
  print(f"Частота кадров: {fpd} FPS")

# Освобождаем ресурсы
cap.release()
