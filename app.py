# app.py
# Streamlit: Generator Draft UU (PDF) – Tanpa input Target/Wilayah/Ringkasan

import io, base64, uuid, datetime
import streamlit as st
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.units import cm

def _today_wib():
    return datetime.datetime.utcnow() + datetime.timedelta(hours=7)

def _b64_pdf(pdf_bytes: bytes) -> str:
    import base64
    return base64.b64encode(pdf_bytes).decode("utf-8")

def _iframe_pdf(pdf_bytes: bytes, height: int = 640):
    b64 = _b64_pdf(pdf_bytes)
    html = f"""
    <iframe
        src="data:application/pdf;base64,{b64}#toolbar=1&navpanes=0&scrollbar=1"
        style="width:100%; height:{height}px; border:1px solid #e5e7eb; border-radius:12px;">
    </iframe>
    """
    st.components.v1.html(html, height=height + 8, scrolling=False)

# --------------------------
# Domain Content Generator (tanpa input tambahan)
# --------------------------
def generate_draft_content(sector: str) -> dict:
    sektor_map = {
        "Ketenagakerjaan": {
            "judul": "RANCANGAN UNDANG-UNDANG TENTANG KESEJAHTERAAN DAN PERLINDUNGAN KETENAGAKERJAAN",
            "tujuan": [
                "Meningkatkan perlindungan hak dasar pekerja dan keselamatan kerja.",
                "Mendorong penciptaan lapangan kerja layak dan pengurangan pengangguran struktural.",
                "Memperkuat dialog sosial dan kepastian hubungan industrial."
            ],
            "masalah": [
                "Ketimpangan upah antar wilayah dan sektor.",
                "Minimnya kepatuhan standar K3 pada UMKM dan sektor informal.",
                "Peningkatan pekerja kontrak/jasa tanpa jaminan sosial memadai."
            ],
            "kebijakan": [
                "Standar upah layak berbasis KHL dengan penyesuaian produktivitas.",
                "Kewajiban JKK, JKM, JHT, JP dengan insentif iuran bagi UMKM.",
                "Sertifikasi K3 bagi perusahaan berisiko tinggi dan audit periodik.",
                "Program reskilling & upskilling nasional."
            ],
            "sanksi": "Administratif (teguran, denda, pembekuan izin) dan pidana untuk pelanggaran berat K3.",
        },
        "Korupsi": {
            "judul": "RANCANGAN UNDANG-UNDANG TENTANG PENCEGAHAN DAN PEMBERANTASAN TINDAK PIDANA KORUPSI TERINTEGRASI",
            "tujuan": [
                "Memperkuat pencegahan berbasis transparansi anggaran.",
                "Meningkatkan efektivitas penindakan lintas lembaga.",
                "Mengoptimalkan pengembalian kerugian negara."
            ],
            "masalah": [
                "Konflik kepentingan pada pengadaan dan perizinan.",
                "Kepatuhan substantif LHKPN yang belum merata.",
                "Keterbatasan telusur aliran dana lintas yurisdiksi."
            ],
            "kebijakan": [
                "e-Procurement penuh dengan publikasi real-time.",
                "Registri Beneficial Ownership yang dapat diakses publik.",
                "Pembekuan aset sementara berbasis intelijen keuangan.",
                "Perlindungan pelapor (whistleblower) dan imbalan informasi."
            ],
            "sanksi": "Pidana penjara & denda proporsional, perampasan aset, larangan menduduki jabatan publik."
        },
        "Pajak": {
            "judul": "RANCANGAN UNDANG-UNDANG TENTANG REFORMASI PERPAJAKAN UNTUK DAYA SAING DAN KEADILAN",
            "tujuan": [
                "Memperluas basis pajak & meningkatkan kepatuhan sukarela.",
                "Mendorong investasi produktif & UMKM naik kelas.",
                "Menyederhanakan sistem pajak agar adil & modern."
            ],
            "masalah": [
                "Tax gap tinggi akibat ekonomi informal dan kepatuhan rendah.",
                "Kompleksitas administrasi bagi wajib pajak kecil.",
                "Insentif yang belum tepat sasaran."
            ],
            "kebijakan": [
                "Single taxpayer account & pre-filled return.",
                "Simplifikasi tarif UMKM dan digitalisasi pembukuan.",
                "Pajak sinyal harga (lingkungan/kesehatan) yang terukur.",
                "Pertukaran data domestik lintas lembaga."
            ],
            "sanksi": "Sanksi administratif proporsional, pidana untuk penggelapan terencana, program pengungkapan sukarela terbatas."
        }
    }

    base = sektor_map.get(sector, sektor_map["Ketenagakerjaan"])

    meta = {
        "judul": base["judul"],
        "sektor": sector,
        "tanggal": _today_wib().strftime("%d %B %Y"),
        "id_dok": f"RUU-{sector[:3].upper()}-{uuid.uuid4().hex[:8]}",
        "ringkasan": f"Dokumen ini adalah draf awal RUU sektor {sector.lower()} untuk kebutuhan pembahasan publik dan harmonisasi.",
    }

    sections = {
        "Tujuan": base["tujuan"],
        "Permasalahan Pokok": base["masalah"],
        "Arah Kebijakan": base["kebijakan"],
        "Landasan Hukum": [
            "UUD Negara Republik Indonesia Tahun 1945.",
            "Ketetapan MPR yang relevan.",
            "UU sektoral terkait dan peraturan pelaksana.",
            "Perjanjian internasional (bila diratifikasi)."
        ],
        "Dampak Fiskal & Ekonomi": [
            "Perkiraan biaya implementasi 3–5 tahun.",
            "Proyeksi penerimaan/efisiensi (bila relevan).",
            "Analisis cost–benefit bagi rumah tangga dan pelaku usaha."
        ],
        "Kelembagaan & Tata Kelola": [
            "Penanggung jawab K/L, koordinasi pusat–daerah.",
            "Pelibatan publik, sistem pelaporan kinerja, dan audit."
        ],
        "Pengawasan & Sanksi": [base["sanksi"]],
        "Timeline Implementasi": [
            "Tahun 1: Peraturan turunan & pilot.",
            "Tahun 2–3: Skala nasional & penguatan kapasitas.",
            "Tahun 4–5: Konsolidasi dan evaluasi menyeluruh."
        ],
    }

    pasal = [
        ("Pasal 1", "Ketentuan Umum", [
            "Dalam Undang-Undang ini yang dimaksud dengan ... adalah ....",
            "Istilah kunci didefinisikan untuk mencegah multi-tafsir."
        ]),
        ("Pasal 2", "Asas & Tujuan", [
            "Asas: kepastian hukum, keadilan, kemanfaatan, transparansi, akuntabilitas.",
            "Tujuan sebagaimana diuraikan pada Bab Pendahuluan."
        ]),
        ("Pasal 3", "Hak & Kewajiban", [
            "Menetapkan hak masyarakat dan kewajiban pemerintah/korporasi.",
            "Pengaturan khusus untuk kelompok rentan/UMKM."
        ]),
        ("Pasal 4", "Kelembagaan & Kewenangan", [
            "Menetapkan lembaga pelaksana, koordinasi, dan mekanisme keputusan."
        ]),
        ("Pasal 5", "Pengawasan & Sanksi", [
            sections["Pengawasan & Sanksi"][0]
        ]),
        ("Pasal 6", "Pendanaan & Evaluasi", [
            "Sumber pendanaan, tata kelola anggaran, dan evaluasi tahunan."
        ])
    ]

    return {"meta": meta, "sections": sections, "pasal": pasal}

