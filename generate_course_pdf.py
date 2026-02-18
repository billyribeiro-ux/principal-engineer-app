#!/usr/bin/env python3
"""
From Zero to Principal Engineer: The Complete Web Development Mastery Course
PDF Generator using ReportLab

This is the main entry point that assembles all chapters into a single PDF.
"""

import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch, cm
from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
    Table, TableStyle, PageBreak, NextPageTemplate, KeepTogether,
    Flowable, Image, ListFlowable, ListItem
)
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.pdfgen import canvas
from reportlab.lib.fonts import addMapping
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ============================================================================
# COLOR PALETTE
# ============================================================================
COLORS = {
    'primary': HexColor('#1a1a2e'),
    'secondary': HexColor('#16213e'),
    'accent': HexColor('#0f3460'),
    'highlight': HexColor('#e94560'),
    'text': HexColor('#1a1a1a'),
    'text_light': HexColor('#555555'),
    'text_muted': HexColor('#888888'),
    'white': HexColor('#ffffff'),
    'bg_code': HexColor('#F5F5F5'),
    'bg_analogy': HexColor('#FFF9E6'),
    'bg_principal': HexColor('#E8F4FD'),
    'bg_mistake': HexColor('#FFF0F0'),
    'bg_exercise': HexColor('#F0F7F0'),
    'border_analogy': HexColor('#E6D590'),
    'border_principal': HexColor('#90C4DE'),
    'border_mistake': HexColor('#E09090'),
    'border_exercise': HexColor('#90C490'),
    'link': HexColor('#0066CC'),
    'chapter_bg': HexColor('#1a1a2e'),
}

# ============================================================================
# PAGE DIMENSIONS
# ============================================================================
PAGE_WIDTH, PAGE_HEIGHT = letter
MARGIN_LEFT = 1.0 * inch
MARGIN_RIGHT = 1.0 * inch
MARGIN_TOP = 1.0 * inch
MARGIN_BOTTOM = 1.0 * inch
FRAME_WIDTH = PAGE_WIDTH - MARGIN_LEFT - MARGIN_RIGHT
FRAME_HEIGHT = PAGE_HEIGHT - MARGIN_TOP - MARGIN_BOTTOM

