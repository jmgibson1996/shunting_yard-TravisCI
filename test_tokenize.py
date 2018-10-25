
import unittest
import shunting_yard as sy


class TokenizeTest(unittest.TestCase):
    def test_single_operator(self):
        print(self._testMethodName)
        tokens = list(sy.tokenize('2*2'))
        self.assertListEqual(tokens, ['2', '*', '2'])

    def test_multiple_operators(self):
        print(self._testMethodName)
        tokens = list(sy.tokenize('(1+2)-(3*4)/5'))
        self.assertListEqual(tokens, ['(', '1', '+', '2', ')', '-', '(', '3', '*', '4', ')', '/', '5'])

class StackIsEmptyTest(unittest.TestCase):
    def test_empty_stack(self):
        print(self._testMethodName)
        stack = list('')
        result = sy.stackIsEmpty(stack)
        assert len(stack) == 0

    def test_occupied_stack(self):
        print(self._testMethodName)
        stack = list('0+1+1+2+3+5+8+13+21+34+55')
        result = sy.stackIsEmpty(stack)
        assert len(stack) != 0

class PushToStackTest(unittest.TestCase):
    def test_if_token_added(self):
        print(self._testMethodName)
        stack = list('(6*6)+(8*8)]')
        sy.pushToStack(stack, '[')
        self.assertListEqual(stack, ['[', '(', '6', '*', '6', ')', '+', '(', '8', '*', '8', ')', ']'])

    def test_if_multi_digit_token_added(self):
        print(self._testMethodName)
        tokens = list('+(6*4)')
        sy.pushToStack(tokens, '10')
        self.assertListEqual(tokens, ['10', '+', '(', '6', '*', '4', ')'])

class PopFromStackTest(unittest.TestCase):
    def test_if_token_removed(self):
        print(self._testMethodName)
        stack = list('-[(6*6)+(8*8)]')
        sy.popFromStack(stack)
        self.assertListEqual(stack, ['[', '(', '6', '*', '6', ')', '+', '(', '8', '*', '8', ')', ']'])

class PeekAtStackTest(unittest.TestCase):
    def test_look_at_top_of_stack(self):
        print(self._testMethodName)
        stack = list('3*[(14+15)-9/2-(6+5)]*359')
        result = sy.peekAtStack(stack)
        assert result == stack[0]

class IsRightBracketTest(unittest.TestCase):
    def test_if_right_parenthesis(self):
        print(self._testMethodName)
        tokens = list('(24+1)/5')
        i = 0
        # iterate through inString and check each token
        for i in range(len(tokens)):
            result = sy.isRightBracket(tokens[i])
            if tokens[i] == ')':
                assert result == True
            else:
                assert result == False
    
    def test_if_right_bracket(self):
        print(self._testMethodName)
        tokens = list('[7*7]+1')
        i = 0
        # iterate through inString and check each token
        for i in range(len(tokens)):
            result = sy.isRightBracket(tokens[i])
            if tokens[i] == ']':
                assert result == True
            else:
                assert result == False

class IsOperatorTest(unittest.TestCase):
    def test_if_operator(self):
        print(self._testMethodName)
        operators = '+-*/'
        tokens = list('[(4*5)-(5*3)]/5')
        i = 0
        # iterate through inString and check each token
        for i in range(len(tokens)):
            result = sy.isOperator(tokens[i])
            if tokens[i] in operators:
                assert result == True
            else:
                assert result == False

class IsNumberTest(unittest.TestCase):
    def test_if_number(self):
        print(self._testMethodName)
        numbers = '1234567890'
        tokens = list('[(9+7-5*3/1)]')
        i = 0
        # iterate through inString and check each token
        for i in range(len(tokens)):
            result = sy.isNumber(tokens[i])
            if tokens[i] in numbers:
                assert result == True
            else:
                assert result == False

    def test_if_double_digit_is_number(self):
        print(self._testMethodName)
        numbers = '1234567890'
        tokens = list('[(10+70-50*30/10)]')
        i = 0
        # iterate through inStrng and chekc each token
        for i in range(len(tokens)):
            result = sy.isNumber(tokens[i])
            if tokens[i] in numbers:
                assert result == True
            else:
                assert result == False

class IsLeftBracketTest(unittest.TestCase):
    def test_if_left_parenthesis(self):
        print(self._testMethodName)
        tokens = list('(6+6)-(2+2)')
        i = 0
        # iterate through inString and check each token
        for i in range(len(tokens)):
            result = sy.isLeftBracket(tokens[i])
            if tokens[i] == '(':
                assert result == True
            else:
                assert result == False

    def test_if_left_bracket(self):
        print(self._testMethodName)
        tokens = list('[9*9]/[5*5]')
        i = 0
        # iterate through inString and check each tokenn
        for i in range(len(tokens)):
            result = sy.isLeftBracket(tokens[i])
            if tokens[i] == '[':
                assert result == True
            else:
                assert result == False

class IsDigitTest(unittest.TestCase):
    def test_single_digit_numuber_is_digit(self):
        print(self._testMethodName)
        result = sy.isDigit('7')
        assert result == True
    
    def test_multi_digit_number_is_digit(self):
        print(self._testMethodName)
        result = sy.isDigit('42')
        assert result == True

    def test_numbers_in_stack(self):
        print(self._testMethodName)
        characters = list('(32*(16+8)-[4/2]')
        i = 0
        # iterate through inString and check each token
        for i in range(len(characters)):
            result = sy.isDigit(characters[i])
            if result is True:
                assert result == True
            else:
                assert result == False

