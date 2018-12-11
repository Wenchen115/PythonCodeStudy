# 定义一个函数，显示可以使用的功能列表给用户
def fun():
    print("欢迎光临用户管理系统")
    print(" 1.delete")
    print(" 2.update")
    print(" 3.find")
    print(" 4.list")
    print(" 5.exit")


# 定义一个列表，用来存储用户的信息
test_user = []

while True:
    fun()  # 调用fun函数
    Var = input("请输入选择的功能：")
    if Var == 'update':
        username = input('请输入用户姓名：')
        userId = input('请输入用户id：')
        age = input('请输入用户年龄：')
        contact = input('请输入联系方式：')
        print("您输入的信息为:{}:{}:{}:{}".format(userId, username, age, contact))
        x = 0  # 计数
        flag = 0  # 定义标志位
        for i in test_user:
            if i['id'] == userId:
                flag = 1
                break
            else:
                x += 1
        if flag == 1:
            print('用户id已存在')
        else:
            user = {}  # 定义存放单个用户的字典
            user['id'] = userId
            user['name'] = username
            user['age'] = age
            user['contact'] = contact

            test_user.append(user)  # 将存放单个用户的字典追加到test_user列表中

    elif Var == 'delete':
        delName = input('请输入用户名：')
        # 记录要删除的下标，flag为标志位，如果找到flag=1，否则为0
        x = 0
        flag = 0
        for i in test_user:
            if i['name'] == delName:
                flag = 1
                break
            else:
                x = x + 1
        if flag == 0:
            print("没有此用户！")
        else:
            del test_user[x]  # 删除test_user列表中索引为x的元素

    elif Var == 'find':
        SearchName = input('请输入要查找的用户名：')
        x = 0
        flag = 0
        for i in test_user:
            if i['name'] == SearchName:
                flag = 1
                break
            else:
                x += 1
        if flag == 0:
            print('没有此用户')
        else:
            print('查询结果：')
        print("id:{} name:{} age:{} contact:{}".format(i['id'], i['name'], i['age'], i['contact']))

    elif Var == 'list':
        print('id   name   age   contact')
        for i in test_user:
            print("{}   {}   {}   {}".format(i['id'], i['name'], i['age'], i['contact']))

    elif Var == 'exit':
        print('退出系统')
        break  # 退出wile循环

    else:
        print("请确认输入是否正确")
