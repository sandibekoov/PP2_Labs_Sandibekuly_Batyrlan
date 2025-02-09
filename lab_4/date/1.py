from datetime import datetime, timedelta

def subtraction():
    today = datetime.now()
    new_date = today - timedelta(days=5)
    print(new_date.strftime("%Y-%m-%d"))

subtraction()
