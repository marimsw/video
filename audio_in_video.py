# Проверка звуковой дорожки

from moviepy.editor import VideoFileClip

def check_audio_in_video(video_path):
  # Загрузка видео
  video = VideoFileClip(video_path)

  # Проверка звуковой дорожки
  if video.audio is not None:
    print('В видео есть звуковая дорожка')
  else:
    print('В видео нет звуковой дорожки')

# Путь до видеофайла
video_path ='/video/2024557.mp4'
check_audio_in_video(video_path)
