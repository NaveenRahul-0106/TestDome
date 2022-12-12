'''
As part of a data processing pipeline, complete the implementation of the pipeline method:

1. The pipeline method should accept a variable number of functions, and it should return a new function that accepts one parameter arg.
2. The returned function should call the first function in pipeline with the parameter arg,
 and call the second function with the result of the first function.
3. The returned function should continue calling each function in pipeline in order, 
following the same pattern, and return the value from the last function.

For example, calling pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2), 
and then calling the returned function with 3 should return 5.0.
'''

def pipeline(*funcs):
    def helper(arg):
        x = arg
        for f in funcs:
            x = f(x)
        return x
    return helper
            
fun = pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2)
print(fun(3))