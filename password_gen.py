import sys
import os
import curses
import secrets
import string
import math
import subprocess

# --- Theme Configuration ---
COLOR_TITLE_START = 10
COLOR_BORDER_GREY = 20
COLOR_TEXT_MUTED = 21
COLOR_TEXT_CYAN = 22
COLOR_TEXT_GREEN = 23
COLOR_TEXT_YELLOW = 24
COLOR_TEXT_MAGENTA = 25
COLOR_TEXT_ORANGE = 26
COLOR_TEXT_RED = 27

# Strictly enforced geometry bounds to accommodate your sub-window coordinate mesh
MIN_ROWS = 40
MIN_COLS = 100


def force_windows_max_size():
    """Natively maximize the console buffer and set UTF-8 code pages if running on Windows."""
    if sys.platform.startswith("win"):
        try:
            import ctypes

            kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
            # Set console output and input code page to UTF-8 (65001)
            kernel32.SetConsoleOutputCP(65001)
            kernel32.SetConsoleCP(65001)

            user32 = ctypes.WinDLL("user32", use_last_error=True)
            hwnd = kernel32.GetConsoleWindow()
            if hwnd:
                user32.ShowWindow(hwnd, 3)  # SW_MAXIMIZE flag
        except Exception:
            pass


def init_cyberpunk_palette():
    curses.start_color()
    curses.use_default_colors()

    can_change = False
    try:
        can_change = curses.can_change_color()
    except Exception:
        pass

    num_colors = 8
    try:
        num_colors = curses.COLORS
    except Exception:
        pass

    if num_colors >= 256:
        if can_change:
            try:
                curses.init_color(COLOR_BORDER_GREY, 300, 300, 300)
                curses.init_color(COLOR_TEXT_MUTED, 500, 500, 500)
                curses.init_color(COLOR_TEXT_CYAN, 0, 800, 1000)
                curses.init_color(COLOR_TEXT_GREEN, 0, 1000, 400)
                curses.init_color(COLOR_TEXT_YELLOW, 1000, 1000, 0)
                curses.init_color(COLOR_TEXT_MAGENTA, 1000, 200, 800)
                curses.init_color(COLOR_TEXT_ORANGE, 1000, 500, 0)
                curses.init_color(COLOR_TEXT_RED, 1000, 0, 300)
            except Exception:
                pass

        curses.init_pair(1, COLOR_TEXT_ORANGE, -1)
        curses.init_pair(2, COLOR_TEXT_GREEN, -1)
        curses.init_pair(3, COLOR_TEXT_MAGENTA, -1)
        curses.init_pair(4, COLOR_TEXT_CYAN, -1)
        curses.init_pair(5, COLOR_TEXT_MUTED, -1)
        curses.init_pair(6, COLOR_BORDER_GREY, -1)
        curses.init_pair(7, curses.COLOR_WHITE, -1)
        curses.init_pair(8, COLOR_TEXT_YELLOW, -1)
        curses.init_pair(9, COLOR_TEXT_RED, -1)

        rainbow = [
            COLOR_TEXT_MAGENTA,
            COLOR_TEXT_RED,
            COLOR_TEXT_ORANGE,
            COLOR_TEXT_YELLOW,
            COLOR_TEXT_GREEN,
            COLOR_TEXT_CYAN,
        ]
        for i, color in enumerate(rainbow):
            curses.init_pair(COLOR_TITLE_START + i, color, -1)
    else:
        # Fallback to standard ANSI colors
        curses.init_pair(1, curses.COLOR_YELLOW, -1)  # ORANGE fallback
        curses.init_pair(2, curses.COLOR_GREEN, -1)
        curses.init_pair(3, curses.COLOR_MAGENTA, -1)
        curses.init_pair(4, curses.COLOR_CYAN, -1)
        # Use white/default, or black if white is background. Under standard use, COLOR_WHITE is safe.
        curses.init_pair(5, curses.COLOR_WHITE, -1)   # MUTED fallback
        curses.init_pair(6, curses.COLOR_WHITE, -1)   # BORDER fallback
        curses.init_pair(7, curses.COLOR_WHITE, -1)
        curses.init_pair(8, curses.COLOR_YELLOW, -1)
        curses.init_pair(9, curses.COLOR_RED, -1)

        rainbow = [
            curses.COLOR_MAGENTA,
            curses.COLOR_RED,
            curses.COLOR_YELLOW,
            curses.COLOR_YELLOW,
            curses.COLOR_GREEN,
            curses.COLOR_CYAN,
        ]
        for i, color in enumerate(rainbow):
            curses.init_pair(COLOR_TITLE_START + i, color, -1)


