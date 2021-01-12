from comp import Comp

a = [int(x) for x in open("inputs/d05.txt").read().strip().split(",")]
c1 = Comp(a)
c1.add_one_input(1)
c1.run()
c1.print_outputs()

c2 = Comp(a)
c2.add_one_input(5)
c2.run()
c2.print_outputs()
