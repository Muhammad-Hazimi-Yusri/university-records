"""
Extract syllabus content from MHTML files and save as clean Markdown.
Strips all CSS, images, fonts, and HTML boilerplate - keeps only the useful module info.

Usage: python extract_syllabus.py
"""

import os
import re
import html as html_mod

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SYLLABUS_DIR = os.path.join(SCRIPT_DIR, "Syllabus")
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "Syllabus-Minimised")


def decode_quoted_printable(text):
    """Decode quoted-printable encoding from MHTML."""
    # Fix soft line breaks (= at end of line) first
    text = re.sub(r"=\r?\n", "", text)
    # Replace all =XX hex sequences (including multi-byte UTF-8) at once
    # Collect consecutive =XX sequences and decode them as a group
    def replace_hex_group(m):
        hex_str = m.group(0)
        pairs = re.findall(r"=([0-9A-Fa-f]{2})", hex_str)
        try:
            return bytes(int(h, 16) for h in pairs).decode("utf-8", errors="replace")
        except Exception:
            return hex_str
    text = re.sub(r"(?:=[0-9A-Fa-f]{2})+", replace_hex_group, text)
    # Decode HTML entities
    text = html_mod.unescape(text)
    return text


def extract_html_from_mhtml(filepath):
    """Extract the HTML part from an MHTML file."""
    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    boundary_match = re.search(r'boundary="([^"]+)"', content)
    if not boundary_match:
        return None

    boundary = boundary_match.group(1)
    separator = "--" + boundary
    parts = content.split(separator)

    for part in parts:
        if "Content-Type: text/html" in part[:500]:
            header_end = part.find("\n\n")
            if header_end == -1:
                header_end = part.find("\r\n\r\n")
            if header_end != -1:
                return decode_quoted_printable(part[header_end:])
    return None


