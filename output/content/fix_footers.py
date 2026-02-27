import os
import glob
import re

def fix_remaining_footers():
    html_files = [
        'sessions.html',
        'intro-session.html',
        '404.html',
        'policies.html',
        'Pilates Vita -1.html',
        'studios_org.html'
    ]
    
    new_footer_html = """  <!-- Footer -->
  <footer class="bg-ink2 text-white">
    <div class="mx-auto max-w-6xl px-4 py-16">
      <div class="grid gap-10 md:grid-cols-3 items-start">
        
        <!-- Left Column: Logo & Address -->
        <div class="md:col-span-1 text-left">
          <img src="./Pilates Vita -1_files/pilates-vita-logo-200-white.png" alt="Pilates Vita"
            class="h-10 w-auto mb-6" />
          <p class="text-sm leading-relaxed text-white/90">
            109 Gloucester Rd.<br />
            South Kensington, SW7 4SS<br />
            London, United Kingdom
          </p>
        </div>

        <!-- Middle Column: Contact -->
        <div class="md:col-span-1 text-left">
          <h4 class="text-xs font-medium tracking-widest uppercase mb-6 text-white/80">Contact</h4>
          <p class="text-sm leading-relaxed text-white/90">
            <span class="inline-block w-20">Phone:</span> <a class="underline hover:no-underline" href="tel:07833123833">07833 123833</a><br />
            <span class="inline-block w-20">WhatsApp:</span> <a class="underline hover:no-underline" href="https://wa.me/447833123833" target="_blank" rel="noreferrer">07833 123833</a><br />
            <span class="inline-block w-20">Email:</span> <a class="underline hover:no-underline" href="mailto:patricia.patricia@mac.com" target="_blank" rel="noreferrer">patricia.patricia@mac.com</a>
          </p>
          <p class="mt-6 text-sm text-white/90">
            <a class="underline hover:no-underline" href="./policies.html">Booking &amp; Cancellation Policy</a>
          </p>
        </div>

        <!-- Right Column: Connect & Certifications -->
        <div class="md:col-span-1 text-left md:text-right">
          <h4 class="text-xs font-medium tracking-widest uppercase mb-6 text-white/80">Connect</h4>
          
          <div class="flex items-center md:justify-end gap-3 mb-8">
            <a class="inline-flex h-10 w-10 items-center justify-center rounded-full bg-white/10 hover:bg-white/15 transition"
              href="https://www.facebook.com/Pilates-Vita-London-UK-2692498114156033/" target="_blank" rel="noreferrer"
              aria-label="Facebook">
              <svg class="h-5 w-5" viewBox="0 0 24 24" fill="currentColor">
                <path d="M13.5 22v-8h2.7l.4-3H13.5V9.1c0-.9.2-1.5 1.5-1.5h1.6V5c-.3 0-1.4-.1-2.7-.1-2.6 0-4.4 1.6-4.4 4.6V11H7v3h2.5v8h4z" />
              </svg>
            </a>
            <a class="inline-flex h-10 w-10 items-center justify-center rounded-full bg-white/10 hover:bg-white/15 transition"
              href="https://www.instagram.com//pilatesvitakensington" target="_blank" rel="noreferrer"
              aria-label="Instagram">
              <svg class="h-5 w-5" viewBox="0 0 24 24" fill="currentColor">
                <path d="M7.5 2h9A5.5 5.5 0 0 1 22 7.5v9A5.5 5.5 0 0 1 16.5 22h-9A5.5 5.5 0 0 1 2 16.5v-9A5.5 5.5 0 0 1 7.5 2zm0 2A3.5 3.5 0 0 0 4 7.5v9A3.5 3.5 0 0 0 7.5 20h9a3.5 3.5 0 0 0 3.5-3.5v-9A3.5 3.5 0 0 0 16.5 4h-9z" />
                <path d="M12 7a5 5 0 1 1 0 10 5 5 0 0 1 0-10zm0 2a3 3 0 1 0 0 6 3 3 0 0 0 0-6z" />
                <path d="M17.5 6.5a1 1 0 1 1 0 2 1 1 0 0 1 0-2z" />
              </svg>
            </a>
            <a class="inline-flex h-10 w-10 items-center justify-center rounded-full bg-white/10 hover:bg-white/15 transition"
              href="mailto:patricia.patricia@mac.com" aria-label="Email">
              <svg class="h-5 w-5" viewBox="0 0 24 24" fill="currentColor">
                <path d="M20 6H4a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2zm0 2-8 5L4 8h16z" />
              </svg>
            </a>
          </div>

          <div class="flex items-center md:justify-end gap-4 mt-6">
            <img src="./Pilates Vita -1_files/pilates-method-alliance-certified.gif" alt="PMA certified" class="h-16 w-auto mix-blend-screen" />
            <img src="./Pilates Vita -1_files/selo.png" alt="Award badge" class="h-16 w-auto mix-blend-screen" />
            <img src="./Pilates Vita -1_files/review-us-google.jpg" alt="Review us on Google" class="h-16 w-auto rounded-md" />
          </div>
        </div>

      </div>

      <div class="mt-14 pt-6 text-center text-xs text-white/50">
        © <span id="year"></span> Pilates Vita. All rights reserved.
      </div>
    </div>
  </footer>"""

    # We use a more permissive regex that matches ANY footer tag and all its inner content
    footer_pattern = re.compile(r'<footer[^>]*>.*?</footer>', re.DOTALL | re.IGNORECASE)

    for file in html_files:
        if not os.path.exists(file):
            continue
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if footer_pattern.search(content):
            content = footer_pattern.sub(new_footer_html, content)
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated footer in {file}")
        else:
            print(f"Warning: Footer not found in {file}")

if __name__ == '__main__':
    fix_remaining_footers()
    print("Done fixing remaining footers")
