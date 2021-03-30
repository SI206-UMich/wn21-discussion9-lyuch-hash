from bs4 import BeautifulSoup
import re
import requests
import unittest

# Task 1: Get the URL that links to the Pokemon Charmander's webpage.
# HINT: You will have to add https://pokemondb.net to the URL retrieved using BeautifulSoup
def getCharmanderLink(soup):
    
   tag=soup.find('div', class_='infocard-list infocard-list-pkmn-lg')
    
   tags=tag.findall('span', class_='infocard-lg-data)
   tag_2=tags[3].find('a')['href']
   tag_2='https://pokemondb.net'+tag_2
    
   return tag_2
    
    

# Task 2: Get the details from the box below "Egg moves". Get all the move names and store
#         them into a list. The function should return that list of moves.
def getEggMoves(pokemon):
    lst=list{}
    url = 'https://pokemondb.net/pokedex/'+pokemon
    resp=requests.get(url)
    soup=BeautifulSoup(resp.content,'html.parser')
    tag=soup.find('table',class_='data_table')
    tag_1=tag.find_all('a',class_='ent-name').text.strip()
    
    
    
    
    
    #add code here

# Task 3: Create a regex expression that will find all the times that have these formats: @2pm @5 pm @10am
# Return a list of these times without the '@' symbol. E.g. ['2pm', '5 pm', '10am']
def findLetters(sentences):
    # initialize an empty list
    emptylist=[]

    # define the regular expression
    

    # loop through each sentence or phrase in sentences
    reg="@(\d{1,2}\:[ap]m)"

    # find all the words that match the regular expression in each sentence
    emptylist=sentences.find_all(reg)  

    # loop through the found words and add the words to your empty list
    return emptylist

    #return the list of the last letter of all words that begin or end with a capital letter



def main():
    url = 'https://pokemondb.net/pokedex/national'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    getCharmanderLink(soup)
    getEggMoves('scizor')

class TestAllMethods(unittest.TestCase):
    def setUp(self):
        self.soup = BeautifulSoup(requests.get('https://pokemondb.net/pokedex/national').text, 'html.parser')

    def test_link_Charmander(self):
        self.assertEqual(getCharmanderLink(self.soup), 'https://pokemondb.net/pokedex/charmander')

    def test_egg_moves(self):
        self.assertEqual(getEggMoves('scizor'), ['Counter', 'Defog', 'Feint', 'Night Slash', 'Quick Guard'])

    def test_findLetters(self):
        self.assertEqual(findLetters(['Come eat lunch at 12','there"s a party @2pm', 'practice @7am','nothing']), ['2pm', '7am'])
        self.assertEqual(findLetters(['There is show @12pm if you want to join','I will be there @ 2pm', 'come at @3 pm will be better']), ['12pm', '3 pm'])

if __name__ == "__main__":
    main()
    unittest.main(verbosity = 2)