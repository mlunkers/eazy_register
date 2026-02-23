from test import *
user_information = {}
user_name = create_user_name()
year,month,day,gender = create_user_information()
account,code = create_user_account()
user_information[user_name] = {}
user_information[user_name]['name'] = user_name
user_information[user_name]['Gender'] = gender
user_information[user_name]['birthday'] = f'{year}-{month}-{day}'
user_information[user_name]['account'] = account
user_information[user_name]['code'] = code
print(user_information)


