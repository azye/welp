import curses
import math


class CursesWindow:
    def set_data(self, data):

        """
        todo: this should really be an 2d array. position keeps track of the outer array
        while the render renders the inside data

        """
        lines = []
        for b in data:
            lines.append(b['name'])
            lines.append('{}  {}  {}'.format(b['price'], b['distance'], b['rating']))
            lines.append('')
        self.data = lines
        print(self.data)

        # self.max_rows = 30

    def open_curses_ui(self):
        curses.wrapper(self.print_window)

    def init_curses(self, stdscr):
        # initializes a color pair 1 where black is the foreground (text) and
        # cyan is the background
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)
        # disable terminal cursor
        curses.curs_set(0)

        self.stdscr = stdscr
        rows, cols = stdscr.getmaxyx()
        box = curses.newwin(rows, cols)
        self.rows = rows
        self.cols = cols

        self.pages = int(math.ceil(len(self.data) / self.rows))
        self.position = 1
        self.current_page = 1

        self.window_box = box
        self.window_box.box()

    def print_initial_screen(self):
        HIGHLIGHT_TEXT = curses.color_pair(1)
        NORMAL_TEXT = curses.A_NORMAL

        for i in range(1, self.rows-1):
            if len(self.data) == 0:
                self.window_box.addstr(1, 1,
                                       "No results found 🍽", HIGHLIGHT_TEXT)
            else:
                if (i == self.position):
                    # y, x, string
                    self.window_box.addstr(i, 2, self.data[i - 1],
                                           HIGHLIGHT_TEXT)
                else:
                    self.window_box.addstr(i, 2, self.data[i - 1], NORMAL_TEXT)
                if i == len(self.data):
                    break

        self.stdscr.refresh()
        self.window_box.refresh()

        return

    def poll_draw_render(self):
        HIGHLIGHT_TEXT = curses.color_pair(1)
        NORMAL_TEXT = curses.A_NORMAL
        key_press = self.stdscr.getch()
        # run until quit keys are pressed
        while key_press != 27 and key_press != 113:
            # refresh the rows for printing
            self.rows, self.cols = self.stdscr.getmaxyx()

            self.window_box.erase()
            self.stdscr.border(0)
            self.window_box.border(0)

            for i in range(1, self.rows - 1):
                if len(self.data) == 0:
                    self.window_box.addstr(1, 1,
                                           "There aren't strings", HIGHLIGHT_TEXT)
                else:
                    if (i == self.position):
                        # y, x, string
                        self.window_box.addstr(i, 2, self.data[i - 1],
                                               HIGHLIGHT_TEXT)
                    else:
                        self.window_box.addstr(i, 2, self.data[i - 1], NORMAL_TEXT)
                    if i == len(self.data):
                        break

            self.stdscr.refresh()
            self.window_box.refresh()
            key_press = self.stdscr.getch()

    def print_window(self, stdscr):
        self.init_curses(stdscr)
        self.print_initial_screen()
        self.poll_draw_render()
        
        
        # row_num = len(self.data)

        # stdscr.refresh()
        # box.refresh()

        # x = stdscr.getch()
        # detects for key changes
        # while x != 27 and x != 113:
        #     if x == curses.KEY_DOWN or x == 106:
        #         if self.current_page == 1:
        #             if self.position < max_row:
        #                 self.position += 1
        #             else:
        #                 if self.pages > 1:
        #                     self.current_page += 1
        #                     self.position = 1 + \
        #                         (max_row * (self.current_page - 1))
        #         elif self.current_page == self.pages:
        #             if self.position < len(self.data):
        #                 self.position += 1
        #         else:
        #             if self.position < max_row + \
        #                     (max_row * (self.current_page - 1)):
        #                 self.position += 1
        #             else:
        #                 self.current_page = self.current_page + 1
        #                 self.position = 1 + (max_row * (self.current_page - 1))
        #     if x == curses.KEY_UP or x == 107:
        #         if self.current_page == 1:
        #             if self.position > 1:
        #                 self.position -= 1
        #         else:
        #             if self.position > (
        #                     1 + (max_row * (self.current_page - 1))):
        #                 self.position -= 1
        #             else:
        #                 self.current_page -= 1
        #                 self.position = max_row + \
        #                     (max_row * (self.current_page - 1))
        #     if x == curses.KEY_LEFT:
        #         if self.current_page > 1:
        #             self.current_page -= 1
        #             self.position = 1 + (max_row * (self.current_page - 1))

        #     if x == curses.KEY_RIGHT:
        #         if self.current_page < self.pages:
        #             self.current_page += 1
        #             self.position = (1 + (max_row * (self.current_page - 1)))
        #     # if x == ord( "\n" ) and row_num != 0:
        #         # stdscr.erase()
        #         # stdscr.border( 0 )
        #         # stdscr.addstr( 14, 3, "YOU HAVE PRESSED '" + strings[ position - 1 ] + "' ON POSITION " + str( position ) )

        #     box.erase()
        #     stdscr.border(0)
        #     box.border(0)

        #     for i in range(1 + (max_row * (self.current_page - 1)),
        #                    max_row + 1 + (max_row * (self.current_page - 1))):
        #         if row_num == 0:
        #             box.addstr(1, 1, "There aren't strings", highlightText)
        #         elif (i + (max_row * (self.current_page - 1))) == self.position + (max_row * (self.current_page - 1)):
        #                 box.addstr(i - (max_row * (self.current_page - 1)), 2, str(i) + " - " + self.data[i - 1], highlightText)
        #         else:
        #             box.addstr(i - (max_row * (self.current_page - 1)),
        #                            2, str(i) + " - " + self.data[i - 1], normalText)
        #             if i == row_num:
        #                 break

        #     stdscr.refresh()
        #     box.refresh()
        #     x = stdscr.getch()

    # rows, cols = stdscr.getmaxyx()
    # print(f'{rows} rows and {cols} cols')

    # gets color pair 1
    # highlightText = curses.color_pair(1)
    # # A_NORMAL is default text styling
    # normalText = curses.A_NORMAL

    # max_row = 30
    # # max number of rows

    # initialize as a box
