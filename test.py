def create_user_name():
    while True:
        first_name = input('输入姓氏（选填）: ')
        if first_name == '':
            break
        else:
            if ' ' in first_name:
                print('姓氏中不能带空格')
                continue
            elif len(first_name) >= 8 and ' ' not in first_name:
                print('长度过长，请重新输入')
                continue
            else:
                break
#收集用户姓氏
    while True:
        last_name = input('输入名字:')
        if last_name == '':
            print('名字不能为空，请输入名字！')
            continue
        elif len(last_name) >= 7 and  ' ' not in last_name:
            print('名字长度过长，请重新输入')
            continue
        elif ' ' in last_name:
            print('不能输入空白')
            continue
        else:
            last_name = last_name.strip()
            break
#收集用户名字
    if first_name:
        user_name = first_name + last_name
        user_name = user_name.title()
        return user_name
    else:
        user_name = last_name
        user_name = user_name.title()
        return user_name
#合并为用户名
def create_user_information(b=None,a=None,c=None):
    alpbhaet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alpbhaet_copy = [i.upper() for i in alpbhaet]
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    gender_choose = ('男','女')
    day_number = list(range(1,32))
    mouth_number_2 = list(range(1,13,2))
    mouth_number_3 = list(range(2,13,2))
    while True:
        year = input('请输入出生年份：')
        if year == '':
            print('年份不能为空')
            continue
        for number in year:
            if number not in numbers:
                b = False
                break
        if b == False:
            for value in year:
                if ' ' not in year and value not in alpbhaet and value not in alpbhaet_copy and value not in numbers:
                    c = True
                    break
            if c == True:
                print('不支持的语言或符号')
                c = None
                b = None
                continue
            else:
                for value in year:
                    if ' ' not in year and value in alpbhaet or value in alpbhaet_copy:
                        a = True
                        break
                if a == True:
                    print('不能输入字母')
                    a = None
                    b = None
                    continue
                elif ' ' in year:
                    print('不能输入空格')
                    b = None
                    continue
        elif b == None :
            year = int(year)
            if year > 2026 or year < 1920:
                print('请输入有效日期')
                continue
            else:
                break
#收集用户出生年份
    while True:
        month = input('请输入你的出生月份')
        if month == '':
            print('月份不能为空')
            continue
        for value in month:
            if value not in numbers:
                a = True
                break
        if a == True:
            for value in month:
                if ' ' not in month and value not in alpbhaet and value not in alpbhaet_copy and value not in numbers:
                    c = True
                    break
            if c == True:
                print('未知的字符')
                c = None
                a = None
                continue
            else:
                for number in month:
                    if ' ' not in month and number in alpbhaet or number in alpbhaet_copy:
                        b = True
                        break
                if ' ' in month:
                    print('不能输入空格')
                    a = None
                    continue
                elif b == True:
                    print('不能输入字母')
                    a = None
                    b = None
                    continue
        elif a == None:
            month = int(month)
            if month not in mouth_number_2 + mouth_number_3:
                print('请输入有效月份')
                continue
            else:
                break
#收集用户出生月份
    while True:
        day = input('请输入出生日')
        if day == '':
            print('出生日不能为空')
            continue
        for value in day:
            if value not in numbers:
                a = False
                break
        if a == False:
            for value in day:
                if ' ' not in day and value not in alpbhaet and value not in alpbhaet_copy and value not in numbers:
                    c = True
                    break
            if c == True:
                print('不能输入符号或语言')
                a = None
                c = None
                continue
            else:
                for value in day:
                    if ' ' not in day and value in alpbhaet or a in alpbhaet_copy:
                        b = True
                        break
                if b == True:
                    print('不能输入字母')
                    a = None
                    b = None
                    continue
                elif ' ' in day:
                    print('不能输入空格')
                    a = None
                    continue
        elif a == None:
            day = int(day)
        if month in mouth_number_2 and day not in day_number:
            print('请输入有效日期')
            continue
        elif month in mouth_number_3 and day not in day_number[:-1]:
            print('请输入有效日期')
            continue
        else:
            break
#收集用户出生日
    while True:
        gender = input('请选择您的性别（男/女）')
        if gender in gender_choose:
            break
        else:
            print('请重新输入')
            continue

    return year, month, day, gender
#收集用户性别
def create_user_account():
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    alpbhaet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    alpbhaet_copy = [i.upper() for i in alpbhaet]
    while True:
        account = input('请创建一个账号：')
        for value in account:
            if value not in numbers and value not in alpbhaet and value not in alpbhaet_copy and value != '_':
                c = True
                break
        if account == '':
            print('账号不能为空')
            continue
        elif c == True:
            print('账号只能包含字母和数字还有下划线')
            c = None
            continue
        else:
            if len(account) < 6 or len(account) > 18:
                print('账号长度限制')
                continue
            else:
                break
#创建账号
    while True:
        code = input('请创建一个密码')
        if code == '':
            print('密码不能为空')
            continue
        for value in account:
            if value not in numbers and value not in alpbhaet and value not in alpbhaet_copy and value != '_':
                c = True
                break
        if c == True:
            print('密码只能包含字母数字和下划线')
        else:
            if len(code) < 6 or len(code) > 18:
                print('密码长度限制')
                continue
            else:
                break
#创建密码
    return account,code

