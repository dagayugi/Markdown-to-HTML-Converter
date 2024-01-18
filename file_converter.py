import os
import markdown
import sys

CURRENT_DIR = os.getcwd()

def excpect_catch_deco(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:
            print(f"{args[0]}が見つかりません。")
        except PermissionError:
            print(f"{args[0]}の権限がありません。")
        except Exception as e:
            print(f"エラーが発生しました: {str(e)}")
    return wrapper

@excpect_catch_deco
def convert_to_html(input_file, output_file):
    """マークダウンファイルをhtmlに変換"""

    with open(input_file, 'r') as f:
        content = f.read()

    with open(output_file, 'w') as f:
        f.write(markdown.markdown(content))

    print('.mdファイルから.htmlファイルを作成しました。')

def main(params):
    """main function"""

    try:
        input_file, output_file = params[1], params[2]
        _, ext = os.path.splitext(input_file)
        
        if ext != '.md':
            print('第1引数のファイル拡張子が不正です。')
            return
        
        _, ext = os.path.splitext(output_file)
        if not ext:
            output_file += '.html'
        elif ext != 'html':
            print('第二引数のファイル拡張子が不正です。')
            return
        convert_to_html(
            os.path.join(CURRENT_DIR, input_file),
            os.path.join(CURRENT_DIR, output_file)
        )
            
    except KeyError:
        print('不正なコマンドの形式です。引数が2つ必要です。(インプットファイル アウトプットファイル)')

if __name__ == '__main__':
    main(sys.argv)

