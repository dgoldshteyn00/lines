from display import *
from draw import *

s = new_screen()
c = [0, 255, 0]

# octants 1 and 5


draw_line(0, 0, X_RES - 1, Y_RES - 1, s, c)
draw_line(0, 0, X_RES - 1, Y_RES / 2, s, c)
draw_line(X_RES - 1, Y_RES - 1, 0, Y_RES / 2, s, c)

# octants 8 and 4
c[BLUE] = 255
draw_line(0, Y_RES - 1, X_RES - 1, 0, s, c)
draw_line(0, Y_RES - 1, X_RES - 1, Y_RES / 2, s, c)
draw_line(X_RES - 1, 0, 0, Y_RES / 2, s, c)

# octants 2 and 6
c[RED] = 255
c[GREEN] = 0
c[BLUE] = 0
draw_line(0, 0, X_RES / 2, Y_RES - 1, s, c)
draw_line(X_RES - 1, Y_RES - 1, X_RES / 2, 0, s, c)

# octants 7 and 3
c[BLUE] = 255
draw_line(0, Y_RES - 1, X_RES / 2, 0, s, c)
draw_line(X_RES - 1, 0, X_RES / 2, Y_RES - 1, s, c)

# horizontal and vertical
c[BLUE] = 0
c[GREEN] = 255
draw_line(0, Y_RES / 2, X_RES - 1, Y_RES / 2, s, c)
draw_line(X_RES / 2, 0, X_RES / 2, Y_RES - 1, s, c)

# display(s) <more trouble than it's worth>
save_ppm(s, 'binary.ppm')
save_ppm_ascii(s, 'ascii.ppm')
# save_extension(s, 'img.png') <invalid file type>

print("binary.ppm")
print("ascii.ppm")
