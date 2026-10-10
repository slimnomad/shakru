from pathlib import Path
from zipfile import ZipFile
from hashlib import sha256
from lxml import etree
from PIL import Image
import json, unittest, sys

ROOT=Path('/Users/aliassylkhan/Desktop/learningsh')
sys.path.insert(0,str(ROOT/'tmp/green-asian-wok/validation-deps'))
OUT=ROOT/'output/green-asian-wok'
BASE=json.loads((ROOT/'tmp/green-asian-wok/baseline.json').read_text())
REF=Path(BASE['reference'])
DOC=OUT/'green-asian-wok-system-design.docx'
NS={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
EDITABLE={'word/document.xml','word/footer1.xml','word/footnotes.xml','word/media/image1.png'}

class DeliveryTests(unittest.TestCase):
    def test_three_valid_independent_images(self):
        paths=sorted((OUT/'concepts').glob('*.png'))
        self.assertEqual(len(paths),3)
        hashes=[]
        for path in paths:
            with Image.open(path) as im:
                im.verify()
            with Image.open(path) as im:
                self.assertGreaterEqual(min(im.size),1000)
                print(f'{path.name}: {im.width} x {im.height} pixels')
            hashes.append(sha256(path.read_bytes()).hexdigest())
        self.assertEqual(len(set(hashes)),3)

    def test_reference_unchanged(self):
        self.assertEqual(sha256(REF.read_bytes()).hexdigest(),BASE['sha256'])

    def test_preserved_package_and_geometry(self):
        with ZipFile(REF) as ref,ZipFile(DOC) as final:
            self.assertEqual(set(ref.namelist()),set(final.namelist()))
            for name in ref.namelist():
                if name not in EDITABLE:self.assertEqual(ref.read(name),final.read(name),name)
            a=etree.fromstring(ref.read('word/document.xml'))
            b=etree.fromstring(final.read('word/document.xml'))
            self.assertEqual(etree.tostring(a.xpath('//w:sectPr',namespaces=NS)[0]),etree.tostring(b.xpath('//w:sectPr',namespaces=NS)[0]))
            self.assertEqual(len(a.xpath('//w:tbl',namespaces=NS)),len(b.xpath('//w:tbl',namespaces=NS)))
            # Ignore intended text updates; all Word XML layout/style attributes and nodes must remain identical.
            for tree in [a,b]:
                for t in tree.xpath('//w:t',namespaces=NS):
                    t.text='';t.attrib.clear()
            self.assertEqual(etree.tostring(a),etree.tostring(b))

    def test_all_template_slots_filled(self):
        with ZipFile(DOC) as z:
            for name in ['word/document.xml','word/footer1.xml','word/footnotes.xml']:
                t=''.join(etree.fromstring(z.read(name)).xpath('//w:t/text()',namespaces=NS))
                self.assertNotIn('[',t,name)
                self.assertNotIn('System Name',t)
            t=' '.join(etree.fromstring(z.read('word/document.xml')).xpath('//w:t/text()',namespaces=NS))
            for heading in ['Abstract','Goals and Non-Goals','Background and Problem Statement','Proposed Architecture','Request Lifecycle','API and Data Contracts','Consistency, Idempotency, and Replay','Security and Privacy Considerations','Operational Readiness','Alternatives Considered','Open Questions','Decision and Next Steps']:
                self.assertIn(heading,t)
            self.assertIn('menu-contract.schema.json',t)

    def test_evidence_and_limitations_present(self):
        audit=(OUT/'audit.md').read_text()
        for n in ['01-home-desktop.jpg','02-order-type-desktop.jpg','03-menu-desktop.jpg','04-dish-options-desktop.jpg','07-home-mobile.jpg','08-menu-mobile.jpg']:
            self.assertTrue((OUT/'evidence'/n).exists())
            self.assertIn(n,audit)
        for text in ['6 reviews','€11.60','01 265 9610','sixth individual record','No order or feedback was submitted']:
            self.assertIn(text,audit)

    def test_schema_is_valid_and_has_guardrails(self):
        import jsonschema
        schema=json.loads((OUT/'menu-contract.schema.json').read_text())
        jsonschema.Draft202012Validator.check_schema(schema)
        check=jsonschema.Draft202012Validator(schema,format_checker=jsonschema.FormatChecker())
        sample={'schema_version':1,'menu_version':'example-not-published','verified_at':'2026-10-10T12:00:00+01:00','items':[{'item_id':'example','name':'Sweet & Sour Chicken','category':'Sweet & Sour Dishes','price_minor':1100,'currency':'EUR','allergens':['Gluten','Eggs','Sesame Seeds'],'options':[]}]}
        check.validate(sample)
        for bad in [-1,11.2]:
            sample['items'][0]['price_minor']=bad
            self.assertTrue(list(check.iter_errors(sample)))
        sample['items'][0]['price_minor']=1100
        sample['items'][0]['currency']='USD'
        self.assertTrue(list(check.iter_errors(sample)))

if __name__=='__main__':unittest.main(verbosity=2)
