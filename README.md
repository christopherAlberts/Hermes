# Hermes
A message bot worthy of the gods!

![](Images/HermesBanner.png)

This bot makes use of the Telegram API, it is however designed to work a bit unconventunaly...

## How It Works

The idea behind this bot was not to make a bot with a template reply. But rather one that that can interact with your programs, whatever they might be. This is done through means of an *exschange*. When a message is sent through. Hermes will determine which PO.Box in the exchange it should go to. It will then take the message to the *"From_Hermes"* folder in the PO.Box. The idea it that what ever program you are interacting with, will monitor the *"From_Hermes"* folder. Once a message comes throught the program will execute the command and return to output to the *"To_Hermes"* folder, at which point Hermes will take the output and use it as the responce to the original message sent.

The Beauty of this setup is that Hermes can interact with any program written in any languge, be it python, java, C# , C++ or even .bat scripts. Below is a diagram illestrating how this process works.

![](Images/Hermes_Workflow.png)




## Try It Out

The Hermes messanger bot makes use of the pyTelegramBorAPI libary. Inoder for this program to work you'll need to install the required packages. You can use the following link to find out how to do this:   https://github.com/eternnoir/pyTelegramBotAPI


There is no limit to the number of programs Hermes can interact with. Just mack sure you create the PO.Box file directories and refrince them accrodingly in the config file:

```
Hermes_Bot_Token:
982gkjh28746u42hraodsmcnB87345gjhg7347
Hermes Chat History File:
C:\Users\zeus\OneDrive\Codes\Python\scr\HermesChatHistory.txt
Hermes 2 Exchange:
C:\Users\zeus\OneDrive\Codes\Python\scr\Exchange\POBox0\From_Hermes
C:\Users\zeus\OneDrive\Codes\Python\scr\Exchange\POBox1\From_Hermes
C:\Users\zeus\OneDrive\Codes\Python\scr\Exchange\POBox2\From_Hermes
C:\Users\zeus\OneDrive\Codes\Python\scr\Exchange\POBox3\From_Hermes
Exchange 2 Hermes:
C:\Users\zeus\OneDrive\Codes\Python\scr\Exchange\POBox0\To_Hermes
C:\Users\zeus\OneDrive\Codes\Python\scr\Exchange\POBox1\To_Hermes
C:\Users\zeus\OneDrive\Codes\Python\scr\Exchange\POBox2\To_Hermes
C:\Users\zeus\OneDrive\Codes\Python\scr\Exchange\POBox3\To_Hermes
End of Config
```

![](Images/pythonpoweredlengthgif.gif)
