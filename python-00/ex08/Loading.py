import sys
import math
import shutil
from time import time


def calculate_remaining_space(i, length, time_spent, speed):
    len_percent_progress = len(f"{math.floor(i/length * 100)}%")
    len_progress = len(f" {i}/{length}")
    progress_info_len = len(
        f" [{math.floor(time_spent / 60):02}" +
        f":{(math.floor(time_spent) % 60):02}" +
        f"<{(math.floor((length-i)/speed / 60)):02}" +
        f":{(math.floor((length-i)/speed) % 60):02} " +
        f", {speed:.2f}it/s]")
    return 3 + len_percent_progress + len_progress + progress_info_len


def ft_tqdm(lst: range) -> None:
    '''
    This function aims to recreate the tqdm function
    which is used to get a progress bar
    '''
    try:
        start_time = time()
        length = len(lst)
        space = 42
        number_bars = shutil.get_terminal_size().columns - space
        for i, index in enumerate(lst, 1):
            time_spent = time() - start_time
            speed = i / time_spent
            current_bar = math.floor(i/length * number_bars)
            space = calculate_remaining_space(i, length, time_spent, speed)
            number_bars = shutil.get_terminal_size().columns - space
            progress_bar = ('|'
                            + '█' * current_bar
                            + ' ' * (number_bars - current_bar)
                            + '|')
            sys.stdout.write(f"{math.floor(i/length * 100)}%"
                             + progress_bar
                             + f" {i}/{length} "
                             + f"[{(math.floor(time_spent /60)):02}"
                             + f":{(math.floor(time_spent %60)):02}"
                             + f"<{(math.floor((length - i) / speed / 60)):02}"
                             + f":{(math.floor((length - i) / speed % 60)):02}"
                             + f", {speed:.2f}it/s]\r")
            sys.stdout.flush()
            yield index
    except Exception as e:
        print({e})
