# this is the regex python import not a download so were chillin
import re

# evil ahh regex got help from our friend for this one basically it filters the java code and isolates each type
TOKEN_PATTERNS = [
    ("COMMENT",     r'/\*[\s\S]*?\*/|//.*'),
    ("FLOAT",       r'\d+\.\d+'),
    ("INTEGER",     r'\d+'),
    ("STRING",      r'"[^"]*"'),
    ("CHAR",        r"'[^'\\]'|'\\.'"),
    ("TYPE",        r'\b(byte|short|int|long|float|boolean|char|String)\b'),
    ("KEYWORD",     r'\b(if|else|while|for|return|void|public|static|double|main)\b'),
    ("IDENTIFIER",  r'[A-Za-z_]\w*'),
    ("OPERATOR",    r'==|!=|<=|>=|&&|\|\||[+\-*/=<>!]'),
    ("DELIMITER",   r'[;,(){}[\].]'),
    ("UNKNOWN",     r'\S+'),
]

# combines all of the token patterns
MASTER = re.compile('|'.join(f'(?P<{n}>{p})' for n, p in TOKEN_PATTERNS))

# list of known class types couldnt find a better way to differentiate variables and classes ask about this tmr if you can
CLASSES = {"System", "Scanner", "Math", "Random", "Arrays", "ArrayList",
                 "HashMap", "StringBuilder", "Integer", "Double", "Boolean"}

# gets the file and converts it into its tokens
def tokenize(filepath):
    # opens file its dependent on filepath so user input can be wierd
    with open(filepath, 'r') as f:
        source = f.read()

    tokens = []

    # scans the source and returns each match one at a time
    for match in MASTER.finditer(source):
        # tells us which pattern matched
        token_type = match.lastgroup
        
        # group() gives us the actual text that was matched
        token_value = match.group()
        
        # skip comments 
        if token_type != "COMMENT":
            tokens.append((token_type, token_value))
    return tokens

# this is the main printer only run this code for debugging (named poorly cause im a chud) 
def main_printer(filepath):
    # inital print for sorting the <20 just adds spaces in between
    print(f"{'LEXEME':<20} TOKEN")

    # speaks for itself is just the prints based on our tokens
    for kind, value in tokenize(filepath):
        if kind == "KEYWORD" or kind == "DELIMITER" or kind == "OPERATOR":
            print(f"{value:<20} {value}")
        elif kind == "TYPE":
            print(f"{value:<20} type")
        elif kind == "IDENTIFIER":
            if value in CLASSES:
                print(f"{value:<20} Class")
            else:
                print(f"{value:<20} var")
        elif kind == "INTEGER":
            print(f"{value:<20} intNum")
        elif kind == "FLOAT":
            print(f"{value:<20} doubleNum")
        elif kind == "STRING" or kind == "CHAR":
            print(f"{value:<20} literal")
        else:
            print(f"{value:<20} {kind}")

# this is the output that DR Atici expcets (I think) so run this
def other_printer(filepath):
    for kind, value in tokenize(filepath):
        if kind == "KEYWORD" or kind == "DELIMITER" or kind == "OPERATOR":
            print(f"{value}", end=" ")
        elif kind == "TYPE":
            print(f"type", end=" ")
        elif kind == "IDENTIFIER":
            if value in CLASSES:
                print(f"Class", end=" ")
            else:
                print(f"var", end=" ")
        elif kind == "INTEGER":
            print(f"intNum", end=" ")
        elif kind == "FLOAT":
            print(f"doubleNum", end=" ")
        elif kind == "STRING" or kind == "CHAR":
            print(f"literal", end=" ")
        else:
            print(f"{kind}", end=" ")


# gets input as a test just run Sample.java
while True:
    run = input("Please enter a file path: ")
    try:
        main_printer(run)
        # other_printer(run)
        break
    except (FileNotFoundError, OSError):
        print("Enter proper file path")

"""
Also I (claude) made a list of java programs to run as tests and they are in here as well they do NOT compile but thats fine 

"""
