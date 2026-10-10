from pathlib import Path
from zipfile import ZipFile
from hashlib import sha256
from lxml import etree
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import json, sys

ROOT=Path('/Users/aliassylkhan/Desktop/learningsh')
TMP=ROOT/'tmp/green-asian-wok'
OUT=ROOT/'output/green-asian-wok'
BASE=json.loads((TMP/'baseline.json').read_text())
REF=Path(BASE['reference'])
assert sha256(REF.read_bytes()).hexdigest()==BASE['sha256']
sys.path.insert(0,'/Users/aliassylkhan/.codex/plugins/cache/openai-primary-runtime/documents/26.1009.11318/skills/documents/scripts')
from docx_ooxml_patch import NS, _qn

def replace_text(el, text):
    ts=el.xpath('.//w:t',namespaces=NS)
    assert ts
    ts[0].text=text
    ts[0].set('{http://www.w3.org/XML/1998/namespace}space','preserve')
    for t in ts[1:]: t.text=''

paragraphs={
8:'Green Asian Wok',9:'Web Design Proposal',
22:'Green Asian Wok needs a clearer path from choosing food to placing an order. This proposal combines the website audit and review findings with a menu-led frontend, while retaining the existing ordering provider for checkout and fulfilment.',
23:'Evidence was collected on 10 October 2026. Three visual concepts are delivered separately. This is a proposed system design, not a shipped website or an assertion about provider capabilities. Operational contacts, schedules and integration access require confirmation.',
28:'The current homepage prioritises a large food banner and app promotion. Desktop ordering then adds a fulfilment page and another banner before dishes. Maps and the site show different phone numbers; collection hours are difficult to interpret across midnight.',
29:'Google showed 4.5 stars from six ratings. Four visible written reviews praised flavour, value or portions; the visible two-star rating had no comment. Five individual records were exposed. These limited observations support honest dish discovery, not claims about delivery reliability.',
33:'Figure 1. Proposed website and ordering provider boundary.',
40:'A customer opens the homepage or menu. Browsing should work without an account or address; delivery and collection are explicit choices.',
41:'The frontend validates required item options and quantities. The provider validates current availability, service area and final prices at checkout.',
42:'Load a business-approved menu version, contact record and day-specific schedule. Treat unconfirmed operational data as unpublished.',
43:'Show dishes, prices and allergen information. Selecting a dish opens options and an updated total before adding it to the basket.',
44:'Store only a transient basket if supported. The provider remains responsible for durable order and payment records.',
45:'Handoff through a supported provider route. If an integration is unavailable, use its official ordering page and make that transition clear.',
46:'Only provider-confirmed success represents an accepted order. Measure menu engagement and successful handoff without recording personal payloads.',
54:'Validate the menu contract before publication; reject missing prices, ambiguous currency and unapproved allergen labels.',
55:'Assign stable item IDs and a version to each approved menu; never use display text as the identifier.',
56:'Retain the menu version and verification timestamp. At checkout, the provider must revalidate price and availability.',
57:'The content contract is the website display source. It is not a payment ledger or proof of restaurant order acceptance.',
58:'The proposed display contract is supplied in ',
59:'menu-contract.schema.json. Provider API access and basket transfer remain unconfirmed.',
63:'Repeated menu reads may be cached. Basket additions must not be duplicated by retries. Payment and order idempotency belong to the provider; this proposal does not assume undocumented provider guarantees. A failed handoff must never display order success.',
67:'Public browsing needs no login. Restrict menu publication to authorised staff; use provider-supported authentication for ordering administration.',
68:'Collect no address or phone number on the marketing site unless a supported flow requires it. Exclude payment, address and contact values from analytics.',
69:'Keep provider credentials server-side if an approved API is used. No secret belongs in browser code or static content.',
70:'Preview menu changes before publishing. Operational support views should expose only the data needed to resolve an issue.',
71:'The business and provider must confirm retention and privacy responsibilities. Keep analytics aggregate and document deletion and support routes before launch.',
81:'Which phone number is correct: Maps 01 265 9610 or the website 01 491 0221 / 085 199 6556?',
82:'What are the correct day-specific delivery and collection intervals, including the after-midnight boundary?',
83:'Does the existing provider support stable menu links, mode persistence, basket handoff or a documented API?',
84:'Who approves menu prices, allergens, real food photography, brand assets and listing updates?',
87:'Recommended architecture: build the selected visual concept around a verified menu record and retain provider ordering. Confirm operational data, replace illustrative assets, implement interactions, then test the complete browse-to-handoff path. Release only after visual, accessibility and provider checks pass.',
}

