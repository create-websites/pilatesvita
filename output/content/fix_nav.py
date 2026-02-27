import os
import glob
import re

def fix_nav():
    html_files = glob.glob('*.html')
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Fix desktop dropdown
        content = content.replace(
            '<a class="block px-5 py-3 text-xs font-medium tracking-widest uppercase hover:bg-white/10 text-center"\n              href="./locations.html">Locations</a>\n            <a class="block px-5 py-3 text-xs font-medium tracking-widest uppercase hover:bg-white/10 text-center"\n              href="./news.html">News</a>',
            '<a class="block px-5 py-3 text-xs font-medium tracking-widest uppercase hover:bg-white/10 text-center"\n              href="./reviews.html">Testimonials</a>\n            <a class="block px-5 py-3 text-xs font-medium tracking-widest uppercase hover:bg-white/10 text-center"\n              href="./news.html">News</a>'
        )

        # Fix mobile dropdown
        content = content.replace(
            '<a class="block px-4 py-3 text-sm font-medium hover:bg-slate-50 uppercase tracking-wide"\n            href="./locations.html">Locations</a>\n          <a class="block px-4 py-3 text-sm font-medium hover:bg-slate-50 uppercase tracking-wide"\n            href="./news.html">News</a>',
            '<a class="block px-4 py-3 text-sm font-medium hover:bg-slate-50 uppercase tracking-wide"\n            href="./reviews.html">Testimonials</a>\n          <a class="block px-4 py-3 text-sm font-medium hover:bg-slate-50 uppercase tracking-wide"\n            href="./news.html">News</a>'
        )

        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

if __name__ == '__main__':
    fix_nav()
    print("Done fixing nav")
