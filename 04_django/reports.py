#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate_report(attachment, title, paragraph):
    '''
    Creates a report called processed.pdf
    '''
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment)
    report_title = Paragraph(title, styles["h1"])
    descriptions = Paragraph(paragraph, styles["BodyText"])
    empty_line = Spacer(1,20)
    report.build([report_title, empty_line, descriptions, empty_line])
