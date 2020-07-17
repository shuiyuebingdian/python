import json
import os
import time

import requests
import urllib3

courseUrl = "https://www.magikid.com/api/Challenge/ChallengeUnits"
unitUrl = "https://www.magikid.com/api/Challenge/UnitList"
challengeUrl = "https://www.magikid.com/api/Challenge/ChallengeInfo"
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "cookie": "Hm_lvt_72ded40e4302dfa9c1f46f09728ef094=1562580298,1565159256; WeChatOpenId=oi6sowrhx4Vjm0L-Ihyqabdusq_k; TimeZone=Asia%2FShanghai; lang=cn; ShowAccountSwitchTips=1; ExpireBarClose=0; DailyCheckTime=2020-7-13; jwt_production_info=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVaWQiOiIxMTAxMDUwNSIsIlVzZXJOYW1lIjoiamFzb25cdTY3NGVcdTZmNDdcdTgyN2EiLCJOYW1lIjoiamFzb25cdTY3NGVcdTZmNDdcdTgyN2EiLCJFbWFpbCI6IiIsIlBhcmVudEVtYWlsIjoiIiwiSXNBY3RpdmUiOiIxIiwiTGFzdExvZ2luIjoiMjAyMC0wNy0xMyAwOToxNTo1NiIsIkRhdGVKb2luZWQiOiIyMDIwLTA1LTExIDExOjI0OjAwIiwiQWNjb3VudFR5cGUiOiIwIiwiSXNDaGlsZCI6IjEiLCJBdmF0YXJVcmwiOiJodHRwczpcL1wvbWFnaWtpZHdlYi5zMy11cy13ZXN0LTEuYW1hem9uYXdzLmNvbVwvYXZhdGFyXC84LmpwZyIsIk9yaWdpbmFsQXZhdGFyIjoiIiwiTGFyZ2VBdmF0YXIiOiIiLCJCaXJ0aGRheSI6IjIwMDktMDgtMDEiLCJDcm93biI6IjcwIiwiR2lmdCI6IjAiLCJUaWNrZXQiOiIwIiwiTWVtYmVyc2hpcFRpbWUiOiIwIiwiRnJlZVRyaWFsRXhwaXJlVGltZSI6IjE1OTYxNTM1OTkiLCJQaG9uZUZyZWVUcmlhbEV4cGlyZVRpbWUiOiIwMDAwLTAwLTAwIDAwOjAwOjAwIiwiTGV2ZWwiOiIwIiwiSXNTdGFmZiI6IjAiLCJDYW5VcGxvYWRBcnR3b3JrIjoiMCIsIklzRGVsZXRlZCI6IjAiLCJDb3VudHJ5IjoiIiwiU2Nob29sIjoiIiwiTm90ZSI6IiIsIkludHJvIjoiIiwiVGhlbWUiOiIiLCJQaG9uZU51bWJlciI6IiIsIkxhYklkIjoiMCIsIkxhYlRlYWNoZXJIaWRlIjoiMCIsIk9yZGVySW54IjoiMCIsIkVtZXJnZUNvbnRhY3QiOiIiLCJXZUNoYXRVbmlvbklkIjoiIiwiV2VDaGF0T3BlbklkIjoiIiwiR2VuZGVyIjoiMCIsIkNpdHkiOiIiLCJQcm92aW5jZSI6IiIsIkRldmljZUlkIjoiIiwiVFZEZXZpY2VJZCI6IiIsIkJlYW5OdW0iOiIwIiwiR29sZENvaW4iOiIwIiwiSXNTdWJzY3JpYmUiOiIwIiwiTmVlZENoYW5nZVVzZXJOYW1lIjoiMCIsIlVzZXJQb3J0cmFpdFJpZ2h0IjoiMCIsIlVzZXJBZ3JlZW1lbnQiOiIiLCJBZ2UiOiIxMCIsIklzTWVtYmVyIjpmYWxzZSwiSXNJbkZyZWVUcmlhbCI6dHJ1ZSwiQmVsb25nTGFicyI6W3siVWlkIjoiMTEwMTA1MDUiLCJMYWJJZCI6IjIzIiwiTGFiTmFtZSI6IlNoYW5naGFpIFpoYW5namlhbmcgTGFiIChIUSkiLCJMYWJOYW1lQ24iOiJcdTRlMGFcdTZkNzdcdTVmMjBcdTZjNWZcdTViOWVcdTlhOGNcdTViYTQoXHU2MDNiXHU5MGU4KSIsIlNsdWciOiJzaGFuZ2hhaSJ9XSwiTm9MYWJOb3ciOjAsIlVzZXJTdGF0aXN0aWNzIjp7IkNsYXNzTnVtIjoiMTIiLCJXcml0aW5nTnVtIjoiMCIsIkhvbWV3b3JrTnVtIjoiMjMiLCJSZWFkaW5nTnVtIjowLCJQcm9jZXNzTnVtIjoxLCJGYXZvcml0ZXNOdW0iOjAsIkFzc2lnbm1lbnROdW0iOiIzMCJ9LCJVc2VyS2lkcyI6W10sIlBhcmVudFVzZXJFbWFpbCI6IiIsIkpXVEV4cGlyZVRpbWUiOjE1OTQ2MzMwMDd9; jwt_production_sign=VtfbW4Jkvs7i3U1HLvPrtsTeFPB1gcyyRhYpe6X4cw0"
}
courseData = "type=31&ageid=3&condition=%7B%22sort%22%3A%22units%22%2C%22keyword%22%3A%22%22%2C%22format%22%3A%22%22%2C%22age%22%3A0%2C%22CatagoryId%22%3A0%2C%22WriteType%22%3A0%2C%22lang%22%3A%22cn%22%7D"
response = requests.post(courseUrl, data=courseData, headers=headers)
jsonRes = json.loads(response.text)

unitList = jsonRes.get("result").get("data")


for unit in unitList:
    unitId = unit.get("UnitId")
    unitData = "id=" + unitId + "&ageid=3"
    unitRes = requests.post(unitUrl, data=unitData, headers=headers)
    jsonUnitRes = json.loads(unitRes.text)
    challengeList = jsonUnitRes.get("result").get("data")
    unitName = jsonUnitRes.get("result").get("unit").get("Title").replace(" ", "")
    for challenge in challengeList:
        challengeData = "id=" + challenge.get("ChallengeId") + "&labreservationid=0&ageid=3"
        challengeRes = requests.post(challengeUrl, data=challengeData, headers=headers)
        jsonChallengeRes = json.loads(challengeRes.text)
        challengeInfo = jsonChallengeRes.get("result").get("data")
        videoUrl = challengeInfo.get("VideoUrl")
        title = challengeInfo.get("Title").replace(" ", "")
        print(videoUrl)

        filePath = "D:/yan/magikid/" + unitName
        if not os.path.exists(filePath):
            os.mkdir(filePath)
        if not os.path.exists(filePath + "/" + title + ".mp4"):
            # 初始下载大小为0
            downsize = 0
            # 获取开始下载前的时间戳
            startTime = time.time()
            # 开始下载文件
            r = requests.get(videoUrl, stream=True)
            total = len(r.content) / 1024 / 1024
            with open(filePath + "/" + title + ".mp4", "wb") as code:
                for chunk in r.iter_content(chunk_size=1000):
                    if chunk:
                        code.write(chunk)
                        downsize += len(chunk)
                        line = 'downloading %d KB/s - %.2f MB， 共 %.2f MB'
                        line = line % (downsize / 1024 / (time.time() - startTime), downsize / 1024 / 1024, total)
                        print(line)
            print("download done")