def generate_password(state):
    pool = ""
    if state["upper"]:
        pool += string.ascii_uppercase
    if state["lower"]:
        pool += string.ascii_lowercase
    if state["digits"]:
        pool += string.digits
    if state["sym"]:
        pool += "!@#$%^&*"

    if state["ex_sim"]:
        for c in "l1I0O":
            pool = pool.replace(c, "")
    if state["ex_amb"]:
        for c in "{}[]()\\/'\"`~,;:<>":
            pool = pool.replace(c, "")

    if not pool:
        return "Pool Error!", 0.0

    pwd = "".join(secrets.choice(pool) for _ in range(state["length"]))
    entropy = math.log2(len(pool)) * state["length"]
    return pwd, entropy


def copy_to_clipboard(text):
    """Cross-platform clipboard copy routing."""
    if sys.platform.startswith("win"):
        try:
            # Leverage Windows native clip.exe tool cleanly
            process = subprocess.Popen(["clip"], stdin=subprocess.PIPE, shell=True)
            process.communicate(input=text.encode("utf-8"))
        except Exception:
            pass
    else:
        try:
            process = subprocess.Popen(
                ["xclip", "-selection", "clipboard"], stdin=subprocess.PIPE
            )
            process.communicate(input=text.encode("utf-8"))
        except FileNotFoundError:
            try:
                process = subprocess.Popen(
                    ["xsel", "--clipboard", "--input"], stdin=subprocess.PIPE
                )
                process.communicate(input=text.encode("utf-8"))
            except FileNotFoundError:
                pass


