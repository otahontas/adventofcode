import computer.comp as comp

def main():
    a = [int(x) for x in open('d09.txt').read().strip().split(',')]
    print(a)
    c = comp.Comp(a)
    c.run()

if __name__ == "__main__":
    main()
