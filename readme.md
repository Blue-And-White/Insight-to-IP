# ![image-20230821142250942](https://blueandwhite.oss-cn-beijing.aliyuncs.com/blog/202308/image-20230821142250942.png)

   攻防演练中，被攻破前，蓝队大多数情况只能获得攻击者的ip地址，尽管现在有很多威胁情报平台，但是在使用过程中我发现，对于一些消息还是存在滞后性，结合更多地接口数据库进行搜集信息能够帮助我们分析。

​	Insight into IP 是一个通过ip地址或域名查询所有者信息的一款工具，目前是一个初始的版本，帮助我们更快速的获得攻击IP信息。

​	支持fofa查询，在第一次运行后，会在根目录下生成配置文件，您可以配置您的秘钥。

   目前有三个参数：

​	

```
- i 指定对指定ip进行搜集
- d 指定域名进行搜集（最好是先执行-i参数后进行查询，通过IP反查更加精确）
- j 开启判断功能，目前支持存活判断，端口判断，以及cdn检测
- o 指定文件输出
```

​	使用示例：

​	![image-20230821142931342](https://blueandwhite.oss-cn-beijing.aliyuncs.com/blog/202308/image-20230821142931342.png)



目前调用的接口还比较少，做不到特别全面，但是基本使用还是能够满足了，如果您有宝贵的意见，欢迎联系我。



更新日志：
2023.10.03 添加了判断扫描功能，加入-l 1参数可以对于域名是否存活以及IP端口开放信息进行判断，更加方便进行分析
