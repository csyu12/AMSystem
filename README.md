# Asset Management Website

> 一个基于Python3.7 + Django 3.0.8 制作的 “资产内部管理网站“

------

### IDE

- Pycharm

### DataBase

- MySQL：5.7.43

### 依赖环境

- Django：3.0.8
- Python：3.7
- django-pure-pagination：0.3.0
- mysqlclient：2.0.1

备注：建议通过Django后台添加测试数据，比较方便
 
------

### 项目部署（本文是在Windows系统环境下调试）

 1. 下载项目

    > 访问 https://github.com/csyu12/Asset-Management-Website 下载本项目源码解压

    > 也可以通过配置PyCharm环境直接Git克隆

 2. 安装项目依赖

    ```python
    # 建议创建虚拟环境，在虚拟环境下安装本项目依赖，以免污染本地包
    pip install -r requirements.txt
    ```
    
 3. 创建并配置数据库（根据实际使用的数据库进行配置，本文以MySQL为例）

    ```mysql
    # 在MySQL终端界面中执行如下命令，创建名为'HRS'数据库
    CREATE DATABASE `HRS` CHARSET UTF8;
    ```
    ```python
    # 在源码`AMWebsit/setting.py` 修改数据库配置，如下所示（根据实际修改）
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
    ```python
    # 在manage.py目录下执行
    # 记录所有关于modes.py的改动，在app_xx目录下自动建立migrations目录，最终生成00xx_initial.py
    python manage.py makemigrations
    
    # 针对生成的00xx_initial.py内容更新数据库，比如创建数据表、增加修改字段属性等
    python manage.py migrate
    ```

 4. 创建后台超级管理员账户

    ```python
    # 按要求输入用户名、邮箱（格式要合法）、密码
    python manage.py createsuperuser
    ```
    
 5. 运行服务

    > 第一种运行方式：通过命令行启动

    ```python
    # 运行如下命令启动服务
    python manage.py runserver
    ```
    ![image](https://github.com/csyu12/Asset-Management-Website/assets/67434922/833d495d-f0ad-4ea5-8ae3-777f143c0c1e)

    > 第二种运行方式：修改'Run/Debug Configurations'，在'Script Path'栏目指定manage.py文件绝对路径，在'Parameters'栏目填写'runserver 80'，最终点击run箭头按钮即可，如下图
    
    ![image](https://github.com/csyu12/Asset-Management-Website/assets/67434922/34ec03a8-70b3-4dfe-91c4-49ec47246635)
    ![image](https://github.com/csyu12/Asset-Management-Website/assets/67434922/f07e6bb0-a09a-4ad7-bc70-ef218c703243)
    ![image](https://github.com/csyu12/Asset-Management-Website/assets/67434922/8034f5fe-a354-4fc0-8cb5-679861080e36)

 7. 进入后台

    > 启动成功后在浏览器输入`http://127.0.0.1:8000/`访问项目主页，并使用第4步创建的超级管理员账户进行登录即可
    
    ![image](https://github.com/csyu12/Asset-Management-Website/assets/67434922/1928b608-1ee7-45b5-b0e0-40dfbb86865b)

