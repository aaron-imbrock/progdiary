import datetime, os
import psycopg2

from dotenv import load_dotenv

load_dotenv()

connection = psycopg2.connect(os.environ["DATABASE_URL"])
