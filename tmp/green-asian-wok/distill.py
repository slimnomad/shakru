from pathlib import Path
from zipfile import ZipFile
from hashlib import sha256
from lxml import etree
import json

ROOT = Path('/Users/aliassylkhan/Desktop/learningsh')
REF = Path('/Users/aliassylkhan/.codex/plugins/cache/openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-system-design/assets/reference.docx')
TMP = ROOT / 'tmp/green-asian-wok'
NS = {'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
with ZipFile(REF) as z:
    inventory = {n: {'size':len(z.read(n)), 'sha256':sha256(z.read(n)).hexdigest()} for n in z.namelist()}
    doc = etree.fromstring(z.read('word/document.xml'))
    paragraphs = doc.xpath('//w:body/w:p', namespaces=NS)
    slots = [{'part':'word/document.xml','locator':f'//w:body/w:p[{i+1}]','style':p.xpath('./w:pPr/w:pStyle/@w:val',namespaces=NS),'text':''.join(p.xpath('.//w:t/text()',namespaces=NS)),'properties':etree.tostring(p.find('w:pPr',NS)).decode() if p.find('w:pPr',NS) is not None else None} for i,p in enumerate(paragraphs)]
    tables = [etree.tostring(t).decode() for t in doc.xpath('//w:tbl',namespaces=NS)]
    styles = z.read('word/styles.xml').decode()
    section = etree.tostring(doc.xpath('//w:sectPr',namespaces=NS)[0]).decode()
    baseline = {'reference':str(REF),'sha256':sha256(REF.read_bytes()).hexdigest(),'page_count':7,'section':section,'slots':slots,'tables':tables,'styles':styles,'parts':inventory}
    (TMP/'baseline.json').write_text(json.dumps(baseline,indent=2))
    title_r = [etree.tostring(p).decode() for p in paragraphs[8:10]]
    md = f'''# System Design template execution contract

Reference: {REF}
SHA256: {baseline['sha256']}
Reference rendered and all seven pages inspected in reference-render.
One portrait Letter section, 12240 by 15840 twips. Margins left/right/top 1008 twips, bottom 893. Header/footer distance 720. First page is distinct. All section properties remain unchanged.

## Typography and recurring components
Use source Helvetica Neue and Helvetica Neue Light, with embedded fonts retained. Preserve exact styles, paragraph properties, run properties, numbering, cell shading, widths, grid tracks and table padding. Source navy headings, pale blue striped tables and light footer remain authoritative over generic document defaults. Full style and component XML evidence is baseline.json; no unknown property is replaced by a guess.
The cover has two Title paragraphs, metadata strip and four-row metadata table. Body uses Heading1 and Heading3, lettered lifecycle and guarantee lists, nine tables, one inline diagram 6.70 by 3.43 inches, one footnote reference and recurring footer. Seven reference page patterns have been inspected.

## Content flow and editable slots
Retain all twelve numbered sections: abstract; goals; background; architecture; lifecycle; API/data contracts; consistency; privacy; readiness; alternatives; questions; decision/milestones.
Every nonempty direct body paragraph and table cell is an editable text slot. Stable locators and exact properties are in baseline.json. Replace all bracketed instructional text. Keep blank spacing and page-break paragraphs intact. Keep all table/header rows, lists and existing structure intact. Unsupported details must be marked unknown or proposed, never invented.
Cover first title is business name; second title is Web Design Proposal. Metadata status is Proposed; owner/reviewer not assigned. Figure caption describes proposed browser-to-provider handoff. Diagram image1.png is an editable image slot, with its original frame/drawing relationship preserved. The new diagram must reuse the template palette and flow layout, replacing only its text/content.
Footer organization slot becomes Green Asian Wok. Footnote text becomes a definition of the evidence date and the proposed architecture boundary. No other header/footer structure changes.

## Package preservation
All parts are preserve-only except word/document.xml text nodes, word/footer1.xml text nodes, word/footnotes.xml text nodes and word/media/image1.png. All XML properties and drawings within edited parts are preserve-only. Preserve relationships, numbering, styles, fonts, theme, settings and content types byte for byte. Baseline inventories every part size and hash.

## Fidelity gates
Reference hash remains unchanged; part inventory has no additions/removals; preserve-only bytes match. Section geometry, tables and list structure match. Render final and compare every page with reference. Content changes may reflow within existing page patterns; prevent clipped rows, stranded headings, overlaps or unwanted blank pages. No style shrinking or new design preset. Exact slot text is checked for completeness and all user-facing facts are traceable to current sources.
'''
    (TMP/'artifact.md').write_text(md)
print('Distilled 89 body paragraphs, 9 tables, 24 package parts and 7 rendered pages')
