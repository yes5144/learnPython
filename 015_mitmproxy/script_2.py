from mitmproxy import ctx


def request(url):
    url.request.headers['User-Agent'] = "MitmProxy channel"
    # print(url.request.headers)
    # info()
    # ctx.log.info(str(url.request.headers))
    # warn()
    ctx.log.warn(str(url.request.headers))
    # # error()
    # ctx.log.error(str(url.request.headers))


# def response(flow):
#     print(flow.request.url)
#     myurl = flow.request.url
#     with open("jie_url.txt", "a+") as f:
#         f.write(myurl + "\n")


def response(flow):
    response = flow.response
    info = ctx.log.info
    info("1-- status code: " + str(response.status_code))
    info("2-- headers: " + str(response.headers))
    info("3-- cookies: " + str(response.cookies))
    info("4-- text: " + str(response.text))

    myurl = flow.request.url
    if myurl.startswith("https"):
        with open("jie_url.txt", "a+") as f:
            f.write("----" + myurl + "\n")