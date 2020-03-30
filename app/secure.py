"""
 Created by Tang on 2020/2/11 11:00
"""
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:root@localhost:3306/fisher'
SECRET_KEY = 'sdfasdgasdgfah'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_TEARDOWN = True

# Email 配置
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TSL = False
MAIL_USERNAME = '1441748573@qq.com'
MAIL_PASSWORD = 'oatijpoqaahghbei'
