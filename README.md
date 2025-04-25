Build a full stack medical institution management platform using Vue 3, Vite, Flask, MySQL/PostgreSQL, and Django ORM.
Utilize Vue 3 and Vite for rapid development, design user-friendly interactive interfaces, and enhance user experience.
Build an efficient RESTful API based on Flask to handle requests such as medical data queries and user authentication.
Using MySQL/PostgreSQL, managing data models through Django ORM to improve data processing efficiency.
Utilize the fetch API to achieve real-time communication between the front-end and back-end, dynamically load medical record detail pages, and improve response speed.
主要用了这些东西：
flask（项目的框架）
flask-sqlalchemy（用来映射数据库的ORM库。）
pymysql（用来连接数据库的）
flask-jwt-extended（实现有状态登录的库，会生成一个token给前端，前端每次请求带token，实现用户认证）

前端运行：
1、文件管理器打开 D:\1209W87\web
2、地址栏输入 cmd，打开cmd命令工具
3、运行命令：npm run dev
4、终端输出的 Local:   http://localhost:5173/，就是访问地址

后端运行：
1、文件管理器打开 D:\1209W87\backend-flask
2、地址栏输入cmd，打开cmd命令工具
3、运行flask run
