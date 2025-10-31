# 📜 Generator Draft UU (PDF) - Streamlit App

This is a simple web application built with Streamlit that generates a preliminary draft of a policy document (*Rancangan Undang-Undang* - RUU) in PDF format. The user can select a policy sector, and the app will instantly create a structured, downloadable PDF based on pre-defined templates.

This project serves as a demonstration of:
*   Building interactive UIs with Streamlit.
*   Generating PDF documents on-the-fly using the `reportlab` library in Python.
*   Managing application state (`st.session_state`) to keep a history of generated documents.
*   Embedding and previewing PDFs directly within a web page.



## ✨ Features

*   **Sector-Based Generation**: Choose from predefined sectors (Labor, Corruption, Tax) to generate a relevant policy draft.
*   **Instant PDF Creation**: Generates a professional-looking PDF document with a title page, structured sections, and draft articles.
*   **In-Browser PDF Preview**: Immediately displays a preview of the generated PDF in an embedded iframe.
*   **Direct Download**: Provides a button to download the generated PDF file.
*   **Session History**: Keeps a running history of all documents generated during the user's session.
*   **History Interaction**: Users can preview or re-download any document from the history list.
*   **Simple & Clean UI**: A straightforward, single-page interface that is easy to use.

## ⚙️ How It Works

The application logic is contained within a single Python script (`app.py`):

1.  **User Input**: The user selects a policy sector from a `st.selectbox`.
2.  **Content Generation (`generate_draft_content`)**: Based on the selected sector, this function retrieves a pre-defined set of content from a Python dictionary. This content includes the document title, objectives, key issues, policy directions, and sample articles.
3.  **PDF Building (`build_pdf_bytes`)**: The retrieved content is passed to this function, which uses the `reportlab` library to programmatically construct the PDF. It defines styles, formats paragraphs, creates tables, and arranges the content into a multi-page document.
4.  **State Management**: The generated PDF (as bytes) and its metadata (filename, sector, timestamp) are stored in `st.session_state.reports`. This list acts as the session history.
5.  **UI Rendering**:
    *   The most recently generated PDF is displayed in an iframe for preview.
    *   A download button is provided for the latest document.
    *   An expander (`st.expander`) lists all other documents in the history, each with its own "Preview" and "Download" buttons.

## 🚀 Setup and Installation

To run this application on your local machine, follow these steps.

### Prerequisites

*   Python 3.8+
*   `pip` (Python package installer)

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Create a Virtual Environment (Recommended)

It's good practice to create a virtual environment to manage dependencies.

*   **On macOS/Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

*   **On Windows:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

### 3. Install Dependencies

The required Python libraries are listed in `requirements.txt`.

```bash
pip install -r requirements.txt
```
If you don't have a `requirements.txt` file, you can create one with the following content or install the packages directly:

**requirements.txt:**
```
streamlit
reportlab
```

**Direct Installation:**
```bash
pip install streamlit reportlab
```

### 4. Run the Streamlit App

Once the dependencies are installed, you can run the application with the following command:

```bash
streamlit run app.py
```

Your web browser should automatically open a new tab with the application running. If not, open a browser and navigate to `http://localhost:8501`.

## 💻 Usage Guide

1.  **Select a Sector**: Choose one of the available options from the dropdown menu (e.g., "Ketenagakerjaan").
2.  **Generate PDF**: Click the "🚀 Generate PDF" button.
3.  **Preview**: The application will display a preview of the generated PDF document directly on the page.
4.  **Download**: Click the "💾 Download PDF" button to save the file to your computer. The filename will be automatically generated with the sector and a timestamp.
5.  **View History**: Click on the "📚 Riwayat Report" expander to see a list of previously generated documents from your current session. You can preview or download any of them.

## 📂 Code Structure

The `app.py` file is organized into several logical sections:

*   **Imports and Helpers**:
    *   Imports necessary libraries (`streamlit`, `reportlab`, `datetime`, etc.).
    *   Helper functions like `_today_wib()`, `_b64_pdf()`, and `_iframe_pdf()`.

*   **Domain Content Generator (`generate_draft_content`)**:
    *   Contains the static, pre-defined content for each policy sector. This function acts as the "content engine" of the app.

*   **PDF Builder (`build_pdf_bytes`)**:
    *   Handles all the `reportlab` logic for creating the PDF document from the content dictionary.

*   **Streamlit UI**:
    *   The main part of the script that defines the web interface, handles user interactions, calls the generator and builder functions, and manages the session state.

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
