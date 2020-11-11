import time
import uiautomator2 as u2
# https://github.com/openatx/uiautomator2/blob/master/QUICK_REFERENCE.md

d = u2.connect()  # connect to device
print(d.info)

d.press("home")

d.app_start("com.jingdong.app.mall", stop=True)
time.sleep(3)

d.xpath(
    '//*[@content-desc="NewAppcenter"]/android.widget.RelativeLayout[4]/android.widget.ImageView[1]'
).click()

# d.xpath('//*[@resource-id="com.jingdong.app.mall:id/g4"]').click()

## 收集水滴
for i in range(21):
    print(i, '==' * 30)
    d.click(0.84, 0.738)
    time.sleep(4)

# d.click(0.269, 0.739)

# for i in (9):
#     d.click(0.829, 0.684)

#     time.sleep(7)

#     d.press("back")
#     d.click(0.816, 0.687)