# ============================================================================
# STYLES
# ============================================================================
def get_styles():
    """Create and return all paragraph styles used in the course."""
    styles = getSampleStyleSheet()

    # Title page styles
    styles.add(ParagraphStyle(
        name='CourseTitle',
        fontName='Helvetica-Bold',
        fontSize=32,
        leading=38,
        textColor=COLORS['white'],
        alignment=TA_CENTER,
        spaceAfter=12,
    ))
    styles.add(ParagraphStyle(
        name='CourseSubtitle',
        fontName='Helvetica',
        fontSize=16,
        leading=22,
        textColor=HexColor('#cccccc'),
        alignment=TA_CENTER,
        spaceAfter=8,
    ))
    styles.add(ParagraphStyle(
        name='CourseTagline',
        fontName='Helvetica-Oblique',
        fontSize=12,
        leading=16,
        textColor=HexColor('#aaaaaa'),
        alignment=TA_CENTER,
        spaceAfter=20,
    ))

    # Chapter title styles
    styles.add(ParagraphStyle(
        name='ChapterNumber',
        fontName='Helvetica-Bold',
        fontSize=60,
        leading=66,
        textColor=COLORS['white'],
        alignment=TA_CENTER,
        spaceAfter=10,
    ))
    styles.add(ParagraphStyle(
        name='ChapterTitle',
        fontName='Helvetica-Bold',
        fontSize=28,
        leading=34,
        textColor=COLORS['white'],
        alignment=TA_CENTER,
        spaceAfter=10,
    ))
    styles.add(ParagraphStyle(
        name='ChapterSubtitle',
        fontName='Helvetica-Oblique',
        fontSize=14,
        leading=18,
        textColor=HexColor('#cccccc'),
        alignment=TA_CENTER,
    ))

    # Part title styles
    styles.add(ParagraphStyle(
        name='PartNumber',
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=HexColor('#cccccc'),
        alignment=TA_CENTER,
        spaceAfter=10,
    ))
    styles.add(ParagraphStyle(
        name='PartTitle',
        fontName='Helvetica-Bold',
        fontSize=36,
        leading=42,
        textColor=COLORS['white'],
        alignment=TA_CENTER,
        spaceAfter=10,
    ))
    styles.add(ParagraphStyle(
        name='PartSubtitle',
        fontName='Helvetica-Oblique',
        fontSize=14,
        leading=18,
        textColor=HexColor('#aaaaaa'),
        alignment=TA_CENTER,
    ))

    # Heading styles
    styles.add(ParagraphStyle(
        name='Heading1',
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=28,
        textColor=COLORS['primary'],
        spaceBefore=24,
        spaceAfter=12,
        keepWithNext=True,
    ))
    styles.add(ParagraphStyle(
        name='Heading2',
        fontName='Helvetica-Bold',
        fontSize=17,
        leading=22,
        textColor=COLORS['accent'],
        spaceBefore=18,
        spaceAfter=8,
        keepWithNext=True,
    ))
    styles.add(ParagraphStyle(
        name='Heading3',
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=COLORS['secondary'],
        spaceBefore=14,
        spaceAfter=6,
        keepWithNext=True,
    ))
    styles.add(ParagraphStyle(
        name='Heading4',
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=COLORS['text'],
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True,
    ))

    # Body text
    styles.add(ParagraphStyle(
        name='BodyText2',
        fontName='Helvetica',
        fontSize=10.5,
        leading=15,
        textColor=COLORS['text'],
        alignment=TA_JUSTIFY,
        spaceBefore=2,
        spaceAfter=6,
    ))

    # Callout box text styles
    styles.add(ParagraphStyle(
        name='CalloutTitle',
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        spaceAfter=4,
    ))
    styles.add(ParagraphStyle(
        name='CalloutBody',
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        alignment=TA_JUSTIFY,
    ))

    # Code styles
    styles.add(ParagraphStyle(
        name='Code',
        fontName='Courier',
        fontSize=8.5,
        leading=11.5,
        textColor=COLORS['text'],
        leftIndent=8,
        rightIndent=8,
        spaceBefore=2,
        spaceAfter=2,
    ))
    styles.add(ParagraphStyle(
        name='CodeTitle',
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=12,
        textColor=COLORS['text_light'],
        spaceBefore=8,
        spaceAfter=2,
    ))
    styles.add(ParagraphStyle(
        name='InlineCode',
        fontName='Courier',
        fontSize=9.5,
        leading=13,
        textColor=COLORS['text'],
    ))

    # Exercise styles
    styles.add(ParagraphStyle(
        name='ExerciseTitle',
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=COLORS['accent'],
        spaceBefore=4,
        spaceAfter=4,
    ))
    styles.add(ParagraphStyle(
        name='ExerciseBody',
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=COLORS['text'],
        alignment=TA_JUSTIFY,
    ))

    # TOC Styles
    styles.add(ParagraphStyle(
        name='TOCPart',
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=20,
        textColor=COLORS['primary'],
        spaceBefore=16,
        spaceAfter=4,
    ))
    styles.add(ParagraphStyle(
        name='TOCChapter',
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=18,
        textColor=COLORS['accent'],
        leftIndent=12,
        spaceBefore=6,
        spaceAfter=2,
    ))
    styles.add(ParagraphStyle(
        name='TOCSection',
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=COLORS['text'],
        leftIndent=30,
    ))

    # Bullet/list style
    styles.add(ParagraphStyle(
        name='BulletText',
        fontName='Helvetica',
        fontSize=10.5,
        leading=15,
        textColor=COLORS['text'],
        leftIndent=20,
        bulletIndent=8,
        spaceBefore=1,
        spaceAfter=3,
    ))

    # Progress checkpoint style
    styles.add(ParagraphStyle(
        name='Checkpoint',
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=COLORS['accent'],
        alignment=TA_CENTER,
        spaceBefore=12,
        spaceAfter=12,
    ))

    return styles


# ============================================================================
# CUSTOM FLOWABLES
# ============================================================================

