# coding:utf-8
import sys
# sys是和python解释器打交道的

# sys.argv
usr = sys.argv[1]
pwd = sys.argv[2]
if usr == 'john' and pwd == '666':
    print("登陆成功")
else:
    exit()

# 命令行输入python3+文件路径+usr+pwd也能达到'登陆成功'的目的
# 没觉得有啥用


# sys.path
# 模块默认是在硬盘中，当你import之后，就加到内存里面了
# 一个模块能否被顺利导入，全看sys.path下面有没有这个模块所在的路径


# sys.modules   当前python解释器执行所导入的所有模块。
print(sys.modules)  # 是我们导入到内存中所有模块的名字:这个模块的内存地址