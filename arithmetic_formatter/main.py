from pytest import main

from arithmetic_arranger import arithmetic_arranger

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

main(['-vv', 'test_module.py::test_template'])