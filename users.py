from test import *
from pathlib import Path
import json
path = Path('users.json')
if not path.exists():
    user_name = create_user_name()
    year,month,day,gender = create_user_information()
    account,code = create_user_account()
    users = create_user_dict(user_name,year,month,day,gender,account,code)
    path.write_text(json.dumps(users))
else:
    users = json.loads(path.read_text())
    while True:
        request_account = input('请输入账号:')
        request_code = input('请输入密码:')
        test = login_verify(request_account,request_code,users)
        if test == True:
            print('登陆成功')
            break
        elif test == None:
            print('账号或密码错误')
            test = None
            continue






