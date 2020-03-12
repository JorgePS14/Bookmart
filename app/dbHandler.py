from flask_sqlalchemy import SQLAlchemy

def setDatabaseEnv(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost:3306/bookmart'
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'password'
    app.config['MYSQL_DB'] = 'bookmart'
    app.secret_key = 'HelloThereGeneralKenobi'
    db = SQLAlchemy(app)

    return db