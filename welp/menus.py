import curses


class CursesWindow:
    def set_data(self, data):
        lines = []
        print(data)
        for b in data:
            lines.append(b['name'])
            lines.append('{}  {}  {}'.format(b['price'], b['distance'],
                         b['rating']))
            lines.append(b['url'].split('?')[0])
            lines.append('')

        # for l in lines:
        #     print(l)

        self.data = lines

    def print_selections(self):
        HIGHLIGHT_TEXT = curses.color_pair(1)
        NORMAL_TEXT = curses.A_NORMAL

        if len(self.data) == 0:
            self.window_box.addstr(1, 1, "No results found 🍴",
                                   HIGHLIGHT_TEXT)
        else:
            if self.rows % 4 != 0:
                self.rows -= (self.rows % 4)

            for i in range(self.rows):
                if 4 * self.position <= i < 4 * self.position + 4:
                    # y, x, string
                    self.window_box.addstr(i, 1, self.data[(self.current_page
                                           * self.rows) + i], HIGHLIGHT_TEXT)
                else:
                    if (self.current_page * self.rows) + i < len(self.data):
                        self.window_box.addstr(i, 1, self.data[
                                               (self.current_page * self.rows)
                                               + i], NORMAL_TEXT)
                if i == len(self.data):
                    break

        self.stdscr.refresh()
        self.window_box.refresh()

    def open_curses_ui(self):
        curses.wrapper(self.print_window)

    def init_curses(self, stdscr):
        # initializes a color pair 1 where black is the foreground (text) and
        # cyan is the background
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)
        # disable terminal cursor
        curses.curs_set(0)

        self.stdscr = stdscr
        self.rows, self.cols = stdscr.getmaxyx()
        self.position = 0
        self.current_page = 0
        self.window_box = curses.newwin(self.rows, self.cols)

    def poll_draw_render(self):
        # HIGHLIGHT_TEXT = curses.color_pair(1)
        # NORMAL_TEXT = curses.A_NORMAL
        key_press = self.stdscr.getch()
        # run until quit keys are pressed
        while key_press != 27 and key_press != 113:
            # refresh the rows for printing
            self.rows, self.cols = self.stdscr.getmaxyx()

            if key_press == curses.KEY_DOWN or key_press == 106:
                self.position += 1
                max_valid_rows = self.rows - (self.rows % 4)

                if self.position * 4 >= max_valid_rows:
                    self.current_page += 1
                    self.position = 0

            if key_press == curses.KEY_UP or key_press == 107:
                self.position -= 1

                if self.position < 0:
                    if self.current_page > 0:
                        self.current_page -= 1
                        self.position = self.rows / 4 - 1
                    else:
                        self.position = 0
            # todo: key left and key right
            self.window_box.erase()

            self.print_selections()

            key_press = self.stdscr.getch()

    def print_window(self, stdscr):
        self.init_curses(stdscr)
        self.print_selections()
        self.poll_draw_render()
