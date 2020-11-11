import time
import uiautomator2 as u2
# https://github.com/openatx/uiautomator2/blob/master/QUICK_REFERENCE.md

d = u2.connect()  # connect to device
print(d.info)

d.press("home")

# print(d.shell(["ls", "-l"]).output)
d.app_start("com.taobao.taobao", stop=True)
print(d.app_current())
print(d.device_info)

# 活动入口
# d.xpath('//*[@content-desc="主互动"]/android.widget.FrameLayout[2]').click()
d.xpath(
    '//*[@resource-id="com.taobao.taobao:id/rv_main_container"]/android.widget.FrameLayout[4]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]'
).click_exists()

d.xpath('//*[@text="赚喵币"]').click()

d.xpath('//*[@text="签到"]').click_exists()

for i in range(20):
    print(i, "==" * 30)
    d.xpath('//*[@text="去浏览"]').click()
    # d(scrollable=True).scroll.horiz.toBeginning()
    # d(scrollable=True).scroll.toEnd()

    ## 模拟手动滑动
    d.swipe(744, 1558, 15, 463)
    # d.drag(100, 100, 800, 900)  # 从(10, 20)滑动到(80, 90)
    # https://github.com/openatx/uiautomator2/blob/master/QUICK_REFERENCE.md

    time.sleep(19)
    d.press("back")
    time.sleep(2)
    # https://github.com/openatx/uiautomator2/blob/master/QUICK_REFERENCE.md

d.xpath(
    '//android.widget.ListView/android.view.View[4]/android.widget.Button[1]')

time.sleep(18)
d.press("back")
# d.screen_on()

d.info.get('screenOn')
