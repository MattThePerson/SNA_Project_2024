

def track_progress(total, progress, text='progress:', inc=1):
    a, b = progress, total
    perc = ((a+1) / b * 100)
    if a%inc == 0 or progress == total-1:
        print("\r {} {:_}/{:_} ({:.5f}%)".format( text, (a+1), b, perc ), end='')
    a += 1
    return a, perc

