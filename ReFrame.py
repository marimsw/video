import subprocess
import os

def get_reframe_count(video_file):
    command = [
        'ffprobe',
        '-v', 'error',
        '-select_streams', 'v:0',
        '-show_entries', 'stream=refs',
        '-of', 'default=noprint_wrappers=1:nokey=1',
        video_file
    ]

    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode != 0:
            print('Ошибка при выполнении:', result.stderr)
            return None

        return result.stdout.strip() or "Информация о ReFrame недоступна."

    except Exception as e:
        print(f'Произошла ошибка: {e}')
        return None

def main():
    video_file = input("Введите путь к видеофайлу: ").strip()

    if not video_file:
        print("Путь к видеофайлу не может быть пустым.")
        return

    if not os.path.isfile(video_file):
        print("Указанный файл не существует. Пожалуйста, проверьте путь.")
        return

    reframe_count = get_reframe_count(video_file)

    if reframe_count is not None:
        print(f'Количество ReFrame в видеофайле: {reframe_count}')
    else:
        print('Не удалось получить информацию о ReFrame.')

if __name__ == "__main__":
    main()
