#format转换数据输出可用*来达到+f效果
poem="""
\tThe lovely world
with logic so firmly
\n\t\twhere there is none
"""
print("---------")
print(poem)
print("----------")
five=10-2+3-6
print(f"This should be five:{five}")
def secret_formula(started):
    jelly_beans=started*500
    jars=jelly_beans/1000
    crates=jars/100
    return jelly_beans,jars,crates#返回相应值
started_point=10000
beans,jars,crates=secret_formula(started_point)
print("With a starting point of:{}".format(started_point))
print(f"We'd have {beans} beans,{jars} jars,and {crates} crates.")
started_point=started_point/10
print("We can also do that this way:")
formula=secret_formula(started_point)
print("We'd have {}beans,{}jars,and {} crates".format(*formula))#*指定导入数据