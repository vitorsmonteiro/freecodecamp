def arithmetic_arranger(problems, print_res=False):
  errors = catch_exceptions(problems)
  if errors:
    return errors
  first_line = ""
  second_line = ""
  split_line = ""
  res_line = ""
  aux = ""
  num_probs = len(problems)
  for i, prob in enumerate(problems):
    items = prob.split()
    top_num = items[0]
    oper = items[1]
    bot_num = items[2]
    num_digits = max(len(top_num), len(bot_num)) + 2
    separator = 4 * " " if i < num_probs - 1 else ""
    first_line += ((num_digits - len(top_num)) * " " + str(top_num) + separator)
    second_line += (oper + " " + (num_digits - len(bot_num) - 2) * " " + str(bot_num) + separator)
    split_line += (num_digits * "-" + separator)
    if print_res:
      res = float(top_num) + float(bot_num) if  oper == "+" else float(top_num) - float(bot_num)
      res_line += ((num_digits - len(str(int(res)))) * " " + str(int(res)) + separator)
      aux = "\n"
  arranged_problems = first_line + "\n" + second_line + "\n" + split_line + aux + res_line
  return arranged_problems

def catch_exceptions(calcs):
  if len(calcs) > 5:
    return "Error: Too many problems."
  for calc in calcs:
    items = calc.split()
    if len(items) > 3:
      return "Error: Missing inputs"
    for item in (items[0], items[2]):
      if len(item) > 4:
        return "Error: Numbers cannot be more than four digits."
      try:
        float(item)
      except:
        return "Error: Numbers must only contain digits."
    if items[1] not in ("+", "-"):
      return "Error: Operator must be '+' or '-'."
    
  return False
  