# --------------------------
# PDF Builder
# --------------------------
def build_pdf_bytes(docdata: dict) -> bytes:
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer, pagesize=A4,
        leftMargin=2*cm, rightMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm
    )
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="H1", fontSize=16, leading=20, spaceAfter=12, alignment=1))
    styles.add(ParagraphStyle(name="H2", fontSize=12.5, leading=16, spaceBefore=8, spaceAfter=6))
    styles.add(ParagraphStyle(name="Body", fontSize=10.5, leading=14))
    styles.add(ParagraphStyle(name="Small", fontSize=9.2, leading=12))
    styles.add(ParagraphStyle(name="Meta", fontSize=9.2, leading=12, textColor=colors.grey))

    meta = docdata["meta"]
    sections = docdata["sections"]
    pasal = docdata["pasal"]

    elements = []
    # Sampul
    elements.append(Paragraph(meta["judul"], styles["H1"]))
    elements.append(Spacer(1, 6))
    elements.append(Paragraph(f"Sektor: <b>{meta['sektor']}</b>", styles["Body"]))
    elements.append(Paragraph(f"Tanggal: {meta['tanggal']}", styles["Body"]))
    elements.append(Paragraph(f"ID Dokumen: {meta['id_dok']}", styles["Meta"]))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(meta["ringkasan"], styles["Body"]))
    elements.append(PageBreak())

    # Bagian-bagian
    for title, bullets in sections.items():
        elements.append(Paragraph(title, styles["H2"]))
        if isinstance(bullets, list):
            for b in bullets:
                elements.append(Paragraph(f"• {b}", styles["Body"]))
        else:
            elements.append(Paragraph(str(bullets), styles["Body"]))
        elements.append(Spacer(1, 8))

    elements.append(PageBreak())

    # Pasal-pasal
    elements.append(Paragraph("RUMUSAN PASAL-PASAL", styles["H2"]))
    for nomor, judul, isi in pasal:
        elements.append(Paragraph(f"<b>{nomor}</b> – {judul}", styles["Body"]))
        for item in isi:
            elements.append(Paragraph(f"- {item}", styles["Body"]))
        elements.append(Spacer(1, 6))

    elements.append(Spacer(1, 16))
    elements.append(Paragraph(
        "Catatan: Naskah ini merupakan draf awal dan masih memerlukan harmonisasi.",
        styles["Small"]
    ))

    doc.build(elements)
    pdf = buffer.getvalue()
    buffer.close()
    return pdf

