"""
python3 visitor_edit.py 用語 ディレクトリ
とすると、指定したディレクトリ内で用語が含まれるファイルが
順次vimの編集モードで開かれる

python3 visitor_edit.py mimetypes ~/develop/github/programming_list_Python/programming/tools/
"""

import os
import sys
from visitor import SearchVisitor

class EditVisitor(SearchVisitor):

    editor = "/usr/bin/vim"

    def visitmatch(self, fpathname, text):
        os.system('%s %s' % (self.editor, fpathname))

if __name__ == '__main__':
    visitor = EditVisitor(sys.argv[1])
    visitor.run('.' if len(sys.argv) < 3 else sys.argv[2])
    print('Edited %d files, visited %d' % (visitor.scount, visitor.fcount))