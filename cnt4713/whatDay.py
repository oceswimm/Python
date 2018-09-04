from datetime import datetime
from datetime import timedelta

print("Welcome to the JetLag algorithm:")
print("The actual time is:",datetime.time(datetime.now()))
print("In France it would be:",datetime.time(datetime.now()+timedelta(hours=6)))
print("In Australia it would be:",datetime.time(datetime.now()+timedelta(hours=14)))
print("In Russia it would be:",datetime.time(datetime.now()+timedelta(hours=7)))
print("In China it would be:",datetime.time(datetime.now()+timedelta(hours=12)))
print("In India it would be:",datetime.time(datetime.now()+timedelta(hours=9.5)))



