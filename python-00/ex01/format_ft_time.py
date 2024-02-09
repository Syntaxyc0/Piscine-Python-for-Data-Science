import time
from datetime import datetime
def main() :
    current_time = time.time()
    formatted_date = datetime.utcfromtimestamp(current_time).strftime('%b %d %Y')

    print(f"Seconds since January 1, 1970: {current_time:.4f} or {current_time:1.2e} in scientific notation")
    print(formatted_date)

if __name__ == '__main__':
    main()