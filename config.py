import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "16743442")

API_HASH = os.environ.get("API_HASH", "12bbd720f4097ba7713c5e40a11dfd2a")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6146904519:AAFOo8p6kAJbsXND7u1ODRmsBb23FEPFYHk") 

FORCE_SUB = os.environ.get("FORCE_SUB", "-1001813095890") 

DB_NAME = os.environ.get("DB_NAME","kunal")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://Abhi12:abhi12@cluster0.bdue3ap.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "5"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/6cb6f227120d1622707ba.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6198858059').split()]

