#!/usr/bin/env python3
"""Script that writes the complete chapter07.py"""

lines = []

def w(*args):
    for line in args:
        lines.append(line)

# ============================================================
# FILE HEADER
# ============================================================
w(
'"""Chapter 7: SvelteKit — The Full-Stack Framework',
'City Planning for Your Component Collection',
'"""',
'import sys, os',
'sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))',
'from generate_course_pdf import (',
'    ChapterCoverPage, h1, h2, h3, h4, p, bullet, code_block, analogy_box,',
'    principal_box, mistake_box, exercise, spacer, checkpoint, page_break,',
'    ExerciseBox, CalloutBox, CodeBlock, HorizontalLine, COLORS, FRAME_WIDTH',
')',
'from reportlab.platypus import PageBreak, Spacer, Paragraph',
'',
'',
'def build_chapter_7(styles):',
'    story = []',
'',
'    # ================================================================',
'    # CHAPTER COVER',
'    # ================================================================',
'    story.append(ChapterCoverPage(',
'        7,',
'        "SvelteKit \u2014 The Full-Stack Framework",',
'        "City Planning for Your Component Collection",',
'        "PART 2: LEVELING UP"',
'    ))',
'    story.append(PageBreak())',
)

with open('/home/user/principal-engineer-app/chapters/chapter07.py', 'w') as f:
    f.write('\n'.join(lines))

print(f"Written {len(lines)} lines")
