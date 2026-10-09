def primo(n):

    if n <= 1:
        return False

    div = 2
    while div < n:
        if n%div == 0:
            return False
        div +=1

    return True
        
        