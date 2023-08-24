======
CLIMBER
======

.. code:: python

    import climber as cb 

    parser = cb.Parser()
    
    @parser(return_type=int)
    @parser.arg(name="num1", required=True, type=int)
    @parser.arg(name="num2", required=True, type=int)
    def add_2(num1: int, num2: int) -> int:
        if parser.validate(num1, num2):
            return num1 + num2
        raise RuntimeError

