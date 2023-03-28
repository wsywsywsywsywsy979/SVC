## code ##
1. 解释基于https://github.com/svc-develop-team/so-vits-svc 复现调整跑通
2. 相较于原始so-vits-svc的修改：修复了部分bug，去掉了需要与git交互的代码（因为运行会因为网络问题导致程序中断）

## data ##
1. datset_raw：从AIShell3中选择的两个说话人的数据（每个说话人100条语音数据）
2. raw：林俊杰的《可惜没如果》只有人声的部分音频片段

## result ##
1. 林俊杰的声音转换从aishell3中选择的两个说话人的声音的结果
2. 结论：同性别之间转换的效果还可以

如果有问题，欢迎commit issue 讨论 ~