tables={
0:[['STATUSProposed','','OWNERNot assigned','','LAST UPDATED10 October 2026']],
1:[['Authors','Codex'],['Reviewers','Business owner and provider'],['Related docs','Website audit and three visual concepts'],['Scope','Customer-facing website and provider handoff']],
2:[['Goals','Non-goals'],['Show useful dishes and prices before ordering','Build a second payment or order ledger'],['Make contact and hours consistent','Infer service quality from six ratings'],['Support mobile, keyboard and readable states','Assert dietary or health claims without approval'],['Verify the provider handoff before release','Assume undocumented provider APIs']],
3:[['Component','Responsibility','Primary storage','Failure behavior'],['Website UI','Accessible menu, search, mode choice and item options','Static build and content delivery network','Useful error and official ordering route'],['Menu content','Dish names, prices, allergens and option groups','Versioned business-approved content file','Reject invalid publication and retain approved content'],['Business record','Contact number, address and day-specific availability','Approved location and schedule record','Hide unconfirmed values and explain unavailable modes'],['Ordering provider','Current prices, checkout, payment and accepted order status','Existing provider service and order records','No unconfirmed success state or duplicate submission'],['Verification','Responsive, keyboard, total and supported handoff checks','Aggregate checks and monitoring records','Flag broken order routes and prevent unsafe release']],
4:[['Field','Type','Required','Description'],['item_id','string','Yes','Stable provider or approved internal identifier'],['name','string','Yes','Business-approved dish name'],['category','string','Yes','One category from the menu taxonomy'],['price_minor','integer','Yes','Non-negative cents; options are separate'],['currency','enum','Yes','EUR for this location'],['allergens','array','Yes','Approved labels; empty only if verified'],['options','array','Yes','Required/optional groups and surcharges']],
5:[['Scenario','Expected behavior','Reasoning'],['Repeated add action','One intentional addition per activation','Prevent double taps and pending retries'],['Invalid menu publication','Keep last approved version','Avoid misleading prices or allergens'],['Provider unavailable','Explain issue; no order confirmation','Do not imply acceptance without provider success'],['Menu changes in basket','Revalidate before payment','Final price belongs to current provider state']],
6:[['Signal','SLO or alert','Owner','Launch gate'],['Order entry','All route checks pass','Site owner','Required'],['Menu visibility','Useful item within opening viewport','Designer','Required'],['Handoff failure','Zero broken supported order links','Developer','Required'],['Content drift','Contacts and menu checked at release','Business','Required'],['Accessibility','Core journey works with keyboard','Developer','Required'],['Rollout constraint: Verify in preview, test provider handoff, retain rollback and publish only after the business confirms operational content. Targets are proposed acceptance gates, not measured production SLOs.']],
7:[['Alternative','Why it was considered','Why it was not selected'],['Keep existing template','Minimal engineering effort','Leaves discovery and content problems'],['Custom checkout','Full control of the journey','Adds payment and fulfilment responsibilities'],['Marketplace-only site','Existing ordering infrastructure','Less control over brand and direct discovery'],['Native app first','Potential repeat ordering convenience','Creates installation friction for first visits']],
8:[['Milestone','Deliverable','Exit criteria'],['M1','Verified content and selected concept','Business confirms disputed details and assets'],['M2','Responsive menu interactions','Keyboard, options and totals pass'],['M3','Verified provider handoff','Real supported flow checked in test mode'],['M4','Production release','Visual QA, rollback and content checks pass']],
}

with ZipFile(REF) as z:
    parts={n:z.read(n) for n in z.namelist()}
doc=etree.fromstring(parts['word/document.xml'])
ps=doc.xpath('//w:body/w:p',namespaces=NS)
for i,text in paragraphs.items(): replace_text(ps[i],text)
for i,rows in tables.items():
    t=doc.xpath('//w:tbl',namespaces=NS)[i]
    trs=t.xpath('./w:tr',namespaces=NS)
    assert len(trs)==len(rows)
    for tr,row in zip(trs,rows):
        cells=tr.xpath('./w:tc',namespaces=NS)
        assert len(cells)==len(row)
        for cell,text in zip(cells,row):
            # Metadata uses separate label/value paragraphs; preserve those roles.
            if i==0 and text:
                cps=cell.xpath('./w:p',namespaces=NS)
                if len(cps)>1:
                    label,value=next((l,text[len(l):]) for l in ['STATUS','OWNER','LAST UPDATED'] if text.startswith(l))
                    replace_text(cps[0],label); replace_text(cps[1],value)
                else: replace_text(cell,text)
            elif text: replace_text(cell,text)