class ColoredRect(Flowable):
    """A simple colored rectangle background - used for full-page backgrounds."""
    def __init__(self, width, height, color):
        Flowable.__init__(self)
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        self.canv.setFillColor(self.color)
        self.canv.rect(0, 0, self.width, self.height, fill=1, stroke=0)


class CalloutBox(Flowable):
    """A styled callout box for analogies, principal engineer insights, mistakes, etc."""
    def __init__(self, title, body_text, bg_color, border_color, title_icon="",
                 width=None, styles=None):
        Flowable.__init__(self)
        self.box_width = width or FRAME_WIDTH
        self.title_text = title
        self.body_text = body_text
        self.bg_color = bg_color
        self.border_color = border_color
        self.title_icon = title_icon
        self.styles = styles or get_styles()
        self._fixed_height = None

    def wrap(self, availWidth, availHeight):
        self.box_width = min(self.box_width, availWidth)
        inner_width = self.box_width - 24  # padding
        # Calculate title height
        title_para = Paragraph(f"<b>{self.title_icon} {self.title_text}</b>",
                              self.styles['CalloutTitle'])
        tw, th = title_para.wrap(inner_width, availHeight)
        # Calculate body height
        body_para = Paragraph(self.body_text, self.styles['CalloutBody'])
        bw, bh = body_para.wrap(inner_width, availHeight)
        self._fixed_height = th + bh + 24  # padding top + bottom + gap
        self._title_para = title_para
        self._body_para = body_para
        self._title_h = th
        self._body_h = bh
        return (self.box_width, self._fixed_height)

    def draw(self):
        canv = self.canv
        # Background
        canv.setFillColor(self.bg_color)
        canv.setStrokeColor(self.border_color)
        canv.setLineWidth(1.5)
        canv.roundRect(0, 0, self.box_width, self._fixed_height, 4, fill=1, stroke=1)
        # Left accent bar
        canv.setFillColor(self.border_color)
        canv.rect(0, 0, 4, self._fixed_height, fill=1, stroke=0)
        # Draw title
        self._title_para.drawOn(canv, 12, self._fixed_height - self._title_h - 8)
        # Draw body
        self._body_para.drawOn(canv, 12, self._fixed_height - self._title_h - self._body_h - 16)


class CodeBlock(Flowable):
    """A styled code block with optional filename header."""
    def __init__(self, code_text, filename=None, width=None, styles=None):
        Flowable.__init__(self)
        self.box_width = width or FRAME_WIDTH
        self.code_text = code_text
        self.filename = filename
        self.styles = styles or get_styles()
        self._fixed_height = None

    def wrap(self, availWidth, availHeight):
        self.box_width = min(self.box_width, availWidth)
        inner_width = self.box_width - 20
        # Prepare code lines
        escaped = self.code_text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        self._code_para = Paragraph(
            f"<font face='Courier' size='8.5'>{escaped}</font>",
            self.styles['Code']
        )
        cw, ch = self._code_para.wrap(inner_width, availHeight)
        header_h = 18 if self.filename else 0
        self._fixed_height = ch + 16 + header_h
        self._header_h = header_h
        self._code_h = ch
        return (self.box_width, self._fixed_height)

    def draw(self):
        canv = self.canv
        # Background
        canv.setFillColor(COLORS['bg_code'])
        canv.setStrokeColor(HexColor('#DDDDDD'))
        canv.setLineWidth(0.5)
        canv.roundRect(0, 0, self.box_width, self._fixed_height, 3, fill=1, stroke=1)
        # Filename header
        if self.filename:
            canv.setFillColor(HexColor('#E8E8E8'))
            canv.roundRect(0, self._fixed_height - self._header_h,
                          self.box_width, self._header_h, 3, fill=1, stroke=0)
            canv.setFillColor(COLORS['text_light'])
            canv.setFont('Helvetica-Bold', 8)
            canv.drawString(10, self._fixed_height - 13, self.filename)
        # Draw code
        self._code_para.drawOn(canv, 10,
                               self._fixed_height - self._header_h - self._code_h - 8)