def clean_text(text):
    """Strip HTML tags, normalize whitespace, and clean up text."""
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def html_to_markdown(html):
    """Convert the syllabus HTML to clean Markdown."""
    lines = []

    # Extract module title
    title_match = re.search(r"<h1[^>]*><b>(.+?)</b></h1>", html, re.DOTALL)
    if title_match:
        title = clean_text(title_match.group(1))
        lines.append(f"# {title}")
        lines.append("")

    # Extract the <article> content
    article_match = re.search(r"<article>(.*?)</article>", html, re.DOTALL)
    if not article_match:
        return None
    article = article_match.group(1)

    # Process section by section using h2 tags
    sections = re.split(r'<h2[^>]*>\s*', article)

    for section in sections[1:]:
        h2_end = section.find("</h2>")
        if h2_end == -1:
            continue
        section_title = clean_text(section[:h2_end])
        section_body = section[h2_end + 5:]

        lines.append(f"## {section_title}")
        lines.append("")

        tables = re.findall(r"<table[^>]*>(.*?)</table>", section_body, re.DOTALL)
        paragraphs = re.findall(r"<p[^>]*>(.*?)</p>", section_body, re.DOTALL)
        h4_sections = re.split(r"<h4[^>]*>", section_body)

        if section_title == "Details" and tables:
            rows = re.findall(r"<tr>(.*?)</tr>", tables[0], re.DOTALL)
            if len(rows) >= 2:
                headers = [clean_text(h) for h in re.findall(r"<th>(.*?)</th>", rows[0], re.DOTALL)]
                values = [clean_text(v) for v in re.findall(r"<td>(.*?)</td>", rows[1], re.DOTALL)]
                for h, v in zip(headers, values):
                    lines.append(f"- **{h}:** {v}")
                lines.append("")

        elif section_title == "Staff" and tables:
            rows = re.findall(r"<td>(.*?)</td>", tables[0], re.DOTALL)
            for row in rows:
                name = clean_text(row)
                if name:
                    lines.append(f"- **Module Lead:** {name}")
            lines.append("")

        elif section_title == "Learning Outcomes" and tables:
            rows = re.findall(r"<tr>(.*?)</tr>", tables[0], re.DOTALL)
            for row in rows[1:]:
                cells = re.findall(r"<td[^>]*>(.*?)</td>", row, re.DOTALL)
                if len(cells) >= 2:
                    ref = clean_text(cells[0])
                    outcome = clean_text(cells[1])
                    lines.append(f"- **{ref}:** {outcome}")
            lines.append("")

        elif "Study Time" in section_body and tables:
            for p in paragraphs:
                text = clean_text(p)
                if text:
                    lines.append(text)
                    lines.append("")

            study_table_match = re.search(r"Study Time.*?<table[^>]*>(.*?)</table>", section_body, re.DOTALL)
            if study_table_match:
                lines.append("### Study Time")
                lines.append("")
                rows = re.findall(r"<tr>(.*?)</tr>", study_table_match.group(1), re.DOTALL)
                for row in rows[1:]:
                    cells = re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", row, re.DOTALL)
                    if len(cells) >= 2:
                        type_text = clean_text(cells[0])
                        hours_text = clean_text(cells[1])
                        lines.append(f"- {type_text}: {hours_text}")
                lines.append("")

        elif section_title == "Assessment and Feedback Summary":
            strategy_match = re.search(r"Assessment Strategy.*?<p[^>]*>(.*?)</p>", section_body, re.DOTALL)
            if strategy_match:
                lines.append("### Assessment Strategy")
                lines.append("")
                text = clean_text(strategy_match.group(1))
                lines.append(text)
                lines.append("")

            for h4_section in h4_sections[1:]:
                h4_end = h4_section.find("</h4>")
                if h4_end == -1:
                    h4_title_match = re.match(r"(.*?)<", h4_section)
                    if h4_title_match:
                        h4_title = h4_title_match.group(1).strip()
                    else:
                        continue
                else:
                    h4_title = clean_text(h4_section[:h4_end])

                if h4_title in ("Summative", "Referral", "Repeat", "Repeat Year"):
                    lines.append(f"### {h4_title}")
                    lines.append("")

                    sub_tables = re.findall(r"<table[^>]*>(.*?)</table>", h4_section, re.DOTALL)
                    sub_paragraphs = re.findall(r"<p[^>]*>(.*?)</p>", h4_section, re.DOTALL)

                    for p in sub_paragraphs:
                        text = clean_text(p)
                        if text:
                            lines.append(text)
                            lines.append("")

                    for tbl in sub_tables:
                        rows = re.findall(r"<tr>(.*?)</tr>", tbl, re.DOTALL)
                        if len(rows) >= 2:
                            headers = [clean_text(h) for h in re.findall(r"<th>(.*?)</th>", rows[0], re.DOTALL)]
                            for row in rows[1:]:
                                values = [clean_text(v) for v in re.findall(r"<td>(.*?)</td>", row, re.DOTALL)]
                                for h, v in zip(headers, values):
                                    if v:
                                        lines.append(f"- **{h}:** {v}")
                            lines.append("")

        elif section_title == "Resources":
            resource_boxes = re.findall(r'<div class="resource-box">(.*?)</div>', section_body, re.DOTALL)
            for box in resource_boxes:
                res_title = re.search(r"<h4>(.*?)</h4>", box, re.DOTALL)
                res_type = re.search(r"<h5[^>]*>(.*?)</h5>", box, re.DOTALL)
                authors = re.search(r"Authors:\s*</b>(.*?)</p>", box, re.DOTALL)
                edition = re.search(r"Edition:\s*</b>(.*?)</p>", box, re.DOTALL)
                year = re.search(r"Year of publication:\s*</b>(.*?)</p>", box, re.DOTALL)
                link = re.search(r'<a href="[^"]*">(.*?)</a>', box, re.DOTALL)

                if res_title:
                    title_text = clean_text(res_title.group(1))
                    type_text = clean_text(res_type.group(1)) if res_type else ""
                    lines.append(f"- **{title_text}** ({type_text})")
                    if authors:
                        lines.append(f"  - Authors: {authors.group(1).strip()}")
                    if edition:
                        lines.append(f"  - Edition: {edition.group(1).strip()}")
                    if year:
                        lines.append(f"  - Year: {year.group(1).strip()}")
                    if link:
                        lines.append(f"  - Link: {clean_text(link.group(1))}")
            lines.append("")

        elif section_title == "Requisites":
            text = clean_text(section_body)
            if text:
                lines.append(text)
                lines.append("")

        else:
            for p in paragraphs:
                text = clean_text(p)
                if text and "Note for students" not in text and "Note for staff" not in text:
                    lines.append(text)
                    lines.append("")
            if not paragraphs:
                text = clean_text(section_body)
                if text and "Note for students" not in text:
                    lines.append(text)
                    lines.append("")

    return "\n".join(lines)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    files = sorted([f for f in os.listdir(SYLLABUS_DIR) if f.endswith(".mhtml")])
    print(f"Processing {len(files)} MHTML files...\n")

    for filename in files:
        filepath = os.path.join(SYLLABUS_DIR, filename)
        md_filename = filename.replace(".mhtml", ".md")
        output_path = os.path.join(OUTPUT_DIR, md_filename)

        html = extract_html_from_mhtml(filepath)
        if not html:
            print(f"  SKIP (no HTML found): {filename}")
            continue

        markdown = html_to_markdown(html)
        if not markdown:
            print(f"  SKIP (no article found): {filename}")
            continue

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(markdown)

        orig_size = os.path.getsize(filepath)
        new_size = os.path.getsize(output_path)
        ratio = (1 - new_size / orig_size) * 100
        print(f"  {filename}")
        print(f"    {orig_size/1024:.0f} KB -> {new_size/1024:.1f} KB ({ratio:.0f}% smaller)")

    orig_total = sum(os.path.getsize(os.path.join(SYLLABUS_DIR, f)) for f in files)
    new_files = [f for f in os.listdir(OUTPUT_DIR) if f.endswith(".md")]
    new_total = sum(os.path.getsize(os.path.join(OUTPUT_DIR, f)) for f in new_files)
    print(f"\nTotal: {orig_total/1024:.0f} KB -> {new_total/1024:.1f} KB ({(1-new_total/orig_total)*100:.0f}% smaller)")
    print(f"Files: {len(files)} -> {len(new_files)}")


if __name__ == "__main__":
    main()
