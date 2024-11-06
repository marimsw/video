# Узнать переменную или постоянную частоту кадров которые соответсвуют VFR или CFR
import subprocess
import json

def chec_frame_rate_type(vido_file):
    command = [
        'ffprobe',
        '-v','error',
        '-select_streams', 'v:0',
        '-show_entries','stream=avg_frame_rate, r_frame_rate',
        '-of', 'json',
        video_file
    ]

    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text= True)

    if result.returncode != 0:
      print('Ошибка при выполнении: ', result.stderr)
      return None

    # Парсинг результата
    info = json.loads(result.stdout)

    if not info.get('streams'):
        print('Не найдено видео потоков.')
        return None

    stream_info =info['streams'][0]
    avg_frame_rate = stream_info.get('avg_frame_rate',' неизвесто')
    r_frame_rate = stream_info.get('r_frame_rate','Неизвестно')

    return avg_frame_rate, r_frame_rate

video_file = input('Введите путь к файлу: ')
frame_rate_info = chec_frame_rate_type(video_file)

if frame_rate_info is not None:
    # avg_frame_rate, r_frame_rate = frame_rate_info
    # print(f'Средняя частота кадров (avg_frame_rate): {avg_frame_rate}')
    # print(f'Частота кадров:{r_frame_rate}')

    # Проверка на VFR
    if avg_frame_rate != r_frame_rate:
        print('Видео имеет переменную частоту кадров(VFR).')
        print('Видео соответсвует требованиям')
    else:
        print('Видео имеет постоянною частоту кадров (CFR).')
        print('Видео не соответсвует требованиям')

else:
    print('Не удалось получить информацию о видеофайле.')