class ExerciseBox(Flowable):
    """A styled exercise box with difficulty rating."""
    def __init__(self, difficulty, title, body_parts, width=None, styles=None):
        Flowable.__init__(self)
        self.box_width = width or FRAME_WIDTH
        self.difficulty = difficulty  # number of stars 1-5
        self.title_text = title
        self.body_parts = body_parts  # list of (style_name, text) tuples
        self.styles = styles or get_styles()

    def wrap(self, availWidth, availHeight):
        self.box_width = min(self.box_width, availWidth)
        inner_width = self.box_width - 28
        stars = '*' * self.difficulty
        labels = {1: 'Beginner', 2: 'Elementary', 3: 'Intermediate',
                  4: 'Advanced', 5: 'Principal Engineer'}
        label = labels.get(self.difficulty, '')
        header_text = f"<b>Exercise: {self.title_text}</b>  [{stars}] {label}"
        self._header_para = Paragraph(header_text, self.styles['ExerciseTitle'])
        hw, hh = self._header_para.wrap(inner_width, availHeight)
        self._header_h = hh
        self._body_paras = []
        total_bh = 0
        for style_name, text in self.body_parts:
            p = Paragraph(text, self.styles[style_name])
            pw, ph = p.wrap(inner_width, availHeight)
            self._body_paras.append((p, ph))
            total_bh += ph + 2
        self._total_body_h = total_bh
        self._fixed_height = hh + total_bh + 24
        return (self.box_width, self._fixed_height)

    def draw(self):
        canv = self.canv
        canv.setFillColor(COLORS['bg_exercise'])
        canv.setStrokeColor(COLORS['border_exercise'])
        canv.setLineWidth(1.5)
        canv.roundRect(0, 0, self.box_width, self._fixed_height, 4, fill=1, stroke=1)
        canv.setFillColor(COLORS['border_exercise'])
        canv.rect(0, 0, 4, self._fixed_height, fill=1, stroke=0)
        self._header_para.drawOn(canv, 14, self._fixed_height - self._header_h - 8)
        y = self._fixed_height - self._header_h - 14
        for para, ph in self._body_paras:
            y -= ph + 2
            para.drawOn(canv, 14, y)


class HorizontalLine(Flowable):
    """A simple horizontal line separator."""
    def __init__(self, width=None, color=None, thickness=0.5):
        Flowable.__init__(self)
        self.line_width = width or FRAME_WIDTH
        self.color = color or HexColor('#CCCCCC')
        self.thickness = thickness

    def wrap(self, availWidth, availHeight):
        return (min(self.line_width, availWidth), self.thickness + 4)

    def draw(self):
        self.canv.setStrokeColor(self.color)
        self.canv.setLineWidth(self.thickness)
        self.canv.line(0, 2, self.line_width, 2)


class ChapterCoverPage(Flowable):
    """Full-page chapter cover with dark background."""
    def __init__(self, chapter_num, title, subtitle="", part_info=""):
        Flowable.__init__(self)
        self.chapter_num = chapter_num
        self.title = title
        self.subtitle = subtitle
        self.part_info = part_info

    def wrap(self, availWidth, availHeight):
        return (PAGE_WIDTH, PAGE_HEIGHT)

    def draw(self):
        canv = self.canv
        # Full page dark background
        canv.setFillColor(COLORS['chapter_bg'])
        canv.rect(-MARGIN_LEFT, -MARGIN_BOTTOM,
                  PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)
        # Decorative line
        canv.setStrokeColor(COLORS['highlight'])
        canv.setLineWidth(3)
        center_x = (PAGE_WIDTH - MARGIN_LEFT - MARGIN_RIGHT) / 2
        canv.line(center_x - 40, PAGE_HEIGHT / 2 + 60,
                  center_x + 40, PAGE_HEIGHT / 2 + 60)
        # Part info
        if self.part_info:
            canv.setFillColor(HexColor('#888888'))
            canv.setFont('Helvetica', 11)
            canv.drawCentredString(center_x, PAGE_HEIGHT / 2 + 80, self.part_info)
        # Chapter number
        canv.setFillColor(COLORS['highlight'])
        canv.setFont('Helvetica-Bold', 72)
        canv.drawCentredString(center_x, PAGE_HEIGHT / 2 + 100,
                               f"CHAPTER {self.chapter_num}")
        # Title
        canv.setFillColor(COLORS['white'])
        canv.setFont('Helvetica-Bold', 28)
        # Word wrap title if needed
        words = self.title.split()
        lines = []
        current = ""
        for w in words:
            test = current + " " + w if current else w
            if canv.stringWidth(test, 'Helvetica-Bold', 28) > FRAME_WIDTH - 40:
                lines.append(current)
                current = w
            else:
                current = test
        if current:
            lines.append(current)
        y_start = PAGE_HEIGHT / 2 + 20
        for i, line in enumerate(lines):
            canv.drawCentredString(center_x, y_start - i * 34, line)
        # Subtitle
        if self.subtitle:
            canv.setFillColor(HexColor('#aaaaaa'))
            canv.setFont('Helvetica-Oblique', 13)
            sub_y = y_start - len(lines) * 34 - 10
            canv.drawCentredString(center_x, sub_y, self.subtitle)


