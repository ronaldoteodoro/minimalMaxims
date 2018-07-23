from Foundation import NSUserNotification
from Foundation import NSUserNotificationCenter
from Foundation import NSUserNotificationDefaultSoundName
from optparse import OptionParser
from bs4 import BeautifulSoup
import requests


def main():
    response = requests.get('https://minimalmaxims.com/')
    search_html = response.text
    soup = BeautifulSoup(search_html, 'html.parser')
    text = soup.find(class_="quotable-quote")
    rawQuote = text.find('p')
    quote = rawQuote.text.strip()
    parser = OptionParser(usage='%prog -t TITLE -m MESSAGE')
    parser.add_option('-t', '--title', action='store', default='Minimal Maxims')
    parser.add_option('-m', '--message', action='store', default= quote )
    parser.add_option('--no-sound', action='store_false', default=True,dest='sound')

    options, args = parser.parse_args()

    notification = NSUserNotification.alloc().init()
    notification.setTitle_(options.title)
    notification.setInformativeText_(options.message)
    if options.sound:
        notification.setSoundName_(NSUserNotificationDefaultSoundName)

    center = NSUserNotificationCenter.defaultUserNotificationCenter()
    center.deliverNotification_(notification)

if __name__ == '__main__':
    main()
