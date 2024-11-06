# Вся доступная информация о видео
import subprocess

def get_video_info(video_file):
    command = [
        'ffprobe',
        '-v', 'error',
        '-show_format',
        '-show_streams',
        video_file
    ]

    result = subprocess.run(command, stdout=subprocess.PIPE, stderr= subprocess.PIPE, text =True)

    if result.returncode !=0:
      print('Ошибка при выполнении: ', result.stderr)
      return None

    return result.stdout.strip()

video_file = input('Введите путь к видеофайлу: ')
video_info = get_video_info(video_file)

if video_info is not None:
  print('Информация о видеофайле :')
  print(video_info)
else:
  print('Не удалось получить информацию о видеофайле ')
