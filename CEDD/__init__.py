from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
import warnings

warnings.filterwarnings( "ignore", category=FutureWarning )
warnings.filterwarnings( "ignore", category=DeprecationWarning )

app = Flask( __name__ )

with app.app_context():
	app.secret_key = 'BlackThunder'

	app.config[ 'PERMANENT_SESSION_LIFETIME' ] = timedelta( minutes=30 )

	app.config[ 'TESTING' ] = True

	app.config[ 'SQLALCHEMY_TRACK_MODIFICATIONS' ] = True

	app.config[ 'SQLALCHEMY_ECHO' ] = True

	app.config[ 'SQLALCHEMY_RECORD_QUERIES' ] = True

	# app.config[ 'SQLALCHEMY_DATABASE_URI' ] = "mysql+pymysql://kishan31199:kishan31@db4free.net:3306/kishan31"
	app.config[ 'SQLALCHEMY_DATABASE_URI' ] = 'sqlite:///rfmd.db'

	# app.config[ 'SQLALCHEMY_MAX_OVERFLOW' ] = 0

	app.config[ 'UPLOAD_FOLDER' ] = 'static/Dataset/Images'
	db = SQLAlchemy( app )
	print( "in project" )

	import CEDD.com.controller.RegistrationController
