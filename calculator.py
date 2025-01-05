from tkinter import *
import math
expression="Welcome!"
on_flag=0
shift_flag=2
temp1=""
temp2=""
def click(val):
    global expression, temp1, temp2, on_flag, shift_flag
    if on_flag == 1:
        if expression == "Welcome Sir":
            expression = ""
        temp2 = temp1
        temp1 = str(val)

        if (temp1 in ["*", "/", "+", "-"] and temp1 == temp2):
            result.set(expression)
            return
        elif temp2 == '%' and temp1 == temp2:
            result.set(expression)
        elif temp1 != "" and temp2 in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9","π"] and temp1 == '(':
            expression = expression+ "*"
        elif temp2 == ')' and temp1 in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9","π"]:
            expression = expression[:-1] + ")*"

        if temp1 == "^":
            expression += "^"  # This will be converted to '**' in equal
        elif temp1 == "x^3":
            expression += "^3"
        elif temp1 == "x^2":
            expression += "^2"
        elif temp1=="x^-1":
            expression+="^-1"
        elif temp1=="10^x":
            expression+="10^"
        else:
            expression += str(val)
        result.set(expression)
        shift_flag = 0
def equal():
    try:
        global expression,on_flag,temp1,temp2,shift_flag
        if on_flag == 1:
            '''
                While passing value of sin i also included a space. Otherwise
                the replacement will be wrong. We can also solve this problem by writing 
                the replacement of inverse section before the normal section
            '''

            expression=expression.replace("sin ","sin")
            expression = expression.replace("cos ", "cos")
            expression = expression.replace("tan ", "tan")
            expression = expression.replace("sin^-1 ", "asin")
            expression = expression.replace("cos^-1 ", "acos")
            expression = expression.replace("tan^-1 ", "atan")
            expression = expression.replace('^', '**')

            '''
                Inverse must write before normal section. If we take example of sin,
                its inverse function is asin. If the normal sin section written before the
                inverse section then the first while lop searching for sin will replace the sin part and
                the evaluation will be wrong.
            '''

            # sin inverse start
            while "asin" in expression:
                asin_pos = expression.find("asin")
                if asin_pos != -1:
                    # Extract the angle following "sin"
                    angle_start = asin_pos + 4  # Position after "sin"
                    angle_end = angle_start

                    # Find the end of the angle (until next operator or end of string)
                    while angle_end < len(expression) and expression[angle_end] not in ["*", "/", "+", "-", "(", ")"]:
                        angle_end += 1

                    angle_str = expression[angle_start:angle_end]

                    if angle_str:  # Ensure the angle is not empty
                        try:
                            angle = float(angle_str)
                            asine_value = math.asin(angle)
                            expression = expression[:asin_pos] + str(asine_value) + expression[angle_end:]
                        except ValueError:
                            result.set("Invalid Expression")
                            expression = ""
                            return
                    else:
                        result.set("Invalid Expression")
                        expression = ""
                        return
            #sin inverse end

            # sin start
            while "sin" in expression:
                sin_pos = expression.find("sin")
                if sin_pos != -1:
                    # Extract the angle following "sin"
                    angle_start = sin_pos + 3  # Position after "sin"
                    angle_end = angle_start

                    # Find the end of the angle (until next operator or end of string)
                    while angle_end < len(expression) and expression[angle_end] not in ["*", "/", "+", "-", "(", ")"]:
                        angle_end += 1

                    angle_str = expression[angle_start:angle_end]

                    if angle_str:  # Ensure the angle is not empty
                        try:
                            angle = float(angle_str)
                            if angle==30.0:
                                sine_value=0.5
                            else:
                                sine_value = math.sin(math.radians(angle))
                            expression = expression[:sin_pos] + str(sine_value) + expression[angle_end:]
                        except ValueError:
                            result.set("Invalid Expression")
                            expression = ""
                            return
                    else:
                        result.set("Invalid Expression")
                        expression = ""
                        return
            # sin end

            # tan inverse start
            while "atan" in expression:
                atan_pos = expression.find("atan")
                if atan_pos != -1:
                    # Extract the angle following "sin"
                    angle_start = atan_pos + 4  # Position after "sin"
                    angle_end = angle_start

                    # Find the end of the angle (until next operator or end of string)
                    while angle_end < len(expression) and expression[angle_end] not in ["*", "/", "+", "-", "(", ")"]:
                        angle_end += 1

                    angle_str = expression[angle_start:angle_end]

                    if angle_str:  # Ensure the angle is not empty
                        try:
                            angle = float(angle_str)
                            atan_value = math.atan(angle)
                            expression = expression[:atan_pos] + str(atan_value) + expression[angle_end:]
                        except ValueError:
                            result.set("Invalid Expression")
                            expression = ""
                            return
                    else:
                        result.set("Invalid Expression")
                        expression = ""
                        return
            # tan inverse end

            # tan start
            while "tan" in expression:
                tan_pos = expression.find("tan")
                if tan_pos != -1:
                    # Extract the angle following "sin"
                    angle_start = tan_pos + 3  # Position after "sin"
                    angle_end = angle_start

                    # Find the end of the angle (until next operator or end of string)
                    while angle_end < len(expression) and expression[angle_end] not in ["*", "/", "+", "-", "(", ")"]:
                        angle_end += 1

                    angle_str = expression[angle_start:angle_end]

                    if angle_str:  # Ensure the angle is not empty
                        try:
                            angle = float(angle_str)
                            tan_value = math.tan(math.radians(angle))
                            if angle==45.0:
                                tan_value=1.0
                            expression = expression[:tan_pos] + str(tan_value) + expression[angle_end:]
                        except ValueError:
                            result.set("Invalid Expression")
                            expression = ""
                            return
                    else:
                        result.set("Invalid Expression")
                        expression = ""
                        return
            # tan end

            # cos inverse start
            while "acos" in expression:
                acos_pos = expression.find("acos")
                if acos_pos != -1:
                    # Extract the angle following "sin"
                    angle_start = acos_pos + 4  # Position after "sin"
                    angle_end = angle_start

                    # Find the end of the angle (until next operator or end of string)
                    while angle_end < len(expression) and expression[angle_end] not in ["*", "/", "+", "-", "(", ")"]:
                        angle_end += 1

                    angle_str = expression[angle_start:angle_end]

                    if angle_str:  # Ensure the angle is not empty
                        try:
                            angle = float(angle_str)
                            acos_value = math.cos(angle)
                            expression = expression[:acos_pos] + str(acos_value) + expression[angle_end:]
                        except ValueError:
                            result.set("Invalid Expression")
                            expression = ""
                            return
                    else:
                        result.set("Invalid Expression")
                        expression = ""
                        return
            # cos inverse end

            # cos start
            while "cos" in expression:
                cos_pos = expression.find("cos")
                if cos_pos != -1:
                    angle_start = cos_pos + 3  # Position after "sin"
                    angle_end = angle_start

                    # Find the end of the angle (until next operator or end of string)
                    while angle_end < len(expression) and expression[angle_end] not in ["*", "/", "+", "-", "(", ")"]:
                        angle_end += 1

                    angle_str = expression[angle_start:angle_end]

                    if angle_str:  # Ensure the angle is not empty
                        try:
                            angle = float(angle_str)
                            if angle==60.0:
                                cos_value=0.5
                            else:
                                cos_value = math.cos(math.radians(angle))
                            expression = expression[:cos_pos] + str(cos_value) + expression[angle_end:]
                        except ValueError:
                            result.set("Invalid Expression")
                            expression = ""
                            return
                    else:
                        result.set("Invalid Expression")
                        expression = ""
                        return
            # cos end

            # factorial start
            while "!" in expression:
                fact_pos = expression.find("!")

                # Check if there's a number before the "!" sign
                if fact_pos > 0 and expression[fact_pos - 1].isdigit():
                    num_end = fact_pos - 1
                    num_start = num_end

                    # Find the start of the number
                    while num_start > 0 and expression[num_start - 1].isdigit():
                        num_start -= 1

                    num = expression[num_start:fact_pos]

                    if num and fact_pos==len(expression)-1 or fact_pos<len(expression) and expression[fact_pos+1] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:  # checking num is empty or not
                        try:
                            number = int(num)
                            factorial = math.factorial(number)
                            expression = expression[:num_start] + str(factorial) + expression[fact_pos + 1:]
                        except ValueError:
                            result.set("Invalid Expression")
                            expression = ""
                            return
                    else:
                        result.set("Invalid Expression")
                        expression = ""
                        return
                else:
                    result.set("Invalid Expression")
                    expression = ""
                    return
            # factorial end

            # ∛ start
            while "∛" in expression:
                qube_root_pos = expression.find("∛")

                if qube_root_pos != -1:
                    coef_start = qube_root_pos

                    # Check if there is a number before the square root symbol (e.g., "3√")
                    if qube_root_pos > 0 and expression[qube_root_pos - 1].isdigit():
                        coef_start = qube_root_pos - 1
                        while coef_start > 0 and expression[coef_start - 1].isdigit():
                            coef_start -= 1
                        coefficient = expression[coef_start:qube_root_pos]
                    else:
                        coefficient = "1"  # Default to 1 if no number is found before "√"

                    num_start = qube_root_pos + 1
                    num_end = num_start

                    # Find the end of the number (until we reach an operator or the end of the string)
                    while num_end < len(expression) and (expression[num_end].isdigit()):
                        num_end += 1

                    num = expression[num_start:num_end]

                    if num:  # Ensure num is not empty
                        try:
                            number = float(num)
                            sqrt_result = number ** (1 / 3)
                            result_value = float(coefficient) * sqrt_result
                            # Round the result to avoid floating point precision issues
                            expression = expression[:coef_start] + str(round(result_value, 10)) + expression[num_end:]
                        except ValueError:
                            result.set("Invalid Expression")
                            expression = ""
                            return
                    else:
                        result.set("Invalid Expression")
                        expression = ""
                        return
                else:
                    result.set("Invalid Expression")
                    expression = ""
                    return
            # ∛ end

            # √ start
            while "√" in expression:
                sqrt_pos = expression.find("√")

                if sqrt_pos != -1:
                    coef_start = sqrt_pos

                    # Check if there is a number before the square root symbol (e.g., "3√")
                    if sqrt_pos > 0 and expression[sqrt_pos - 1].isdigit():
                        coef_start = sqrt_pos - 1
                        while coef_start > 0 and expression[coef_start - 1].isdigit():
                            coef_start -= 1
                        coefficient = expression[coef_start:sqrt_pos]
                    else:
                        coefficient = "1"  # Default to 1 if no number is found before "√"

                    num_start = sqrt_pos + 1
                    num_end = num_start

                    # Find the end of the number (until we reach an operator or the end of the string)
                    while num_end < len(expression) and (expression[num_end].isdigit() ):
                        num_end += 1

                    num = expression[num_start:num_end]

                    if num:  # Ensure num is not empty
                        try:
                            number = float(num)
                            sqrt_result = number ** (1/2)
                            result_value = float(coefficient) * sqrt_result
                            # Round the result to avoid floating point precision issues
                            expression = expression[:coef_start] + str(round(result_value, 10)) + expression[num_end:]
                        except ValueError:
                            result.set("Invalid Expression")
                            expression = ""
                            return
                    else:
                        result.set("Invalid Expression")
                        expression = ""
                        return
                else:
                    result.set("Invalid Expression")
                    expression = ""
                    return
            # √ end

            # π start
            while "π" in expression:
                pi_pos = expression.find("π")

                if pi_pos != -1:
                    # Check if there's a number before the "π" symbol
                    if pi_pos > 0 and expression[pi_pos - 1].isdigit():
                        num_end = pi_pos - 1
                        num_start = num_end

                        # Find the start of the number
                        while num_start > 0 and expression[num_start - 1].isdigit():
                            num_start -= 1

                        num = expression[num_start:pi_pos]

                        # Ensure num is not empty and check that there's no digit immediately after "π"
                        if num and (pi_pos == len(expression) - 1 or (
                                pi_pos < len(expression) - 1 and not expression[pi_pos + 1].isdigit())):
                            try:
                                number = float(num)
                                pi_val = number * 3.141592654
                                expression = expression[:num_start] + str(pi_val) + expression[pi_pos + 1:]
                            except ValueError:
                                result.set("Invalid Expression")
                                expression = ""
                                return
                        else:
                            result.set("Invalid Expression")
                            expression = ""
                            return
                    else:
                        # If there's no number before "π", just replace "π" with its value
                        expression = expression[:pi_pos] + "3.141592654" + expression[pi_pos + 1:]
                        result.set(expression)
                else:
                    result.set("Invalid Expression")
                    expression=""
                    return

            # π end

            # log start
            while "log " in expression:
                log_pos = expression.find("log ")
                if log_pos != -1:
                    val_start = log_pos + 4  # Position after "sin"
                    val_end = val_start

                    # Find the end of the angle (until next operator or end of string)
                    while val_end < len(expression) and expression[val_end] not in ["*", "/", "+", "-", "(", ")","π","∛","√","!"]:
                        val_end += 1

                    value = expression[val_start:val_end]

                    if value:  # Ensuring value is not empty
                        try:
                            log_value = math.log10(float(value))
                            expression = expression[:log_pos] + str(log_value) + expression[val_end:]
                        except ValueError:
                            result.set("Invalid Expression")
                            expression = ""
                            return
                    else:
                        result.set("Invalid Expression")
                        expression = ""
                        return
                else:
                    result.set("Invalid Expression")
                    expression = ""
                    return
            # log end

            # ln start
            while "ln " in expression:
                ln_pos = expression.find("ln ")
                if ln_pos != -1:
                    val_start = ln_pos + 3  # Position after "ln"
                    val_end = val_start

                    # Find the end of the angle (until next operator or end of string)
                    while val_end < len(expression) and expression[val_end] not in ["*", "/", "+", "-", "(", ")",
                                                                                        "π", "∛", "√", "!"]:
                        val_end += 1

                    value = expression[val_start:val_end]

                    if value:  # Ensuring value is not empty
                        try:
                            ln_value = math.log(float(value))
                            expression = expression[:ln_pos] + str(ln_value) + expression[val_end:]
                        except ValueError:
                            result.set("Invalid Expression")
                            expression = ""
                            return
                    else:
                        result.set("Invalid Expression")
                        expression = ""
                        return
                else:
                    result.set("Invalid Expression")
                    expression = ""
                    return
            # ln end

            # e^x start
            while "e" in expression:
                exp_pos = expression.find("e")
                if exp_pos != -1:
                    val_start = exp_pos + 1  # Position after "e"
                    val_end = val_start

                    # Find the end of the angle (until next operator or end of string)
                    while val_end < len(expression) and expression[val_end] not in ["*", "/", "+", "-", "(", ")",
                                                                                        "π", "∛", "√", "!"]:
                        val_end += 1

                    value = expression[val_start:val_end]

                    if value:  # Ensuring value is not empty
                        try:
                            exp_value = math.exp(float(value))
                            expression = expression[:exp_pos] + str(exp_value) + expression[val_end:]
                        except ValueError:
                            result.set("Invalid Expression")
                            expression = ""
                            return
                    else:
                        result.set("Invalid Expression")
                        expression = ""
                        return
                else:
                    result.set("Invalid Expression")
                    expression = ""
                    return
            # e^x end

            # nPr start
            while "P" in expression:
                p_pos = expression.find("P")
                if p_pos > 0:
                    n_end = p_pos - 1  # Position after "ln"
                    n_start = n_end
                    while n_start > 0 and expression[n_start - 1].isdigit():
                        n_start -= 1
                    n_value=expression[n_start:p_pos]

                    r_start=p_pos + 1
                    r_end=r_start
                    # Find the end of the angle (until next operator or end of string)
                    while r_end < len(expression) and expression[r_end] not in ["*", "/", "+", "-", "(", ")"]:
                        r_end += 1

                    r_value = expression[r_start:r_end]

                    if n_value and r_value:  # Ensuring value is not empty
                        try:
                            npr = math.factorial(int(n_value))/math.factorial(int(int(n_value)-int(r_value)))
                            expression = expression[:n_start] + str(npr) + expression[r_end:]
                        except ValueError:
                            result.set("Invalid Expression")
                            expression = ""
                            return
                    else:
                        result.set("Invalid Expression")
                        expression = ""
                        return
                else:
                    result.set("Invalid Expression")
                    expression = ""
                    return
            # nPr end

            # nCr start
            while "C" in expression:
                c_pos = expression.find("C")
                if c_pos > 0:
                    n_end = c_pos - 1  # Position after "ln"
                    n_start = n_end
                    while n_start > 0 and expression[n_start - 1].isdigit():
                        n_start -= 1
                    n_value=expression[n_start:c_pos]

                    r_start=c_pos + 1
                    r_end=r_start
                    # Find the end of the angle (until next operator or end of string)
                    while r_end < len(expression) and expression[r_end] not in ["*", "/", "+", "-", "(", ")"]:
                        r_end += 1

                    r_value = expression[r_start:r_end]

                    if n_value and r_value:  # Ensuring value is not empty
                        try:
                            ncr = math.factorial(int(n_value))/((math.factorial(int(r_value)))*(math.factorial(int(int(n_value)-int(r_value)))))
                            expression = expression[:n_start] + str(ncr) + expression[r_end:]
                        except ValueError:
                            result.set("Invalid Expression")
                            expression = ""
                            return
                    else:
                        result.set("Invalid Expression")
                        expression = ""
                        return
                else:
                    result.set("Invalid Expression")
                    expression = ""
                    return
            #nCr end

            if expression != "":
                total = str(eval(expression))
            else:
                total = ""
            if len(total)>25:
                total=str(round(float(total),20))
            expression = total
            shift_flag=0
            temp1 = expression[-1]
            temp2 = expression[-2]
            result.set(expression)

    except Exception as e:
        result.set("Invalid Expression")
        expression = ""
