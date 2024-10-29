# Глубина цвета

import subprocess

def get_video_color_depth(video_path):
  # Запускаем ffprobe для получения информации о видео
    command = [
        'ffprobe',
        '-v', 'error',
        '-select_streams', 'v:0',
        '-show_entries', 'stream=bits_per_raw_sample',
        '-of', 'default=noprint_wrappers=1:nokey=1',
        video_path
    ]

    result = subprocess.run(command, stdout= subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if result.returncode == 0:
        depth = result.stdout.strip()
        if depth:
          print(f'Глубина цвета: {depth} бит')
        else:
          print('Не удалось определить глубину цвета.')
    else:
      print('Ошибка при выполнении команды:', result.stderr)

# Укажите путь к вашему видеофайлу
video_path = '/video/2024557.mp4'
get_video_color_depth(video_path)