def open_github_silently():
    """Cross-platform web link deployment routing."""
    url = "https://github.com/nariman-z"
    if sys.platform.startswith("win"):
        try:
            os.startfile(url)
        except AttributeError:
            try:
                subprocess.Popen(f"start {url}", shell=True)
            except Exception:
                pass
    else:
        try:
            subprocess.Popen(
                ["xdg-open", url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
            )
        except Exception:
            pass


def draw_banner(stdscr):
    h, w = stdscr.getmaxyx()
    if h < MIN_ROWS or w < MIN_COLS:
        return False

    banner_p1 = [
        "██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██╗     ██████╗ ",
        "██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██║     ██╔══██╗",
        "██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║     ██║  ██║",
        "██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║     ██║  ██║",
        "██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║███████╗██████╔╝",
        "╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═════╝ ",
    ]
    banner_p2 = [
        " ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ ",
        "██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗",
        "██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝",
        "██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗",
        "╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║",
        " ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝",
    ]

    for i in range(6):
        color_idx = COLOR_TITLE_START + (i % 6)
        stdscr.attron(curses.color_pair(color_idx))
        if 1 + i < h and 2 < w:
            stdscr.addstr(1 + i, 2, banner_p1[i][: w - 4])
        if 7 + i < h and 2 < w:
            stdscr.addstr(7 + i, 2, banner_p2[i][: w - 4])
        stdscr.attroff(curses.color_pair(color_idx))
    return True


def draw_ui(stdscr, state):
    stdscr.erase()
    h, w = stdscr.getmaxyx()

    # Dynamic protection boundary check before building subwindows
    if h < MIN_ROWS or w < MIN_COLS:
        try:
            if h > 1 and w > 5:
                stdscr.attron(curses.color_pair(9) | curses.A_BOLD)
                stdscr.addstr(1, 2, "[!] SCREEN TOO SMALL FOR CRYPTOPUNK INTERFACE"[:w - 3])
                stdscr.attroff(curses.color_pair(9) | curses.A_BOLD)
            if h > 3 and w > 5:
                stdscr.addstr(3, 2, f"Current size:  {w} x {h}"[:w - 3])
            if h > 4 and w > 5:
                stdscr.addstr(4, 2, f"Required size: {MIN_COLS} x {MIN_ROWS}"[:w - 3])
            if h > 7 and w > 5:
                stdscr.attron(curses.color_pair(4))
                stdscr.addstr(7, 2, "Please resize or maximize your terminal window."[:w - 3])
            if h > 8 and w > 5:
                stdscr.addstr(8, 2, "Waiting for a valid terminal size..."[:w - 3])
                stdscr.attroff(curses.color_pair(4))
            stdscr.refresh()
        except curses.error:
            pass
        return False

    draw_banner(stdscr)

    if 14 < h:
        stdscr.attron(curses.color_pair(5))
        stdscr.addstr(14, 2, "Interactive OpenSSL Password Generator")
        stdscr.addstr(15, 2, "Secure. Strong. Beautiful.")
        stdscr.attroff(5)

    # Dynamic layout positions
    gen_box_y = 30
    gen_box_h = 6
    cmd_box_y = gen_box_y + gen_box_h
    footer_y = cmd_box_y + 4

    try:
        if footer_y < h:
            stdscr.attron(curses.color_pair(3))
            stdscr.addstr(footer_y, 2, "🌐 Powered by OpenSSL")
            stdscr.attron(curses.color_pair(4))
            stdscr.addstr(footer_y, 68, "Stay secure. Stay strong.")
    except curses.error:
        pass

    stdscr.refresh()

    # 2. Options Window
    opt_win = curses.newwin(11, 65, 17, 2)
    opt_win.attron(curses.color_pair(6))
    opt_win.box()
    opt_win.attroff(6)
    opt_win.attron(curses.color_pair(1) | curses.A_BOLD)
    opt_win.addstr(0, 3, " Password Options ")
    opt_win.attroff(1 | curses.A_BOLD)

    options_text = [
        ("Password Length", f"[ {state['length']:>2} ]"),
        ("Include Uppercase (A-Z)", f"[ {('x' if state['upper'] else ' ')} ]"),
        ("Include Lowercase (a-z)", f"[ {('x' if state['lower'] else ' ')} ]"),
        ("Include Numbers (0-9)", f"[ {('x' if state['digits'] else ' ')} ]"),
        ("Include Symbols (!@#$%^&*)", f"[ {('x' if state['sym'] else ' ')} ]"),
        (
            "Exclude Similar Characters (l1I0O)",
            f"[ {('x' if state['ex_sim'] else ' ')} ]",
        ),
        (
            "Exclude Ambiguous Symbols ({}[])(...)",
            f"[ {('x' if state['ex_amb'] else ' ')} ]",
        ),
    ]

    for idx, (label, val) in enumerate(options_text):
        if idx == state["focus"]:
            opt_win.attron(curses.A_REVERSE | curses.color_pair(8))
        else:
            opt_win.attron(curses.color_pair(7))
        opt_win.addstr(1 + idx, 2, f" {label:<45} {val:>13} ")
        opt_win.attroff(curses.A_REVERSE | curses.color_pair(8) | curses.color_pair(7))
    opt_win.refresh()

    # 3. Help Window
    help_win = curses.newwin(14, 30, 17, 69)
    help_win.attron(curses.color_pair(3))
    help_win.box()
    help_win.attron(curses.color_pair(1) | curses.color_pair(3))
    help_win.addstr(0, 9, " Quick Guide ")
    help_win.attroff(1 | curses.color_pair(3))

    help_win.attron(curses.color_pair(4))
    help_win.addstr(1, 2, "↑↓")
    help_win.attron(curses.color_pair(7))
    help_win.addstr(1, 10, ": Move Selection")

    help_win.attron(curses.color_pair(4))
    help_win.addstr(2, 2, "←→")
    help_win.attron(curses.color_pair(7))
    help_win.addstr(2, 10, ": Change Length")

    help_win.attron(curses.color_pair(4))
    help_win.addstr(3, 2, "Space")
    help_win.attron(curses.color_pair(7))
    help_win.addstr(3, 10, ": Toggle Option")

    help_win.attron(curses.color_pair(4))
    help_win.addstr(5, 2, "[R]")
    help_win.attron(curses.color_pair(7))
    help_win.addstr(5, 10, ": New Password")

    help_win.attron(curses.color_pair(4))
    help_win.addstr(6, 2, "[C]")
    help_win.attron(curses.color_pair(7))
    help_win.addstr(6, 10, ": Copy Password")

    help_win.attron(curses.color_pair(4))
    help_win.addstr(7, 2, "[S]")
    help_win.attron(curses.color_pair(7))
    help_win.addstr(7, 10, ": Save Password")

    help_win.attron(curses.color_pair(4))
    help_win.addstr(8, 2, "[E]")
    help_win.attron(curses.color_pair(7))
    help_win.addstr(8, 10, ": Copy OpenSSL Cmd")

    help_win.attron(curses.color_pair(4))
    help_win.addstr(9, 2, "[I]")
    help_win.attron(curses.color_pair(7))
    help_win.addstr(9, 10, ": Open GitHub Link")

    help_win.attron(curses.color_pair(4))
    help_win.addstr(11, 2, "[Q]")
    help_win.attron(curses.color_pair(9))
    help_win.addstr(11, 10, ": Exit Terminal")

    help_win.refresh()

    if state["length"] < 8:
        strength_str, strength_color, check_char = "Weak  ", curses.color_pair(9), "✗"
    elif state["length"] < 12:
        strength_str, strength_color, check_char = "Medium", curses.color_pair(8), "⚠"
    else:
        strength_str, strength_color, check_char = "Strong", curses.color_pair(2), "✓"

    # 4. Center-Bottom Output Box
    gen_win = curses.newwin(gen_box_h, 65, gen_box_y, 2)
    gen_win.attron(curses.color_pair(6))
    gen_win.box()
    gen_win.attroff(6)
    gen_win.attron(curses.color_pair(2) | curses.A_BOLD)
    gen_win.addstr(0, 2, " Generated Password ")
    gen_win.attroff(2 | curses.A_BOLD)

    gen_win.addstr(
        2, 4, f"{state['pwd'][:40] + ('...' if len(state['pwd']) > 40 else ''):<40}"
    )

    footer_row = 4
    gen_win.attron(curses.color_pair(5))
    gen_win.addstr(footer_row, 2, f"Entropy: {state['entropy']:.2f} bits")
    gen_win.addstr(footer_row, 30, "Strength: ")
    gen_win.attron(strength_color)
    gen_win.addstr(footer_row, 40, f"{strength_str} {check_char}")
    gen_win.attroff(strength_color)
    gen_win.refresh()

    # 5. Commands Control Board
    cmd_win = curses.newwin(3, 97, cmd_box_y, 2)
    cmd_win.attron(curses.color_pair(1))
    cmd_win.box()
    cmd_win.addstr(0, 2, " Commands ")
    cmd_win.attroff(1)

    action_key = "[G]" if state["is_first_generation"] else "[R]"
    action_desc = "Generate" if state["is_first_generation"] else "Regenerate"

    commands = [
        (action_key, action_desc),
        ("[C]", "Copy"),
        ("[S]", "Save"),
        ("[E]", "Export (OpenSSL)"),
        ("[I]", "Info"),
        ("[Q]", "Quit"),
    ]
    curr_x = 2
    for key, desc in commands:
        cmd_win.attron(curses.color_pair(4))
        cmd_win.addstr(1, curr_x, key)
        cmd_win.attron(curses.color_pair(7))
        cmd_win.addstr(1, curr_x + len(key), f" {desc}   ")
        curr_x += len(key) + len(desc) + 4
    cmd_win.refresh()
    return True


def main(stdscr):
    init_cyberpunk_palette()
    curses.curs_set(0)

    state = {
        "length": 16,
        "upper": True,
        "lower": True,
        "digits": True,
        "sym": True,
        "ex_sim": False,
        "ex_amb": True,
        "focus": 0,
        "pwd": "",
        "entropy": 0.0,
        "is_first_generation": False,
    }

    state["pwd"], state["entropy"] = generate_password(state)

    while True:
        ui_valid = draw_ui(stdscr, state)

        ch = stdscr.getch()

        if ch == curses.KEY_RESIZE:
            curses.update_lines_cols()
            continue

        if not ui_valid:
            continue

        if ch in [ord("q"), ord("Q"), 27]:
            break

        if ch == curses.KEY_UP:
            state["focus"] = (state["focus"] - 1) % 7
        elif ch == curses.KEY_DOWN:
            state["focus"] = (state["focus"] + 1) % 7

        elif ch == curses.KEY_LEFT:
            if state["focus"] == 0:
                state["length"] = 64 if state["length"] <= 4 else state["length"] - 1
                state["pwd"], state["entropy"] = generate_password(state)

        elif ch == curses.KEY_RIGHT:
            if state["focus"] == 0:
                state["length"] = 4 if state["length"] >= 64 else state["length"] + 1
                state["pwd"], state["entropy"] = generate_password(state)

        elif ch in [ord(" "), 10, 13, curses.KEY_ENTER]:
            f = state["focus"]
            if f == 1:
                state["upper"] = not state["upper"]
            elif f == 2:
                state["lower"] = not state["lower"]
            elif f == 3:
                state["digits"] = not state["digits"]
            elif f == 4:
                state["sym"] = not state["sym"]
            elif f == 5:
                state["ex_sim"] = not state["ex_sim"]
            elif f == 6:
                state["ex_amb"] = not state["ex_amb"]
            state["pwd"], state["entropy"] = generate_password(state)

        elif ch in [ord("g"), ord("G"), ord("r"), ord("R")]:
            state["pwd"], state["entropy"] = generate_password(state)

        elif ch in [ord("c"), ord("C")]:
            if state["pwd"]:
                copy_to_clipboard(state["pwd"])

        elif ch in [ord("s"), ord("S")]:
            if state["pwd"]:
                try:
                    with open("passwords.txt", "a", encoding="utf-8") as f:
                        f.write(state["pwd"] + "\n")
                except Exception:
                    pass

        elif ch in [ord("e"), ord("E")]:
            openssl_cmd = f"openssl rand -base64 {state['length']}"
            copy_to_clipboard(openssl_cmd)

        elif ch in [ord("i"), ord("I")]:
            open_github_silently()


if __name__ == "__main__":
    force_windows_max_size()
    curses.wrapper(main)
