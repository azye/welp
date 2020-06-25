

import curses
import math

class CursesWindow:
    # def __init__(self):
    #     b = curses.initscr()
    #     self.curse = curses.newpad(100, 100)
        # curses.noecho()
        # curses.cbreak()
        # b.keypad(True)

#     def render_screen(self):
#         self.curse.clear()
#         for y in range(0, 99):
#             for x in range(0, 99):
#                 self.curse.addch(y,x, ord('a') + (x*x+y*y) % 26)
#         self.curse.refresh( 0,0, 5,5, 20,75)

    def open_screen(self):
        curses.wrapper(self.print_window)

    def print_window(self, stdscr):
        # screen = curses.initscr() # init the curses screen
        curses.noecho() # no echo mode blocks input echo
        curses.cbreak() # react to buffered input without return
        curses.start_color() # enables color
        stdscr.keypad( 1 ) 
        curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_CYAN)
        highlightText = curses.color_pair( 1 )
        normalText = curses.A_NORMAL
        stdscr.border( 0 )
        curses.curs_set( 0 )
        max_row = 10 #max number of rows
        box = curses.newwin( max_row + 2, 64, 1, 1 )
        box.box()


        strings = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "l", "m", "n" ] #list of strings
        row_num = len( strings )

        pages = int( math.ceil( row_num / max_row ) )
        position = 1
        page = 1
        for i in range( 1, max_row + 1 ):
            if row_num == 0:
                box.addstr( 1, 1, "There aren't strings", highlightText )
            else:
                if (i == position):
                    box.addstr( i, 2, str( i ) + " - " + strings[ i - 1 ], highlightText )
                else:
                    box.addstr( i, 2, str( i ) + " - " + strings[ i - 1 ], normalText )
                if i == row_num:
                    break

        stdscr.refresh()
        box.refresh()

        x = stdscr.getch()
        while x != 27:
            if x == curses.KEY_DOWN:
                if page == 1:
                    if position < i:
                        position = position + 1
                    else:
                        if pages > 1:
                            page = page + 1
                            position = 1 + ( max_row * ( page - 1 ) )
                elif page == pages:
                    if position < row_num:
                        position = position + 1
                else:
                    if position < max_row + ( max_row * ( page - 1 ) ):
                        position = position + 1
                    else:
                        page = page + 1
                        position = 1 + ( max_row * ( page - 1 ) )
            if x == curses.KEY_UP:
                if page == 1:
                    if position > 1:
                        position = position - 1
                else:
                    if position > ( 1 + ( max_row * ( page - 1 ) ) ):
                        position = position - 1
                    else:
                        page = page - 1
                        position = max_row + ( max_row * ( page - 1 ) )
            if x == curses.KEY_LEFT:
                if page > 1:
                    page = page - 1
                    position = 1 + ( max_row * ( page - 1 ) )

            if x == curses.KEY_RIGHT:
                if page < pages:
                    page = page + 1
                    position = ( 1 + ( max_row * ( page - 1 ) ) )
            if x == ord( "\n" ) and row_num != 0:
                stdscr.erase()
                stdscr.border( 0 )
                stdscr.addstr( 14, 3, "YOU HAVE PRESSED '" + strings[ position - 1 ] + "' ON POSITION " + str( position ) )

            box.erase()
            stdscr.border( 0 )
            box.border( 0 )

            for i in range( 1 + ( max_row * ( page - 1 ) ), max_row + 1 + ( max_row * ( page - 1 ) ) ):
                if row_num == 0:
                    box.addstr( 1, 1, "There aren't strings",  highlightText )
                else:
                    if ( i + ( max_row * ( page - 1 ) ) == position + ( max_row * ( page - 1 ) ) ):
                        box.addstr( i - ( max_row * ( page - 1 ) ), 2, str( i ) + " - " + strings[ i - 1 ], highlightText )
                    else:
                        box.addstr( i - ( max_row * ( page - 1 ) ), 2, str( i ) + " - " + strings[ i - 1 ], normalText )
                    if i == row_num:
                        break



            stdscr.refresh()
            box.refresh()
            x = stdscr.getch()
