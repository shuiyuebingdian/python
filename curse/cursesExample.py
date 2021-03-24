import curses

stdscr = curses.initscr()

# def main(stdscr):
#     # Clear screen
#     stdscr.clear()
#
#     # This raise ZeroDivisionError when i== 10
#     for i in range(0, 11):
#         v = i - 10
#         stdscr.addstr(i, 0, '10 devided by {} is {}'.format(v, 10 / v))
#
#     stdscr.refresh()
#     stdscr.getkey()
#
# wrapper(main())
