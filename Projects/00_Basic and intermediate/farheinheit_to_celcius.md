Here's a question and worked explanation using your code.

**Question**

Sam writes a program to convert temperatures from Fahrenheit to Celsius:

```python
def fahrenheit_to_celsius(far):
    celsius = (far - 32) * 5 / 9
    return celsius

def main():
    far = float(input("Enter your degree in fahrenheit  "))
    value = fahrenheit_to_celsius(far)
    print(value)

if __name__ == "__main__":
    main()
```

a) Trace the program when the user enters `212`. What is printed?
b) Why does the program use `float()` on the input instead of `int()`?
c) What would happen if the `return` statement were replaced with `print(celsius)`?
d) The program prints `37.77777777777778` for an input of `100`. Suggest one way to make the output show only two decimal places.

---

**Explanation**

**a) Tracing the execution.** The program starts at `main()`. The line `far = float(input(...))` pauses and waits for the user, storing whatever is typed as a number in `far`. With `212`, that gives `far = 212.0`.

Control then jumps into `fahrenheit_to_celsius(212.0)`. The parameter `far` inside the function is a *local* variable — it's a separate box from the `far` in `main`, even though they share a name. The calculation runs:
$$celsius = (212 - 32) \times \frac{5}{9} = 180 \times \frac{5}{9} = 100.0$$
`return celsius` sends the value `100.0` back to `main`, where it is stored in `value`. `print(value)` outputs `100.0`. The function ends, `main()` ends, and the program finishes.

**b) Why `float()`.** Temperature in Celsius rarely lands on a whole number — as the `100` example shows, the result is `37.777…`. Using `int()` would throw away any decimal the user types and would even raise a `ValueError` if the user entered something like `98.6`. Since `input()` always returns a **string**, the conversion function is required regardless; `float()` just preserves the full precision of the value.

**c) Return vs. print.** This is the key idea. `return` hands a value *back* to the caller so it can be stored, reused, or further processed. `print` only displays text on the screen and hands back `None`. So if the function printed instead of returned, `value` would become `None`, and `print(value)` in `main` would output `None` — you'd see the number once (from inside the function) then `None`, and the result would be useless for anything else, like averaging several temperatures.

**d) Rounding the output.** Wrap the value in the built-in `round` function, e.g. `print(round(value, 2))`, which gives `37.78`. An f-string works just as well: `print(f"{value:.2f}")`.

