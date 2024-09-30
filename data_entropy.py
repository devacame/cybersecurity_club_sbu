from math import log

# Just for fun, Data from https://reusablesec.blogspot.com/2009/05/character-frequency-analysis-info.html
ASCII_FREQUENCY_DATA = {
    ord("a"): 7.52766,
    ord("e"): 7.0925,
    ord("o"): 5.17,
    ord("r"): 4.96032,
    ord("i"): 4.69732,
    ord("s"): 4.61079,
    ord("n"): 4.56899,
    ord("1"): 4.35053,
    ord("t"): 3.87388,
    ord("l"): 3.77728,
    ord("2"): 3.12312,
    ord("m"): 2.99913,
    ord("d"): 2.76401,
    ord("0"): 2.74381,
    ord("c"): 2.57276,
    ord("p"): 2.45578,
    ord("3"): 2.43339,
    ord("h"): 2.41319,
    ord("b"): 2.29145,
    ord("u"): 2.10191,
    ord("k"): 1.96828,
    ord("4"): 1.94265,
    ord("5"): 1.88577,
    ord("g"): 1.85331,
    ord("9"): 1.79558,
    ord("6"): 1.75647,
    ord("8"): 1.66225,
    ord("7"): 1.621,
    ord("y"): 1.52483,
    ord("f"): 1.2476,
    ord("w"): 1.24492,
    ord("j"): 0.836677,
    ord("v"): 0.833626,
    ord("z"): 0.632558,
    ord("x"): 0.573305,
    ord("q"): 0.346119,
    ord("A"): 0.130466,
    ord("S"): 0.108132,
    ord("E"): 0.0970865,
    ord("R"): 0.08476,
    ord("B"): 0.0806715,
    ord("T"): 0.0801223,
    ord("M"): 0.0782306,
    ord("L"): 0.0775594,
    ord("N"): 0.0748134,
    ord("P"): 0.073715,
    ord("O"): 0.0729217,
    ord("I"): 0.070908,
    ord("D"): 0.0698096,
    ord("C"): 0.0660872,
    ord("H"): 0.0544319,
    ord("G"): 0.0497332,
    ord("K"): 0.0460719,
    ord("F"): 0.0417393,
    ord("J"): 0.0363083,
    ord("U"): 0.0350268,
    ord("W"): 0.0320367,
    ord("."): 0.0316706,
    ord("!"): 0.0306942,
    ord("Y"): 0.0255073,
    ord("*"): 0.0241648,
    ord("@"): 0.0238597,
    ord("V"): 0.0235546,
    ord("-"): 0.0197712,
    ord("Z"): 0.0170252,
    ord("Q"): 0.0147064,
    ord("X"): 0.0142182,
    ord("_"): 0.0122655,
    ord("$"): 0.00970255,
    ord("#"): 0.00854313,
    ord(","): 0.00323418,
    ord("/"): 0.00311214,
    ord("+"): 0.00231885,
    ord("?"): 0.00207476,
    ord(";"): 0.00207476,
    ord("^"): 0.00195272,
    ord("\t"): 0.00189169,
    ord("%"): 0.00170863,
    ord("~"): 0.00152556,
    ord("="): 0.00140351,
    ord("&"): 0.00134249,
    ord("`"): 0.00115942,
    ord("\\"): 0.00115942,
    ord(")"): 0.00115942,
    ord("]"): 0.0010984,
    ord("["): 0.0010984,
    ord(":"): 0.000549201,
    ord("<"): 0.000427156,
    ord("("): 0.000427156,
    ord("æ"): 0.000183067,
    ord(">"): 0.000183067,
    ord('"'): 0.000183067,
    ord("ü"): 0.000122045,
    ord("|"): 0.000122045,
    ord("{"): 0.000122045,
    ord("'"): 0.000122045,
    ord("ö"): 6.10223e-05,
    ord("ä"): 6.10223e-05,
    ord("}"): 6.10223e-0,
}
ASCII_ENTROPY = -1 * sum((val/100*log(val/100, 8) for val in ASCII_FREQUENCY_DATA.values()))


def calculateEntropy(hex_data):
    data = int(hex_data, 16)
    data_map: dict[int, int] = {}
    for key in range(256):
        data_map[key] = 0
    length = 0
    while data > 0:
        key = data & 255
        data_map[key] += 1
        data >>= 8
        length += 1
    return -1 * sum(
        (val / length * log(val / length, 8) for val in data_map.values() if val)
    )


def hex_to_text(hex_data):
    # return bytes.fromhex(hex_data)
    data = int(hex_data, 16)
    text = ""
    while data > 0:
        char = data & 255
        text = chr(char) + text
        data >>= 8
    return text
