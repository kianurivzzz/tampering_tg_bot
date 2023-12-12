from dotenv import load_dotenv, dotenv_values

load_dotenv()
dotenv_val = dotenv_values('.env')

BOT_TOKEN = dotenv_val['BOT_TOKEN']

SHEETS_TOKEN_PATH = dotenv_val['SHEETS_TOKEN_PATH']
TAMP_SHEET = dotenv_val['TAMP_SHEET']
DB_SHEET = dotenv_val['DB_SHEET']

DB_PATH = dotenv_val['DB_PATH']
