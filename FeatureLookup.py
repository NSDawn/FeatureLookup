# FeatureLookup.py
# Nishant Suria

# - - - - - - - - - - - - - - - - - - - 

# data declaration
data = {
    "i": "+-++-+0--+------0000++-+-+",
    "y": "+-++-+0--+--++--0000++-+-+",
    "ɨ": "+-++-+0--+------0000++---+",
    "ʉ": "+-++-+0--+--++--0000++---+",
    "ɯ": "+-++-+0--+------0000++--++",
    "u": "+-++-+0--+--++--0000++--++",
    "ɪ": "+-++-+0--+------0000++-+--",
    "ʏ": "+-++-+0--+--++--0000++-+--",
    "ʊ": "+-++-+0--+--++--0000++--+-",
    "e": "+-++-+0--+------0000+--+-+",
    "ø": "+-++-+0--+--++--0000+--+-+",
    "ɘ": "+-++-+0--+------0000+----+",
    "ɵ": "+-++-+0--+--++--0000+----+",
    "ɤ": "+-++-+0--+------0000+---++",
    "o": "+-++-+0--+--++--0000+---++",
    "ɛ": "+-++-+0--+------0000+--+--",
    "œ": "+-++-+0--+--++--0000+--+--",
    "ə": "+-++-+0--+------0000+-----",
    "ɞ": "+-++-+0--+--++--0000+-----",
    "ʌ": "+-++-+0--+------0000+---+-",
    "ɔ": "+-++-+0--+--++--0000+---+-",
    "æ": "+-++-+0--+------0000+-++-0",
    "ɶ": "+-++-+0--+--++--0000+-++-0",
    "a": "+-++-+0--+------0000+-+--0",
    "ɑ": "+-++-+0--+------0000+-+-+0",
    "ɒ": "+-++-+0--+--++--0000+-+-+0",

    "j": "--++-+0--+------000-++-+-+",
    "ʋ": "--++-+0--+--+-+-000--00000",
    "ɥ": "--++-+0--+--++--000-++-+-+",
    "w": "--++-+0--+--++--000-++--++",

    "ʙ": "-+++-+0+-+--+---000--00000",
    "l": "-+++-+0--+-----++--+-00000",
    "r": "-+++-+0+-+-----++----00000",
    "ɾ": "-+++-+0-++-----++----00000",
    "ɹ": "--++-+0--+-----+-+---00000",
    "ʎ": "-+++-+0--+-----+-+-+++-+-0",
    "ʟ": "-+++-+0--+------000+++-000",
    "ʀ": "-+++-+0+-+------000-+---+0",
    "m": "-+-++-0--+--+---000--00000",
    "ɱ": "-+-++-0--+--+-+-000--00000",
    "n": "-+-++-0--+-----++----00000",
    "ɳ": "-+-++-0--+-----+-----00000",
    "ɲ": "-+-++-0--+-----+-+--++-+-0",
    "ŋ": "-+-++-0--+------000-++-000",
    "ɴ": "-+-++-0--+------000-+---+0",

    "p": "-+----------+---000--00000",
    "b": "-+-------+--+---000--00000",
    "ɸ": "-+---++-----+---000--00000",
    "β": "-+---++--+--+---000--00000",
    "f": "-+---++-----+-+-000--00000",
    "v": "-+---++--+--+-+-000--00000",

    "θ": "-+---++--------+++---00000",
    "ð": "-+---++--+-----+++---00000",
    "t": "-+-------------++----00000",
    "d": "-+-------+-----++----00000",
    "s": "-+---++--------++-+--00000",
    "z": "-+---++--+-----++-+--00000",
    "ʃ": "-+---++--------+-++--00000",
    "ʒ": "-+---++--+-----+-++--00000",

    "ts":"-+----+--------++-+--00000",
    "dz":"-+----+--+-----++-+--00000",
    "tʃ":"-+----+--------+-++--00000",
    "dʒ":"-+----+--+-----+-++--00000",

    "c": "-+-------------+-+--++-+-0",
    "ɟ": "-+-------+-----+-+--++-+-0",
    "ç": "-+---++--------+-+--++-+-0",
    "ʝ": "-+---++--+-----+-+--++-+-0",

    "k": "-+--------------000-++-000",
    "g": "-+-------+------000-++-000",
    "x": "-+---++---------000-++-000",
    "ɣ": "-+---++--+------000-++-000",
    "q": "-+--------------000-+---+0",
    "ɢ": "-+-------+------000-+---+0",
    "χ": "-+---++---------000-+---+0",
    "ʁ": "-+---++--+------000-+---+0",

    "ħ": "-+---++---------000-+-+-+0",
    "ʕ": "-+---++--+------000-+-+-+0",

    "h": "-----++---+-----000--00000",
    "ɦ": "-----++--++-----000--00000",
    "ʔ": "-+---------+----000--00000", 
}

features = [
"syllabic", "consonantal", "approximant", "sonorant", 
"nasal", "continuant", "delayed", "trill", "tap",
"voice", "spr.gl", "constr.gl",
"labial", "round", "labiodental", "coronal", "anterior", "distributed", "strident",
"lateral", "dorsal", 
"high", "low", "front", "back", "tense",
]


