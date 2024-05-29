import re

def contains_chinese_and_print(file_path):
    # 正则表达式匹配中文字符
    chinese_char_pattern = re.compile(r'[\u4e00-\u9fa5]')
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, 1):
                if chinese_char_pattern.search(line):
                    print(f"Line {line_number}: {line.strip()}")
    except FileNotFoundError:
        print(f"文件 {file_path} 未找到。")
    except Exception as e:
        print(f"读取文件时发生错误：{e}")

# 指定要检查的文件路径
file_path = 'example.txt'

# 调用函数
contains_chinese_and_print(file_path)