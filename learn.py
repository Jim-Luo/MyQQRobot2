#-*- coding:utf-8 -*-
import re
import time
learnList={


}

def learnProcess(bot, contact, content):
    for label,reply in learnList.items():
        if re.search(re.compile(label),content):
            for term in learnList[label]:
                bot.SendTo(contact,term)
                time.sleep(0.5)

def learnListAppend(bot, contact, content):
    try:
        contentList=content.split(' ')
        rawContentList = contentList[2:]
        learnList[contentList[1]] = rawContentList
    except:
        bot.SendTo(contact,'额，你说啥？')
    else:
        bot.SendTo(contact,'学习了')
