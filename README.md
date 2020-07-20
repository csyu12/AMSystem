#  Asset Management Website

> 一个基于Python3.7 + Django 3.0.8 制作的 “资产内部管理系统“

------

### IDE

- Pycharm

### DataBase

- MySQL：5.7版

### 依赖环境

- Django：3.0.8
- Python：3.7
- django-pure-pagination：0.3.0
- mysqlclient：2.0.1


------

### 项目部署（本人是Windows10系统）

1. 下载项目

   * 访问 https://github.com/csyu12/RS_System 下载本项目源码解压

   * 通过PyCharm直接下载，如图：

      ![Image text](README_IMG/1.png)

      ![Image text](README_IMG/2.png)

2. 安装项目依赖

   ```
   pip install -r requirements.txt
   ```

3. 创建数据库

   MySQL数据库中执行：

   ```mysql
   CREATE DATABASE `HRS` CHARSET UTF8;
   ```

   修改`RS_system/setting.py` 修改数据库配置，如下所示：

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'HOST': 'localhost',
           'PORT': '3306',
           'NAME': 'HRS',
           'USER': 'root',
           'PASSWORD': '123456',
       }
   }
   ```

   在终端下执行:

   ```python
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```

4. 创建后台管理员账户

   ```python
   python3 manage.py createsuperuser
   ```

   按要求输入用户名、邮箱（格式要合法）、密码

5. 运行服务器

   * 第一种方法：在终端中输入

   ```python
   python3 manage.py runserver
   ```

   `在浏览器打开 http://127.0.0.1:8000/ 即可访问主页`

   * 第二种方法：可以运行manage.py文件，修改配置，如下图。后续只需要运行manage.py即可

     ![Image text](README_IMG/3.png)

     ![Image text](README_IMG/4.png)

6. 进入后台

   - 在浏览器输入127.0.0.1:8000/admin
   - 使用第5步创建的后台管理员账户进行登录