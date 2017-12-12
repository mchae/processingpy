def showGrid(s=20, black=155, text=True):
    """Display grid lines"""
    rows = height/s
    cols = width/s
    stroke(black)
    for i in range(rows):
        line(0, s*i, width, s*i)
    for i in range(cols):
        line(s*i, 0, s*i, height)
        
    if (text):
        text(str(width), width - 20, 10)
        text(str(height), 0, height)
