#!/usr/bin/env python3
from pathlib import Path
import posixpath
import re

ROOT = Path(__file__).resolve().parents[1]

HEADER_TEMPLATE = (ROOT / "partials/header.html").read_text(encoding="utf-8")
FOOTER_TEMPLATE = (ROOT / "partials/footer.html").read_text(encoding="utf-8")

PRODUCT_LINK = "https://www.klicktipp.com/?a=226599"
GRUNDLAGENKURS_LINK = "https://www.klicktipp.com/de/support/wissensdatenbank/grundlagenkurs/?a=226599"
LEADS_LINK = "https://www.klicktipp.com/de/marketing-suite/leads-generieren/?a=226599"
EMAIL_LINK = "https://www.klicktipp.com/de/marketing-suite/email-marketing/?a=226599"
CRM_LINK = "https://www.klicktipp.com/de/marketing-suite/marketing-crm/?a=226599"

NAV_ITEMS = [
    ("Start", ""),
    ("Grundlagenkurs", "grundlagenkurs/"),
    ("Leads", "leads-generieren/landingpage-ohne-programmierer/"),
    ("E-Mail", "email-marketing/newsletter-schneller-erstellen/"),
    ("CRM", "marketing-crm/tags-statt-listenchaos/"),
    ("Follow-up", "follow-up-prozess/"),
]

FOOTER_GROUPS = [
    (
        "Start",
        [
            ("Startseite", ""),
            ("Grundlagenkurs", "grundlagenkurs/"),
            ("Follow-up-System", "follow-up-prozess/"),
            ("Follow-up-Checkliste", "follow-up-checkliste/"),
            ("Lead-Magnet nachfassen", "lead-magnet-nachfassen/"),
            ("Webinar-Follow-up", "webinar-follow-up/"),
        ],
    ),
    (
        "Leads generieren",
        [
            ("Landingpage ohne Programmierer", "leads-generieren/landingpage-ohne-programmierer/"),
            ("Leadmagnet automatisch ausliefern", "leads-generieren/leadmagnet-automatisch-ausliefern/"),
            ("Opt-in-Formular starten", "leads-generieren/optin-formular-starten/"),
            ("Newsletter-Empfehlungen", "leads-generieren/newsletter-empfehlungen/"),
            ("SMS und E-Mail-Leads", "leads-generieren/sms-und-email-leads/"),
        ],
    ),
    (
        "E-Mail-Marketing",
        [
            ("Newsletter schneller erstellen", "email-marketing/newsletter-schneller-erstellen/"),
            ("Betreffzeilen und KI-Copywriter", "email-marketing/betreffzeilen-und-ki-copywriter/"),
            ("E-Mail-Zustellbarkeit verbessern", "email-marketing/email-zustellbarkeit-verbessern/"),
            ("Newsletter-Analytics verstehen", "email-marketing/newsletter-analytics-verstehen/"),
            ("Dynamische Inhalte und Personalisierung", "email-marketing/dynamische-inhalte-personalisierung/"),
        ],
    ),
    (
        "Marketing CRM",
        [
            ("Tags statt Listenchaos", "marketing-crm/tags-statt-listenchaos/"),
            ("Kontakte zentral organisieren", "marketing-crm/kontakte-zentral-organisieren/"),
            ("Segmentierung nach Interesse", "marketing-crm/segmentierung-nach-interesse/"),
            ("Doppelte Kontakte vermeiden", "marketing-crm/doppelte-kontakte-vermeiden/"),
            ("Kontakthistorie und LeadValue", "marketing-crm/kontakthistorie-und-leadvalue/"),
        ],
    ),
]

PAGES = {
    "index.html": "Start",
    "grundlagenkurs/index.html": "Grundlagenkurs",
    "follow-up-prozess/index.html": "Follow-up",
    "follow-up-checkliste/index.html": "Follow-up",
    "lead-magnet-nachfassen/index.html": "Follow-up",
    "webinar-follow-up/index.html": "Follow-up",
    "rechtliches/impressum.html": None,
    "rechtliches/datenschutz.html": None,
}


def href_for(page: Path, target: str) -> str:
    start = "." if page.parent == Path(".") else page.parent.as_posix()
    destination = "." if target == "" else target.rstrip("/")
    relative = posixpath.relpath(destination, start=start)
    if relative == ".":
        return "./"
    suffix = "/" if target == "" or target.endswith("/") else ""
    return f"{relative}{suffix}"


def render_nav(page: Path, active: str | None, footer: bool = False) -> str:
    lines = []
    for label, target in NAV_ITEMS:
        href = href_for(page, target)
        text = "Follow-up-Checkliste" if footer and label == "Checkliste" else label
        text = "Lead-Magnet nachfassen" if footer and label == "Lead-Magnet" else text
        text = "Webinar-Follow-up" if footer and label == "Webinar" else text
        current = ""
        if label == active and not footer:
            current = ' aria-current="page"' if href == "./" else ' data-active-section="true"'
        lines.append(f'      <a href="{href}"{current}>{text}</a>')
    return "\n".join(lines)


def render_footer_nav(page: Path) -> str:
    blocks = []
    for title, items in FOOTER_GROUPS:
        links = "\n".join(f'        <a href="{href_for(page, target)}">{label}</a>' for label, target in items)
        blocks.append(
            "      <div class=\"footer-nav-group\">\n"
            f"        <strong>{title}</strong>\n"
            f"{links}\n"
            "      </div>"
        )
    return "\n".join(blocks)


def render_header(page: Path, active: str | None) -> str:
    cta_map = {
        "Grundlagenkurs": (GRUNDLAGENKURS_LINK, "Grundlagenkurs öffnen"),
        "Leads": (LEADS_LINK, "Leads mit KlickTipp"),
        "E-Mail": (EMAIL_LINK, "E-Mail-Marketing ansehen"),
        "CRM": (CRM_LINK, "Marketing CRM ansehen"),
    }
    cta_href, cta_text = cta_map.get(active, (PRODUCT_LINK, "KlickTipp ansehen"))
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
        .replace("{{FOOTER_NAV_ITEMS}}", render_footer_nav(page))
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
    for page in sorted(ROOT.glob("leads-generieren/*/index.html")):
        PAGES[page.relative_to(ROOT).as_posix()] = "Leads"
    for page in sorted(ROOT.glob("email-marketing/*/index.html")):
        PAGES[page.relative_to(ROOT).as_posix()] = "E-Mail"
    for page in sorted(ROOT.glob("marketing-crm/*/index.html")):
        PAGES[page.relative_to(ROOT).as_posix()] = "CRM"
    for relative_path, active in PAGES.items():
        sync_page(relative_path, active)


if __name__ == "__main__":
    main()
