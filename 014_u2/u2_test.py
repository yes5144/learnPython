import uiautomator2 as u2
d = u2.connect('192.168.1.112')
print(d.info)
print("==" * 60)
d(text="QQ").click()
d(text="登录").click()
# d(text=u"QQ号/手机号/邮箱").set_text("1922820882")
d(resourceId="com.tencent.mobileqq:id/em2").set_text('xkxkxk')
d(resourceId="com.tencent.mobileqq:id/password").set_text('xkxkxk')
d(resourceId="com.tencent.mobileqq:id/login").click()
d(text="动态").click()
d(text="好友动态").click()
d(description=u"说说,").click()
d(resourceId="com.tencent.mobileqq:id/name", text=u"分享新鲜事…").click()
d(resourceId="com.tencent.mobileqq:id/name",
  text=u"分享新鲜事...").set_text("Hello ")
d(resourceId="com.tencent.mobileqq:id/ivTitleBtnRightText").click()
d(resourceId="com.tencent.mobileqq:id/ivTitleBtnLeft").click()
d(resourceId="com.tencent.mobileqq:id/ivTitleBtnLeft").click()

# 作者：人生苦短丨我爱python
# 链接：https://www.jianshu.com/p/bab443ceba3a
# 来源：简书
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。