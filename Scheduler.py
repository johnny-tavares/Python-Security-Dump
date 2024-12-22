import schedule;
from datetime import time, timedelta, datetime
import time as tm

def job():
    print("Job is ran")

s = schedule.every().day.at("10:30").do(job)

counter = 0

while True:
    schedule.run_pending()
    tm.sleep(1)
    counter+=1
    if counter == 10:
        schedule.cancel_job(s)