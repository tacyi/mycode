"""old AI method
计算机生成人类语言
LSTM,Transfer去做
GPT-2
"""
import random

grammar = """
句子 = s_句子 ，连词 句子 | s_句子
连词 = 而且 | 但是 | 不过
s_句子 = 主 谓 宾
谓 = 吃 | 喝 | 玩
宾 = 皮球 | 桃子
主 = 你 | 我 | 他
"""
grammar2 = """
句子 = 打招呼 玩 活动 吗？
打招呼 = 你好 | 您好 | 好久不见
玩 = 需要玩 | 喜欢玩 | 想玩
活动 = 骑马 | 打球 | 喝茶
"""

# def generate_verb():
#     return random.choice('吃|喝|玩'.split('|'))
#
#
# def generate_binyu():
#     return random.choice('皮球|桃子'.split('|'))
#
#
# print(generate_binyu() + generate_verb())
def get_grammar(grammar_string):
    grammar_gen = dict()
    for line in grammar_string.split('\n'):
        if not line.strip(): continue
        # print(line)
        stmt, expr = line.split('=')
        expressions = expr.split('|')
        # grammar_gen[stmt]= expressions
        grammar_gen[stmt.strip()] = [e.strip() for e in expressions]

    # print(grammar_gen)
    return grammar_gen

def generate_sentence(gram, target='句子'):
    if target not in gram: return target
    exp = random.choice(gram[target])
    return ''.join([generate_sentence(gram, e) for e in exp.split()])

print(generate_sentence(get_grammar(grammar2)))
print(generate_sentence(get_grammar(grammar)))