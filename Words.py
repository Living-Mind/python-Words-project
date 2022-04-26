from bs4 import BeautifulSoup
import requests

print('Добре дошли в Думинатор')

def All():
    word = input('\nНапишете думата, която търсите: ')
    print("-----------------------------------------")

    headers = {'User-Agent': 'Mozilla/5.0'}
    websitesTuple = ('https://slovored.com/search/all/' + word, 'https://rechnik.chitanka.info/w/' + word)

    outputSlovored = requests.get(websitesTuple[0], headers=headers).text
    formatWebsite1 = BeautifulSoup(outputSlovored, 'html.parser')

    outputRechnik = requests.get(websitesTuple[1], headers=headers).text
    formatWebsite2 = BeautifulSoup(outputRechnik, 'html.parser')

    def Prevod_function():
        slovoredBgToEng = formatWebsite1.div.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.table.tr.td.next_sibling.b
        print('\nПревод на английски: ' + slovoredBgToEng.string)
        print("-----------------------------------------")

    def Slovored_function():
        print('\nДумата не бе намерена в тълковеня речник.\n\nРезултат от Словоред:')

        unsolicitedTags = formatWebsite1.findAll(('b','br'))
        for match in unsolicitedTags:
            match.decompose()

        sectionOutputSlovored = formatWebsite1.div.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.table.tr.td.next_sibling  
        for string in sectionOutputSlovored.stripped_strings:
            print(string.replace(")","").replace("(","").replace(". 1.","1. ").replace("Търсената дума е намерена","------------------------------"))

    unsolicitedTags2 = formatWebsite2.findAll(('i','abbr'))
    for match in unsolicitedTags2:
        match.decompose()

    try:
        sectionOutputRechnik = formatWebsite2.div.next_sibling.next_sibling.h1.next_sibling.next_sibling.next_sibling.next_sibling.h2.next_sibling.next_sibling
        for string in sectionOutputRechnik.stripped_strings:
            print(string)
        Prevod_function()
    except:
        try:
            Prevod_function()
            Slovored_function()
        except:
            Slovored_function()

    print("\nИзбор на опция:\n1) Отново търсене на дума\n2) Изход")

    Options = int(input("Посочете номер на опция: "))
    if Options == 1:
        All()
    elif Options == 2:
        raise SystemExit
    else:
        print("Няма такава опция.")
All()
