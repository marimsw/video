import subprocess
import json

def get_video(file_path):
  command = [
      'ffprobe',
      '-v', 'error',
      '-select_streams', 'v:0',
      '-show_entries', 'stream=width,height,r_frame_rate',
      '-of', 'json',
      file_path
  ]

  result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

  if result.returncode != 0:
      print('Ошибка при выполнении ffprobe:', result.stderr)
      return None
  return json.loads(result.stdout)
def determine_tv_standart(video_info):
    #width = video_info['streams'][0]['width']
    width = video_info['streams'][0]['width']    
    height = video_info['streams'][0]['height']
    frame_rate = eval(video_info['streams'][0]['r_frame_rate'])

    # Проверка на PAL
    if (width == 1920 and height == 1080 and frame_rate == 25) or (width == 1080 and height == 1920) :
      return 'PAL'
    # Если не PAL, а другой стандарт 
    return 'Другой стандарт'

if __name__ == '__main__':
  video_file = '/content/video/1995584.mp4'
  video_info = get_video(video_file)
  tv_standard= determine_tv_standart(video_info)
  print(f' Телевизионный стандарт : {tv_standard}')
