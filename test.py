#-*- coding:utf-8 -*-
from qqbot import QQBotSlot  as qqbotslot, RunBot
import learn
import info
import tulingApi

@qqbotslot
def onQQMessage(bot,contact,member,content):
    if content=='-intro':
        bot.SendTo(contact,'大家好，我是交大志愿填报助手，欢迎向我咨询有关消息')
    if content=='-stop':
        bot.SendTo(contact,'我还会回来的')
        bot.Stop()
    if content=='-restart':
        bot.Restart()
    if content=='--info':
        bot.SendTo(contact,info.information)
    if content.startswith('-learn '):
        learn.learnListAppend(bot, contact, content)
    if '@ME' in content:
        t = tulingApi.TulingAPI()
        bot.SendTo(contact,t.get_turing_text(content))
    if getattr(member, 'uin', None) != bot.conf.qq:
        learn.learnProcess(bot, contact, content)

if __name__=='__main__':
    RunBot()