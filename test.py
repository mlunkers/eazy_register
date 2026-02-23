def create_user_name():
    while True:
        first_name = input('输入姓氏（选填）: ')
        if len(first_name) >= 8:
            print('长度过长，请重新输入')
            continue
        else:
            first_name = first_name.strip()
            break

    while True:
        last_name = input('输入名字:')
        if last_name == '':
            print('名字不能为空，请输入名字！')
            continue
        elif len(last_name) >= 7:
            print('名字长度过长，请重新输入')
            continue
        else:
            last_name = last_name.strip()
            break

    if first_name:
        user_name = first_name + last_name
        user_name = user_name.title()
        return user_name
    else:
        user_name = last_name
        user_name = user_name.title()
        return user_name

def create_user_information():
    gender_choose = ('男','女')
    day_number = list(range(1,32))
    mouth_number_2 = list(range(1,13,2))
    mouth_number_3 = list(range(2,13,2))

    while True:
        year = input('请输入出生年份：')
        if year == '':
            print('年份不能为空')
            continue
        elif year != '':
            year = int(year)
            if year > 2026 or year < 1920:
                print('请输入有效日期')
                continue
            else:
                break
        else:
            print('你输入的似乎不是数值')
            continue

    while True:
        month = input('请输入你的出生月份')
        if month == '':
            print('月份不能为空')
            continue
        elif month != '':
            month = int(month)
            if month not in mouth_number_2 and mouth_number_3:
                print('请输入有效月份')
                continue
            else:
                break

    while True:
        day = input('请输入出生日')
        if day == '':
            print('出生日不能为空')
            continue
        elif day != '':
            day = int(day)
            if month in mouth_number_2 and day not in day_number:
                print('请输入有效日期：')
                continue
            elif month in mouth_number_3 and day not in day_number[:-1]:
                print('请输入有效日期：')
                continue
            else:
                break
    while True:
        gender = input('请选择您的性别（男/女）')
        if gender in gender_choose:
            break
        else:
            print('请重新输入')
            continue

    return year, month, day, gender

def create_user_account():
    while True:
        account = input('请创建一个账号：')
        if account == '':
            print('账号不能为空')
            continue
        elif account != '':
            if len(account) < 6 or len(account) > 18:
                print('密码长度限制')
                continue
            else:
                break

    while True:
        code = input('请创建一个密码')
        if code == '':
            print('密码不能为空')
            continue
        elif code != '':
            if len(code) < 6 or len(code) > 18:
                print('密码长度限制')
                continue
            else:
                break

    return account,code

