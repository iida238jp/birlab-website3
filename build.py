"""Optional editor helper. Generated HTML works without Python or a build step."""
import json
import subprocess
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent
D = json.loads((ROOT / 'content.json').read_text())

def esc(value):
    return escape(str(value), quote=True)

def size(file):
    result = subprocess.check_output(['/usr/bin/sips', '-g', 'pixelWidth', '-g', 'pixelHeight', str(ROOT / 'assets' / file)]).decode()
    return (int(result.split('pixelWidth: ')[1].split()[0]), int(result.split('pixelHeight: ')[1].split()[0]))

SIZES = {p.name: size(p.name) for p in (ROOT/'assets').iterdir() if p.is_file()}

def render(lang):
    t = D['copy'][lang]
    base = '' if lang == 'en' else '../'
    def img(file, alt, cls='', eager=False):
        w,h = SIZES[file]
        loading = 'fetchpriority="high"' if eager else 'loading="lazy"'
        return '<img src="{}assets/{}" alt="{}" width="{}" height="{}" {} class="{}">'.format(base,file,esc(alt),w,h,loading,cls)
    def heading(id,number,title,text):
        return '<div class="section-heading"><p class="eyebrow">{} / {}</p><div><h2>{}</h2><p>{}</p></div></div>'.format(number,esc(t[id]),title,esc(text))
    nav = ''.join('<a href="#{}">{}</a>'.format(id,esc(t[id])) for id in D['nav'])
    langs = ''.join('<a class="language-link" href="{}#home" hreflang="{}" lang="{}" {}>{}</a>'.format(base+('index.html' if l=='en' else 'ja/index.html'),l,l,'aria-current="page"' if l==lang else '',label) for l,label in [('en','EN'),('ja','日本語')])
    research = ''.join('''<article class="research-card" data-content-id="{id}"><figure><div class="research-image">{image}</div><figcaption>{caption}</figcaption></figure><p class="eyebrow">0{n}</p><h3>{title}</h3><p>{text}</p></article>'''.format(id=r['id'],image=img(r['image'],r['alt'][lang]),caption=esc(r['caption'][lang]),n=i+1,title=esc(r['title'][lang]),text=esc(r['text'][lang])) for i,r in enumerate(D['research']))
    examples = ''.join('<figure>{}<figcaption>{}</figcaption></figure>'.format(img(e['image'],e['alt'][lang]),esc(e['caption'][lang])) for e in D['examples'])
    videos = ''.join('''<figure class="video"><div class="video-stage" data-video-id="{id}" data-video-title="{title}"><button class="video-play" aria-label="{play}: {title}">{poster}<span class="play-label">{play}</span></button><noscript><iframe src="https://www.youtube-nocookie.com/embed/{id}" title="{title}" loading="lazy" allow="encrypted-media; picture-in-picture" allowfullscreen></iframe></noscript></div><figcaption>{title}<span>{provider}</span></figcaption></figure>'''.format(id=v['id'],title=esc(v['caption'][lang]),play=esc(t['play']),poster=img('video-'+v['id']+'.jpg',v['caption'][lang]),provider=esc(t['videoProvider'])) for v in D['videos'])
    people=''
    for place,members in D['members'].items():
        rows=''.join('<div data-member="{}"><dt>{}</dt><dd>{}</dd></div>'.format(esc(name),esc(name),esc(t[role])) for name,role in members)
        people+='<article class="location"><h3>{}</h3><p>{}</p><dl>{}</dl></article>'.format(esc(t[place]),esc(t[place+'Dept']),rows)
    papers=''.join('''<li data-doi="{doi}"><div class="paper-year">{year}</div><div><p class="paper-venue">{venue}</p><h3 lang="en">{title}</h3><p class="paper-authors" lang="en">{authors}</p><a class="doi" href="https://doi.org/{doi}" aria-label="DOI: {title}">doi: {doi}</a></div></li>'''.format(**{k:esc(v) for k,v in p.items()}) for p in D['papers'])
    events=''.join('<figure>{}<figcaption><h3>{}</h3><p>{}</p></figcaption></figure>'.format(img(e['image'],e['alt'][lang]),esc(e['title'][lang]),esc(e['place'][lang])) for e in D['events'])
    join=''.join('<article><h3>{}</h3><p>{}</p></article>'.format(esc(t['join'+key]),esc(t['join'+key+'Text'])) for key in ['Students','Researchers','Collaborators'])
    heroalt={'en':'Foodly humanoid robot with two arms and soft green grippers','ja':'二本の腕と緑色の柔軟なグリッパを備えたヒューマノイドロボットFoodly'}[lang]
    groupalt={'en':'Members and alumni at the BIRL reunion workshop at UCL in London, December 2023','ja':'2023年12月、ロンドンのUCLで開催されたBIRL同窓ワークショップのメンバーと卒業生'}[lang]
    result='''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="{description}"><meta name="theme-color" content="#f5f3ed"><title>{title}</title><link rel="stylesheet" href="{base}style.css"><link rel="alternate" hreflang="en" href="{base}index.html"><link rel="alternate" hreflang="ja" href="{base}ja/index.html"><script src="{base}script.js" defer></script></head>
<body><noscript><style>.menu-toggle,.video-play{{display:none!important}}@media(max-width:780px){{.header nav{{display:flex}}}}</style></noscript><a class="skip" href="#main">{skip}</a>
<header class="header"><a class="brand" href="#home" aria-label="BIRL"><strong>BIRL<span class="brand-dot">.</span></strong><span>{lab}</span></a><button class="menu-toggle" aria-controls="navigation" aria-expanded="false">{menu}</button><nav id="navigation" aria-label="{navLabel}">{nav}</nav><div class="languages" aria-label="{language}">{langs}</div></header>
<main id="main"><section class="hero wrap" id="home"><div class="hero-copy"><p class="eyebrow">{heroLabel}</p><h1>{heroTitle}</h1><p class="intro">{heroText}</p><div class="affiliations"><p>{tokyo}<span>{tokyoDept}</span></p><p>{cambridge}<span>{cambridgeDept}</span></p></div></div><figure class="hero-figure">{heroimg}<figcaption>{heroCaption}</figcaption></figure></section>
<section class="section wrap" id="research">{researchHeading}<div class="research-grid">{research}</div><div class="visual-strip"><p class="eyebrow">{examplesLabel}</p><div class="example-grid">{examples}</div></div><div class="video-strip"><p class="eyebrow">{videoLabel}</p><div class="video-grid">{videos}</div></div></section>
<section class="people-section" id="people"><div class="section wrap">{peopleHeading}<figure class="group-photo">{groupimg}<figcaption>{historical}</figcaption></figure><div class="pi"><p class="eyebrow">{pi}</p><h3>{piName}</h3><p>{tokyo} / {cambridge}</p></div><div class="people-grid" aria-label="{currentMembers}">{people}</div></div></section>
<section class="section wrap" id="publications">{publicationsHeading}<ol class="paper-list" aria-label="{paperLabel}">{papers}</ol></section>
<section class="community-section" id="community"><div class="section wrap">{communityHeading}<p class="eyebrow past">{past}</p><div class="community-grid">{events}</div></div></section>
<section class="section wrap join" id="join"><div>{joinHeading}<p class="enquiry">{enquiry}</p><div class="contact"><p class="eyebrow">{contact}</p><a href="mailto:{email}">{email}</a></div><p class="availability">{availability}</p></div><div class="join-paths">{join}</div></section></main>
<footer class="wrap"><div><strong>BIRL.</strong><span>{footer}</span></div><p>{visualCredit}<br>© <span id="year">2026</span> BIRL</p></footer></body></html>'''.format(
        **{k:esc(v) for k,v in t.items() if k not in ['heroTitle','researchTitle','peopleTitle','communityTitle','joinTitle','research','people','join','examples']},
        lang=lang,base=base,nav=nav,langs=langs,heroTitle=t['heroTitle'],heroimg=img('foodly.jpeg',heroalt,eager=True),
        researchHeading=heading('research','01',t['researchTitle'],t['researchText']),research=research,
        examplesLabel=esc(t['examples']),examples=examples,videos=videos,
        peopleHeading=heading('people','02',t['peopleTitle'],t['peopleText']),groupimg=img('reunion.jpg',groupalt),people=people,
        publicationsHeading=heading('publications','03',t['publicationsTitle'],t['publicationsText']),papers=papers,
        communityHeading=heading('community','04',t['communityTitle'],t['communityText']),events=events,
        joinHeading=heading('join','05',t['joinTitle'],t['joinText']),email=esc(D['email']),join=join)
    target=ROOT/('index.html' if lang=='en' else 'ja/index.html')
    target.parent.mkdir(exist_ok=True)
    target.write_text(result,encoding='utf-8')

for lang in ['en','ja']:
    render(lang)
print('Generated English and Japanese homepages from shared content.json')
