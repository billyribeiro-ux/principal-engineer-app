#!/usr/bin/env python3
"""Script to generate chapter04.py"""

lines = []

def L(s=""):
    lines.append(s)

# Header
L('#!/usr/bin/env python3')
L('"""')
L('Chapter 4: JavaScript -- Making Things Come Alive')
L('The Electricity and Plumbing in Your House')
L('"""')
L()
L('import sys, os')
L("sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))")
L('from generate_course_pdf import (')
L('    ChapterCoverPage, h1, h2, h3, h4, p, bullet, code_block, analogy_box,')
L('    principal_box, mistake_box, exercise, spacer, checkpoint, page_break,')
L('    ExerciseBox, CalloutBox, CodeBlock, HorizontalLine, COLORS, FRAME_WIDTH')
L(')')
L('from reportlab.platypus import PageBreak, Spacer, Paragraph')
L()
L()
L('def build_chapter_4(styles):')
L('    story = []')
L()
L('    # Chapter cover')
L('    story.append(ChapterCoverPage(4, "JavaScript -- Making Things Come Alive",')
L('                                  "The Electricity and Plumbing in Your House",')
L('                                  "PART 1: FOUNDATIONS"))')
L('    story.append(PageBreak())')
L()

with open('/home/user/principal-engineer-app/chapters/chapter04.py', 'w') as f:
    f.write('\n'.join(lines))

print(f"Written {len(lines)} lines so far")
