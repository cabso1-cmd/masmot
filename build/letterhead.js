const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, ImageRun, Header, Footer,
  AlignmentType, BorderStyle, HeadingLevel, Table, TableRow, TableCell,
  WidthType, ShadingType, VerticalAlign, PageOrientation
} = require("docx");

const IMG = p => fs.readFileSync(path.join(__dirname, "..", "assets", "img", p));

const NAVY = "0F2A47";
const NAVY_DARK = "0A2440";
const AMBER = "F2A93B";
const AMBER_DARK = "E0932A";
const SLATE = "5B6B7C";
const SLATE_LIGHT = "AEBAC7";

const SITE = {
  address1: "2150 Winston Park Dr, Unit 203",
  address2: "Oakville, ON  L6H 5V1, Canada",
  phone: "+1 647 848 7287",
  fax: "+1 647 946 8310",
  email: "operations@masmotlogistics.ca",
  web: "masmotlogistics.ca",
};

function buildHeader() {
  return new Header({
    children: [
      new Paragraph({
        alignment: AlignmentType.LEFT,
        spacing: { after: 120 },
        border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: AMBER, space: 10 } },
        children: [
          new ImageRun({
            type: "png",
            data: IMG("logo-horizontal@2x.png"),
            transformation: { width: 231, height: 69.5 },
          }),
        ],
      }),
    ],
  });
}

function footerLine(icon, text) {
  return new TextRun({ text: `  ${text}   `, size: 15, color: SLATE, font: "Calibri" });
}

function buildFooter() {
  return new Footer({
    children: [
      new Paragraph({
        spacing: { before: 100 },
        border: { top: { style: BorderStyle.SINGLE, size: 4, color: "D8DEE6", space: 8 } },
        alignment: AlignmentType.CENTER,
        children: [
          new TextRun({ text: `${SITE.address1}, ${SITE.address2}`, size: 15, color: SLATE, font: "Calibri" }),
        ],
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 20 },
        children: [
          new TextRun({ text: `T ${SITE.phone}   |   F ${SITE.fax}   |   ${SITE.email}   |   ${SITE.web}`, size: 15, color: SLATE, font: "Calibri", bold: false }),
        ],
      }),
    ],
  });
}

function letterBody() {
  const grey = "9AA6B2";
  const placeholder = (t, opts = {}) => new Paragraph({
    spacing: { after: 120 },
    children: [new TextRun({ text: t, color: grey, italics: true, font: "Calibri", size: 22, ...opts })],
  });

  return [
    new Paragraph({ spacing: { after: 260 }, children: [new TextRun({ text: "[Date]", font: "Calibri", size: 22, color: "33404D" })] }),

    placeholder("[Recipient Name]"),
    placeholder("[Title]"),
    placeholder("[Company Name]"),
    placeholder("[Address Line 1]"),
    placeholder("[City, Province, Postal Code]", { spacing: undefined }),

    new Paragraph({ spacing: { before: 260, after: 220 }, children: [new TextRun({ text: "Dear [Recipient Name],", font: "Calibri", size: 22, color: "33404D" })] }),

    new Paragraph({
      spacing: { after: 220 },
      children: [
        new TextRun({ text: "Re: ", bold: true, font: "Calibri", size: 22, color: NAVY }),
        new TextRun({ text: "[Subject line]", font: "Calibri", size: 22, color: "33404D" }),
      ],
    }),

    new Paragraph({
      spacing: { after: 220 },
      children: [new TextRun({
        text: "Replace this paragraph with the body of your letter. This template carries the Masmot Logistics letterhead in the header and footer on every page, so you can focus on the content — the branding, contact details, and page margins are already set.",
        font: "Calibri", size: 22, color: "33404D",
      })],
    }),

    new Paragraph({
      spacing: { after: 420 },
      children: [new TextRun({
        text: "Add further paragraphs as needed. Delete this placeholder text before sending.",
        font: "Calibri", size: 22, color: "33404D",
      })],
    }),

    new Paragraph({ spacing: { after: 20 }, children: [new TextRun({ text: "Sincerely,", font: "Calibri", size: 22, color: "33404D" })] }),
    new Paragraph({ spacing: { before: 700, after: 20 }, children: [new TextRun({ text: "[Your Name]", font: "Calibri", size: 22, bold: true, color: NAVY })] }),
    new Paragraph({ spacing: { after: 20 }, children: [new TextRun({ text: "[Your Title]", font: "Calibri", size: 22, color: "33404D" })] }),
    new Paragraph({ children: [new TextRun({ text: "Masmot Logistics Ltd", font: "Calibri", size: 22, color: "33404D" })] }),
  ];
}

const doc = new Document({
  sections: [
    {
      properties: {
        page: {
          size: { width: 12240, height: 15840 }, // US Letter
          margin: { top: 2000, bottom: 1600, left: 1300, right: 1300 },
        },
      },
      headers: { default: buildHeader() },
      footers: { default: buildFooter() },
      children: letterBody(),
    },
  ],
});

Packer.toBuffer(doc).then(buf => {
  const out = path.join(__dirname, "output", "Masmot-Logistics-Letterhead-Template.docx");
  fs.writeFileSync(out, buf);
  console.log("wrote", out);
});
