# functions with outputs

def format_name(f_name, l_name):
  """
  Take the 1st and last name and format it
  to return the title case version of the name
  """
  if f_name == "" or l_name == "":
    return "You didn't provide a valid input"
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"{formated_f_name} {formated_l_name}"

formated_string = format_name("AliNE", "AYUMI")
print(formated_string)