class store_results:
    results_file = "./results.txt"

    def __init__(self, function_ref):
        self.function_ref = function_ref

    def __call__(self, *args):
        with open(self.results_file, "a") as file:
            file.write(f"Function {self.function_ref.__name__} was called. Result: {self.function_ref(*args)}\n")
        return self.function_ref(*args)


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
