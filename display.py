from subprocess import Popen, PIPE
from os import remove

# constants
X_RES = 500
Y_RES = 500
MAX_COLOR = 255
RED = 0
GREEN = 1
BLUE = 2

DEFAULT_COLOR = [0, 0, 0]


def new_screen(width=X_RES, height=Y_RES):
    screen = []
    for y in range(height):
        row = []
        screen.append(row)
        for x in range(width):
            screen[y].append(DEFAULT_COLOR[:])
    return screen


def plot(screen, color, x, y):
    new_y = Y_RES - 1 - y
    if 0 <= x < X_RES and 0 <= new_y < Y_RES:
        screen[int(new_y)][int(x)] = color[:]


def clear_screen(screen):
    for y in range(len(screen)):
        for x in range(len(screen[y])):
            screen[y][x] = DEFAULT_COLOR[:]


def save_ppm(screen, f_name):
    f = open(f_name, 'wb')
    ppm = 'P6\n' + str(len(screen[0])) + ' ' + str(len(screen)) + ' ' + str(MAX_COLOR) + '\n'
    f.write(ppm.encode())
    for y in range(len(screen)):
        for x in range(len(screen[y])):
            pixel = screen[y][x]
            f.write(bytes(pixel))
    f.close()


def save_ppm_ascii(screen, f_name):
    f = open(f_name, 'w')
    ppm = 'P3\n' + str(len(screen[0])) + ' ' + str(len(screen)) + ' ' + str(MAX_COLOR) + '\n'
    for y in range(len(screen)):
        row = ''
        for x in range(len(screen[y])):
            pixel = screen[y][x]
            row += str(pixel[RED]) + ' '
            row += str(pixel[GREEN]) + ' '
            row += str(pixel[BLUE]) + ' '
        ppm += row + '\n'
    f.write(ppm)
    f.close()


def save_extension(screen, f_name):
    ppm_name = f_name[:f_name.find('.')] + '.ppm'
    save_ppm_ascii(screen, ppm_name)
    p = Popen(['convert', ppm_name, f_name], stdin=PIPE, stdout=PIPE)
    p.communicate()
    remove(ppm_name)


def display(screen):
    ppm_name = 'pic.ppm'
    save_ppm_ascii(screen, ppm_name)
    p = Popen(['display', ppm_name], stdin=PIPE, stdout=PIPE)
    p.communicate()
    remove(ppm_name)
