from table import Table

def main ():
    table = Table((int(256),int(256))) # builds board from table file
    table.animate()
    for _ in table.animate():
        pass

if __name__ == '__main__':
    main()