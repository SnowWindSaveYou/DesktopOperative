# 简介
明日方舟丝卡蒂桌宠，主体是gpt出来前写的，改造ing

# TODO List
- 感情图标显示
- 工具栏
- 场景交互
- 多线程加载
- 主线任务链
- 接入GPT


# 事件
通过flag管理可运行事件状态
```json
"talk_sample":{ //事件唯一索引，
        "flag":["f0","f2"],  // 事件前置flag要求，如果是No代表只能通过对话触发
        "content":"你给我喵一个", // 事件文本内容
        "state":"Idle",     // 事件时的角色动作, 可选项有 [Idle, Attack, Interact, Loss, Move,Sit,Start]
        "emotion":"Normal", // 事件时的角色感情 可选项有 [Amazing,Angry,Loss,Happy,Shy]
        "duration":500,     // 事件持续事件ms
        "flag_add":["f3"],  // 执行事件后要增加的flag
        "flag_remove":["f2"], // 执行事件后要去除的flag
        "trust":1,          // 执行事件后的信赖值变化
        "options":[         //事件回应选项
            {
                "option":"喵",//回应文本
                "flag":["love"],//显示该选项需要的flag
                "next":"talk_sample.second"//该选项对应的下一个事件
            },
            { "option":"......"}//回应文本
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

