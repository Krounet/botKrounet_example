It's just a simple set of python programs that interact with an arduino and a twitter bot.

First, you must create a twitter application. For that, check here : https://developer.twitter.com/en.

You must install pySerial and Tweepy packages too.

https://pythonhosted.org/pyserial/

https://www.tweepy.org/

In this application, an Arduino detects when a button is pushed and send a message. A python script recovers this message via a serial communication between the Arduino and a PC. Then, the python script is connected to a bot that tweet a message on twitter.

For the tests, my twitter bot is @BotKrounet

