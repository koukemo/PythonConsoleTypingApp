class StandardInputreader:
    @staticmethod
    def input_int(message: str = "> ") -> int:
        """Receives standard input of numerical values.

        Args:
            message (str): Message to be displayed when input is accepted.

        Yeilds:
            int: The number entered.
        """
        while True:
            try:
                input_num = int(input(message))
                break
            except ValueError:
                print("A numeric value was not entered.")
                print("Please try again.")
        
        return input_num
    
    @staticmethod
    def input_string(message: str = "> ") -> str:
        """Receives standard input of strings.

        Args:
            message (str): Message to be displayed when input is accepted.

        Yeilds:
            str: The string entered.
        """
        input_str = input(message)

        return input_str