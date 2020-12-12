def convert_temp(unit_in, unit_out, temp):
    """Convert farenheit <-> celsius and return results.

    C = (f-32)/1.8
    F = (1.8*c)+32

    - unit_in: either "f" or "c" 
    - unit_out: either "f" or "c"
    - temp: temperature (in f or c, depending on unit_in)

    Return results of conversion, if any.

    If unit_in or unit_out are invalid, return "Invalid unit [UNIT_IN]".

    For example:

      convert_temp("c", "f", 0)  =>  32.0
      convert_temp("f", "c", 212) => 100.0
    """
    #todo: invalid number check
    # YOUR CODE HERE
    if unit_in == unit_out and (temp is int or float):
          return unit_in
    elif unit_in.lower() == "c" and unit_out.lower() =="f" and (temp is int or float):
        return (1.8*temp)+32
    elif unit_in.lower() =="f" and unit_out.lower() =="c" and (temp is int or float):
        return (temp-32)/1.8
    else:
        return "Invalid unit [UNIT_IN]"


print("c", "f", 0, convert_temp("c", "f", 0), "should be 32.0")
print("f", "c", 212, convert_temp("f", "c", 212), "should be 100.0")
print("z", "f", 32, convert_temp("z", "f", 32), "should be Invalid unit z")
print("c", "z", 32, convert_temp("c", "z", 32), "should be Invalid unit z")
print("f", "f", 75.5, convert_temp("f", "f", 75.5), "should be 75.5")

