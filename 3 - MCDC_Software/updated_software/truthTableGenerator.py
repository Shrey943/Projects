import os
import sys

import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox

from itertools import product

from pandas import read_excel, DataFrame, ExcelWriter
from tabulate import tabulate
from collections import OrderedDict


class Calculating(object):

    def calculation_truthtb(self, inputv, outputFile):
        symbols = {'&', '|'}

        statement = inputv
        try:

            variables = self.get_variables(statement)
            truth_table_values, tautology = self.get_truth_table(statement)
            truth_table_values = [
                ['T' if el == 1 else 'F' for el in row] for row in truth_table_values]
            # print(truth_table_values)
            st = ("""MC/DC Truth table: \t{}\n{}""").format(
                statement,
                tabulate(truth_table_values, headers=variables + ['Ans']),
                'is' if tautology else 'is not')

            i=1
            for a in truth_table_values:
                a.insert(0,i)
                i+=1

            eq = DataFrame([['Expression :', statement]])
            tt = DataFrame(['Truth Table:-'])
            tb = DataFrame([['Combinations'] + variables + ['Ans']] + truth_table_values)
            
            # out_path = path
            writer = ExcelWriter(outputFile+'.xlsx', engine='xlsxwriter')
            eq.to_excel(writer, sheet_name="Sheet1",
                        startrow=0, header=None, index=False)
            tt.to_excel(writer, sheet_name="Sheet1",
                        startrow=1, header=None, index=False)
            tb.to_excel(writer, sheet_name="Sheet1",
                        startrow=2, header=None, index=False)
            writer.save()
            return "success"
        except PermissionError:
            return 'name'
        
        return st

    def parenthetic_contents(self, string):
        stack = []
        for i, char in enumerate(string):
            if char == '(':
                stack.append(i)
            elif char == ')' and stack:
                start = stack.pop()
                yield (len(stack), string[start + 1: i])

    def and_func(self, p, q):
        return p and q

    def or_func(self, p, q):
        return p or q

    def negate(self, p):
        return not p

    def apply_negations(self, string):
        new_string = string[:]
        for i, char in enumerate(string):
            if char == '!':
                try:
                    next_char = string[i+1]  # Character proceeding '!'
                    num = int(next_char)
                    negated = str(int(negate(num)))
                    new_string = new_string.replace('!'+string[i+1], negated)
                except:
                    pass
        return new_string

    def eval_logic(self, string):
        string = string.replace(' ', '')  # Remove spaces
        string = self.apply_negations(string)  # Switch !0 to 1, !1 to 0
        new_string = string[:]
        operators = {
            '&': self.and_func,
            '|': self.or_func,
        }
        boolean = int(string[0])
        for i, char in enumerate(string):
            if char in operators:
                boolean = operators[char](boolean, int(string[i+1]))
        try:
            return int(boolean)  # Return boolean as 0 or 1
        except:
            return int(string)  # Return the value of the string itself

    def get_variables(self, statement):
        # Identify variables
        variables = {char for char in statement if char.isalpha()}
        variables = list(variables)
        variables.sort()
        return variables

    def truth_combos(self, statement):

        variables = self.get_variables(statement)
        combo_list = []
        for booleans in product([False, True], repeat=len(variables)):
            # Replace True with 1, False with 0
            int_bool = [int(x) for x in booleans]
            combo_list.append(dict(zip(variables, int_bool)))
        return combo_list

    def replace_variables(self, string, truth_values):
        for variable in truth_values:
            bool_string = str(truth_values[variable])
            string = string.replace(variable, bool_string)
        return string

    def simplify(self, valued_statement):
        brackets_list = list(self.parenthetic_contents(valued_statement))
        if not brackets_list:
            # There are no brackets in the statement
            return str(self.eval_logic(valued_statement))
        # Deepest level of nested brackets
        deepest_level = max([i for (i, j) in brackets_list])
        for level, string in brackets_list:
            if level == deepest_level:
                bool_string = str(self.eval_logic(string))
                valued_statement = valued_statement.replace(
                    '('+string+')', bool_string)
        return valued_statement

    def solve(self, valued_statement):
        while len(valued_statement) > 1:
            valued_statement = self.simplify(valued_statement)
        return int(valued_statement)

    def get_truth_table(self, statement):
        if statement[0] != '(':
            statement = '('+statement+')'  # Add brackets to ends
        variables = self.get_variables(statement)
        combo_list = self.truth_combos(statement)
        truth_table_values = []
        tautology = True
        for truth_values in combo_list:
            valued_statement = self.replace_variables(statement, truth_values)
            ordered_truth_values = OrderedDict(sorted(truth_values.items()))
            answer = self.solve(valued_statement)
            truth_table_values.append(
                list(ordered_truth_values.values()) + [answer])
            if answer != 1:
                tautology = False
        
        return truth_table_values, tautology

    def generate_mcdc(self, filename):
        equation = read_excel(filename, index_col=None, na_values=[
                              'NA'], skiprows=0, header=None).loc[0, 1]
        truthtable = read_excel(filename, index_col=None, na_values=[
                                'NA'], skiprows=1).values.tolist()
        truthtable = [[1 if el == 'T' else 0 for el in row]
                      for row in truthtable]
        print(truthtable)
        return equation



if __name__ == '__main__':
    cal = Calculating()
    print(cal.calculation_truthtb('a&b', 'c:/Users/Master Shrey/Desktop/software test/output67'))
