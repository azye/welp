import curses
import math

rows_in_entry = 5


class SelectionWindow:
    def __init__(self, data, stdscr, window):
        self.window_box = window
        self.stdscr = stdscr
        self.business = data
        self.rows, self.cols = stdscr.getmaxyx()

    def print_business(self):
        NORMAL_TEXT = curses.A_NORMAL

        if not self.business:
            self.window_box.addstr(1, 1, "Not a valid business 🍴",
                                   NORMAL_TEXT)
        else:
            business_data = self.business.get_full_printable()

            for i in range(self.rows):
                if i == len(business_data):
                    break

                self.window_box.addstr(i, 1, business_data[i], NORMAL_TEXT)

        self.stdscr.refresh()
        self.window_box.refresh()

    def poll_draw_render(self):
        key_press = self.stdscr.getch()

        # run until quit keys are pressed
        while key_press != 27 and key_press != 113:
            # refresh the rows for printing
            self.rows, self.cols = self.stdscr.getmaxyx()

            if key_press == curses.KEY_DOWN or key_press == 106:
                pass

            if key_press == curses.KEY_UP or key_press == 107:
                pass

            if key_press == curses.KEY_LEFT or key_press == 104:
                pass

            if key_press == curses.KEY_RIGHT or key_press == 108:
                pass

            self.window_box.erase()
            self.print_business()

            key_press = self.stdscr.getch()


class CursesWindow:
    def __init__(self, client):
        self.client = client

    def set_data(self, data):
        self.data = data

    def print_selections(self):
        HIGHLIGHT_TEXT = curses.color_pair(1)
        NORMAL_TEXT = curses.A_NORMAL

        if len(self.data) == 0:
            self.window_box.addstr(1, 1, "No results found 🍴",
                                   NORMAL_TEXT)
        else:
            if self.rows % rows_in_entry != 0:
                self.rows -= (self.rows % rows_in_entry)
            max_entries = int(self.rows / rows_in_entry)
            data_start_idx = int(self.current_page * max_entries)
            i = 0

            for entry in self.data[data_start_idx:data_start_idx +
                                   max_entries]:
                for row in entry.get_printable():

                    if self.position * rows_in_entry <= i < self.position * \
                       rows_in_entry + 4:
                        self.window_box.addstr(i, 0, ' ', HIGHLIGHT_TEXT)

                    self.window_box.addstr(i, 1, row, NORMAL_TEXT)
                    i += 1

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
        max_valid_rows = self.rows - (self.rows % rows_in_entry)
        max_entries = int(self.rows / rows_in_entry)
        max_pages = int(math.ceil(len(self.data) / max_entries) - 1)
        # run until quit keys are pressed
        while key_press != 27 and key_press != 113:
            # refresh the rows for printing
            self.rows, self.cols = self.stdscr.getmaxyx()

            if key_press == curses.KEY_RESIZE:
                self.position = 0
                self.current_page = 0
                self.rows, self.cols = self.stdscr.getmaxyx()
                max_valid_rows = self.rows - (self.rows % rows_in_entry)
                self.max_pages = math.ceil(len(self.data) / max_entries) - 1

            if key_press == 10:
                data_start_idx = int(self.current_page * max_entries)

                current_entry = self.data[int(data_start_idx):int(data_start_idx +
                                          max_entries)][int(self.position)]
                # print(current_entry)
                self.window_box.erase()
                business_details = self.client.yelp.get_business(current_entry.id)
                current_entry.hours = business_details['hours'] if 'hours' in business_details else None
                w = SelectionWindow(current_entry, self.stdscr, self.window_box)
                w.print_business()
                w.poll_draw_render()

            if key_press == curses.KEY_DOWN or key_press == 106:
                self.position += 1
                max_valid_rows = self.rows - (self.rows % rows_in_entry)
                # max_pages = math.ceil(len(self.data) / max_valid_rows) - 1
                if self.position * rows_in_entry >= max_valid_rows:
                    if self.current_page < max_pages:
                        self.current_page += 1
                        self.position = 0
                    else:
                        self.position -= 1

                if self.current_page == max_pages:
                    positions_in_page = math.ceil(
                        len(self.data[self.current_page * max_entries:]) - 1)
                    if self.position > positions_in_page:
                        self.position -= 1

            if key_press == curses.KEY_UP or key_press == 107:
                self.position -= 1

                if self.position < 0:
                    if self.current_page > 0:
                        self.current_page -= 1
                        self.position = (max_valid_rows / rows_in_entry) - 1
                    else:
                        self.position = 0

            if key_press == curses.KEY_LEFT or key_press == 104:
                if self.current_page > 0:
                    self.current_page -= 1
                    self.position = 0

            if key_press == curses.KEY_RIGHT or key_press == 108:
                if self.current_page < max_pages:
                    self.current_page += 1
                    self.position = 0

            self.window_box.erase()
            self.print_selections()

            key_press = self.stdscr.getch()

    def print_window(self, stdscr):
        self.init_curses(stdscr)
        self.print_selections()
        self.poll_draw_render()
