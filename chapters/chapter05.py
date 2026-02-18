#!/usr/bin/env python3
"""
Chapter 5: TypeScript - JavaScript with Guardrails
A Spell-Checker for Your Code
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from generate_course_pdf import (
    ChapterCoverPage, h1, h2, h3, h4, p, bullet, code_block, analogy_box,
    principal_box, mistake_box, exercise, spacer, checkpoint, page_break,
    ExerciseBox, CalloutBox, CodeBlock, HorizontalLine, COLORS, FRAME_WIDTH
)
from reportlab.platypus import PageBreak, Spacer, Paragraph


def build_chapter_5(styles):
    story = []

    # Chapter Cover
    story.append(ChapterCoverPage(5, "TypeScript - JavaScript with Guardrails", "A Spell-Checker for Your Code", "PART 2: LEVELING UP"))
    story.append(PageBreak())

    story.append(h1("Chapter 5: TypeScript - JavaScript with Guardrails", styles))
    story.append(p("TypeScript is one of the most transformative technologies in modern web development. It takes JavaScript - a language famous for its flexibility and occasional chaos - and adds a powerful type system that catches errors before your code ever runs. In this chapter, we will master TypeScript from the ground up, learning not just syntax but the mental models that make you a TypeScript expert.", styles))
    story.append(spacer(12))

    return story
