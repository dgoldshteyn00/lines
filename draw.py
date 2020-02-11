from display import *


def draw_line(x0, y0, x1, y1, screen, color):  # standard version
    if abs(y1 - y0) < abs(x1 - x0):  # m < 1
        if x1 > x0:
            low_power_plot(x0, y0, x1, y1, screen, color)  # positive slope
        else:
            low_power_plot(x1, y1, x0, y0, screen, color)  # negative slope
    else:  # m >= 1
        if y1 > y0:
            high_power_plot(x0, y0, x1, y1, screen, color)  # positive slope
        else:
            high_power_plot(x1, y1, x0, y0, screen, color)  # negative slope


def low_power_plot(x0, y0, x1, y1, screen, color):  # m < 1
    dx = x1 - x0
    dy = y1 - y0
    y_increment = 1
    if dy < 0:
        y_increment = -1
        dy *= -1
    D = 2 * dy - dx
    y = y0
    for x in range(x0, x1):
        plot(screen, color, x, y)
        if D > 0:
            y += y_increment
            D -= 2 * dx
        D += 2 * dy


def high_power_plot(x0, y0, x1, y1, screen, color):  # m >= 1
    dx = x1 - x0
    dy = y1 - y0
    x_increment = 1
    if dx < 0:
        x_increment = -1
        dx *= -1
    D = 2 * dy - dx
    x = x0
    for y in range(y0, y1):
        plot(screen, color, x, y)
        if D > 0:
            x += x_increment
            D -= 2 * dy
        D += 2 * dx


def draw_line_2(x0, y0, x1, y1, screen, color):  # this version uses error calculations
    dx = abs(x1 - x0)
    mx = 1 if x0 < x1 else -1
    dy = -abs(y1 - y0)
    my = 1 if y0 < y1 else -1
    error = dx + dy
    while 1 == 1:  # for i in range(1000): <test code>
        plot(screen, color, x0, y0)
        if x0 == x1 and y0 == y1:
            break
        error_2 = 2 * error
        if error_2 >= dy:
            error += dy
            x0 += mx
        if error_2 <= dx:
            error += dx
            y0 += my
