
product_list = [
    ('Iphone',5800),
    ('Mac Pro',9800),
    ('Bike',800),
    ('Watch',10600),
    ('Coffee',31),
    ('lemon Python',5800),
]
shopping_list = []
salary = input("请输入你的工资:")
if salary.isdigit():
    salary = int(salary)
    while True:
        for index,item in enumerate(product_list):#这个函数自行去理解
        user_choice = input("选择要买嘛？>>>:")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >=0:
                p_item = product_list[user_choice]
                if p_item[1] <= salary: #买的起
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    print("添加 {0}到购物车，你现在的余额是{1} " .format(p_item,salary) )
                else:
                    print("你的余额只剩[%s]啦" % salary)
            else:
                print("产品编号[%s] 不存在!"% user_choice)
        elif user_choice == 'q':
            print("--------购物清单------")
            for p in shopping_list:
                print(p)
            print("你现在的余额:",salary)
            exit()
        else:
            print("无效选项")