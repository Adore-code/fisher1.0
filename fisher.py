"""
 Created by Tang on 2020/2/11 10:30
"""
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=8099)
    # 单进程  单线程
    #