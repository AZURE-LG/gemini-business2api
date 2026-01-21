#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
账户信息提取工具
从 data/accounts.json 中提取 mail_provider----mail_address----mail_password 格式的数据
"""

import json
import os


def extract_account_info():
    """提取账户信息并保存为指定格式"""
    # 获取当前脚本所在目录（项目根目录）
    root_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 输入和输出文件路径
    input_file = os.path.join(root_dir, 'data', 'accounts.json')
    output_json_file = os.path.join(root_dir, 'data', 'pwd.json')
    output_txt_file = os.path.join(root_dir, 'data', 'pwd.txt')
    
    try:
        # 读取 accounts.json 文件
        with open(input_file, 'r', encoding='utf-8') as f:
            accounts = json.load(f)
        
        # 提取信息并格式化
        result = []
        for account in accounts:
            mail_provider = account.get('mail_provider', '')
            mail_address = account.get('mail_address', '')
            mail_password = account.get('mail_password', '')
            
            # 按照 mail----email----password 格式组织
            formatted_data = {
                'mail': mail_provider,
                'email': mail_address,
                'password': mail_password,
                'formatted': f"{mail_provider}----{mail_address}----{mail_password}"
            }
            result.append(formatted_data)
        
        # 保存到 pwd.json
        with open(output_json_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        
        # 保存到 pwd.txt（每行一个）
        with open(output_txt_file, 'w', encoding='utf-8') as f:
            for item in result:
                f.write(item['formatted'] + '\n')
        
        print(f"✓ 成功提取 {len(result)} 条账户信息")
        print(f"✓ JSON结果已保存到: {output_json_file}")
        print(f"✓ TXT结果已保存到: {output_txt_file}")
        
        # 输出前3条示例
        if result:
            print("\n前3条数据示例:")
            for i, item in enumerate(result[:3], 1):
                print(f"{i}. {item['formatted']}")
        
        return True
        
    except FileNotFoundError:
        print(f"✗ 错误: 找不到文件 {input_file}")
        return False
    except json.JSONDecodeError as e:
        print(f"✗ JSON 解析错误: {e}")
        return False
    except Exception as e:
        print(f"✗ 发生错误: {e}")
        return False


if __name__ == '__main__':
    extract_account_info()
