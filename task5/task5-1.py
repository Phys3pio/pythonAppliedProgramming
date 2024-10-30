import tkinter as tk
from PIL import Image, ImageTk
import cv2
import threading
import os
# appSettings.py
pl_video = 1  # По умолчанию работаем с видеофайлом
video_path = "1/vData/cats_video.mp4"  # Путь к тестовому видео


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Загружаем настройки из appSettings.py
        from appSettings import pl_video, video_path
        self.pl_video = pl_video
        self.video_path = video_path

        # Инициализация виджетов
        self.init_ui()

    def init_ui(self):
        # Настройки окна
        self.title("Анализ видео")
        self.geometry("800x600")

        # Кнопка запуска/паузы
        self.play_button = tk.Button(self, text="Запустить", command=self.play_pause)
        self.play_button.place(x=20, y=20)

        # Кнопка снимка
        self.photo_button = tk.Button(self, text="Снимок", command=self.take_photo)
        self.photo_button.place(x=120, y=20)

        # Checkbutton для выбора видеопотока
        self.stream_checkbutton = tk.Checkbutton(self, text="Видеопоток")
        self.stream_checkbutton.place(x=220, y=20)

        # Поле для отображения видео
        self.video_canvas = tk.Canvas(self, width=640, height=480)
        self.video_canvas.place(x=20, y=60)

        # Поле для отображения снимков
        self.photo_canvas = tk.Canvas(self, width=320, height=240)
        self.photo_canvas.place(x=680, y=60)

        # Кнопка сохранения снимка
        self.save_button = tk.Button(self, text="Сохранить", command=self.save_photo)
        self.save_button.place(x=700, y=300)

        # Кнопка настроек
        self.settings_button = tk.Button(self, text="Настройки", command=self.open_settings)
        self.settings_button.place(x=20, y=550)

    def play_pause(self):
        if not hasattr(self, 'video_player'):
            # Создаем объект VideoPlayer
            self.video_player = VideoPlayer(pl_video=self.pl_video, video_path=self.video_path, master=self, width=640,
                                            height=480)
            self.video_player.place(relx=0.05, rely=0.15)

            # Меняем текст кнопки
            self.play_button.config(text="Пауза")
        elif self.video_player.pause:
            # Возобновляем воспроизведение
            self.video_player.pause = False
            self.video_player.update()
            self.play_button.config(text="Пауза")
        else:
            # Останавливаем воспроизведение
            self.video_player.pause = True
            self.play_button.config(text="Продолжить")

    def take_photo(self):
        if self.stream_checkbutton.var.get():
            # Запускаем метод find_in_stream в отдельном потоке
            self.cycleResult = threading.Event()
            self.lock = threading.Lock()
            thread = threading.Thread(target=self.find_in_stream, args=(self.cycleResult, self.lock,))
            thread.start()
        else:
            # Делаем снимок и отображаем его на photo_canvas
            pass

    def find_in_stream(self, cycle_result, lock):
        while not cycle_result.is_set():
            with lock:
                # Обрабатываем поток видео и сохраняем снимки
                pass

    def save_photo(self):
        # Сохраняем текущий снимок в отдельную папку
        pass

    def open_settings(self):
        # Открываем окно настроек
        settings = Settings(self)
        settings.grab_set()  # Блокируем основное окно до закрытия окна настроек


class Settings(tk.Toplevel):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Загружаем настройки из appSettings.py
        from appSettings import pl_video, video_path
        self.pl_video = pl_video
        self.video_path = video_path

        # Инициализация виджетов
        self.init_ui()

    def init_ui(self):
        # Настройки окна
        self.title("Настройки")
        self.geometry("400x200")

        # Поле ввода пути к видео
        self.video_path_entry = tk.Entry(self, width=50)
        self.video_path_entry.insert(0, self.video_path)
        self.video_path_entry.pack(pady=10)

        # Кнопка обновления пути
        self.update_button = tk.Button(self, text="Обновить", command=self.update_path)
        self.update_button.pack(pady=10)

    def update_path(self):
        # Обновляем путь к видео в appSettings.py
        new_path = self.video_path_entry.get()
        with open('appSettings.py', 'w') as f:
            f.write(f'pl_video = {self.pl_video}\n')
            f.write(f'video_path = "{new_path}"\n')

        # Обновляем переменную video_path в классе MainWindow
        self.master.video_path = new_path


class VideoPlayer:
    def __init__(self, pl_video, video_path, master, width, height):
        self.pl_video = pl_video
        self.video_path = video_path
        self.master = master
        self.width = width
        self.height = height

        # Объект VideoCapture
        if self.pl_video == 1:
            self.stream = cv2.VideoCapture(self.video_path)
        else:
            self.stream = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        # Canvas для отображения видео
        self.canvas = tk.Canvas(master, width=self.width, height=self.height)

        # Флаг паузы
        self.pause = False

    def place(self, relx, rely):
        self.canvas.place(relx=relx, rely=rely)
        self.update()

    def update(self):
        if self.stream.isOpened():
            ret, frame = self.stream.read()
            if ret:
                # Конвертация кадра в формат, подходящий для отображения в tkinter
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = Image.fromarray(frame)
                frame = ImageTk.PhotoImage(frame)

                # Отображение кадра на canvas
                self.canvas.create_image(0, 0, image=frame, anchor='nw')
                self.master.after(30, self.update)
            else:
                self.stream.release()
        else:
            print("Ошибка открытия видеопотока")

    def place_forget(self):
        self.canvas.place_forget()
        self.pause_video()
        self.stream.release()

    def pause_video(self):
        self.pause = True
def main():
    root = MainWindow()
    root.mainloop()

if __name__ == "__main__":
    main()