class InfixToPostfixTest(unittest.TestCase):
    # Infix -> Postfix : A+B -> AB+
    def test_infix_to_postfix_simple(self):
        print(self._testMethodName)
        inString = list('9+19')
        result0 = list(sy.infixToPostfix(inString))
        self.assertListEqual(result0, ['9', ' ', '19', ' ', '+'])
        
        inString = list('66-6')
        result1 = list(sy.infixToPostfix(inString))
        self.assertListEqual(result1, ['66', ' ', '6', ' ', '-'])
        
        inString = list('2*3')
        result2 = list(sy.infixToPostfix(inString))
        self.assertListEqual(result2, ['2', ' ', '3', ' ', '*'])
        
        inString = list('4/1')
        result3 = list(sy.infixToPostfix(inString))
        self.assertListEqual(result3, ['4', ' ', '1', ' ', '/'])
    
    def test_infix_to_postfix_brackets(self):
        print(self._testMethodName)
        inString0 = list('(7*8)/2')
        result0 = list(sy.infixToPostfix(inString0))
        self.assertListEqual(result0, ['7', ' ', '8', ' ', '*', ' ', '2', ' ', '/'])

        inString1 = list('[9*9]-5')
        result1 = list(sy.infixToPostfix(inString1))
        self.assertListEqual(result1, ['9', ' ', '9', ' ', '*', ' ', '5', ' ', '-'])
    
    def test_infix_to_postfix_complex(self):
        print(self._testMethodName)
        inString = list('[100-(4*5)+9]/7+2*(6/3)-4')
        result = list(sy.infixToPostfix(inString))
        self.assertListEqual(result, ['100', ' ', '4', ' ', '5', ' ', '*', ' ', '-', '9', ' ', '+', ' ', '7', ' ', '/', ' ', '2', ' ', '6', ' ', '3', ' ', '/', ' ', '*', ' ', '+', ' ', '4', ' ', '-'])

    def test_infix_to_postfix_with_letters(self):
        print(self._testMethodName)
        inString = list('A+B-C*D/E')
        result = list(sy.infixToPostfix(inString))
        self.assertListEqual(result, ['+', ' ', '*', ' ', '/', ' ', '-'])

    def test_infix_to_postfix_with_special_characters(self):
        print(self._testMethodName)
        inString = list('~+!-@*#/$+%-^*&/{+}-\*|/:+;-,*</.+>-?*"/`"')
        result = list(sy.infixToPostfix(inString))
        self.assertListEqual(result, ['+', ' ', '*', ' ', '/', ' ', '-', ' ', '+', ' ', '*', ' ', '/', ' ', '-', ' ', '+', ' ', '*', ' ', '/', ' ', '-', ' ', '+', ' ', '*', ' ', '/', ' ', '-', ' ', '+', ' ', '*', ' ', '/', ' ', '-'])

    def test_infix_to_postfix_with_only_operators(self):
        print(self._testMethodName)
        inString0 = list('+-*/')
        result0 = list(sy.infixToPostfix(inString0))
        self.assertListEqual(result0, ['+', ' ', '*', ' ', '/', ' ', '-'])

        inString1 = list('/*-+')
        result1 = list(sy.infixToPostfix(inString1))
        self.assertListEqual(result1, ['/', ' ', '*', ' ', '-', ' ', '+'])

class ComparePrecedenceTest(unittest.TestCase):
    def test_left_lower_right(self):
        print(self._testMethodName)
        result0 = sy.comparePrecedence('+', '*')
        assert result0 == -1

        result1 = sy.comparePrecedence('+', '/')
        assert result1 == -1
        
        result2 = sy.comparePrecedence('-', '*')
        assert result2 == -1
        
        result3 = sy.comparePrecedence('-', '/')
        assert result3 == -1
    
    def test_left_equal_right(self):
        print(self._testMethodName)
        result0 = sy.comparePrecedence('+', '-')
        assert result0 == 0

        result1 = sy.comparePrecedence('-', '+')
        assert result1 == 0
    
    def test_left_highter_right(self):
        print(self._testMethodName)
        result0 = sy.comparePrecedence('*', '+')
        assert result0 == 1

        result1 = sy.comparePrecedence('*', '-')
        assert result1 == 1

        result2 = sy.comparePrecedence('/', '+')
        assert result2 == 1

        result3 = sy.comparePrecedence('/', '-')
        assert result3 == 1

class AppendToOutputTest(unittest.TestCase):
    def test_append_to_empty_outString(self):
        print(self._testMethodName)
        outString = list('')
        token = '8'
        sy.appendToOutput(outString, token)
        self.assertListEqual(outString, ['8'])

    def test_append_to_occupied_outString(self):
        print(self._testMethodName)
        outString = list('36 - 2 ( 20 + 12 / 4 * 3 - 2 * 2 ) +')
        token = '10'
        sy.appendToOutput(outString, token)
        self.assertListEqual(outString, ['36', '-', '2', '(', '20', '+', '12', '/', '4', '*', '3', '-', '2', '*', '2', ')', '+', '10'])
