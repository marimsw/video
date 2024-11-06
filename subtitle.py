# Нахождение субтитров в видео

import subprocess

def get_subtitle_streams(video_path):
    command=[
        'ffprobe',
        '-v', 'error',
        '-select_streams', 's',
        '-show_entries', 'stream=index,codec_name,language',
        '-of', 'csv=p=0',
        video_path
    ]

    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if result.returncode == 0:
      subtitles = result.stdout.strip()
      if subtitles:
        print('Найденные субтитры: ')
        print(subtitles)
      else:
        print("Субтитры не найдены.")
    else:
      print("Ошибка при выполнении команды: ", result.stderr)

# Путь к файлу
video_path = '/video/сцена 1.mp4'
get_subtitle_streams(video_path)
