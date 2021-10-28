import os
from app import db 

if os.path.exists("db/database.db"):
    print("...apagando banco antigo...")
    db.drop_all()

print("...criando banco...")
db.create_all()