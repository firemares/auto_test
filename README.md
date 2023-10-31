<div align="center">


<h1>api_auto</h1>

</div>

## 项目介绍
api_auto 是一个基于UI进行自动化测试测项目，
主要依赖于selenium、request和paramiko等第三方库来实现。
该工具通过模拟用户使用时的操作，实现对系统各项功能的运行状态进行检测，目前该工具已覆盖90%的功能模块。
api_auto的宗旨是 让繁琐的工作自动化。



## 主要文件及其功能介绍

> **<h4>zaxy文件夹</h4>**
> 存放着稳定版本的工具


> **<h4>function.py</h4>**
> 存放大部分公共函数


> **<h4>connect_linux.py</h4>**
> 检测api审计系统的安装环境--并且辅助环境配置
> 1. 检测各个组件的开启状态
> 2. 检测防火墙是否开启了各个组件所需要开放的端口
> 3. 检测java进程是否启动




> **<h4>agent_check.py</h4>**
> 测试agent基于【多ip】的运行结果
> 1. 在采集机器上检测是否安装agent，未安装则自动安装
> 2. 在api审计系统上开启agent按钮，并检测该系统宿主机返回的【Agenton】和【ip】参数是否准确
> 3. 在采集机器上模拟用户访问网页时产生的流量
> 4. 检测api审计系统是否采集到对应流量





> **<h4>all_mod.py</h4>**
> 统合了全部流程进行自动化测试的工具



> **<h4>test_kafka.py</h4>**
>kafka模块测试


> **<h4>read_sen_txt.py</h4>**
>专门触发敏感的流量


> **<h4>auto_threads.py</h4>**
>触发全部主要功能的流量


## 使用方式



**<h4>针对：all_mod.py，connect_linux.py</h4>**
**全局搜索--【每次启动必须修改的地方】**
**每个存在该注释的的下方，存在您需要修改的内容**
**修改完成后启动即可**
> 
> 
> 
**<h4>1.全量测试方法</h4>**
> first：
> 访问auto_treads.py
> 修改IP，为本次（asi系统安装地址）
> 
> 
> second：
> 访问all_mod.py
> run()中修改为asi系统服务器地址
> 
> 
> 
> finall：
> 直接执行
> 等待页面出现"请给纳管服务提前命名"
> 
> 
> 输入测试服务名称（不能是系统已纳管服务--否则会报错）
> eg： 输入（test1.com）



**<h4>2.造数据的方法（敏感、威胁等测试常用的）</h4>**

> 访问auto_threads.py
> 修改json=xxx内xxx的内容
> 
> 
> 
> thread(100, 3, 'tesdsadasadt1.com')参数内容对应： 单个线程请求数量，线程数，服务名称





直接运行即可打流
## 安装教程
``` sh
# 更新所需要的第三方库
pip install -r requirements.txt

