
import unittest
import shunting_yard as sy


class TokenizeTest(unittest.TestCase):
    def test_single_operator(self):
        print(self._testMethodName)
        tokens = list(sy.tokenize('2*2'))
        self.assertListEqual(tokens, ['2', '*', '2'])
        print(tokens)

    def test_multiple_operators(self):
        print(self._testMethodName)
        tokens = list(sy.tokenize('(1+2)-(3*4)/5'))
        self.assertListEqual(tokens, ['(', '1', '+', '2', ')', '-', '(', '3', '*', '4', ')', '/', '5'])
        print(tokens)

class StackIsEmptyTest(unittest.TestCase):
    def test_empty_stack(self):
        print(self._testMethodName)
        stack = list('')
        result = sy.stackIsEmpty(stack)
        if result is True:
            print(result, ':', len(stack))
        else:
            print(result, ':', len(stack))

    def test_occupied_stack(self):
        print(self._testMethodName)
        stack = list('0+1+1+2+3+5+8+13+21+34+55')
        result = sy.stackIsEmpty(stack)
        if result == 0:
            print(result, ':', len(stack))
        else:
            print(result, ':', len(stack))

class PushToStackTest(unittest.TestCase):
    def test_if_token_added(self):
        print(self._testMethodName)
        stack = list('(6*6)+(8*8)]')
        print(stack)
        sy.pushToStack(stack, '[')
        self.assertListEqual(stack, ['[', '(', '6', '*', '6', ')', '+', '(', '8', '*', '8', ')', ']'])
        print(stack)

    def test_if_multi_digit_token_added(self):
        print(self._testMethodName)
        tokens = list('+(6*4)')
        print(tokens)
        sy.pushToStack(tokens, '10')
        self.assertListEqual(tokens, ['10', '+', '(', '6', '*', '4', ')'])
        print(tokens)

class PopFromStackTest(unittest.TestCase):
    def test_if_token_removed(self):
        print(self._testMethodName)
        stack = list('-[(6*6)+(8*8)]')
        print(stack)
        sy.popFromStack(stack)
        self.assertListEqual(stack, ['[', '(', '6', '*', '6', ')', '+', '(', '8', '*', '8', ')', ']'])
        print(stack)

class PeekAtStackTest(unittest.TestCase):
    def test_look_at_top_of_stack(self):
        print(self._testMethodName)
        stack = list('3*[(14+15)-9/2-(6+5)]*359')
        print(stack)
        result = sy.peekAtStack(stack)
        print(result)

class IsRightBracketTest(unittest.TestCase):
    def test_if_right_parenthesis(self):
        print(self._testMethodName)
        tokens = list('(24+1)/5')
        i = 0
        # iterate through inString and check each token
        for i in range(len(tokens)):
            result = sy.isRightBracket(tokens[i])
            if result is True:
                print(result, ':', tokens[i])
            else:
                print(result, ':', tokens[i])
    
    def test_if_right_bracket(self):
        print(self._testMethodName)
        tokens = list('[7*7]+1')
        i = 0
        # iterate through inString and check each token
        for i in range(len(tokens)):
            result = sy.isRightBracket(tokens[i])
            if result is True:
                print(result, ':', tokens[i])
            else:
                print(result, ':', tokens[i])

    def test_if_multi_digit_token_added(self):
        print(self._testMethodName)
        tokens = list('+(6*4)')
        print(tokens)
        sy.pushToStack(tokens, '10')
        self.assertListEqual(tokens, ['10', '+', '(', '6', '*', '4', ')'])
        print(tokens)

class PopFromStackTest(unittest.TestCase):
    def test_if_token_removed(self):
        print(self._testMethodName)
        stack = list('-[(6*6)+(8*8)]')
        print(stack)
        sy.popFromStack(stack)
        self.assertListEqual(stack, ['[', '(', '6', '*', '6', ')', '+', '(', '8', '*', '8', ')', ']'])
        print(stack)

class PeekAtStackTest(unittest.TestCase):
    def test_look_at_top_of_stack(self):
        print(self._testMethodName)
        stack = list('3*[(14+15)-9/2-(6+5)]*359')
        print(stack)
        result = sy.peekAtStack(stack)
        print(result)

class IsRightBracketTest(unittest.TestCase):
    def test_if_right_parenthesis(self):
        print(self._testMethodName)
        tokens = list('(24+1)/5')
        i = 0
        # iterate through inString and check each token
        for i in range(len(tokens)):
            result = sy.isRightBracket(tokens[i])
            if result is True:
                print(result, ':', tokens[i])
            else:
                print(result, ':', tokens[i])
    
    def test_if_right_bracket(self):
        print(self._testMethodName)
        tokens = list('[7*7]+1')
        i = 0
        # iterate through inString and check each token
        for i in range(len(tokens)):
            result = sy.isRightBracket(tokens[i])
            if result is True:
                print(result, ':', tokens[i])
            else:
                print(result, ':', tokens[i])

    def test_if_left_bracket(self):
        print(self._testMethodName)
        tokens = list('[9*9]/[5*5]')
        i = 0
        # iterate through inString and check each token
        for i in range(len(tokens)):
            result = sy.isLeftBracket(tokens[i])
            if result == True:
                print(result, ':', tokens[i])
            else:
                print(result, ':', tokens[i])

