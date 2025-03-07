import nltk
from nltk import CFG, ChartParser
grammar = CFG.fromstring("""
    S  -> NP VP
    PP -> IN NP
    NP -> DT Noun | NP PP
    VP -> Verb NP | VP PP
    Verb -> 'VB' | 'VBD' | 'VBG' | 'VBN' | 'VBP' | 'VBZ'
    Noun -> 'NN' | 'NNP' | 'NNPS' | 'NNS'
    '$' -> '$'
    ',' -> ','
    '-LRB-' -> '-LRB-'
    '-RRB-' -> '-RRB-'
    '.' -> '.'
    ':' -> ':'
    'CC' -> 'CC'
    'CD' -> 'CD'
    'DT' -> 'DT'
    'EX' -> 'EX'
    'FW' -> 'FW'
    'GW' -> 'GW'
    'HYPH' -> 'HYPH'
    'IN' -> 'IN'
    'JJ' -> 'JJ'
    'JJR' -> 'JJR'
    'JJS' -> 'JJS'
    'MD' -> 'MD'
    'NN' -> 'NN'
    'NNP' -> 'NNP'
    'NNPS' -> 'NNPS'
    'NNS' -> 'NNS'
    'PDT' -> 'PDT'
    'POS' -> 'POS'
    'PRP' -> 'PRP'
    'PRP$' -> 'PRP$'
    'RB' -> 'RB'
    'RBR' -> 'RBR'
    'RBS' -> 'RBS'
    'RP' -> 'RP'
    'TO' -> 'TO'
    'UH' -> 'UH'
    'VB' -> 'VB'
    'VBD' -> 'VBD'
    'VBG' -> 'VBG'
    'VBN' -> 'VBN'
    'VBP' -> 'VBP'
    'VBZ' -> 'VBZ'
    'WDT' -> 'WDT'
    'WP' -> 'WP'
    'WRB' -> 'WRB'
    '``' -> '``'
""")

# Create a parser with the defined CFG
parser = ChartParser(grammar)
def is_grammatically_correct(sentence):
    tokens = sentence.split()
    try:
        for tree in parser.parse(tokens):
            return True
    except nltk.parse.chart.ChartParseError:
        return False
