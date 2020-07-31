import random
from random import shuffle

def subject( kemu,question_num, open_addr, save_addr):
    with open(open_addr, 'r') as f:
        # print(f.readlines())
        strage = []
        num = 0
        s = list(f.readlines())
        for i in range(len(s)):
            if s[i][0:2] == '- ' and len(s[i])>3:
                # print(s[i])
                num += 1
                # strage.append(s[i][0:-1].replace('- ', str(num)+'. '))
                strage.append(s[i][0:-1])
        print(strage)
        print(len(strage))
        a = len(strage)


    b = question_num



    def random_num(a,b):
    # print("请输入题数 抽屉数:")
    # a, b = map(int, input().split())
    #     print(a,b)
        ls = list(range(a))
        ls2 = []
        # 从x个数字中随机抽取10个数字
        for i in range(b):
            rd = random.choice(ls)  # 此处亦可去重
            ls2.append(rd)
            # ls.remove(rd)
        return ls2

    # 如果有重复，重新执行一次，直到没有重复为止
    ls2 = random_num(a,b)
    # print(ls2)
    while len(set(ls2)) != len(ls2):  # 去重
        ls2 = random_num(a, b)

        # pass

    # 检验结果
    # print(ls)
    ls2.sort()
    # print(ls2)
    result = []
    for i in ls2:
        print(strage[i])
        result.append(strage[i])



    # with open('随机抽题-题目列表.md', 'w+') as f1:
    with open(save_addr, 'a+') as f1:
        # f1.write('-' * 60 + '操作系统'+'-' * 60+'\n'*2 )
        # f1.write(kemu+'\n')
        f1.write('\n')   # 科目间隔
        for i in result:
            ret.append(i)
            f1.write(str(i)+'\n'*2)

# 初始化清空文件内容
with open('/Users/Merlin/Git/develop-interview/面试抽题.md', 'w+') as f1:
    f1.write('***请严格按照题目顺序作答：***'+'\n')
ret = []
ret0 = []
subject( '**手撕代码：**', 4, '/Users/Merlin/Git/develop-interview/机试思路.md', '/Users/Merlin/Git/develop-interview/面试抽题.md')


subject( '**操作系统：**', 4, '/Users/Merlin/Git/develop-interview/操作系统.md', '/Users/Merlin/Git/develop-interview/面试抽题.md')
subject( '**计算机网络：**', 4, '/Users/Merlin/Git/develop-interview/计算机网络.md', '/Users/Merlin/Git/develop-interview/面试抽题.md')
subject( '**数据库：**', 4, '/Users/Merlin/Git/develop-interview/数据库.md', '/Users/Merlin/Git/develop-interview/面试抽题.md')
subject( '**Python相关：**', 4, '/Users/Merlin/Git/develop-interview/面试题库.md', '/Users/Merlin/Git/develop-interview/面试抽题.md')
subject( '**项目问题：**', 4, '/Users/Merlin/Git/develop-interview/项目相关.md', '/Users/Merlin/Git/develop-interview/面试抽题.md')

# 科目顺序无序
# print(len(ret))
# ret0.append(ret[0:4])
# ret0.append(ret[4:8])
# ret0.append(ret[8:12])
# ret0.append(ret[12:16])
# ret0.append(ret[16:20])
# ret0.append(ret[20:])
# shuffle(ret0)
# # print(ret0)
# ret00 = [n for a in ret0 for n in a ]
# print(ret00)
# with open('/Users/Merlin/Git/develop-interview/面试抽题.md', 'w+') as f2:
#     f2.write('***请严格按照题目顺序作答：***'+'\n')
#     for i in ret00:
#         f2.write(str(i) + '\n' * 2)

# 全无序
# print(ret)
# shuffle(ret)
# with open('/Users/Merlin/Git/develop-interview/面试抽题.md', 'w+') as f2:
#     f2.write('***请严格按照题目顺序作答：***'+'\n')
#     for i in ret:
#         f2.write(str(i) + '\n' * 2)

'''
待完善：
    如何随机化科目类型、题目
    
    至PPT，更能集中精力

'''