parts['word/document.xml']=etree.tostring(doc,xml_declaration=True,encoding='UTF-8',standalone=True)
for name,text in [('word/footer1.xml','Green Asian Wok | System Design RFC'),('word/footnotes.xml',' Evidence reflects publicly visible pages on 10 October 2026. Architecture and acceptance gates are proposals.')]:
    x=etree.fromstring(parts[name]); replace_text(x,text)
    parts[name]=etree.tostring(x,xml_declaration=True,encoding='UTF-8',standalone=True)

# Replace the editable diagram image; retain its original drawing frame and relationship.
source_img=Image.open(BytesIO(parts['word/media/image1.png']))
W,H=source_img.size
img=Image.new('RGB',(W,H),'#F5FAFD'); d=ImageDraw.Draw(img)
scale=W/1400
def xy(rect):return tuple(round(v*scale) for v in rect)
def font(size,bold=False):
    n='word/fonts/HelveticaNeue-bold.ttf' if bold else 'word/fonts/HelveticaNeue-regular.ttf'
    try:return ImageFont.truetype(BytesIO(parts[n]),round(size*scale))
    except OSError:return ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',round(size*scale))
def txt(x,y,t,size=18,fill='#0B2D4B',bold=False):d.text(xy((x,y)),t,font=font(size,bold),fill=fill)
d.rectangle(xy((0,0,1400,100)),fill='#0B2D4B')
txt(35,23,'Green Asian Wok   Proposed architecture',22,'white',True)
txt(35,58,'Website owns discovery   Ordering provider owns checkout and accepted orders',16,'#D8E8F3')
boxes=[(50,165,270,275,'Customer browser','Browse and configure'),(385,165,640,275,'Website','Menu and mode choices'),(760,165,1040,275,'Ordering provider','Price and order validation'),(1150,165,1360,275,'Restaurant','Prepare and fulfil'),(385,395,640,505,'Approved content','Menu, assets, contacts'),(760,395,1040,505,'Provider records','Orders and payments'),(1150,395,1360,505,'Verification','Handoff and UI checks')]
for x1,y1,x2,y2,title,sub in boxes:
    d.rounded_rectangle(xy((x1,y1,x2,y2)),radius=round(5*scale),fill='#FFFFFF' if y1<300 else '#E3EEF6',outline='#40627B',width=max(1,round(scale)))
    txt(x1+15,y1+26,title,18,bold=True); txt(x1+15,y1+60,sub,15)
def arrow(x1,y1,x2,y2):
    d.line(xy((x1,y1,x2,y2)),fill='#357498',width=round(3*scale))
    if x1==x2:d.polygon([xy((x2,y2)),xy((x2-10,y2-20)),xy((x2+10,y2-20))],fill='#357498')
    else:d.polygon([xy((x2,y2)),xy((x2-20,y2-10)),xy((x2-20,y2+10))],fill='#357498')
for coords in [(270,220,385,220),(640,220,760,220),(1040,220,1150,220),(512,275,512,395),(900,275,900,395),(1255,275,1255,395)]:arrow(*coords)
txt(50,570,'Supported handoff only. Provider APIs and basket transfer are not yet confirmed.',17)
d.rectangle((0,H-round(36*scale),W,H),fill='#DDEBF5')
d.text((round(35*scale),H-round(27*scale)),'Proposed boundary   No payment processing or durable order storage in the website',font=font(14),fill='#40627B')
buf=BytesIO();img.save(buf,format='PNG');parts['word/media/image1.png']=buf.getvalue()
img.save(TMP/'architecture.png')
final=OUT/'green-asian-wok-system-design.docx'
with ZipFile(final,'w') as z:
    for n,b in parts.items():z.writestr(n,b)
print('Created',final)
print('Reference unchanged:',sha256(REF.read_bytes()).hexdigest()==BASE['sha256'])
