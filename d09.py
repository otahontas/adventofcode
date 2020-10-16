from comp import Comp

a = [int(x) for x in open("inputs/d09.txt").read().strip().split(",")]
c = Comp(a)
c.add_one_input(1)
c.run()
c.print_outputs()

c2 = Comp(a)
c2.add_one_input(2)
c2.run()
c2.print_outputs()