# - - - - - - - - - - - - - - - - - - - 

# fn that converts the string data declared into referenceable dictionaries
def dict_convert(in_string) :

    dict_entry = {}
    assert len(in_string) == len(features)
    for e in range(len(in_string)) :
        dict_entry[features[e]] = in_string[e]

    return dict_entry

# fn that prints dicts
def dict_print(in_dict) :
    for key in in_dict :
        print(key + ": [" + in_dict[key] + "]")

# - - - - - - - - - - - - - - - - - - - 

# fn init
def init() :
    for key in data :
        data[key] = dict_convert(data[key])
    print("Welcome to FeatureLookup.py.")
    print("Type <help> for help.")

# fn main
def main() :
    init()
    
    on = True
    while on :
        cmd = input("\n> ").strip().split(" ")

        if cmd[0] == "end" :
            print("FeatureLookup.py terminated.\n")
            on = False
        elif cmd[0] == "help" :
            print("This program is a translation of the PHONOLOGICAL FEATURES CHART (vers. 2015-2, based on Hayes 2009), for ease of use.")
            print("- - - - - - - - -")
            print("This program includes 4 functions, as follows:\n")
            print("The <list> function lists all items of a given type.\nUsage: list\n       list <phoneme>\n       list <feature> <+/-/0>\n")
            print("The <compare> function lists the similar features of two phonemes. \nUsage: compare <phoneme1> <phomeme2>\n")
            print("The <contrast> function lists the different features of two phonemes. \nUsage: contrast <phoneme1> <phomeme2>\n")
            print("The <end> function terminates the program.\nUsage: end")
            print("- - - - - - - - -")
            print("This program covers the basic phonemes provided by the chart, and does not include diacritics.")
            print("Type <list> for a list of all phonemes in this program's dictionary.")
        elif cmd[0] == "list" : 
            if len(cmd) == 1 :
                i = 0
                for entry in data :
                    i += 1 
                    print("{0:<4}".format(entry), end = (" " if i % 8 != 0 else "\n"))
                if i % 8 != 0 :
                    print("")
            elif len(cmd) == 2:
                if cmd[1] in data :
                    dict_print (data[cmd[1]])
                else :
                    print("Feature value must be specified as +, -, or 0." if cmd[1] in features else "Phoneme <" + cmd[1] + "> not found.")
                    print("Usage: list\n       list <phoneme>\n       list <feature> <+/-/0>")
            elif len(cmd) == 3 :
                if cmd[1] in features :
                    if cmd[2] in ["+", "-", "0"] :
                        i = 0
                        for entry in data : 
                            if data[entry][cmd[1]] == cmd[2] :
                                i += 1
                                print("{0:<4}".format(entry), end = (" " if i % 8 != 0 else "\n"))
                        if i % 8 != 0 :
                            print("")
                        if i == 0 : 
                            print("No phoneme with the given feature was found.")
                    else : 
                        print("Feature value must be +, -, or 0.")
                        print("Usage: list\n       list <phoneme>\n       list <feature> <+/-/0>")  
                else :
                    print("Feature <" + cmd[1] + "> not found.")
                    print("Usage: list\n       list <phoneme>\n       list <feature> <+/-/0>")  
            else : 
                print("Usage: list\n       list <phoneme>\n       list <feature> <+/-/0>")
        elif cmd[0] in ["compare", "com"] :
            if len(cmd) == 3 :
                if cmd[1] in data and cmd[2] in data : 
                    compare_dict = {}
                    for entry in data[cmd[1]] :
                        if data[cmd[1]][entry] ==  data[cmd[2]][entry] :
                            compare_dict[entry] = data[cmd[1]][entry]
                    if len(compare_dict) == 0 :
                        print("No similarities were found.")
                    else :
                        dict_print(compare_dict)
                else : 
                    print("Phonemes not found or invalid.")
                    print("Usage: compare <phoneme1> <phomeme2>")
            else : 
                print("Usage: compare <phoneme1> <phomeme2>")
        elif cmd[0] in ["contrast", "con"] :
            if len(cmd) == 3 :
                if cmd[1] in data and cmd[2] in data : 
                    contrast_dict = {}
                    for entry in data[cmd[1]] :
                        if data[cmd[1]][entry] !=  data[cmd[2]][entry] :
                            contrast_dict[entry] = data[cmd[1]][entry] + "/" + data[cmd[2]][entry]
                    if len(contrast_dict) == 0 :
                        print("No differences were found.")
                    else :
                        dict_print(contrast_dict)
                else : 
                    print("Phonemes not found or invalid.")
                    print("Usage: contrast <phoneme1> <phomeme2>")
            else : 
                print("Usage: contrast <phoneme1> <phomeme2>")
        elif cmd[0] == "" : 
            pass
        else :
            print("Command <" + cmd[0] + "> not understood.")

# - - - - - - - - - - - - - - - - - - - 

if __name__ == '__main__' :
    main()
