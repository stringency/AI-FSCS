推荐使用pycharm专业版操作，python3.10

1.先拉取项目到本地

2.进入VENV环境

3.安装python需要的依赖包

在项目文件目录（根目录）

pip install -r requirements.txt

4.需要提前安装MySQL，否则需要修改setting.py关于databases的数据

创建数据库，也可以理解为初始化数据库

在项目文件夹目录下执行

python manage.py makemigrations mainsite

python manage.py migrate

5.运行项目

