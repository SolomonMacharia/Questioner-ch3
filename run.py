from app import create_app
from migrate import create_tables

create_tables()

app = create_app()