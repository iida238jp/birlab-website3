"""Rebuild ready-to-upload HTML from content/*.html. Python 3, no dependencies."""
import json, os
from pathlib import Path
from html import escape
ROOT=Path(__file__).resolve().parent
D=json.loads((ROOT/'site.json').read_text(encoding='utf-8'))
PAGE_PATHS={p['key']:p['path'] for p in D['pages']}

def write_page(page,lang):
    path=('ja/' if lang=='ja' else '')+page['path']+'index.html'
    dest=ROOT/path;dest.parent.mkdir(parents=True,exist_ok=True)
    base=os.path.relpath(ROOT,dest.parent).replace(os.sep,'/')+'/'
    if base=='./':base=''
    local=lambda p:base+p
    nav=''.join('<a href="{}"{}>{}</a>'.format(local(('ja/' if lang=='ja' else '')+PAGE_PATHS[key]+'index.html'),' aria-current="page"' if page['active']==key else '',ja if lang=='ja' else en) for key,en,ja in D['nav'])
    langs=''.join('<a href="{}" lang="{}" hreflang="{}"{}>{}</a>'.format(local(('ja/' if l=='ja' else '')+page['path']+'index.html'),l,l,' aria-current="page"' if l==lang else '',label) for l,label in [('en','EN'),('ja','日本語')])
    body=(ROOT/'content'/lang/(page['key']+'.html')).read_text(encoding='utf-8')
    # Content URLs are rooted in this site, never at the domain root: works on GitHub project Pages and file://.
    body=body.replace('@ROOT@',base)
    if lang=='ja':
        # Localise links to available Japanese page counterparts; assets stay shared.
        for p in sorted(D['pages'],key=lambda p:len(p['path']),reverse=True):
            old='href="'+base+p['path']+'index.html';new='href="'+base+'ja/'+p['path']+'index.html'
            body=body.replace(old,new)
    label={'en':('Skip to content','Menu','Main navigation','Contact','Research photographs and archival material: BIRL and credited contributors.'),'ja':('本文へ移動','メニュー','メインナビゲーション','お問い合わせ','研究写真・記録：BIRLおよび各クレジット記載の提供者。')}[lang]
    title=page['title'][lang]
    heading='' if page['key']=='home' else '<h1>'+escape(title)+'</h1>'
    homeclass=' homepage' if page['key']=='home' else ''
    document='''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} — BIRL</title><meta name="description" content="Bio-Inspired Robotics Laboratory — University of Tokyo and University of Cambridge. Research, members, publications, events and contact."><link rel="icon" href="{logo}"><link rel="stylesheet" href="{css}"><script src="{js}" defer></script><link rel="alternate" hreflang="en" href="{en}"><link rel="alternate" hreflang="ja" href="{ja}"></head>
<body><a class="skip" href="#main">{skip}</a><header class="site-header"><div class="identity"><a class="logo" href="{home}" aria-label="BIRL home"><img src="{logo}" width="170" height="60" alt="BIRL — Bio-Inspired Robotics Laboratory"></a><div><{brandtag} class="site-name"><a href="{home}">Bio-Inspired Robotics Laboratory</a></{brandtag}><p class="affiliations">Department of Precision Engineering, University of Tokyo<br>Department of Engineering, University of Cambridge</p></div></div><div class="navigation-row"><details class="mobile-navigation"><summary>{menu}</summary><nav aria-label="{navlabel}">{nav}</nav></details><nav class="desktop-navigation" aria-label="{navlabel}">{nav}</nav><div class="languages" aria-label="Language">{langs}</div></div></header><main id="main" class="page{homeclass}">{heading}{body}</main><footer class="site-footer"><p><strong>BIRL</strong> · <a href="https://www.u-tokyo.ac.jp/en/">University of Tokyo</a> · <a href="https://www.cam.ac.uk/">University of Cambridge</a></p><p><a href="{contact}">{contactlabel}</a> · <a href="https://www.youtube.com/channel/UCssbO6gQLdwC2T3ZNkAo1wA">BIRL YouTube</a></p><p class="credit">{credit}</p></footer></body></html>'''.format(brandtag='h1' if page['key']=='home' else 'p',lang=lang,title=escape(title),logo=local(D['logo']),css=local('style.css'),js=local('script.js'),en=local(page['path']+'index.html'),ja=local('ja/'+page['path']+'index.html'),home=local(('ja/' if lang=='ja' else '')+'index.html'),skip=label[0],menu=label[1],navlabel=label[2],nav=nav,langs=langs,homeclass=homeclass,heading=heading,body=body,contact=local(('ja/' if lang=='ja' else '')+'contact/index.html'),contactlabel=label[3],credit=label[4])
    dest.write_text(document,encoding='utf-8')

for p in D['pages']:
    for lang in ['en','ja']:write_page(p,lang)
for source,target in D['redirects'].items():
    for lang in ['en','ja']:
        dest=ROOT/('ja' if lang=='ja' else '')/source/'index.html';dest.parent.mkdir(parents=True,exist_ok=True)
        url='../'+target.replace('/#','/index.html#')
        dest.write_text('<!doctype html><html lang="'+lang+'"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="refresh" content="0;url='+url+'"><title>BIRL — page moved</title></head><body><p>This page has moved. <a href="'+url+'">Continue to BIRL</a>.</p></body></html>',encoding='utf-8')
print('Built',len(D['pages'])*2,'pages and',len(D['redirects'])*2,'compatibility pages.')
