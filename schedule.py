from apscheduler.schedulers.background import BackgroundScheduler
import sys 
sys.path.append('..')
from epost import send, read
import settings

def job():
    send(read(settings.database))
    print("Email sent.")

def schedule():
    scheduler = BackgroundScheduler()
    scheduler.add_job(job, 'cron', day_of_week='mon', hour=10)
    print("Job scheduled. Starting schedule...")
    scheduler.start()
