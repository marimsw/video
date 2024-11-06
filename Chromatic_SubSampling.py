import subprocess

def get_chromatic_subsaming(video_file):

    command=[
        'ffprobe',
        '-v', 'error',
        '-select_streams', 'v:0',
        '-show_entries', 'stream=pix_fmt',
        '-of', 'default=noprint_wrappers=1:nokey=1',
        video_file
    ]

    result = subprocess.run(command, stdout= subprocess.PIPE, stderr= subprocess.PIPE,text= True)

    if result.returncode != 0:
      print('Ошибка при выполнении: ', result.stderr)
      return None

    return result.stdout.strip()

def convertе_pix_fmt(pix_fmt):
    # Словарь для преобразования форматов пикселей в хроматическое субдискретизирование
    subsamiling_dict ={
        'yuv420p': '4:2:0',
        'yuv422p': '4:2:2',
        'yuv444p': '4:4:4',
        'yuv410p': '4:1:0',
        'yuv411p': '4:1:1',
        'yuv440p': '4:4:0',

        'yuvj420p': '4:2:0 (JPEG)',
        'yuvj422p': '4:2:2 (JPEG)',
        'yuvj444p': '4:4:4 (JPEG)',
        'yuvj411p': '4:1:1 (JPEG)',
        'yuvj410p': '4:1:0 (JPEG)',
        'yuv420p10le': '4:2:0 10-bit',
        'yuv422p10le': '4:2:2 10-bit',
        'yuv444p10le': '4:4:4 10-bit',
        'yuv420p12le': '4:2:0 12-bit',
        'yuv422p12le': '4:2:2 12-bit',
        'yuv444p12le': '4:4:4 12-bit',
    }
    return subsamiling_dict.get(pix_fmt, 'Неизвестный формат')



video_file= input('Введи путь к видеофайлу: ')
pix_fmt= get_chromatic_subsaming(video_file)
if pix_fmt:
  samiling= convertе_pix_fmt(pix_fmt)
  print(f'Chromatic SubSampling: {samiling}')
  if samiling == '4:2:0':
    print('Этот формат соответствует стандартам видео 4:2:0')

  else:
    print('Этот формат не соответствует стандартам видео 4:2:0 ')
else:
    print('Не удалось найти информацию о Chromatic SubSampling') 