class PartCoverPage(Flowable):
    """Full-page part cover."""
    def __init__(self, part_num, title, subtitle=""):
        Flowable.__init__(self)
        self.part_num = part_num
        self.title = title
        self.subtitle = subtitle

    def wrap(self, availWidth, availHeight):
        return (PAGE_WIDTH, PAGE_HEIGHT)

    def draw(self):
        canv = self.canv
        canv.setFillColor(COLORS['primary'])
        canv.rect(-MARGIN_LEFT, -MARGIN_BOTTOM,
                  PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)
        center_x = (PAGE_WIDTH - MARGIN_LEFT - MARGIN_RIGHT) / 2
        # Part number
        canv.setFillColor(COLORS['highlight'])
        canv.setFont('Helvetica-Bold', 18)
        canv.drawCentredString(center_x, PAGE_HEIGHT / 2 + 100,
                               f"PART {self.part_num}")
        # Decorative line
        canv.setStrokeColor(COLORS['highlight'])
        canv.setLineWidth(2)
        canv.line(center_x - 60, PAGE_HEIGHT / 2 + 80,
                  center_x + 60, PAGE_HEIGHT / 2 + 80)
        # Title
        canv.setFillColor(COLORS['white'])
        canv.setFont('Helvetica-Bold', 32)
        canv.drawCentredString(center_x, PAGE_HEIGHT / 2 + 40, self.title)
        # Subtitle
        if self.subtitle:
            canv.setFillColor(HexColor('#aaaaaa'))
            canv.setFont('Helvetica-Oblique', 14)
            canv.drawCentredString(center_x, PAGE_HEIGHT / 2, self.subtitle)


class TitlePage(Flowable):
    """The course title page."""
    def __init__(self):
        Flowable.__init__(self)

    def wrap(self, availWidth, availHeight):
        return (PAGE_WIDTH, PAGE_HEIGHT)

    def draw(self):
        canv = self.canv
        # Full dark background
        canv.setFillColor(COLORS['primary'])
        canv.rect(-MARGIN_LEFT, -MARGIN_BOTTOM,
                  PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)
        center_x = (PAGE_WIDTH - MARGIN_LEFT - MARGIN_RIGHT) / 2
        # Decorative top bar
        canv.setFillColor(COLORS['highlight'])
        canv.rect(-MARGIN_LEFT, PAGE_HEIGHT - MARGIN_BOTTOM - 6,
                  PAGE_WIDTH, 6, fill=1, stroke=0)
        # Title
        canv.setFillColor(COLORS['white'])
        canv.setFont('Helvetica-Bold', 14)
        canv.drawCentredString(center_x, PAGE_HEIGHT / 2 + 200,
                               "FROM ZERO TO")
        canv.setFont('Helvetica-Bold', 38)
        canv.drawCentredString(center_x, PAGE_HEIGHT / 2 + 160,
                               "PRINCIPAL ENGINEER")
        # Line
        canv.setStrokeColor(COLORS['highlight'])
        canv.setLineWidth(2)
        canv.line(center_x - 100, PAGE_HEIGHT / 2 + 140,
                  center_x + 100, PAGE_HEIGHT / 2 + 140)
        # Subtitle
        canv.setFillColor(HexColor('#cccccc'))
        canv.setFont('Helvetica', 15)
        canv.drawCentredString(center_x, PAGE_HEIGHT / 2 + 115,
                               "The Complete Web Development Mastery Course")
        # Tech stack
        canv.setFillColor(COLORS['highlight'])
        canv.setFont('Helvetica-Bold', 12)
        canv.drawCentredString(center_x, PAGE_HEIGHT / 2 + 80,
                               "HTML  ·  CSS  ·  JavaScript  ·  TypeScript  ·  Svelte 5  ·  SvelteKit  ·  GSAP")
        # Tagline
        canv.setFillColor(HexColor('#999999'))
        canv.setFont('Helvetica-Oblique', 11)
        canv.drawCentredString(center_x, PAGE_HEIGHT / 2 + 40,
                               'Everything you need to go from "What is a browser?"')
        canv.drawCentredString(center_x, PAGE_HEIGHT / 2 + 25,
                               "to architecting systems that serve millions.")
        # Bottom bar
        canv.setFillColor(COLORS['highlight'])
        canv.rect(-MARGIN_LEFT, -MARGIN_BOTTOM,
                  PAGE_WIDTH, 6, fill=1, stroke=0)