class IsDigitTest(unittest.TestCase):
    def test_single_digit_numuber_is_digit(self):
        print(self._testMethodName)
        result = sy.isDigit('7')
        if result is True:
            print(result)
        else:
            print(result)
    
    def test_multi_digit_number_is_digit(self):
        print(self._testMethodName)
        result = sy.isDigit('42')
        if result is True:
            print(result)
        else:
            print(result)

    def test_numbers_in_stack(self):
        print(self._testMethodName)
        characters = list('(32*(16+8)-[4/2]')
        i = 0
        # iterate through inString and check each token
        for i in range(len(characters)):
            result = sy.isDigit(characters[i])
            if result is True:
                print(result, ':', characters[i])
            else:
                print(result, ':', characters[i])

class InfixToPostfixTest(unittest.TestCase):
    # Infix -> Postfix : A+B -> AB+
    def test_infix_to_postfix_simple(self):
        print(self._testMethodName)
        inString = '9+19'
        print(inString)
        result0 = sy.infixToPostfix(inString)
        print(result0)
        
        inString = '66-6'
        print(inString)
        result1 = sy.infixToPostfix(inString)
        print(result1)
        
        inString = '2*3'
        print(inString)
        result2 = sy.infixToPostfix(inString)
        print(result2)
        
        inString = '4/1'
        print(inString)
        result3 = sy.infixToPostfix(inString)
        print(result3)
    
    def test_infix_to_postfix_brackets(self):
        print(self._testMethodName)
        inString0 = '(7*8)/2'
        print(inString0)
        result0 = sy.infixToPostfix(inString0)
        print(result0)

        inString1 = '[9*9]-5'
        print(inString1)
        result1 = sy.infixToPostfix(inString1)
        print(result1)
    
    def test_infix_to_postfix_complex(self):
        print(self._testMethodName)
        inString = '[100-(4*5)+9]/7+2*(6/3)-4'
        print(inString)
        result = sy.infixToPostfix(inString)
        print(result)

    def test_infix_to_postfix_with_letters(self):
        print(self._testMethodName)
        inString = 'A+B-C*D/E'
        print(inString)
        result = sy.infixToPostfix(inString)
        print(result)

    def test_infix_to_postfix_with_special_characters(self):
        print(self._testMethodName)
        inString = '~+!-@*#/$+%-^*&/{+}-\*|/:+;-,*</.+>-?*"/`"'
        print(inString)
        result = sy.infixToPostfix(inString)
        print(result)

    def test_infix_to_postfix_with_only_operators(self):
        print(self._testMethodName)
        inString0 = '+-*/'
        print(inString0)
        result0 = sy.infixToPostfix(inString0)
        print(result0)

        inString1 = '/*-+'
        print(inString1)
        result1 = sy.infixToPostfix(inString1)
        print(result1)

class ComparePrecedenceTest(unittest.TestCase):
    def test_left_lower_right(self):
        print(self._testMethodName)
        result0 = sy.comparePrecedence('+', '*')
        print(result0)

        result1 = sy.comparePrecedence('+', '/')
        print(result1)
        
        result2 = sy.comparePrecedence('-', '*')
        print(result2)
        
        result3 = sy.comparePrecedence('-', '/')
        print(result3)
    
    def test_left_equal_right(self):
        print(self._testMethodName)
        result0 = sy.comparePrecedence('+', '-')
        print(result0)

        result1 = sy.comparePrecedence('-', '+')
        print(result1)
    
    def test_left_highter_right(self):
        print(self._testMethodName)
        result0 = sy.comparePrecedence('*', '+')
        print(result0)

        result1 = sy.comparePrecedence('*', '-')
        print(result1)

        result2 = sy.comparePrecedence('/', '+')
        print(result2)

        result3 = sy.comparePrecedence('/', '-')
        print(result3)

class AppendToOutputTest(unittest.TestCase):
    def test_append_to_empty_outString(self):
        print(self._testMethodName)
        outString = ''
        token = '8'
        print(outString)
        result = sy.appendToOutput(outString, token)
        if result == token:
            print(result)
        else:
            print('ERROR: could not append token')

    def test_append_to_occupied_outString(self):
        print(self._testMethodName)
        outString = '36 - 2 ( 20 + 12 / 4 * 3 - 2 * 2 ) +'
        token = '10'
        print(outString)
        result = sy.appendToOutput(outString, token)
        print(result)
