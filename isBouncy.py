def isBouncy(number):
    check=str(number)
    sortiert=''.join(sorted(check))
    if check==sortiert:
        return(False)
    if check==sortiert[::-1]:
        return(False)
    else:
        return(True)
