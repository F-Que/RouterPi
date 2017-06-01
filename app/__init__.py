from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app import Index
from app import Status
from app import RouterLogin
from app import Lanport
from app import Hotpoint
from app import Wanport
from app import Dhcp
from app import Clist
from app import Chpwd
from app import Sysrestart