# --------------------------
# Streamlit UI (tanpa field tambahan)
# --------------------------
st.set_page_config(page_title="Generator Draft UU (PDF)", page_icon="📜", layout="centered")
st.title("📜 Generator Draft Policy (UU) – Indonesia")
st.caption("Pilih sektor, klik **Generate**, pratinjau & unduh PDF.")

if "reports" not in st.session_state:
    st.session_state.reports = []

with st.form("generator_form", clear_on_submit=False):
    sektor = st.selectbox(
        "Pilih sektor report yang akan digenerate",
        ["Ketenagakerjaan", "Korupsi", "Pajak"],
        index=0
    )
    submitted = st.form_submit_button("🚀 Generate PDF", use_container_width=True)

if submitted:
    with st.spinner("Menyusun naskah & membuat PDF..."):
        data = generate_draft_content(sektor)
        pdf_bytes = build_pdf_bytes(data)
        ts = _today_wib().strftime("%Y%m%d_%H%M%S")
        fname = f"draft_RUU_{sektor}_{ts}.pdf".replace(" ", "_")
        st.session_state.reports.insert(0, {
            "name": fname,
            "sector": sektor,
            "created_at": ts,
            "bytes": pdf_bytes
        })
    st.success("Report berhasil digenerate!")

# Output
if not st.session_state.reports:
    st.info("Belum ada report. Silakan pilih sektor dan klik **Generate PDF**.")
else:
    latest = st.session_state.reports[0]
    st.subheader("📄 Pratinjau Terbaru")
    st.write(f"**{latest['name']}** — Sektor: `{latest['sector']}` — Dibuat: `{latest['created_at']}` (WIB)")
    _iframe_pdf(latest["bytes"], height=680)
    st.download_button(
        "💾 Download PDF",
        data=latest["bytes"],
        file_name=latest["name"],
        mime="application/pdf",
        use_container_width=True
    )

    with st.expander("📚 Riwayat Report"):
        if len(st.session_state.reports) == 1:
            st.write("_Belum ada riwayat selain dokumen terbaru._")
        else:
            for i, rep in enumerate(st.session_state.reports[1:], start=1):
                colA, colB, colC = st.columns([6, 2, 2])
                with colA:
                    st.write(f"**{rep['name']}**  \nSektor: `{rep['sector']}` — Dibuat: `{rep['created_at']}`")
                with colB:
                    if st.button("Preview", key=f"pv_{i}"):
                        st.session_state.reports.insert(0, st.session_state.reports.pop(i))
                        st.rerun()
                with colC:
                    st.download_button("Download", data=rep["bytes"], file_name=rep["name"], mime="application/pdf", key=f"dl_{i}")
