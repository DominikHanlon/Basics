#!/usr/bin/env python3
from bs4 import BeautifulSoup
from typing import Optional
import pprint

"""
Fetch the title from a given HTML document
"""
def get_title(html_document: str) -> Optional[str]:
    soup = BeautifulSoup(html_document, 'html.parser')

    if None == soup.title:
        return None

    return soup.title.string
