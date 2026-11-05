import argparse

parser = argparse.ArgumentParser()
parser.add_argument("part", type=int,
                    help='first number')
parser.add_argument("base", type=int,
                    help='second number')
args = parser.parse_args()

def calculate(part,base):
    if base != 0:
        result = part * 100 / base
        return result
    else:
        return None

def output(part,base,result):
    if result != None:
        print()
        print("  ▒█▀▄▒██▀▒█▀▄░▄▀▀▒██▀░█▄░█░▀█▀▒▄▀▄░▄▀▒▒██▀ ")
        print("  ░█▀▒░█▄▄░█▀▄░▀▄▄░█▄▄░█▒▀█░▒█▒░█▀█░▀▄█░█▄▄ ")
        print()

        print(f" ● {result} %")
        print(f" ◉ Part | {part}")
        print(f" ◉ Base | {base}")
        print()
    else:
        print()
        print("  ▒█▀▄▒██▀▒█▀▄░▄▀▀▒██▀░█▄░█░▀█▀▒▄▀▄░▄▀▒▒██▀ ")
        print("  ░█▀▒░█▄▄░█▀▄░▀▄▄░█▄▄░█▒▀█░▒█▒░█▀█░▀▄█░█▄▄ ")
        print()
        print("  ▒██▀▒█▀▄▒█▀▄░▄▀▄▒█▀▄ ")
        print("  ░█▄▄░█▀▄░█▀▄░▀▄▀░█▀▄ ")
        print()

result = calculate(args.part,args.base)
output(args.part,args.base,result)
