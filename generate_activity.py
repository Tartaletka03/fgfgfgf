import os
import datetime
import random

repo_path = "."  # Текущая директория (репозиторий Git)
today = datetime.date.today()
start_date = today - datetime.timedelta(weeks=8)  # 8 недель назад
end_date = today - datetime.timedelta(days=1)  # До вчерашнего дня, чтобы сегодня не было коммитов
file_name = "dummy_file.txt"  # Имя файла, который будем коммитить

def generate_commits(start_date, end_date):
    """Генерирует коммиты в случайные дни в течение 8 недель."""
    current_date = start_date
    week_start = start_date
    while week_start <= end_date:
        # Выбор случайных дней в течение недели
        commit_days = random.sample(
            [week_start + datetime.timedelta(days=i) for i in range(7)],
            random.randint(3, 4)  # 3-4 дня коммитов в неделю
        )
        for commit_date in commit_days:
            # Создание коммитов в выбранный день
            num_commits = random.randint(2, 4)
            for i in range(num_commits):
                date_str = commit_date.strftime("%Y-%m-%d")
                commit_message = f"Simulated commit on {date_str} #{i+1}"

                # Запись в файл
                with open(file_name, "a") as f:
                    f.write(f"{commit_message}\n")

                # Добавление файла и коммит
                os.system("git add " + file_name)
                os.system(f'git commit --date="{date_str} {random.randint(8, 17)}:00:00" -m "{commit_message}"')  # Случайное время

        week_start += datetime.timedelta(weeks=1) # Переход к следующей неделе

    print("Локальные коммиты созданы. Теперь сделайте 'git push'.")

# Вызов функции для генерации коммитов
generate_commits(start_date, end_date)