#_*_coding:utf-8_*_

def file_iter():
    with open('/Users/ouhiroshi/Desktop/warpped.txt') as f:
        try:
            while True:
                line = next(f)
                print(line, end='')
        
        except StopIteration:
            pass

def file_iter_new():
    with open('/Users/ouhiroshi/Desktop/warpped.txt') as f:
        try:
            while True:
                line = next(f, None)
                if line is None:
                    break
                
                print(line, end='')
        except StopIteration as identifier:
            pass

if __name__ == "__main__":
   # file_iter()
   file_iter_new()