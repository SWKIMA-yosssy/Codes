#ランダム機能を使うことをPythonに知らせるために、
# randomモジュールをインポートする
import random
#3つのリストを作成する。動詞のリスト、形容詞のリスト、
#そして名詞のリスト
verbs = ['Leverage', 'Sync', 'Target' , 'Gamify', 'Offline',
         'Crowd-sourced', '24/7', 'Lean-in', '30,000 foot']
adjectives = ['A/B Tested', 'Freemium', 'Hyperlocal', 'Siloed', 'B-to-B', 'Oriented',
              'Cloud-based', 'API-based']
nouns = ['Early Adopter', 'Low-hanging Fruit', 'Pipeline', 'Splash page', 'Productivity',
          'Process', 'Tipping Point', 'Paradigm']
verb = random.choice(verbs)
adjective = random.choice(adjectives)
noun = random.choice(nouns)
phrase = verb + ' ' + adjective + ' ' + noun
print(phrase)
