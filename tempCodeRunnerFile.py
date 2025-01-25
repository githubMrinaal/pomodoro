        reps+=1
        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60

        if reps%8==0:
            count_down(long_break_sec)
            timer.config(text="LONG BREAK",fg=RED)
        elif reps%2==0:
            count_down(short_break_sec)
            timer.config(text="SHORT BREAK",fg=PINK)
        else:
            count_down(work_sec)
            timer.config(text="WORK",fg=GREEN)