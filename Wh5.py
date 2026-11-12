class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

def is_admin(func):
    def wrapper(user, *args, **kwargs):
        if user.role == "admin":
            return func(user, *args, **kwargs)
        else:
            print("У вас нет доступа")
    return wrapper

@is_admin
def delete_video(user):
    print("Видео удалено")

admin = User("Ardager", "admin")
user = User("Bek", "user")

delete_video(admin)
delete_video(user)


import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        execution_time = round(end_time - start_time, 1)
        print(f"Время выполнения: {execution_time} секунд")
        return result

    return wrapper

@timer
def download_video():
    time.sleep(2)
    print("Видео загружено")

download_video()
