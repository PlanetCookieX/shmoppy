from main_window.MainWindow import MainWindow


def run():
    windows = make_windows()
    update(windows)


def make_windows():
    windows = []

    main_window = MainWindow()
    windows.append(main_window)

    return windows


def update(windows):
    while True:
        for window in windows:
            window.update()
        # Super hacky. Grab the main window, grab its parent tkinter
        windows[0].get_internal().update_idletasks()
        windows[0].get_internal().update()


if __name__ == '__main__':
    run()
