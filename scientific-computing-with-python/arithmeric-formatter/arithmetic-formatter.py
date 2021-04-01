# Project: Arithmetic Formatter
# Course: Scientific Computing with Python (freeCodeCamp)
# Programming language: Python
# Developer: Valeriy B.


# Creating an function with one optional argument *result
def arithmetic_arranger(problems, *result):
    
    # Checking ERROR situations
    # 1 Verifying if max number of problems is 5
    if len(problems) > 5:
        return "Error: Too many problems."
    else:

        # 2 Verifying if operators are 'addition' or 'substraction'
        plus_minus = []
        for p in problems:
            if p.split()[1] == "+" or p.split()[1] == "-":
                plus_minus.append(0)
            else:
                plus_minus.append(1)
        if 1 in plus_minus:
            return "Error: Operator must be '+' or '-'."
        else:

            # 3 verifing if numbers are digits
            digits = []
            for d in problems:
                if d.split()[0].isdigit() and d.split()[2].isdigit():
                    digits.append(0)
                else:
                    digits.append(1)
            if 1 in digits:
                return "Error: Numbers must only contain digits."
            else:

                # 4 Verifying if problems numbers are not bigger than four digits
                more_than_4 = []
                for m in problems:
                    if len(m.split()[0]) <= 4 and len(m.split()[2]) <= 4:
                        more_than_4.append(0)
                    else:
                        more_than_4.append(1)
                if 1 in more_than_4:
                    return "Error: Numbers cannot be more than four digits."
                else:

                    # Counting the maximum length of an element in the problem to right align elements properly
                    number_length = []
                    for problem in problems:
                        elem_length = []
                        for elem in problem.split():
                            elem_length.append(len(elem))
                        number_length.append(max(elem_length))

                    # Creating a list with formatted rows
                    formatted_list = []
                    c = 0
                    row_list_1 = []
                    row_list_2 = []
                    row_list_3 = []
                    row_list_4 = []
                    for problem in problems:
                        row_list_1.append(problem.split()[0].rjust(number_length[c] + 2))
                        row_list_2.append(problem.split()[1] + " " + problem.split()[2].rjust(number_length[c]))
                        row_list_3.append("-" * (number_length[c] + 2))
                        row_list_4.append(str(eval(problem.split()[0] + problem.split()[1] + problem.split()[2])).rjust(number_length[c] + 2))
                        c += 1

                    # Verifying if optional argument exists
                    if result:
                        formatted_list = ["    ".join(row_list_1), "    ".join(row_list_2), "    ".join(row_list_3), "    ".join(row_list_4)]
                    else:
                        formatted_list = ["    ".join(row_list_1), "    ".join(row_list_2), "    ".join(row_list_3)]
                    
                    # Returning the result
                    final_string = "\n".join(formatted_list)
                    return final_string

print(arithmetic_arranger(["32 + 258", "3801 - 2", "45 + 43", "123 + 49"], True))