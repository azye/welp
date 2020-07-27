import curses
import math

class CursesWindow:
    def __init__(self, data):
        self.data = data

    def open_screen(self):
        curses.wrapper(self.print_window)
    
    def init_stuff(self):
        # initializes a color pair 1 where black is the foreground (text) and cyan is the background
        curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_CYAN)
        # disable terminal cursor
        curses.curs_set( 0 )

    def print_window(self, stdscr):
        self.init_stuff()

        rows, cols = stdscr.getmaxyx()

        # gets color pair 1
        highlightText = curses.color_pair( 1 )
        # A_NORMAL is default text styling
        normalText = curses.A_NORMAL

        max_row = 30 # max number of rows
        
        box = curses.newwin( rows, cols )
        box.box()

        strings = self.data
        row_num = len( strings )

        pages = int( math.ceil( row_num / max_row ) )
        position = 1
        page = 1
        # prints out the strings
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
        # detects for key changes
        while x != 27 and x != 113:
            if x == curses.KEY_DOWN or x == 106:
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
            if x == curses.KEY_UP or x == 107:
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
            # if x == ord( "\n" ) and row_num != 0:
                # stdscr.erase()
                # stdscr.border( 0 )
                # stdscr.addstr( 14, 3, "YOU HAVE PRESSED '" + strings[ position - 1 ] + "' ON POSITION " + str( position ) )

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