# ============================================================================
# HELPER FUNCTIONS FOR CONTENT BUILDERS
# ============================================================================

def h1(text, styles):
    return Paragraph(text, styles['Heading1'])

def h2(text, styles):
    return Paragraph(text, styles['Heading2'])

def h3(text, styles):
    return Paragraph(text, styles['Heading3'])

def h4(text, styles):
    return Paragraph(text, styles['Heading4'])

def p(text, styles):
    return Paragraph(text, styles['BodyText2'])

def bullet(text, styles):
    return Paragraph(f"• {text}", styles['BulletText'])

def code_block(code, filename=None, styles=None):
    return CodeBlock(code, filename=filename, styles=styles)

def analogy_box(text, styles):
    return CalloutBox(
        "Real-World Analogy:",
        text,
        COLORS['bg_analogy'],
        COLORS['border_analogy'],
        title_icon="",
        styles=styles
    )

def principal_box(text, styles):
    return CalloutBox(
        "Principal Engineer Insight:",
        text,
        COLORS['bg_principal'],
        COLORS['border_principal'],
        title_icon="",
        styles=styles
    )

def mistake_box(text, styles):
    return CalloutBox(
        "Common Mistake:",
        text,
        COLORS['bg_mistake'],
        COLORS['border_mistake'],
        title_icon="",
        styles=styles
    )

def exercise(difficulty, title, body_parts, styles):
    return ExerciseBox(difficulty, title, body_parts, styles=styles)

def spacer(height=6):
    return Spacer(1, height)

def checkpoint(text, styles):
    return Paragraph(f"--- CHECKPOINT: {text} ---", styles['Checkpoint'])

def page_break():
    return PageBreak()


# ============================================================================
# PAGE NUMBER HANDLER
# ============================================================================

class PageNumCanvas(canvas.Canvas):
    """Custom canvas that adds page numbers and chapter headers."""
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []
        self._current_chapter = ""

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self._draw_page_extras(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def _draw_page_extras(self, page_count):
        page_num = self._pageNumber
        # Skip page number on very first pages (title, TOC start)
        if page_num <= 2:
            return
        # Page number at bottom center
        self.setFont('Helvetica', 9)
        self.setFillColor(COLORS['text_muted'])
        self.drawCentredString(PAGE_WIDTH / 2, 0.5 * inch,
                               f"{page_num}")


# ============================================================================
# DOCUMENT BUILDER
# ============================================================================

def build_document(output_path, story):
    """Build the final PDF document from a story (list of flowables)."""
    doc = BaseDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=MARGIN_LEFT,
        rightMargin=MARGIN_RIGHT,
        topMargin=MARGIN_TOP,
        bottomMargin=MARGIN_BOTTOM,
        title="From Zero to Principal Engineer",
        author="The Principal Engineer's Web Development Mastery Course",
    )

    frame = Frame(
        MARGIN_LEFT, MARGIN_BOTTOM,
        FRAME_WIDTH, FRAME_HEIGHT,
        id='main_frame'
    )

    template = PageTemplate(id='main', frames=[frame])
    doc.addPageTemplates([template])

    doc.build(story, canvasmaker=PageNumCanvas)
    print(f"PDF generated: {output_path}")
    print(f"File size: {os.path.getsize(output_path) / (1024*1024):.1f} MB")


