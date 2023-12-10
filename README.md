推荐使用pycharm专业版操作，python3.10

1.先创建一个文件夹（名字必须为mysite2，原因未知，应该是里面的一些配置都是我创建项目时候配置好了，不是这个名字得改配置，暂时不知道怎么改，可以研究下）拉取项目到本地

2.用pycharm打开mysite2文件夹项目（注意要打开直属子文件中有manage.py的文件夹mysiti2），自己创建一个独立VENV环境，进入VENV环境，直接运行\VENV\Scripts\activate文件

3.安装python需要的依赖包

在项目文件目录（根目录）

pip install -r requirements.txt

4.需要提前安装MySQL，否则需要修改setting.py关于databases的数据

先修改一些MySQL的参数，让他与你电脑的参数一致，不然无法连接数据库

创建数据库，也可以理解为初始化数据库

在项目文件夹目录下执行

python manage.py makemigrations

python manage.py migrate

5.运行项目，编辑配置Django服务器，选定工作目录，有红色恢复按钮就按，应用，运行绿色三角符号

