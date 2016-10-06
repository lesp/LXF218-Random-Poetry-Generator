from gtts import gTTS
import os
import random
start = "y"
try:
    while start == "y":
        accents = [
            "af",
            "sq",
            "ar",
            "hy",
            "bn",
            "ca",
            "zh",
            "zh-cn",
            "zh-tw",
            "zh-yue",
            "hr",
            "cs",
            "da",
            "nl",
            "en",
            "en-au",
            "en-uk",
            "en-us",
            "eo",
            "fi",
            "fr",
            "de",
            "el",
            "hi",
            "hu",
            "is",
            "id",
            "it",
            "ja",
            "ko",
            "la",
            "lv",
            "mk",
            "no",
            "pl",
            "pt-br",
            "ro",
            "ru",
            "sr",
            "sk",
            "es",
            "es-es",
            "es-us",
            "sw",
            "sv",
            "ta",
            "th",
            "tr",
            "vi",
            "cy"
            ]
        accent = random.choice(accents)
        print("We are using",accent,"accent")
        words = []
        for i in range(6):
            words.append(str(input("Type in a funny word >> ")))
        random.shuffle(words)
        print(words)

        phrases = [
            " It is lovely to see that there are ",
            " flowering in the breeze ",
            " and that their life is filled with ease ",
            " Say you space cowboy ",
            " In this world of wonder ",
            " where is my mind? "
            ]

        random.shuffle(phrases)
        print(phrases)

        poem = phrases[0]+words[0]+phrases[1]+words[1]+phrases[2]+words[2]+phrases[3]+words[3]+phrases[4]+words[4]+phrases[5]+words[5]

        tts = gTTS(text=poem, lang=accent)
        print("============")
        print("What filename would you like to give your poem?")
        filename = str(input("Please name your file and press ENTER >> "))
        filename = filename+".mp3"
        print(filename)
        tts.save(filename)
        cmd = "mpg321 "+filename
        os.system(cmd)
        print("Would you like to write another poem?")
        answer = str(input("Please answer y or n "))
        if answer == "n":
            start = "n"
            print("Ok, thanks for playing")
        else:
            print("Here we go again!")
except KeyboardInterrupt:
    print("EXIT")
