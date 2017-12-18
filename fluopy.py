def showGrid(s=20, black=155, num=True):
    """Display grid lines"""
    rows = height/s
    cols = width/s
    stroke(black)
    for i in range(rows):
        line(0, s*i, width, s*i)
    for i in range(cols):
        line(s*i, 0, s*i, height)
        
    if (num):
        text("   0", 0, 10)
        text(str(width), width - 20, 10)
        #pushStyle()
        fill(255, 0, 0)
        text("0", 0, 10)
        text(str(height), 0, height)
        fill(0)
        #popStyle()