# ============================================================================
# MAIN - Import chapters and assemble
# ============================================================================

if __name__ == '__main__':
    styles = get_styles()
    story = []

    # Title Page
    story.append(TitlePage())
    story.append(PageBreak())

    # Table of Contents placeholder page
    story.append(Paragraph("TABLE OF CONTENTS", styles['Heading1']))
    story.append(Spacer(1, 12))

    toc_entries = [
        ("PART 1: FOUNDATIONS", [
            ("Chapter 1: How the Web Actually Works", ""),
            ("Chapter 2: HTML — The Skeleton", ""),
            ("Chapter 3: CSS — The Paint and Interior Design", ""),
            ("Chapter 4: JavaScript — Making Things Come Alive", ""),
        ]),
        ("PART 2: LEVELING UP", [
            ("Chapter 5: TypeScript — JavaScript with Guardrails", ""),
            ("Chapter 6: Svelte 5 — The Modern UI Framework", ""),
            ("Chapter 7: SvelteKit — The Full-Stack Framework", ""),
            ("Chapter 8: GSAP — Professional-Grade Animation", ""),
        ]),
        ("PART 3: MASTERY", [
            ("Chapter 9: Architecture and System Design", ""),
            ("Chapter 10: Capstone Project — Production TradeBoard", ""),
        ]),
    ]

    for part_title, chapters in toc_entries:
        story.append(Paragraph(part_title, styles['TOCPart']))
        for ch_title, _ in chapters:
            story.append(Paragraph(ch_title, styles['TOCChapter']))
        story.append(Spacer(1, 4))

    story.append(PageBreak())

    # Now import and generate all chapter content
    print("Importing chapter modules...")

    from chapters.chapter01 import build_chapter_1
    from chapters.chapter02 import build_chapter_2
    from chapters.chapter03 import build_chapter_3
    from chapters.chapter04 import build_chapter_4
    from chapters.chapter05 import build_chapter_5
    from chapters.chapter06 import build_chapter_6
    from chapters.chapter07 import build_chapter_7
    from chapters.chapter08 import build_chapter_8
    from chapters.chapter09 import build_chapter_9
    from chapters.chapter10 import build_chapter_10

    # Part 1
    story.append(PartCoverPage(1, "FOUNDATIONS",
                               '"Understanding the Kitchen Before You Cook"'))
    story.append(PageBreak())

    print("Building Chapter 1...")
    story.extend(build_chapter_1(styles))
    print("Building Chapter 2...")
    story.extend(build_chapter_2(styles))
    print("Building Chapter 3...")
    story.extend(build_chapter_3(styles))
    print("Building Chapter 4...")
    story.extend(build_chapter_4(styles))

    # Part 2
    story.append(PartCoverPage(2, "LEVELING UP",
                               '"Now You Can Cook. Let\'s Become a Chef."'))
    story.append(PageBreak())

    print("Building Chapter 5...")
    story.extend(build_chapter_5(styles))
    print("Building Chapter 6...")
    story.extend(build_chapter_6(styles))
    print("Building Chapter 7...")
    story.extend(build_chapter_7(styles))
    print("Building Chapter 8...")
    story.extend(build_chapter_8(styles))

    # Part 3
    story.append(PartCoverPage(3, "MASTERY",
                               '"Now You\'re a Chef. Let\'s Earn Michelin Stars."'))
    story.append(PageBreak())

    print("Building Chapter 9...")
    story.extend(build_chapter_9(styles))
    print("Building Chapter 10...")
    story.extend(build_chapter_10(styles))

    # Build final PDF
    output_path = os.path.join(os.path.dirname(__file__), 'principal_engineer_course.pdf')
    print(f"\nAssembling PDF with {len(story)} flowable elements...")
    build_document(output_path, story)
    print("Done!")
