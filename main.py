import os
import shutil
import time
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

class SortFiles:
    def __init__(self, folder_name) -> None:
        self.folder_name = folder_name
    
    def sorter(self):
        start_time = time.time()
        
        # Перевіряем чи є ця папка, чи треба створювати
        if not os.path.exists(self.folder_name):
            os.makedirs(self.folder_name)
            
        files = os.listdir(self.folder_name)
        
        for file_name in files:
            file_path = os.path.join(self.folder_name, file_name)  # Полный путь к файлу
            # Перевіряем, чи це обьєкт чи файл
            if os.path.isfile(file_path):
                _, ext = os.path.splitext(file_path)
                ext = ext[1:].lower()
                
                # Робимо папку для розширення
                if ext:
                    folder_path = os.path.join(self.folder_name, ext)
                else:
                    folder_path = os.path.join(self.folder_name, 'other')
                
                # Перевіряємо чи існує папка для данного росширення, якщо ні то - створюємо її
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                    
                shutil.move(file_path, folder_path)
        
        end_time = time.time()
        result_time = end_time - start_time
        print(f'Файли отсортовані, це зайняло {result_time} секунд.')

if __name__ == "__main__":
    sort_folder = 'folder'
    sorter = SortFiles(sort_folder)
    # ---------------стандартний запуск
    # sorter.sorter()
    
    # -------------- запуск просто потоками
    thread = Thread(target=sorter.sorter)
    thread.start()
    
    # ------------- запуск через Пул потоки
    # with ThreadPoolExecutor() as executor:
    #     executor.submit(sorter.sorter)
    