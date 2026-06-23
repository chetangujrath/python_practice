import shutil
import logging
import schedule

def check_disk():
    disk = shutil.disk_usage('/')
    per_used = (disk.total - disk.free)/disk.total*100
    if per_used > 75:
        logging.warning("Disk is alomost full")
    elif per_used >95:
        logging.critical("disk is in critical stage")
    print(per_used)

check_disk()

schedule.every(2).seconds.do(check_disk) #cron setup

while True:
    schedule.run_pending()