#   --------------------------------注释区--------------------------------
#   入口：康师傅味道馆小程序
#   积分换泡面
#   抓任意请求体的encryptsessionid 把值全部塞进去
#   变量:yuanshen_ksf 多号： @分割
#   商品刷新时间：工作日周一，周五下午15:00
#   --------------------------------一般不动区-------------------------------
#                     _ooOoo_
#                    o8888888o
#                    88" . "88
#                    (| -_- |)
#                     O\ = /O
#                 ____/`---'\____
#               .   ' \\| |// `.
#                / \\||| : |||// \
#              / _||||| -:- |||||- \
#                | | \\\ - /// | |
#              | \_| ''\---/'' | |
#               \ .-\__ `-` ___/-. /
#            ___`. .' /--.--\ `. . __
#         ."" '< `.___\_<|>_/___.' >'"".
#        | | : `- \`.;`\ _ /`;.`/ - ` : | |
#          \ \ `-. \_ __\ /__ _/ .-` / /
#  ======`-.____`-.___\_____/___.-`____.-'======
#                     `=---='
# 
#  .............................................
#           佛祖保佑             永无BUG
#           佛祖镇楼             BUG辟邪
#佛曰:  
#        写字楼里写字间，写字间里程序员；  
#        程序人员写程序，又拿程序换酒钱。  
#        酒醒只在网上坐，酒醉还来网下眠；  
#        酒醉酒醒日复日，网上网下年复年。  
#        但愿老死电脑间，不愿鞠躬老板前；  
#        奔驰宝马贵者趣，公交自行程序员。  
#        别人笑我忒疯癫，我笑自己命太贱；  
#        不见满街漂亮妹，哪个归得程序员？
#
#   --------------------------------代码区--------------------------------

import lzma, base64
exec(lzma.decompress(base64.b64decode('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')))