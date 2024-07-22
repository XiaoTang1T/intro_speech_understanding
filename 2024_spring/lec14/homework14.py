import datetime
import gtts
import random

def what_time_is_it(lang, filename):
    '''
    Tell me what time it is.
    
    Parameters:
    lang (str) - language in which to speak
    filename (str) - the filename into which the audio should be recorded
    '''
    # 获取当前时间
    (date, time) = datetime.datetime.now().isoformat().split("T")
    (hour, minutes, seconds) = time.split(":")
    
    # 根据语言设置不同的文本
    if lang == "en":
        text = f"{hour} hours and {minutes} minutes"
    elif lang == "ja":
        text = f"{hour}時{minutes}分です"
    elif lang == "zh":
        text = f"现在是{hour}点{minutes}分"
    else:
        text = "I'm sorry, I don't know that language"
    
    # 使用 gtts 生成语音文件
    gtts.gTTS(text, lang=lang).save(filename)
    
def tell_me_a_joke(lang, audiofile):
    '''
    Tell me a joke.
    
    Parameters:
    lang (str) - language
    audiofile (str) - audio file in which to record the joke
    '''
    filename = f'jokes_{lang}.txt'
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            jokes = f.readlines()
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return
    except UnicodeDecodeError:
        print("Error reading the joke file. Please check the file encoding.")
        return
    
    joke = random.choice(jokes)
    print(joke.strip())
    
    # 使用 gtts 生成语音文件
    gtts.gTTS(joke.strip(), lang=lang).save(audiofile)

def what_day_is_it(lang, audiofile):
    '''
    Tell me what day it is.

    Parameters:
    lang (str) - language in which to record the date
    audiofile (str) - filename in which to read the date
    
    Returns:
    url (str) - URL that you can look up in order to see the calendar for this month and year
    '''
    today = datetime.date.today()
    year = today.year
    month = today.month
    day = today.day
    weekday = today.isoweekday()
    
    # 根据语言设置不同的文本
    if lang == "en":
        weekdays = ['', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        months = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        text = f"{weekdays[weekday]}, {months[month]} {day}, {year}"
        gtts.gTTS("Today is " + text, lang="en").save(audiofile)
    elif lang == "ja":
        weekdays = ' 月火水木金土日'
        text = f"{weekdays[weekday]}曜日,{month}月{day}日, {year}年"
        gtts.gTTS("今日は" + text, lang="ja").save(audiofile)
    elif lang == "zh":
        weekdays = ['', '周一', '周二', '周三', '周四', '周五', '周六', '星期日']
        text = f'{weekdays[weekday]}, {month}月{day}日, {year}年'
        gtts.gTTS("今天是" + text, lang="zh").save(audiofile)
    else:
        print("I'm sorry, I don't know that language")
        return

def personal_assistant(lang, filename):
    '''
    Listen to the user, and respond to one of three types of requests:
    What time is it?
    What day is it?
    Tell me a joke!
    
    Parameters:
    lang (str) - language
    filename (str) - filename in which to store the result
    '''
    if lang == "en":
        keywords = ["what time", "joke", "what day", "I'm sorry, I didn't understand you"]
    elif lang == "ja":
        keywords = ["何時", "冗談", "何日", "すみません、よくわかりませんでした"]
    elif lang == "zh":
        keywords = ["几点", "玩笑", "什么日子", "对不起，我没听懂你的话"]
    else:
        print("I don't know that language!")
        return
    
    text = input("What would you like me to do?").strip().lower()
    
    print("I heard", text)
    if keywords[0] in text:
        what_time_is_it(lang, filename)
    elif keywords[1] in text:
        tell_me_a_joke(lang, filename)
    elif keywords[2] in text:
        what_day_is_it(lang, filename)
    else:
        print(keywords[3])
        print('I will try again')
