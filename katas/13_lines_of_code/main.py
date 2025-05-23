from io import StringIO
from enum import Enum

THREE_LINES = '''
// This file contains 3 lines of code
   public interface Dave {
     /**
      * count the number of lines in a file
      */
     int countLines(File inFile); // not the real signature!
   }
'''.strip() # remove xtra first/last \n

FIVE_LINES = '''
/*****
 * This is a test program with 5 lines of code
 *  \/* no nesting allowed!
 //*****//***/// Slightly pathological comment ending...

public class Hello {
    public static final void main(String [] args) { // gotta love Java
        // Say hello
      System./*wait*/out./*for*/println/*it*/("Hello/*");
    }

}
'''.strip() # remove xtra first/last \n


class LT(Enum):
    SANS_CODE = 0
    CODE = 1
    COMMENT = 2
    START_COMMENT = 3
    END_COMMENT = 4

def line_type(line: str) -> LT:
    line = line.strip()
    if not line:
        return LT.SANS_CODE
    if line.startswith('//'):
        return LT.COMMENT
    if line.startswith('/*'):
        return LT.START_COMMENT
    if line.endswith('*/'):
        return LT.END_COMMENT
    return LT.CODE



def line_count(fs: str, debug=False) -> int:
    count = 0
    in_comment = False
    for line in StringIO(initial_value=fs):
        if not in_comment:
            match line_type(line):
                case  LT.CODE:
                    count += 1
                    if debug:
                        print(f"code: {line}")
                case LT.START_COMMENT:
                    in_comment = True
                    print(f"sc: {line}")
                case LT.END_COMMENT:
                    in_comment = False
                    print(f"ec: {line}")
                case LT.SANS_CODE | LT.COMMENT:
                    print(f"c_sc: {line}")
                    pass
                case _:
                    assert False
    print(count)
    return count

if __name__ == "__main__":
    assert line_count(THREE_LINES, True) == 3
    assert line_count(FIVE_LINES) == 5
