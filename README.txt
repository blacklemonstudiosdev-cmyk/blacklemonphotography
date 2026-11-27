BlackLemon Photography

index.html            the site and the scroll intro
logo.png              your logo (white on transparent)
home page/            text1.json, text2.json, text2.png
photos/               your photos, plus photos.json (the list of file names)
license/              text.json, button.json

Adding photos: drop them into photos/, then run  python3 update-photos.py
(Vercel cannot list a folder, so the site reads photos/photos.json instead.)
The sample-XX.jpg files are placeholders. Delete them before you go live.

Text files: label and heading are single strings; body is a list, one string per paragraph.
license/button.json: put a link in "url" when you are ready; while it is empty the button does nothing.
