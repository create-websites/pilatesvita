import os
import glob
import re

def update_nav():
    html_files = glob.glob('*.html')
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Desktop Nav Replacements
        content = content.replace(
            '<a class="nav-link" href="./sessions.html">Session Types</a>',
            '<a class="nav-link" href="./sessions.html">Sessions and Prices</a>'
        )
        content = content.replace(
            '<a class="nav-link" href="./reviews.html">Testimonials</a>',
            '<a class="nav-link" href="./locations.html">Locations</a>'
        )

        content = content.replace(
            '<a class="block px-5 py-3 text-xs font-medium tracking-widest uppercase hover:bg-white/10 text-center"\n              href="./about.html">Our Story</a>\n          </div>',
            '<a class="block px-5 py-3 text-xs font-medium tracking-widest uppercase hover:bg-white/10 text-center"\n              href="./about.html">Our Story</a>\n            <a class="block px-5 py-3 text-xs font-medium tracking-widest uppercase hover:bg-white/10 text-center"\n              href="./reviews.html">Testimonials</a>\n            <a class="block px-5 py-3 text-xs font-medium tracking-widest uppercase hover:bg-white/10 text-center"\n              href="./news.html">News</a>\n          </div>'
        )
        
        # In case the newlines are different (e.g., CRLF vs LF or spacing)
        # We can use regex for the About dropdown end to make it more robust.
        about_dropdown_pattern = re.compile(
            r'(<a class="block[^>]+href="\./about\.html">Our Story</a>.*?)(</div>)', 
            re.DOTALL
        )
        
        # Check if we already did the replacement to avoid duplicate entries
        if 'href="./news.html">News</a>' not in content:
            def replace_about(match):
                return match.group(1) + \
                       '  <a class="block px-5 py-3 text-xs font-medium tracking-widest uppercase hover:bg-white/10 text-center"\n              href="./reviews.html">Testimonials</a>\n' + \
                       '            <a class="block px-5 py-3 text-xs font-medium tracking-widest uppercase hover:bg-white/10 text-center"\n              href="./news.html">News</a>\n          ' + match.group(2)
            content = about_dropdown_pattern.sub(replace_about, content)
            
        content = content.replace(
            '<a class="nav-link" href="./certification.html">Certification</a>',
            '<a class="nav-link" href="./certification.html">Franchising</a>'
        )

        # Mobile Nav Replacements
        content = content.replace(
            '<a class="block px-4 py-3 text-sm font-medium hover:bg-slate-50 uppercase tracking-wide"\n            href="./sessions.html">Session Types</a>',
            '<a class="block px-4 py-3 text-sm font-medium hover:bg-slate-50 uppercase tracking-wide"\n            href="./sessions.html">Sessions and Prices</a>'
        )
        content = content.replace(
            '<a class="block px-4 py-3 text-sm font-medium hover:bg-slate-50 uppercase tracking-wide"\n            href="./reviews.html">Testimonials</a>',
            '<a class="block px-4 py-3 text-sm font-medium hover:bg-slate-50 uppercase tracking-wide"\n            href="./locations.html">Locations</a>'
        )
        
        if '<a class="block px-4 py-3 text-sm font-medium hover:bg-slate-50 uppercase tracking-wide"\n            href="./news.html">News</a>' not in content:
            mobile_about_pattern = re.compile(
                r'(<a class="block[^>]+href="\./about\.html">Our Story</a>\s*)(<div class="border-t border-slate-200"></div>\s*<div class="px-4 py-3 text-xs font-semibold uppercase tracking-wide text-slate-500">What Is Pilates\?</div>)',
                re.DOTALL
            )
            def replace_mobile_about(match):
                return match.group(1) + \
                       '<a class="block px-4 py-3 text-sm font-medium hover:bg-slate-50 uppercase tracking-wide"\n            href="./reviews.html">Testimonials</a>\n          ' + \
                       '<a class="block px-4 py-3 text-sm font-medium hover:bg-slate-50 uppercase tracking-wide"\n            href="./news.html">News</a>\n\n          ' + match.group(2)
            content = mobile_about_pattern.sub(replace_mobile_about, content)

        content = content.replace(
            '<a class="block px-4 py-3 text-sm font-medium hover:bg-slate-50 uppercase tracking-wide"\n            href="./certification.html">Certification</a>',
            '<a class="block px-4 py-3 text-sm font-medium hover:bg-slate-50 uppercase tracking-wide"\n            href="./certification.html">Franchising</a>'
        )
        
        # Single line fallbacks for session types/testimonials if formatting is slightly different
        content = re.sub(r'href="\./sessions\.html">\s*Session Types\s*</a>', r'href="./sessions.html">Sessions and Prices</a>', content)
        content = re.sub(r'href="\./reviews\.html">\s*Testimonials\s*</a>', r'href="./locations.html">Locations</a>', content)
        content = re.sub(r'href="\./certification\.html">\s*Certification\s*</a>', r'href="./certification.html">Franchising</a>', content)

        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

if __name__ == '__main__':
    update_nav()
    print("Done updating nav")
