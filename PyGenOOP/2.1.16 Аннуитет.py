def annual_return(start, percent, year):
    for i in range(year):
        start *= float(1 + percent / 100)
        yield start
