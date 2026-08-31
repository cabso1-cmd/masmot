# Installing the Masmot Logistics email signature in Outlook

This folder contains:

- **`aboo-signature.html`** — the signature itself, pre-filled with your name, title (Operations Manager), and Masmot Logistics contact details.
- **`signature-preview.png`** — what it looks like, for reference.

The signature's logo is linked to `https://masmotlogistics.ca/assets/img/signature/signature-icon.png`. That file is already included in the website package (under `assets/img/signature/`), so **once the website is live on masmotlogistics.ca, the logo will just work** — Outlook fetches it from your own domain, and it'll stay in sync automatically if you ever update the logo.

If you want the signature working *before* the site is deployed, see "Using it before the site is live" below.

---

## Option A — Outlook on the web / "New Outlook" (Windows or Mac)

1. Go to **Settings** (gear icon, top right) → **Accounts** → **Signatures**.
2. Click **New signature**, name it "Masmot Logistics".
3. Open `aboo-signature.html` in Chrome or Edge, select all the signature content (click just above/left of the logo and drag to below the confidentiality line), and copy it (**Ctrl/Cmd+C**).
4. Click into the signature editor box in Outlook and paste (**Ctrl/Cmd+V**).
5. Under **Select default signatures**, set it for **New messages** and **Replies/forwards**, then **Save**.

## Option B — Outlook desktop app (Windows, classic Outlook)

1. **File → Options → Mail → Signatures…**
2. Click **New**, name it "Masmot Logistics", click OK.
3. Open `aboo-signature.html` in a browser (double-click the file), select all the signature content, and copy it.
4. Paste into the signature editing box in Outlook.
5. Set it as the default for new messages and replies/forwards. Click **OK**.

## Option C — Outlook desktop app (Mac, classic Outlook)

1. **Outlook menu → Settings → Signatures**.
2. Click **+** to add a new signature, name it "Masmot Logistics".
3. Open `aboo-signature.html` in Safari or Chrome, select all the signature content, copy it.
4. Click into the signature body field and paste.
5. Under **Default signatures**, assign it to your account for new messages and replies.

---

## Using it before the site is live

Until `masmotlogistics.ca` is deployed, the logo image won't load from its web address. Two options:

1. **Fastest fix — do nothing.** Deploy the site first (see the main `README.md`), then install the signature — the logo will resolve correctly right away since the image ships as part of the site files.
2. **Want it working today anyway?** In the signature editor, right-click the broken image icon → remove it, then use Outlook's **Insert Picture** button to insert `signature-icon.png` (found in `assets/img/signature/` in the website package) directly. Outlook will embed a local copy. Note: if you ever change the logo, you'll need to re-insert it manually with this method, whereas the linked version updates itself automatically.

## Editing your details later

Open `aboo-signature.html` in a text editor — the name, title, phone, email, and address are plain text near the top of the file. Update the text, then re-copy/paste it into Outlook following the steps above (Outlook does not read this file live — it only stores what you paste into it).
