import curses
import math


class CursesWindow:
    def set_data(self, data):
        self.data = data
        self.max_rows = 30

    def open_curses_ui(self):
        curses.wrapper(self.print_window)

    def init_curses(self):
        # initializes a color pair 1 where black is the foreground (text) and
        # cyan is the background
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)
        # disable terminal cursor
        curses.curs_set(0)

    def print_initial_screen(self, box):
        # gets color pair 1
        highlightText = curses.color_pair(1)
        # A_NORMAL is default text styling
        normalText = curses.A_NORMAL

        max_row = 30
        self.rows, self.cols = box.getmaxyx()

        row_num = len(self.data)

        self.pages = int(math.ceil(row_num / max_row))
        self.position = 1
        self.current_page = 1

        for i in range(1, max_row + 1):
            if row_num == 0:
                box.addstr(1, 1, "There aren't strings", highlightText)
            else:
                if (i == self.position):
                    # y, x, string
                    box.addstr(i, 2, str(i) + " - " +
                               self.data[i - 1], highlightText)
                else:
                    box.addstr(i, 2, str(i) + " - " +
                               self.data[i - 1], normalText)
                if i == row_num:
                    break
        return

    def print_window(self, stdscr):
        self.init_curses()

        rows, cols = stdscr.getmaxyx()
        print(f'{rows} rows and {cols} cols')
        # gets color pair 1
        highlightText = curses.color_pair(1)
        # A_NORMAL is default text styling
        normalText = curses.A_NORMAL

        max_row = 30  # max number of rows

        # initialize as a box
        box = curses.newwin(rows, cols)
        box.box()

        self.print_initial_screen(box)

        row_num = len(self.data)

        stdscr.refresh()
        box.refresh()

        x = stdscr.getch()
        # detects for key changes
        while x != 27 and x != 113:
            if x == curses.KEY_DOWN or x == 106:
                if self.current_page == 1:
                    if self.position < max_row:
                        self.position += 1
                    else:
                        if self.pages > 1:
                            self.current_page += 1
                            self.position = 1 + \
                                (max_row * (self.current_page - 1))
                elif self.current_page == self.pages:
                    if self.position < len(self.data):
                        self.position += 1
                else:
                    if self.position < max_row + \
                            (max_row * (self.current_page - 1)):
                        self.position += 1
                    else:
                        self.current_page = self.current_page + 1
                        self.position = 1 + (max_row * (self.current_page - 1))
            if x == curses.KEY_UP or x == 107:
                if self.current_page == 1:
                    if self.position > 1:
                        self.position -= 1
                else:
                    if self.position > (
                            1 + (max_row * (self.current_page - 1))):
                        self.position -= 1
                    else:
                        self.current_page -= 1
                        self.position = max_row + \
                            (max_row * (self.current_page - 1))
            if x == curses.KEY_LEFT:
                if self.current_page > 1:
                    self.current_page -= 1
                    self.position = 1 + (max_row * (self.current_page - 1))

            if x == curses.KEY_RIGHT:
                if self.current_page < self.pages:
                    self.current_page += 1
                    self.position = (1 + (max_row * (self.current_page - 1)))

            box.erase()
            stdscr.border(0)
            box.border(0)

            for i in range(1 + (max_row * (self.current_page - 1)),
                           max_row + 1 + (max_row * (self.current_page - 1))):
                if row_num == 0:
                    box.addstr(1, 1, "There aren't strings", highlightText)
                else:
                    if (i + (max_row * (self.current_page - 1)) == self.position + (max_row * (self.current_page - 1))):
                        box.addstr(i - (max_row * (self.current_page - 1)), 2, str(i) + " - " + self.data[i - 1], highlightText)
                    else:
                        box.addstr(i - (max_row * (self.current_page - 1)), 2, str(i) + " - " + self.data[i - 1], normalText)
                    if i == row_num:
                        break

            stdscr.refresh()
            box.refresh()
            x = stdscr.getch()
