import os
import time

# Wait for repo to get updated
os.system("git fetch && git reset --hard origin/master ")
time.sleep(10)
# Call insert
os.system("python3 utils/push/hookTriggeredInsert.py")
