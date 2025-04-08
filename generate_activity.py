import os
import subprocess
import datetime
import random

def generate_fake_commits(repo_path, weeks=8):
    """
    Генерирует фиктивные коммиты для указанного репозитория.

    Args:
        repo_path (str): Путь к локальному репозиторию Git.
        weeks (int): Количество недель назад, за которые нужно генерировать коммиты.
    """

    if not os.path.exists(repo_path):
        print(f"Ошибка: Репозиторий не найден по пути: {repo_path}")
        return

    os.chdir(repo_path) # Переходим в директорию репозитория

    today = datetime.date.today()

    for week in range(weeks):
        # Выбираем случайное количество дней для коммитов в эту неделю (3-4 дня)
        num_days = random.randint(3, 4)
        days_this_week = random.sample(range(7), num_days) # Выбираем случайные дни недели

        for day_offset in days_this_week:
            date = today - datetime.timedelta(weeks=week, days=day_offset)
            num_commits = random.randint(2, 4)

            for i in range(num_commits):
                # Создаем фиктивный файл (если его еще нет)
                filepath = "dummy_file.txt"  # Можно изменить имя файла

                if not os.path.exists(filepath):
                    with open(filepath, "w") as f:
                        f.write("Initial dummy content.\n")

                    run_git_command(["git", "add", filepath])

                # Добавляем изменение в фиктивный файл
                with open(filepath, "a") as f:
                    f.write(f"Fake commit {date} - {i}\n")

                # Формируем дату и время для коммита
                date_str = date.strftime("%Y-%m-%d")
                time_str = f"{random.randint(0, 23):02}:{random.randint(0, 59):02}:{random.randint(0, 59):02}"
                commit_date = f"{date_str} {time_str}"

                # Создаем коммит с указанной датой
                run_git_command(["git", "add", "."])
                run_git_command(["git", "commit", "-m", f"Fake commit on {date_str} {time_str}",
                                 "--date", commit_date])

    print("Фиктивные коммиты сгенерированы.  Теперь выполните `git push` для отправки на GitHub.")


def run_git_command(command):
    """
    Запускает команду Git с помощью subprocess и выводит вывод.
    """
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print(result.stdout)
        if result.stderr:
            print(f"STDERR: {result.stderr}")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка выполнения команды: {e}")
        print(f"STDERR: {e.stderr}")

# *** ВАЖНО:  Путь к репозиторию: "." означает текущую директорию ***
repo_path = "."
generate_fake_commits(repo_path)