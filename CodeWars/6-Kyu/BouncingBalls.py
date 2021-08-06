def bouncing_ball(h, bounce, window):
    if (bounce >= 1) or (bounce <= 0) or (h <= 0) or (window >= h):
        return -1

    seeCount = 1
    while h > window:
        h = h * bounce
        if h > window:
            seeCount += 2

    return seeCount