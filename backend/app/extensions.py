from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# instances of extensions
db = SQLAlchemy()
migrate = Migrate()