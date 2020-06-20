

# import curses


# class CursesWindow:
#     def __init__(self):
#         b = curses.initscr()
#         self.curse = curses.newpad(100, 100)
#         curses.noecho()
#         curses.cbreak()
#         b.keypad(True)


#     def render_screen(self):
#         self.curse.clear()
#         for y in range(0, 99):
#             for x in range(0, 99):
#                 self.curse.addch(y,x, ord('a') + (x*x+y*y) % 26)
#         self.curse.refresh( 0,0, 5,5, 20,75)
