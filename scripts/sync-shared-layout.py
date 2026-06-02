#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

HEADER_TEMPLATE = (ROOT / "partials/header.html").read_text(encoding="utf-8")
FOOTER_TEMPLATE = (ROOT / "partials/footer.html").read_text(encoding="utf-8")

PRODUCT_LINK = "https://www.klicktipp.com/?a=226599"
GRUNDLAGENKURS_LINK = "https://www.klicktipp.com/de/support/wissensdatenbank/grundlagenkurs/?a=226599"

NAV_ITEMS = [
    ("Start", ""),
    ("Grundlagenkurs", "grundlagenkurs/"),
    ("Follow-up-System", "follow-up-prozess/"),
    ("Checkliste", "follow-up-checkliste/"),
    ("Lead-Magnet", "lead-magnet-nachfassen/"),
    ("Webinar", "webinar-follow-up/"),
]

PAGES = {
    "index.html": "Start",
    "grundlagenkurs/index.html": "Grundlagenkurs",
    "follow-up-prozess/index.html": "Follow-up-System",
    "follow-up-checkliste/index.html": "Checkliste",
    "lead-magnet-nachfassen/index.html": "Lead-Magnet",
    "webinar-follow-up/index.html": "Webinar",
    "rechtliches/impressum.html": None,
    "rechtliches/datenschutz.html": None,
}


def href_for(page: Path, target: str) -> str:
    page_dir = "" if page.name == "index.html" and page.parent == Path(".") else f"{page.parent.as_posix()}/"
    if page == Path("index.html"):
        return "./" if target == "" else target
    if target == "":
        return "../"
    if target == page_dir:
        return "./"
    return f"../{target}"


def render_nav(page: Path, active: str | None, footer: bool = False) -> str:
    lines = []
    for label, target in NAV_ITEMS:
        href = href_for(page, target)
        text = "Follow-up-Checkliste" if footer and label == "Checkliste" else label
        text = "Lead-Magnet nachfassen" if footer and label == "Lead-Magnet" else text
        text = "Webinar-Follow-up" if footer and label == "Webinar" else text
        current = ' aria-current="page"' if label == active and not footer else ""
        lines.append(f'      <a href="{href}"{current}>{text}</a>')
    return "\n".join(lines)


def render_header(page: Path, active: str | None) -> str:
    cta_href = GRUNDLAGENKURS_LINK if active == "Grundlagenkurs" else PRODUCT_LINK
    cta_text = "Grundlagenkurs öffnen" if active == "Grundlagenkurs" else "KlickTipp ansehen"
    return (
        HEADER_TEMPLATE
        .replace("{{BRAND_HREF}}", href_for(page, ""))
        .replace("{{NAV_ITEMS}}", render_nav(page, active))
        .replace("{{CTA_HREF}}", cta_href)
        .replace("{{CTA_TEXT}}", cta_text)
    )


def render_footer(page: Path) -> str:
    return (
        FOOTER_TEMPLATE
        .replace("{{BRAND_HREF}}", href_for(page, ""))
        .replace("{{FOOTER_NAV_ITEMS}}", render_nav(page, None, footer=True))
        .replace("{{IMPRESSUM_HREF}}", href_for(page, "rechtliches/impressum.html"))
        .replace("{{DATENSCHUTZ_HREF}}", href_for(page, "rechtliches/datenschutz.html"))
    )


def indent_block(block: str, indent: str) -> str:
    return "\n".join(f"{indent}{line}" if line else "" for line in block.splitlines())


def replace_shared_block(text: str, name: str, tag: str, rendered: str) -> str:
    marker_re = re.compile(
        rf"(?ms)^([ \t]*)<!-- xioo-shared-{name}:start -->.*?^\1<!-- xioo-shared-{name}:end -->"
    )
    tag_re = re.compile(rf"(?ms)^([ \t]*)<{tag}\b.*?^\1</{tag}>")
    marker_match = marker_re.search(text)
    tag_match = tag_re.search(text)
    match = marker_match or tag_match
    if not match:
        raise RuntimeError(f"Kein {name}-Block gefunden")
    indent = match.group(1)
    wrapped = (
        f"{indent}<!-- xioo-shared-{name}:start -->\n"
        f"{indent_block(rendered, indent)}\n"
        f"{indent}<!-- xioo-shared-{name}:end -->"
    )
    return text[: match.start()] + wrapped + text[match.end():]


def sync_page(relative_path: str, active: str | None) -> None:
    page = Path(relative_path)
    path = ROOT / page
    text = path.read_text(encoding="utf-8")
    text = replace_shared_block(text, "header", "header", render_header(page, active))
    text = replace_shared_block(text, "footer", "footer", render_footer(page))
    path.write_text(text, encoding="utf-8")


def main() -> None:
    for relative_path, active in PAGES.items():
        sync_page(relative_path, active)


if __name__ == "__main__":
    main()
