# TODO List
- 感情图标显示
- 工具栏
- 场景交互
- 多线程加载
- 主线任务链


# 事件
通过flag管理可运行事件状态
```json
"talk_sample":{ //事件唯一索引，
        "req":["f1","f2"],  // 事件前置flag要求，
        "content":"......", // 事件文本内容
        "state":"Idle",     // 事件时的角色动作
        "emotion":"Normal", // 事件时的角色感情
        "duration":500,     // 事件持续事件
        "flag_add":["f3"],  // 执行事件后要增加的flag
        "flag_remove":["f2"], // 执行事件后要去除的flag
        "trust":0,          // 执行事件后的信赖变化
        "options":[         //事件回应选项
            {
                "option":"喵",//回应文本
                "req":["love"],//显示该选项需要的flag
                "next":"talk_sample.second"//该选项对应的下一个事件
            },
            { "option":"......"}
        ]
    },
```


# 利用Wiki可以下载的Webm格式动画
可以利用ffmpeg将webm转换为PNG序列帧

命令行将视频以4帧每秒转为png序列：
```
ffmpeg -vcodec libvpx -i .\NAME.webm -r 4 NAME/%04d.png
```
当然也可以用网络上的转换器什么的，但下个ffmpeg还是很方便的

# Reference
https://github.com/CharlesPikachu/Tools/tree/master/DesktopPet