def on_func():
    global on_flag,expression,shift_flag,temp1,temp2
    on_flag = 1
    if shift_flag==2:
        shift_flag=0
    temp1 = ""
    temp2 = ""
    expression=""
    result.set(expression)
def shift():
    global shift_flag,on_flag
    if on_flag==1:
        shift_flag=1
def delete_one():
    global expression,temp1,temp2,shift_flag,on_flag
    if on_flag==1:
        expression=expression[0:-1]
        if len(expression) == 1:
            temp1=expression[-1]
            temp2=""
        if len(expression) >= 2:
            temp1 = expression[-1]
            temp2 = expression[-2]
        shift_flag=0
        result.set(expression)
def delete_all():
    global expression,shift_flag,on_flag,temp1,temp2
    if on_flag==1:
        if shift_flag==1:
            on_flag=0
            expression="Thank You!"
            shift_flag=2
        else:
            temp1=""
            temp2=""
            expression=""
            shift_flag=0
        result.set(expression)

if __name__=="__main__":
    form = Tk()
    form.title("Calculator")
    form.geometry("450x550")
    form.minsize(420,540)

    frame = Frame(form, relief="solid", background="#6B6B6B",bd=2,padx=5,pady=5)

    heading = Label(frame, text="SCIENTIFIC CALCULATOR", font=("Times New Roman", 15, "bold")
    , height=1, width=31, fg="white", bg="#6B6B6B",pady=5)
    heading.grid(row=0, column=0, columnspan=5)
    result = StringVar()
    result.set(expression) # displaying welcome message
    screen = Entry(frame, font=("Times New Roman",20),bd=4,textvariable=result,state=DISABLED) #disabling screen to get input directly from keyboard
    screen.grid(row=1, column=0, columnspan=5, sticky=EW)

    #row1
    inverse = Button(frame, text="x^-1 / x!", fg="black", bg="#8B8878", command=lambda :click("!" if shift_flag == 1 else "x^-1"), height=2, width=8)
    inverse.grid(row=2, column=0, pady=5)
    ncr = Button(frame, text="nCr / nPr", fg="black", bg="#8B8878", command=lambda: click("P" if shift_flag==1 else "C"), height=2, width=8)
    ncr.grid(row=2, column=1, padx=2, pady=5)
    square = Button(frame, text="x^2", fg="black", bg="#8B8878", command=lambda: click("x^2"), height=2, width=8)
    square.grid(row=2, column=2, padx=2, pady=5)
    x3 = Button(frame, text="x^3 / ∛", fg="black", bg="#8B8878", command=lambda: click("∛" if shift_flag == 1 else "x^3"), height=2, width=8)
    x3.grid(row=2, column=3, padx=2, pady=5)
    on = Button(frame, text="On", fg="black", bg="#009ACD", command=on_func, height=2, width=8)
    on.grid(row=2, column=4, padx=2, pady=5)

    #row2
    pow = Button(frame, text="^", fg="black", bg="#8B8878", command=lambda: click("^"), height=2, width=8)
    pow.grid(row=3, column=0, pady=5)
    root = Button(frame, text="√", fg="black", bg="#8B8878", command=lambda: click("√"), height=2, width=8)
    root.grid(row=3, column=1, padx=2, pady=5)
    log = Button(frame, text="log / 10^x", fg="black", bg="#8B8878", command=lambda: click("10^x" if shift_flag==1 else "log "), height=2, width=8)
    log.grid(row=3, column=2, padx=2, pady=5)
    ln = Button(frame, text="ln / e", fg="black", bg="#8B8878", command=lambda: click("e" if shift_flag==1 else "ln "), height=2, width=8)
    ln.grid(row=3, column=3, padx=2, pady=5)
    pi = Button(frame, text="π", fg="black", bg="#8B8878", command=lambda: click("π"), height=2, width=8)
    pi.grid(row=3, column=4, padx=2, pady=5)

    #row3
    sin = Button(frame, text="sin/sin^-1", fg="black", bg="#8B8878", command=lambda: click("sin^-1 " if shift_flag == 1 else "sin "),height=2, width=8)
    sin.grid(row=4, column=0, pady=5)
    cos = Button(frame, text="cos/cos^-1", fg="black", bg="#8B8878", command=lambda: click("cos^-1 " if shift_flag == 1 else "cos "), height=2, width=8)
    cos.grid(row=4, column=1, padx=2, pady=5)
    tan = Button(frame, text="tan/tan^-1", fg="black", bg="#8B8878", command=lambda: click("tan^-1 " if shift_flag == 1 else "tan "), height=2, width=8)
    tan.grid(row=4, column=2, padx=2, pady=5)
    modulus = Button(frame, text="(", fg="black", bg="#8B8878", command=lambda: click('('), height=2, width=8)
    modulus.grid(row=4, column=3, padx=2, pady=5)
    mod = Button(frame, text=")", fg="black", bg="#8B8878", command=lambda: click(')'), height=2, width=8)
    mod.grid(row=4, column=4, padx=2, pady=5)

    #row4
    number7=Button(frame,text="7", fg="black", bg="#C1CDCD", command=lambda :click(7),height=2,width=8)
    number7.grid(row=5,column=0,pady=5)
    number8=Button(frame,text="8", fg="black", bg="#C1CDCD", command=lambda :click(8),height=2,width=8)
    number8.grid(row=5,column=1,padx=2,pady=5)
    number9=Button(frame,text="9", fg="black", bg="#C1CDCD", command=lambda :click(9),height=2,width=8)
    number9.grid(row=5,column=2,padx=2,pady=5)
    deletes=Button(frame,text="DEL", fg="black", bg="#EE3B3B", command=delete_one,height=2,width=8)
    deletes.grid(row=5,column=3,padx=2,pady=5)
    ac= Button(frame, text="AC", fg="black", bg="#EE3B3B", command=delete_all, height=2, width=8)
    ac.grid(row=5, column=4, padx=2, pady=5)

    #row5
    number4=Button(frame,text="4", fg="black", bg="#C1CDCD", command=lambda :click(4),height=2,width=8)
    number4.grid(row=6,column=0,pady=5)
    number5=Button(frame,text="5", fg="black", bg="#C1CDCD", command=lambda :click(5),height=2,width=8)
    number5.grid(row=6,column=1,padx=5,pady=5)
    number6=Button(frame,text="6", fg="black", bg="#C1CDCD", command=lambda :click(6),height=2,width=8)
    number6.grid(row=6,column=2,pady=5)
    number_mul=Button(frame,text="X", fg="black", bg="#C1CDCD", command=lambda :click('*'),height=2,width=8)
    number_mul.grid(row=6,column=3,pady=5)
    number_divide = Button(frame, text="/", fg="black", bg="#C1CDCD", command=lambda: click('/'), height=2, width=8)
    number_divide.grid(row=6, column=4, pady=5)

    #row6
    number1=Button(frame,text="1", fg="black", bg="#C1CDCD", command=lambda :click(1),height=2,width=8)
    number1.grid(row=7,column=0,pady=5)
    number2=Button(frame,text="2", fg="black", bg="#C1CDCD", command=lambda :click(2),height=2,width=8)
    number2.grid(row=7,column=1,padx=5,pady=5)
    number3=Button(frame,text="3", fg="black", bg="#C1CDCD", command=lambda :click(3),height=2,width=8)
    number3.grid(row=7,column=2,pady=5)
    plus=Button(frame,text="+", fg="black", bg="#C1CDCD", command=lambda :click('+'),height=2,width=8)
    plus.grid(row=7,column=3,pady=5)
    minus = Button(frame, text="-", fg="black", bg="#C1CDCD", command=lambda: click('-'), height=2, width=8)
    minus.grid(row=7, column=4, pady=5)

    #row7
    number0=Button(frame,text="0", fg="black", bg="#C1CDCD", command=lambda :click(0),height=2,width=8)
    number0.grid(row=8,column=0,pady=5)
    point=Button(frame,text=".", fg="black", bg="#C1CDCD", command=lambda :click('.'),height=2,width=8)
    point.grid(row=8,column=1,padx=5,pady=5)
    shift=Button(frame,text="Shift", fg="black", bg="#EEAD0E", command=shift,height=2,width=8)
    shift.grid(row=8,column=2,pady=5)
    ans = Button(frame, text="%", fg="black", bg="#C1CDCD", command=lambda: click('%'), height=2, width=8)
    ans.grid(row=8, column=3, pady=5)
    equal = Button(frame, text="=", fg="black", bg="#66CD00", command=equal, height=2, width=8)
    equal.grid(row=8, column=4, pady=5)
    frame.pack(padx=10,pady=50)
    form.mainloop()
