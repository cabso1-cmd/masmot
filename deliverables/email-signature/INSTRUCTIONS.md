# Installing the Masmot Logistics email signature in Outlook

This folder contains:

- **`aboo-signature.html`** — the signature itself, pre-filled with your name, title (Operations Manager), and Masmot Logistics contact details.
- **`signature-preview.png`** — what it looks like, for reference.

The logo is embedded directly inside `aboo-signature.html` (as a data URI, not a link to a website), so it displays correctly as soon as you paste the signature into Outlook — it does **not** depend on masmotlogistics.ca being live. That's a deliberate change from an earlier version of this file, which linked to the not-yet-deployed site and showed a broken-image icon; if you already pasted that version into Outlook, re-copy from this updated file and paste again to replace it.

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

## Editing your details later

Open `aboo-signature.html` in a text editor — the name, title, phone, email, and address are plain text near the top of the file. Update the text, then re-copy/paste it into Outlook following the steps above (Outlook does not read this file live — it only stores what you paste into it).
